import time
import traceback
import pepperapi as api
from pepperapi import ALVideoDevice, ALMotion, event, ALFaceDetection, ALGazeAnalysis, ALPeoplePerception, ALAutonomousLife, ALTextToSpeech
import pepperapi.robot_client as rc
from PIL import Image
import io
rc.init("192.168.0.147")
def look_straight():
    joints = ['HeadYaw', 'HeadPitch']
    print(ALMotion.getAngles(joints, True))
    print("---")
    ALMotion.setAngles(joints,[0,0],.2)    
    t = time.time()
    while time.time()-t < 1:
        print(ALMotion.getAngles(joints, False))

print(api.ALBasicAwareness.isRunning())
try:
    while True:
        time.sleep(.1)
except:
    pass

