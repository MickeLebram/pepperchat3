from dataclasses import dataclass, field
from typing import List, Optional
from query import Query
from situation import Situation, SituationField


@dataclass
class ToolResult:
    output: dict # Sent to the model as the result of the tool call
    followup_items: List[dict] = field(default_factory=list) # Conversation items sent after the result, e.g. an image message
    needs_response: bool = False # The model must get a new response to react to the result
    silent: bool = False # The model chose not to respond to the utterance


class InstructionModule:
    """A section of the system instructions, together with the situation fields and tools it uses."""

    def __init__(self,
                 instructions:str = "", # Flush-left text, placed inside <system_instructions>
                 situation_fields:List[SituationField] = None,
                 tools:List[dict] = None,
                ):
        self.instructions = instructions
        self.situation_fields = situation_fields or []
        self.tools = tools or []

    def handle_tool_call(self, name:str, args:dict, situation:Situation, query:Query) -> ToolResult:
        """Called on a worker thread when the model calls one of the module's tools."""
        return ToolResult({"status": "error", "message": f"Unhandled tool: {name}"})

    def tool_call_started(self, name:str) -> Optional[str]:
        """Called as soon as the model starts calling one of the module's tools.
        May return a phrase to say, used if the response has no text yet."""
        return None
