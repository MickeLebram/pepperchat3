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
        self.query_text = ""
        self.response_text = ""
        self.done = False
        self.duration = 0
        self.canceled = False
        self.audio_chunks = []
    def __str__(self):
        return str(self.__dict__)



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
            self._send_data({
                "type": "response.create",
            })
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
                "instructions": self.system_prompt,
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
                        "turn_detection": {
                            "type": "server_vad",
                            "create_response": False # We decide ourselves when it's time for response
                        }
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
                evt = json.loads(message)
                t = evt.get("type", "")
                #print(t)
                if t == "error":
                    if error := evt.get("error"):
                        if error.get("code") == "response_cancel_not_active":
                            return
                    # OBS! ERROR: {'type': 'error', 'event_id': 'event_Cf56YfnjwVCABifRNL02D', 'error': {'type': 'invalid_request_error', 'code': 'session_expired', 'message': 'Your session hit the maximum duration of 60 minutes.', 'param': None, 'event_id': None}}
                    # print("ERROR:", evt)
                    syslogger.error(f"Error event: {evt}")
                elif t == "response.audio.delta":
                    b = base64.b64decode(evt.get("delta", ""))
                    if self.response_audio_callback:
                        frames = np.frombuffer(b, dtype=np.int16)
                        self.response_audio_callback(24000, 1, frames)
                elif t == "conversation.item.input_audio_transcription.delta":
                    self._cur_query.query_text += evt.get("delta")
                elif t == "conversation.item.input_audio_transcription.completed":
                    self._cur_query.query_text += " "
                    # print("USER:", evt.get("transcript"), evt)
                elif t == "response.output_text.delta":
                    text = evt.get("delta")
                    self._cur_query.response_text += text
                    if not self._cur_query.canceled:
                        for cbk in  self.query_update_callbacks:
                            cbk(self._cur_query)
                        for cbk in self.intermediate_response_text_callbacks:
                            cbk(text)
                # elif delta := evt.get("delta"):
                #     print(t,delta)
                elif t == "response.done":
                    if evt["response"]["status"] == "completed":
                        self._cur_query.done = True
                        self._cur_query.duration = time.time() - self._cur_query.start_time
                    if not self._cur_query.canceled:
                        for cbk in self.query_update_callbacks:
                            cbk(self._cur_query)
                    self._set_state(self.STATE_IDLE)
                else:
                    pass
                syslogger.debug(f"EVENT:{(time.time() - self._cur_query.start_time):.1f} {evt}")
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

