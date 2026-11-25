import base64
import textwrap
from typing import Callable, List
from chat.instruction_module import InstructionModule, ToolResult
from syslogger import syslogger

class LookInstruction(InstructionModule):
    def __init__(self,
                 image_capture_callback:Callable[[], bytes], # Returns a JPEG image, ex. 640x480
                 confirmation_phrase:str = "Vänta, jag ska titta.", # Said if the model looks without saying anything first. None disables
                ):
        super().__init__()
        self.tools=[
            {
                "type": "function",
                "name": "look",
                "description": (
                    "Look with your eyes and see what is in front of you right now. "
                    "Use this when the user asks what you see, asks you to look at something, "
                    "or when seeing would help you answer. "
                    "Looking takes a moment, so before calling this tool, first say a short "
                    "phrase in the language of the conversation, e.g. \"Let me have a look\". "
                    "Talk about what you see as something you see yourself, not as a picture or photo. "
                    "Never claim to see something unless you used this tool."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {},
                }
            }
        ]
        self.image_capture_callback = image_capture_callback
        self.confirmation_phrase = confirmation_phrase

    def tool_call_started(self, name):
        return self.confirmation_phrase

    def handle_tool_call(self, name, args, situation, query):
        # The model always needs a new response to react to the image (or the failure)
        try:
            jpeg = self.image_capture_callback()
        except Exception as e:
            syslogger.exception("Image capture failed")
            return ToolResult({"status": "error", "message": str(e)}, needs_response=True)
        image_item = {
            "type": "message",
            "role": "user",
            "content": [{
                "type": "input_image",
                "image_url": "data:image/jpeg;base64," + base64.b64encode(jpeg).decode("ascii"),
            }],
        }
        return ToolResult(
            {"status": "ok", "message": "What you see right now follows in the next message."},
            followup_items=[image_item],
            needs_response=True,
        )
