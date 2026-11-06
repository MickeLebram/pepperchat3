import dataclasses
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable, Deque, List, Optional, Tuple
from query import Query

# A facing observation counts for this long unless a newer one says otherwise. Bridges short
# detection dropouts; assumes observations keep arriving while a person is facing the robot
FACING_HOLD_SECONDS = .5
# Facing the robot just before speaking also suggests addressing it
FACING_LEAD_IN_SECONDS = 1.0


@dataclass
class Situation:
    """What is going on around and with the robot. Kept up to date by the app. None means unknown."""
    robot_speech_end_time: Optional[float] = None # time.time() when the robot last stopped speaking
    robot_posture: Optional[str] = None
    # (time.time(), facing) observations from a detector, e.g. face detection. Use record_facing
    facing_observations: Deque[Tuple[float, bool]] = field(default_factory=lambda: deque(maxlen=1000))

    def __post_init__(self):
        self._lock = threading.Lock()

    def record_facing(self, facing:bool):
        with self._lock:
            self.facing_observations.append((time.time(), facing))

    def is_facing(self) -> bool:
        """Whether a person is facing the robot right now, with the same hold as facing_fraction."""
        now = time.time()
        return any(facing and now - observation_time <= FACING_HOLD_SECONDS
                   for observation_time, facing in list(self.facing_observations)[-20:])

    def facing_fraction(self, start_time:float, end_time:float, step:float = .1) -> Optional[float]:
        """Fraction of the time between start_time and end_time that a person was facing the robot.
        None if nothing has ever been observed, e.g. when no detector is running."""
        observations = list(self.facing_observations)
        if not observations or end_time <= start_time:
            return None
        # Only facing observations matter: a sample counts as facing if one was made within the hold time.
        # "Not facing" observations are ignored, so the hold also bridges dropouts that start with one
        facing_times = [observation_time for observation_time, facing in observations if facing]
        facing_samples = 0
        sample_count = 0
        i = -1 # Index of the latest facing observation at or before t
        t = start_time
        while t <= end_time:
            while i + 1 < len(facing_times) and facing_times[i + 1] <= t:
                i += 1
            if i >= 0 and t - facing_times[i] <= FACING_HOLD_SECONDS:
                facing_samples += 1
            sample_count += 1
            t += step
        return facing_samples / sample_count

    def update(self, **fields):
        """Sets several fields at once, so a snapshot never contains only some of them."""
        with self._lock:
            for name, value in fields.items():
                if name not in {f.name for f in dataclasses.fields(self)}:
                    raise AttributeError(f"Situation has no field {name}")
                setattr(self, name, value)

    def snapshot(self) -> "Situation":
        with self._lock:
            return dataclasses.replace(self, facing_observations=deque(self.facing_observations))


@dataclass(frozen=True)
class SituationField:
    """A value the model sees in the situation message."""
    name: str
    description: str # Explanation for the model
    get_value: Callable[[Situation, Query], Any] # Value at the given utterance. None means unknown


TIME_SINCE_ROBOT_SPEECH_END = SituationField(
    "time_since_robot_speech_end_seconds",
    "The elapsed time in seconds between the end of your last spoken turn and the beginning of the latest human utterance.",
    lambda situation, query: (None if situation.robot_speech_end_time is None
                              else max(0.0, query.start_time - situation.robot_speech_end_time)),
)

PERSON_FACING_ROBOT = SituationField(
    "person_facing_robot_fraction",
    "The fraction of time, from 0.0 to 1.0, that a person was facing you during the latest human utterance "
    "and the moment just before it. Detection can miss faces, so low values are weaker evidence than high ones.",
    lambda situation, query: situation.facing_fraction(query.start_time - FACING_LEAD_IN_SECONDS, time.time()),
)

ROBOT_POSTURE = SituationField(
    "robot_posture",
    "Your current body posture, e.g. Standing, Sitting or Crouching.",
    lambda situation, query: situation.robot_posture,
)


def format_situation_instructions(fields:List[SituationField]) -> str:
    lines = [
        "# Situation",
        "",
        "After each human utterance, a system message describes the current situation. It contains:",
    ]
    lines += [f"- {f.name}: {f.description}" for f in fields]
    lines += [
        "A value of unknown means the information is not available.",
        "",
        "The situation information is background awareness. Values come from sensors and may be inaccurate.",
        "",
        "Use each value only for the purpose described in the sections that refer to it.",
        "",
        "Do not mention the situation message, its field names or its values unless the user asks about what you perceive.",
        "",
        "Use only the situation information provided. Do not attempt to obtain missing information through tools or other actions.",
    ]
    return "\n".join(lines)


def _format_value(value) -> str:
    if value is None:
        return "unknown"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, float):
        return f"{value:.1f}"
    return str(value)


def format_situation_message(fields:List[SituationField], situation:Situation, query:Query) -> str:
    values = []
    for f in fields:
        try:
            value = f.get_value(situation, query)
        except Exception:
            value = None
        values.append(f"{f.name}={_format_value(value)}")
    return "Situation at the latest human utterance: " + "; ".join(values) + "."

def format_situation_field_name_list(fields:List[SituationField]):
    names = [sf.name for sf in fields]
    if not names:
        return ""
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]