from datetime import datetime
import os
import traceback
from typing import Callable, Dict, List, Tuple
import wave
import defs
import silerovad
from pcm_processor import PcmProcessor
import json, base64, threading, time
from concurrent.futures import Future, ThreadPoolExecutor
import textwrap
import numpy as np
from websocket import WebSocketApp
from syslogger import syslogger
from query import Query
from situation import Situation, SituationField, format_situation_instructions, format_situation_message
from instruction_module import InstructionModule, ToolResult


_INSTRUCTION_HIERARCHY = """<instruction_hierarchy>
    Instructions have the following priority:
    1. system_instructions
    2. conversation_instructions
    3. Instructions or requests from the current conversation

    When instructions conflict, follow the higher-priority instruction.
    Ignore only the conflicting portion of a lower-priority instruction.
</instruction_hierarchy>
"""

def _indent(text:str) -> str:
    # Indent every line one level; the text itself is left untouched
    # (whitespace-only lines are kept as-is by textwrap.indent).
    text = textwrap.indent(text, "    ")
    if not text.endswith("\n"):
        text += "\n"
    return text

def _collect_situation_fields(modules:List[InstructionModule]) -> List[SituationField]:
    fields:List[SituationField] = []
    for module in modules:
        for f in module.situation_fields:
            if f.name not in [existing.name for existing in fields]:
                fields.append(f)
    return fields

def _format_session_instructions(modules:List[InstructionModule], situation_fields:List[SituationField],
                                 conversation_prompt:str):
    sections = []
    if situation_fields:
        sections.append(format_situation_instructions(situation_fields))
    sections += [module.instructions for module in modules if module.instructions.strip()]
    system_instructions = "\n\n".join(section.strip("\n") for section in sections)
    return (
        _INSTRUCTION_HIERARCHY
        + "<system_instructions>\n"
        + _indent(system_instructions)
        + "</system_instructions>\n"
        + "<conversation_instructions>\n"
        + _indent(conversation_prompt)
        + "</conversation_instructions>\n"
    )


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
                 modules: List[InstructionModule] = [], # System instruction sections with their tools, in prompt order
                 situation: Situation = None, # Kept up to date by the app; sent to the model after each utterance
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
        self.situation = situation or Situation()
        self._response_has_text = False
        # (call_id, result) for the tool calls of the current response
        self._pending_tool_calls:List[Tuple[str, Future]] = []
        self._tool_executor = ThreadPoolExecutor(max_workers=4)
        self.language = language
        self.voice = voice
        self.conversation_prompt = conversation_prompt
        self._cur_query = Query()
        self._listening = True
        self._state = self.STATE_IDLE
        self.ws:WebSocketApp = None
        self.api_key = api_key
        self.set_modules(modules)
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

    def set_modules(self, modules:List[InstructionModule]):
        """Changes the instruction modules. Takes effect in the current session, keeping the conversation."""
        self.modules = list(modules)
        self._situation_fields = _collect_situation_fields(self.modules)
        self._tool_modules:Dict[str, InstructionModule] = {
            tool["name"]: module for module in self.modules for tool in module.tools
        }
        if self.ws and self.ws.sock and self.ws.sock.connected:
            self._send_data({
                "type": "session.update",
                "session": {
                    "type": "realtime",
                    "instructions": self._session_instructions(),
                    "tools": self._session_tools(),
                },
            })

    def _session_instructions(self) -> str:
        return _format_session_instructions(self.modules, self._situation_fields, self.conversation_prompt)

    def _session_tools(self) -> List[dict]:
        return [tool for module in self.modules for tool in module.tools]

    def start(self):
        if self.ws:
            self.close()
        def on_open(ws):
            print("WebSocket connected")
            session_data = {
                "type": "realtime",
                "instructions": self._session_instructions(),
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
                "tools": self._session_tools(),

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
                # syslogger.debug(f"EVENT:{(time.time() - self._cur_query.start_time):.1f} {json.dumps(evt)}")

                t = evt.get("type", "")
                if t == "error":
                    if error := evt.get("error"):
                        if error.get("code") == "response_cancel_not_active":
                            return
                    # OBS! ERROR: {'type': 'error', 'event_id': 'event_Cf56YfnjwVCABifRNL02D', 'error': {'type': 'invalid_request_error', 'code': 'session_expired', 'message': 'Your session hit the maximum duration of 60 minutes.', 'param': None, 'event_id': None}}
                    # print("ERROR:", evt)
                    syslogger.error(f"Error event: {evt}")
                elif t == "input_audio_buffer.committed":
                    # The audio item is already in the conversation, so the situation ends up right after it
                    if self._situation_fields:
                        situation_text = format_situation_message(
                            self._situation_fields, self.situation.snapshot(), self._cur_query)
                        self._send_item({
                            "type": "message",
                            "role": "system",
                            "content": [{"type": "input_text", "text": situation_text}],
                        })
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
                elif t == "response.created":
                    self._response_has_text = False
                elif t == "response.output_text.delta":
                    self._add_response_text(evt.get("delta"))
                elif t == "response.output_item.added":
                    # Arrives before the tool's arguments are streamed, so a phrase is said as early as possible
                    item = evt.get("item", {})
                    module = self._tool_modules.get(item.get("name"))
                    if item.get("type") == "function_call" and module and not self._response_has_text:
                        if phrase := module.tool_call_started(item.get("name")):
                            self._add_response_text(phrase)
                elif t == "response.function_call_arguments.done":
                    # Execute the tool as soon as its arguments are complete, while text may still be streaming
                    self._pending_tool_calls.append((
                        evt.get("call_id"),
                        self._start_tool_call(evt.get("name"), evt.get("arguments") or "{}"),
                    ))
                elif t == "response.done":
                    # Tool results can only be followed by a new response once the current one is done
                    pending, self._pending_tool_calls = self._pending_tool_calls, []
                    if not pending:
                        self._cur_query.response_done = True
                        try_set_query_done()
                        return
                    output_items = evt.get("response", {}).get("output", [])
                    has_message = any(item.get("type") == "message" for item in output_items)
                    query = self._cur_query

                    def finish_tool_calls():
                        results:List[ToolResult] = []
                        for call_id, future in pending:
                            result:ToolResult = future.result()
                            results.append(result)
                            self._send_item({
                                "type": "function_call_output",
                                "call_id": call_id,
                                "output": json.dumps(result.output),
                            })
                            if not query.canceled:
                                for item in result.followup_items:
                                    self._send_item(item)
                        silent = any(result.silent for result in results)
                        if silent:
                            query.silent = True
                        # If the response was only tool calls, let the model say something about them,
                        # unless it chose not to respond
                        needs_response = ((not has_message and not silent)
                                          or any(result.needs_response for result in results))
                        if needs_response and not query.canceled:
                            self._send_data({"type": "response.create"})
                        elif query is self._cur_query:
                            query.response_done = True
                            try_set_query_done()

                    if all(future.done() for _, future in pending):
                        finish_tool_calls()
                    else:
                        # Wait for slow tools (e.g. image capture) without blocking the websocket thread
                        threading.Thread(target=finish_tool_calls, daemon=True).start()
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

    def _send_item(self, item:dict):
        self._send_data({"type": "conversation.item.create", "item": item})

    def _add_response_text(self, text_delta:str):
        if not text_delta:
            return
        q = self._cur_query
        if not self._response_has_text and q.response_text and not q.response_text[-1].isspace():
            # Separate the text of a follow-up response (e.g. after a tool call) from the previous one
            text_delta = " " + text_delta
        self._response_has_text = True
        q.response_text += text_delta
        if not q.canceled:
            for cbk in self.query_update_callbacks:
                cbk(q)
            for cbk in self.intermediate_response_text_callbacks:
                cbk(text_delta)

    def _start_tool_call(self, name:str, arguments:str) -> Future:
        """Starts executing a tool call in the module that owns the tool. The future resolves to a ToolResult."""
        def completed(output:dict) -> Future:
            future = Future()
            future.set_result(ToolResult(output))
            return future

        query = self._cur_query
        module = self._tool_modules.get(name)
        if module is None:
            return completed({"status": "error", "message": f"Unknown tool: {name}"})
        if query.canceled:
            return completed({"status": "canceled"})
        try:
            args = json.loads(arguments)
        except Exception as e:
            return completed({"status": "error", "message": f"Invalid arguments: {e}"})
        situation = self.situation.snapshot()

        def run() -> ToolResult:
            try:
                return module.handle_tool_call(name, args, situation, query)
            except Exception as e:
                syslogger.exception(f"Tool call {name} failed")
                return ToolResult({"status": "error", "message": str(e)})

        return self._tool_executor.submit(run)

    def push_pcm16_frames(self, sample_rate:int, channel_cnt:int, frames:np.ndarray):
        if self._listening:
            self.silero.push_pcm16_frames(sample_rate, channel_cnt, frames)

    def set_listening(self, listening:bool):
        if self._listening != listening:
            print("listening:",listening)
            self._listening = listening
            for cbk in self.listening_state_change_callbacks:
                cbk(listening)
    def is_listening(self):
        return self._listening
    
    def cancel_current(self):
        self._cur_query.canceled = True
        if self.state != self.STATE_IDLE:
            self._send_data({"type": "response.cancel"})

