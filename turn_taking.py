import textwrap
from instruction_module import InstructionModule, ToolResult
import situation


STAY_SILENT_TOOL = {
    "type": "function",
    "name": "stay_silent",
    "description": (
        "Do not respond to the latest utterance. "
        "Use this when the speech was not directed at you, e.g. when people are talking to each other. "
        "When you call this tool, do not produce any text."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
    }
}


class GroupTurnTaking(InstructionModule):
    """For a room with several people, where not all speech is directed at the robot."""
    def __init__(self):
        super().__init__(
            situation_fields=[situation.TIME_SINCE_ROBOT_SPEECH_END, situation.PERSON_FACING_ROBOT],
            tools=[STAY_SILENT_TOOL],
        )
        self.instructions=textwrap.dedent(f"""\
            # Turn-taking rule

            You are participating in natural conversations with people in a shared physical environment.

            Not all speech you hear is directed at you. Before responding, determine whether the latest utterance was probably intended for you.

            Use two sources of information when making this determination:

            1. **Conversational context:** Consider what you last said, whether the latest utterance is a natural response or follow-up, whether someone explicitly addresses you or another person, and whether you are already engaged in an ongoing conversation.

            2. **Situation:** Consider {situation.format_situation_field_name_list(self.situation_fields)} in the situation message.

            Treat the situation information as supporting evidence, not strict requirements. A short elapsed time can suggest conversational continuity, particularly after you have asked a question. People can speak to you without facing you, and people can face you while speaking to someone else. Unknown values should not count as negative evidence.

            Conversational relevance alone does not establish that you are the intended recipient.

            During an active conversation, interpret natural follow-ups, brief answers, and acknowledgments as likely directed at you unless there is evidence to the contrary.

            When speech is clearly directed at someone else or belongs to a separate human conversation, do not respond: call the stay_silent tool and produce no text at all.

            When the intended recipient is uncertain, use the conversational context and the situation information to decide whether responding would be natural. Avoid unnecessarily interrupting human-to-human conversations, but do not require explicit addressing during an ongoing interaction.

            When you are addressed, respond promptly and naturally.
        """)

    def handle_tool_call(self, name, args, situation, query):
        return ToolResult({"status": "ok"}, silent=True)



class OneOnOneTurnTaking(InstructionModule):
    """For a single person talking to the robot. Asks for clarification when speech is unclear."""
    def __init__(self):
        super().__init__()
        self.instructions = textwrap.dedent("""\
            # Turn-taking rule

            You are talking with one person. All speech you hear is directed at you.

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
        """)
