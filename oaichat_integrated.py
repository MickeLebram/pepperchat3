from datetime import datetime
import os
import traceback
from typing import Callable, List, Tuple
import wave
import defs
import silerovad
from pcm_processor import PcmProcessor
import json, base64, threading, time
import numpy as np
from websocket import WebSocketApp
from syslogger import syslogger

class Query:
    def __init__(self):
        self.start_time = time.time()
        self.response_text = ""
        self.response_done = False
        self.query_transcript:str = None
        self.query_interpretation:str = None
        self.done = False
        self.duration = 0
        self.canceled = False
    def __str__(self):
        return str(self.__dict__)
    @property
    def query_text(self):
        ret = "trans:"
        if self.query_transcript:
            ret += self.query_transcript
        ret += " interpret:"
        if self.query_interpretation:
            ret += self.query_interpretation
        return ret
    
class TagBlockParser:
    def __init__(self, tag):
        self.start_tag = f"<{tag}>"
        self.end_tag = f"</{tag}>"
        self.reset()

    def reset(self):
        self.is_inside = False
        self.pending = ""
        self.content = ""
        self.content_done = False

    def feed(self, chunk: str) -> str:
        """
        Returns chars outside of the block
        Captures chars inside of the block
        """
        outside_chars = ""
        for ch in chunk:
            self.pending += ch

            if self.is_inside:
                if self.pending.endswith(self.end_tag):
                    self.content += self.pending[:-len(self.end_tag)]
                    self.pending = ""
                    self.is_inside = False
                    self.content_done = True
                    continue

                # Capture only chars that can no longer be part of end tag
                while self.pending and not self.end_tag.startswith(self.pending):
                    self.content += self.pending[0]
                    self.pending = self.pending[1:]

            else:
                if self.pending.endswith(self.start_tag):
                    self.pending = ""
                    self.is_inside = True
                    continue

                # Return only chars that can no longer be part of start tag
                while self.pending and not self.start_tag.startswith(self.pending):
                    outside_chars += self.pending[0]
                    self.pending = self.pending[1:]

        return outside_chars

    def flush(self) -> str:
        if self.is_inside:
            self.content += self.pending
            return ""
        return self.pending
        
SYSTEM_PROMPT_PREFIX = """
=== OUTPUT FORMAT ===

Every response MUST begin with exactly one <heard> tag.

Format:

<heard>best interpretation of the user's speech</heard>

followed immediately by the assistant response.

Examples:

<heard>What time is it?</heard>
No idea. Look at a clock.

<heard>Can you help me?</heard>
Maybe. What's the problem?

Rules:
- Every response must contain exactly one <heard> tag.
- The tag must be the first content emitted.
- Never omit the tag.
- Never emit text before the tag.

=== CONVERSATION INSTRUCTIONS ===

"""
class OaiChatIntegrated:
    STATE_IDLE = "IDLE"
    STATE_SENDING_SPEECH = "SENDING_SPEECH"
    STATE_RECEIVING_RESPONSE = "RECEIVING_RESPONSE"

    def __init__(self, 
                 api_key:str,
                 system_prompt = "", 
                 language = "sv", 
                 voice="", #ex. sage
                 response_audio_callback: Callable[[int, int, np.ndarray], None] = None,
                ):
        def on_pcm16_frames(sample_rate:int, channel_cnt:int, frames:np.ndarray):
            if self.state != self.STATE_SENDING_SPEECH:
                #self.cancel_current()
                self._cur_query = Query()  
                self._heard_filter.reset()
                wavname = str(input_audio_wav_dir / f"{int(self._cur_query.start_time*1000)}.wav")
                self.input_audio_wav_file = wave.open(wavname, "wb")
                self.input_audio_wav_file.setnchannels(self.pcm_processor.channel_cnt)
                self.input_audio_wav_file.setframerate(self.pcm_processor.sample_rate)
                self.input_audio_wav_file.setsampwidth(2)
                self._set_state(self.STATE_SENDING_SPEECH)
                syslogger.debug(f"start wav:{wavname}")
            for chunk in self.pcm_processor.get_frame_chunks(sample_rate, channel_cnt, frames):
                self.input_audio_wav_file.writeframes(chunk.tobytes())
                self._send_data({
                    "type": "input_audio_buffer.append",
                    "audio": base64.b64encode(bytes(chunk.tobytes())).decode("ascii"),
                })

        def on_speech_end(sample_rate:int, channel_cnt:int, pcm16_chunks:List[np.ndarray]):
            self._set_state(self.STATE_RECEIVING_RESPONSE)
            self._send_data({"type": "input_audio_buffer.commit"})
            self.input_audio_wav_file.close()

        input_audio_wav_dir = defs.WAV_DIR / datetime.now().strftime('%Y-%m-%d_%H%M%S')
        os.makedirs(input_audio_wav_dir, exist_ok=True)
        self.input_audio_wav_file:wave.Wave_write = None
        self.pcm_processor = PcmProcessor(24000, 1, millis_per_chunk=100) # Realtime API expects PCM16 mono ~24 kHz
        self._sending_speech = False
        self.silero = silerovad.SileroVad(
            threshold=.35,
            head_millis=1000,
            speech_stream_callback=on_pcm16_frames,
            speech_end_callback=on_speech_end
        )
        self.state_callbacks:List[Callable[[str], None]] = []
        self.query_update_callbacks:List[Callable[[Query], None]] = []
        self.listening_state_change_callbacks:List[Callable[[bool], None]] = []
        self.intermediate_response_text_callbacks:List[Callable[[str], None]] = []
        self.response_audio_callback = response_audio_callback
        self.language = language
        self.voice = voice
        self.system_prompt = system_prompt
        self._cur_query = Query()
        self._heard_filter = TagBlockParser("heard")
        self._listening = True
        self._state = self.STATE_IDLE
        self.ws:WebSocketApp = None
        self.api_key = api_key
        self.start()
    @property
    def state(self):
        return self._state
    
       
    def _set_state(self, state):
        if self._state != state:
            self._state = state
            syslogger.debug(state)
            for cbk in self.state_callbacks:
                cbk(state)
    def start(self):
        if self.ws:
            self.close()
        def on_open(ws):
            print("WebSocket connected")
            session_data = {
                "type": "realtime",
                "instructions": SYSTEM_PROMPT_PREFIX + self.system_prompt,
                "output_modalities": ["text", "audio"] if self.voice else ["text"],  
                "audio": {
                    "input": {
                        "format": {
                            "type": "audio/pcm",
                            "rate": 24000
                        },
                        "transcription": {
                            "model": "gpt-4o-mini-transcribe",
                            "language": "sv"
                        },
                        "turn_detection": None, # We decide ourselves when it's time for response

                    },
                }

            }
            if self.voice:
                session_data["audio"]["output"] = {
                    "format": {
                        "type": "audio/pcm",
                        "rate": 24000
                    },
                    "voice": self.voice,
                }


            self._send_data({
                "type": "session.update",
                "session": session_data,
            })

        def on_error(ws, error):
            print("WebSocket error:", error)

        def on_close(ws, code, msg):
            print("WebSocket closed:", code, msg)
            self.ws = None


        def on_message(ws, message):
            try:
                def try_set_query_done():
                    q = self._cur_query
                    if q.done or q.canceled:
                        return
                    if q.response_done and q.query_transcript:
                        q.done = True
                        q.duration = time.time() - self._cur_query.start_time
                        for cbk in self.query_update_callbacks:
                            cbk(self._cur_query)
                    self._set_state(self.STATE_IDLE)

                evt = json.loads(message)
                syslogger.debug(f"EVENT:{(time.time() - self._cur_query.start_time):.1f} {json.dumps(evt)}")

                t = evt.get("type", "")
                if t == "error":
                    if error := evt.get("error"):
                        if error.get("code") == "response_cancel_not_active":
                            return
                    # OBS! ERROR: {'type': 'error', 'event_id': 'event_Cf56YfnjwVCABifRNL02D', 'error': {'type': 'invalid_request_error', 'code': 'session_expired', 'message': 'Your session hit the maximum duration of 60 minutes.', 'param': None, 'event_id': None}}
                    # print("ERROR:", evt)
                    syslogger.error(f"Error event: {evt}")
                elif t == "input_audio_buffer.committed":
                    self._send_data({"type": "response.create"})
                elif t == "response.audio.delta":
                    b = base64.b64decode(evt.get("delta", ""))
                    if self.response_audio_callback:
                        frames = np.frombuffer(b, dtype=np.int16)
                        self.response_audio_callback(24000, 1, frames)
                elif t == "conversation.item.input_audio_transcription.completed":
                    transcript = evt.get("transcript")
                    self._cur_query.query_transcript = transcript if transcript else "EMPTY"
                    try_set_query_done()
                elif t == "response.output_text.delta":
                    filtered_text = self._heard_filter.feed(evt.get("delta"))
                    if self._heard_filter.content_done:
                        self._cur_query.query_interpretation = self._heard_filter.content
                    self._cur_query.response_text += filtered_text
                    if not self._cur_query.canceled:
                        for cbk in  self.query_update_callbacks:
                            cbk(self._cur_query)
                        if filtered_text:
                            for cbk in self.intermediate_response_text_callbacks:
                                cbk(filtered_text)
                elif t == "response.done":
                    self._heard_filter.flush()
                    self._cur_query.query_interpretation = self._heard_filter.content
                    self._cur_query.response_done = True
                    try_set_query_done()
                else:
                    pass
                # print("cur:",self._cur_query)
            except Exception as e:
                syslogger.exception(f"Exception {e} when handling event {evt}")


        self.ws = WebSocketApp(
            "wss://api.openai.com/v1/realtime?model=gpt-realtime",
            header=[
                "Authorization: Bearer " + self.api_key,
                #"OpenAI-Beta: realtime=v1",
            ],
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
        threading.Thread(target=self.ws.run_forever, daemon=True).start()        
    def __del__(self):
        self.close()
    
    def close(self):
        try:
            self.cancel_current()
            self.ws.close()
            while(self.ws):
                time.sleep(.1)
        except:
            traceback.print_exc()

    def set_system_prompt(self, prompt:str):
        self.system_prompt = prompt
        self.start()

    def _send_data(self, data:dict):
        self.ws.send(json.dumps(data))
        if data["type"] == "input_audio_buffer.append":
            data = data.copy()
            data["audio"] = "..."
        syslogger.debug(f"SEND DATA:{json.dumps(data)}")

    def push_pcm16_frames(self, sample_rate:int, channel_cnt:int, frames:np.ndarray):
        if self._listening:
            self.silero.push_pcm16_frames(sample_rate, channel_cnt, frames)
    
    def set_listening(self, listening:bool):
        if self._listening != listening:
            print("listening:",listening)
            self._listening = listening
            for cbk in self.listening_state_change_callbacks:
                cbk(listening)
    
    def cancel_current(self):
        self._cur_query.canceled = True
        if self.state != self.STATE_IDLE:
            self._send_data({"type": "response.cancel"})

