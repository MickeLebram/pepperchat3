import base64
import textwrap
from typing import Callable, List
from chat.instruction_module import InstructionModule, ToolResult
from syslogger import syslogger

class ActionsInstruction(InstructionModule):
    def __init__(self,
                 action_names:List[str],
                 action_callback:Callable[[str], bool], # Performs the named action. Returns False if it can't be performed right now
                ):
        super().__init__(
            instructions=textwrap.dedent("""\
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

                User: "Hello there!"
                → You may call robot_action with action="wave"
                → Respond with something like "Hi! Nice to meet you."

                Never claim that you performed a physical action unless you used
                robot_action.
            """),
            tools=[{
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
                            "enum": action_names
                        }
                    },
                    "required": ["action"]
                }
            }],
        )
        self.action_callback = action_callback

    def handle_tool_call(self, name, args, situation, query):
        action = args["action"]
        if self.action_callback(action):
            return ToolResult({"status": "ok", "action": action})
        return ToolResult({"status": "not_performed", "action": action,
                           "message": "The action can't be performed right now."})
