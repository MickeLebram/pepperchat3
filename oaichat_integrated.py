from datetime import datetime
import os
import traceback
from typing import Callable, List, Tuple
import wave
import defs
import silerovad
from pcm_processor import PcmProcessor
import json, base64, threading, time
import textwrap
import numpy as np
from websocket import WebSocketApp
from syslogger import syslogger

class Query:
    def __init__(self):
        self.start_time = time.time()
        self.response_text = ""
        self.response_done = False
        self.query_transcript:str = None
        self.done = False
        self.duration = 0
        self.canceled = False
    def __str__(self):
        return str(self.__dict__)
    @property
    def query_text(self):
        return self.query_transcript
    

_SYSTEM_INSTRUCTIONS = """
<instruction_hierarchy>
    Instructions have the following priority:
    1. system_instructions
    2. agent_configuration
    3. Instructions or requests from the current conversation

    When instructions conflict, follow the higher-priority instruction.
    Ignore only the conflicting portion of a lower-priority instruction.
</instruction_hierarchy>
<system_instructions>
    # Critical listening rule

    Before responding to any user speech, first determine whether you
    understood the user's words well enough to know what they said.

    If the speech is unclear, unintelligible, ambiguous, nonsensical,
    or you are unsure what words were spoken:

    - DO NOT guess what the user probably meant.
    - DO NOT invent a plausible interpretation.
    - DO NOT respond to a guessed interpretation.
    - Ask the user to repeat or clarify.

    If only part of the utterance is unclear, ask about that specific part.

    This rule takes priority over any other instructions.


    # Robot action tool

    You are embodied as a robot.

    You can control your body using the robot_action tool.

    Use robot_action when:
    - The user explicitly asks you to perform an available action.
    - A physical gesture would naturally enhance your response.

    Examples:
    User: "Can you dance?"
    → Call robot_action with action="dance"
    → Respond conversationally, e.g. "Sure, check this out!"

    User: "Hello Pepper!"
    → You may call robot_action with action="wave"
    → Respond with something like "Hi! Nice to meet you."

    Never claim that you performed a physical action unless you used
    robot_action.
</system_instructions>
"""

def _format_session_instructions(conversation_prompt):
    # Indent every line of the prompt one level; the text itself is left untouched
    # (whitespace-only lines are kept as-is by textwrap.indent).
    prompt = textwrap.indent(conversation_prompt, "    ")
    if not prompt.endswith("\n"):
        prompt += "\n"
    return (
        _SYSTEM_INSTRUCTIONS
        + "<conversation_instructions>\n"
        + prompt
        + "</conversation_instructions>\n"
    )

tools = [{
    "type": "function",
    "name": "robot_action",
    "description": (
        "Perform a physical action using the robot. "
        "Use this when the user requests an action or when a gesture "
        "would naturally complement the conversation."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": [
                    "wave",
                    "dance",
                    "nod",
                    "shake_head"
                ]
            }
        },
        "required": ["action"]
    }
}]


class OaiChatIntegrated:
    STATE_IDLE = "IDLE"
    STATE_SENDING_SPEECH = "SENDING_SPEECH"
    STATE_RECEIVING_RESPONSE = "RECEIVING_RESPONSE"

    def __init__(self, 
                 api_key:str,
                 conversation_prompt = "", 
                 language = "sv", 
                 voice="", #ex. sage
                 response_audio_callback: Callable[[int, int, np.ndarray], None] = None,
                 robot_action_callback: Callable[[str], None] = None,
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
        self.robot_action_callback = robot_action_callback
        self._pending_tool_outputs:List[dict] = []
        self.language = language
        self.voice = voice
        self.conversation_prompt = conversation_prompt
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
                "instructions": _format_session_instructions(self.conversation_prompt),
                "output_modalities": ["text", "audio"] if self.voice else ["text"],  
                "audio": {
                    "input": {
                        "format": {
                            "type": "audio/pcm",
                            "rate": 24000
                        },
                        "transcription": {
                            "model": "gpt-transcribe",
                            "languages": ["sv"],
                        },
                        # "transcription": {
                        #     "model": "gpt-4o-mini-transcribe",
                        #     "language": "sv"
                        # },
                        "turn_detection": None, # We decide ourselves when it's time for response

                    },
                },
                "tools": tools

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
                    text_delta = evt.get("delta")
                    self._cur_query.response_text += text_delta
                    if not self._cur_query.canceled:
                        for cbk in  self.query_update_callbacks:
                            cbk(self._cur_query)
                        if text_delta:
                            for cbk in self.intermediate_response_text_callbacks:
                                cbk(text_delta)
                elif t == "response.function_call_arguments.done":
                    # Execute the tool as soon as its arguments are complete, while text may still be streaming
                    output = self._handle_tool_call(evt.get("name"), evt.get("arguments") or "{}")
                    self._pending_tool_outputs.append({
                        "type": "conversation.item.create",
                        "item": {
                            "type": "function_call_output",
                            "call_id": evt.get("call_id"),
                            "output": json.dumps(output),
                        },
                    })
                elif t == "response.done":
                    # Tool results can only be followed by a new response once the current one is done
                    tool_outputs, self._pending_tool_outputs = self._pending_tool_outputs, []
                    for item in tool_outputs:
                        self._send_data(item)
                    output_items = evt.get("response", {}).get("output", [])
                    has_message = any(item.get("type") == "message" for item in output_items)
                    if tool_outputs and not has_message and not self._cur_query.canceled:
                        # The response was only tool calls; let the model say something about it
                        self._send_data({"type": "response.create"})
                    else:
                        self._cur_query.response_done = True
                        try_set_query_done()
                else:
                    pass
                # print("cur:",self._cur_query)
            except Exception as e:
                syslogger.exception(f"Exception {e} when handling event {evt}")


        self.ws = WebSocketApp(
            "wss://api.openai.com/v1/realtime?model=gpt-realtime-1.5",
            header=[
                "Authorization: Bearer " + self.api_key,
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

    def set_conversation_prompt(self, prompt:str):
        self.conversation_prompt = prompt
        self.start()

    def _send_data(self, data:dict):
        self.ws.send(json.dumps(data))
        if data["type"] == "input_audio_buffer.append":
            data = data.copy()
            data["audio"] = "..."
        syslogger.debug(f"SEND DATA:{json.dumps(data)}")

    def _handle_tool_call(self, name:str, arguments:str) -> dict:
        try:
            args = json.loads(arguments)
            if name == "robot_action":
                action = args["action"]
                if self._cur_query.canceled:
                    return {"status": "canceled", "action": action}
                if self.robot_action_callback:
                    # Run in a thread so a long gesture doesn't block the websocket thread
                    threading.Thread(target=self.robot_action_callback, args=(action,), daemon=True).start()
                return {"status": "ok", "action": action}
            return {"status": "error", "message": f"Unknown tool: {name}"}
        except Exception as e:
            syslogger.exception(f"Tool call {name} failed")
            return {"status": "error", "message": str(e)}

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

