from typing import Callable, List

from apidefs import api, rc
import traceback
import defs
import threading, time, json, os
from datetime import datetime
from pepper_text_speaker import PepperTextSpeaker
import pcm_utils
import subtitles
from  oaichat_integrated import OaiChatIntegrated, Query
from situation import Situation
from turn_taking import GroupTurnTaking
from robot_modules import RobotActions, Look
import gui
from syslogger import syslogger
from config import config
from utils import AnimationRunner
from PIL import Image
import io

def main():
    syslogger.debug("main")
    gui.show_init_dialog()
    robot = api.ALSystem.robotName()
    print("robot", robot)

    pts = PepperTextSpeaker(subtitles.SubtitleServer())

    mute_mic_until = 0
    def mute_mic_a_while(dur):
        nonlocal mute_mic_until
        mute_mic_until = max(mute_mic_until, time.time() + dur)
    def ontouch(data):
        for sensor in data:
            bodypart, touched = sensor[:2]
            if touched and bodypart == "Head":
                syslogger.info("Head touched, please be quiet")
                mute_mic_a_while(3)
                oai.cancel_current()
                pts.stop_talking()
    api.event.TouchChanged.subscribe(ontouch)

    logfile = os.path.join(defs.LOG_DIR, datetime.now().strftime("dialogue_%Y-%m-%d_%H%M%S.log"))
    syslogger.info(f"Logging to {logfile}")
    

    def log_query(query:Query):
        entry = {
            'time': datetime.fromtimestamp(query.start_time).isoformat(),
            'user': query.query_text.strip(),
            'response': query.response_text.strip(),
            'duration': round(query.duration, 2)
        }
        with open(logfile, 'a', encoding='utf-8') as f:
            json.dump(entry, f, ensure_ascii=False)
            f.write(',\n')

    def on_query_update(query:Query):
        #print(query)
        if query.query_text and not query.response_text:
            syslogger.info(f"USER: {query.query_text.strip()}")
        if query.done:
            syslogger.info(query)
            log_query(query)


    def perform_robot_action(action:str):
        print("PERFORM:",action)
        if action == "wave":
            AnimationRunner.run("animations/Stand/Gestures/Hey_1")
        elif action == "shake your head":
            AnimationRunner.run("animations/Stand/Reactions/ShakeBody_1")
        elif action == "dance":
            if robot == "pepper": # OBS! Nao ramlar när den kör funny dancer
                AnimationRunner.run("animations/Stand/Waiting/FunnyDancer_1")
            else:
                AnimationRunner.run("animations/Stand/Waiting/KungFu_1")
        elif action == "play air guitar":
            AnimationRunner.run("animations/Stand/Waiting/AirGuitar_1")
    
    def get_head_cam_image() -> bytes:
        """Get jpeg bytes from an image captured with the head cam"""
        cam = api.ALVideoDevice.subscribeCamera("testcam", 0, 1, 11, 5)
        image_data = api.ALVideoDevice.getImageRemote(cam)
        width, height, pixels = image_data[0], image_data[1], image_data[6]
        api.ALVideoDevice.unsubscribe(cam)
        image = Image.frombytes("RGB", (width, height), pixels)
        file = defs.TMP_DIR / "head_cam_image.jpg"
        image.save(file)
        return open(file, "br").read()

    # Fields left as None are sent to the model as unknown
    situation = Situation()

    cleanups:List[Callable[[], None]] = [] # Called before exit
    def run_face_detection():
        # Face detection mainly finds faces turned towards the camera, so it works as a facing detector.
        # It reports about 10 times per second while a face is visible, and once with no faces when it's lost
        name = "PepperchatFacing"
        api.ALFaceDetection.subscribe(name)
        api.event.FaceDetected.subscribe(lambda faces: situation.record_facing(bool(faces)))

        def cleanup():
            api.ALFaceDetection.unsubscribe(name)
            print(f"ALFaceDetection unsubscribed {name}")
        cleanups.append(cleanup)
    run_face_detection()

    oai = OaiChatIntegrated(
        api_key=config.openai_api_key,
        conversation_prompt=config.get_prompt(),
        modules=[
            GroupTurnTaking(),
            RobotActions(["wave", "shake your head", "dance", "play air guitar"], perform_robot_action),
            Look(get_head_cam_image),
        ],
        situation=situation,
    )
    oai.query_update_callbacks.append(on_query_update)
    oai.intermediate_response_text_callbacks.append(pts.push_text)
    oai.silero.threshold = .5

    def run_eye_feedback():
        # Color shows whether a face is detected (green) or not (blue).
        # Brightness shows whether the robot is listening (full) or not (dim)
        api.ALAutonomousBlinking.setEnabled(False) # Blinking would override the eye color
        def loop():
            prev_color = None
            prev_update = 0
            while True:
                try:
                    brightness = 1 if oai.is_listening() else .15
                    color = (0, brightness, 0) if situation.is_facing() else (0, 0, brightness)
                    # Refresh now and then, in case something else (e.g. an animation) changed the eyes
                    if color != prev_color or time.time() - prev_update > 1:
                        api.ALLeds.fadeRGB("FaceLeds", *color, .1)
                        prev_color = color
                        prev_update = time.time()
                except Exception:
                    traceback.print_exc()
                time.sleep(.1)
        threading.Thread(target=loop, daemon=True).start()

        def cleanup():
            api.ALAutonomousBlinking.setEnabled(True)
        cleanups.append(cleanup)
    run_eye_feedback()

    def muter():
        was_speaking = False
        while True:
            speaking = pts.speaking
            if was_speaking and not speaking:
                situation.robot_speech_end_time = time.time()
            was_speaking = speaking
            if oai.state == oai.STATE_RECEIVING_RESPONSE or pts.speaking:
                mute_mic_a_while(.2)
            oai.set_listening(time.time() > mute_mic_until)
            time.sleep(.1)
    threading.Thread(target=muter, daemon=True).start()
    pcm_utils.listen_on_local_mic(24000,[oai.push_pcm16_frames])

    try:
        gui.run(oai)
    finally:
        for cleanup in cleanups:
            cleanup()

if __name__ == "__main__":
    main()
