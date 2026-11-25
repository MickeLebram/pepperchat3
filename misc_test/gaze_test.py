
import time
import threading
from typing import Callable, List
import pepperapi as api
import pepperapi.robot_client as rc
rc.init("192.168.0.147")

# Face analysis refines "looking at robot" using the face; try both True and False
FACE_ANALYSIS_ENABLED = True
TOLERANCE = None # 0..1, used only with face analysis. None keeps the robot's current value

cleanups:List[Callable[[], None]] = [] #Needs to be called before exit

def t():
    return f"{time.time():.2f}"

def run_gaze_analysis():
    name = "Testgaze"
    api.ALPeoplePerception.subscribe(name)
    api.ALGazeAnalysis.subscribe(name)
    api.ALGazeAnalysis.setFaceAnalysisEnabled(FACE_ANALYSIS_ENABLED)
    if TOLERANCE is not None:
        api.ALGazeAnalysis.setTolerance(TOLERANCE)
    print(f"Face analysis: {api.ALGazeAnalysis.isFaceAnalysisEnabled()}, tolerance: {api.ALGazeAnalysis.getTolerance()}")

    api.event.GazeAnalysis_PersonStartsLookingAtRobot.subscribe(
        lambda person_id: print(f"{t()} EVENT starts looking: {person_id}"))
    api.event.GazeAnalysis_PersonStopsLookingAtRobot.subscribe(
        lambda person_id: print(f"{t()} EVENT stops looking: {person_id}"))
    api.event.GazeAnalysis_PeopleLookingAtRobot.subscribe(
        lambda person_ids: print(f"{t()} EVENT looking at robot: {person_ids}"))

    def cleanup():
        api.ALGazeAnalysis.unsubscribe(name)
        api.ALPeoplePerception.unsubscribe(name)
        print(f"ALGazeAnalysis and ALPeoplePerception unsubscribed {name}")
    cleanups.append(cleanup)

def get_memory(key:str):
    try:
        return api.ALMemory.getData(key)
    except Exception:
        return None # The key doesn't exist (yet), e.g. for a person that was just lost

def set_eyes(r, g, b):
    api.ALAutonomousBlinking.setEnabled(False)
    api.ALLeds.fadeRGB("FaceLeds", r, g, b, .2)

def run_polling():
    def doit():
        prev_color = None
        prev_update = time.time()
        while True:
            visible = get_memory("PeoplePerception/VisiblePeopleList") or []
            looking_any = False
            parts = []
            for person_id in visible:
                prefix = f"PeoplePerception/Person/{person_id}"
                looking = get_memory(f"{prefix}/IsLookingAtRobot")
                score = get_memory(f"{prefix}/LookingAtRobotScore")
                looking_any = looking_any or bool(looking)
                score_text = f"{score:.2f}" if isinstance(score, float) else score
                parts.append(f"id={person_id} looking={looking} score={score_text}")
            print(f"{t()} visible={len(visible)} " + " | ".join(parts))

            if looking_any:
                color = (0, 1, 0) # Someone is looking at the robot
            elif visible:
                color = (0, 0, .3) # People seen, nobody looking
            else:
                color = (0, 0, 0) # Nobody seen
            if color != prev_color or time.time() - prev_update > 1:
                set_eyes(*color)
                prev_color = color
                prev_update = time.time()
            time.sleep(.2)
    threading.Thread(target=doit, daemon=True).start()

run_gaze_analysis()
run_polling()

try:
    while True:
        time.sleep(1)
finally:
    for cleanup in cleanups:
        cleanup()
