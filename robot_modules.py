import base64
import textwrap
import threading
from typing import Callable, List
from instruction_module import InstructionModule, ToolResult
from situation import ROBOT_POSTURE
from syslogger import syslogger


ROBOT_ACTION_INSTRUCTIONS = textwrap.dedent(f"""\
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

    Consider {ROBOT_POSTURE.name} in the situation message. Some actions may not be possible in every posture.

    Never claim that you performed a physical action unless you used
    robot_action.
    """)

def _format_action_tool(actions:List[str]):
    return {
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
                    "enum": actions
                }
            },
            "required": ["action"]
        }
    }


class RobotActions(InstructionModule):
    def __init__(self,
                 action_names:List[str],
                 action_callback:Callable[[str], None], # Performs the named action
                ):
        super().__init__(
            instructions=ROBOT_ACTION_INSTRUCTIONS,
            situation_fields=[ROBOT_POSTURE],
            tools=[_format_action_tool(action_names)],
        )
        self.action_callback = action_callback

    def handle_tool_call(self, name, args, situation, query):
        action = args["action"]
        # Run in a thread so a long gesture doesn't delay the tool result
        threading.Thread(target=self.action_callback, args=(action,), daemon=True).start()
        return ToolResult({"status": "ok", "action": action})


LOOK_TOOL = {
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


class Look(InstructionModule):
    def __init__(self,
                 image_capture_callback:Callable[[], bytes], # Returns a JPEG image, ex. 640x480
                 confirmation_phrase:str = "Vänta, jag ska titta.", # Said if the model looks without saying anything first. None disables
                ):
        super().__init__(tools=[LOOK_TOOL])
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
