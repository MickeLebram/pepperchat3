
from dataclasses import dataclass, replace
import os
import time
import traceback
from typing import Callable, List
import pepperapi as api
import pepperapi.robot_client as rc
import threading
rc.init("192.168.0.147")

@dataclass
class FaceDetectionState:
    facing:bool = False

cur_state = FaceDetectionState()
last_detection_time = 0
cleanups:List[Callable[[], None]] = [] #Needs to be called before exit
def run_face_detection():
    name = "Testfejs"
    api.ALFaceDetection.subscribe(name)
    def on_face_detected(x):
        global last_detection_time
        print(f"{time.time():.2f} {'FACE' if x else 'empty'}")
        if x:
            last_detection_time = time.time()        

    api.event.FaceDetected.subscribe(on_face_detected)

    def cleanup():
        api.ALFaceDetection.unsubscribe(name)
        print(f"ALFaceDetection.unsubscribed {name}")
    cleanups.append(cleanup)

def run_eye_feedback():
    def doit():
        prev_state = replace(cur_state)
        prev_update = time.time()
        while True:
            cur_state.facing = time.time() - last_detection_time < 1.0
            if time.time() - prev_update > 1 or prev_state.facing != cur_state.facing:
                r = 0
                g = 1 if cur_state.facing else 0
                b = 0
                api.ALAutonomousBlinking.setEnabled(False)
                api.ALLeds.fadeRGB("FaceLeds", r, g, b, .2)
                prev_state = replace(cur_state)
                prev_update = time.time()
            time.sleep(.1)
    threading.Thread(target=doit, daemon=True).start()

run_face_detection()
run_eye_feedback()

try:
    while True:
        time.sleep(.1)
finally:
    for cleanup in cleanups:
        cleanup()