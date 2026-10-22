import time

from pepperapi import ALVideoDevice, ALMotion
import pepperapi.robot_client as rc
from PIL import Image
import io
#rc.init("192.168.0.147")
rc.init("192.168.1.12")
def look_straight():
    joints = ['HeadYaw', 'HeadPitch']
    print(ALMotion.getAngles(joints, True))
    print("---")
    ALMotion.setAngles(joints,[0,0],.2)    
    t = time.time()
    while time.time()-t < 1:
        print(ALMotion.getAngles(joints, False))

look_straight()
