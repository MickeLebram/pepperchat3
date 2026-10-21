from apidefs import api, rc
import traceback
import defs
import threading, time, json, os
from datetime import datetime
from pepper_text_speaker import PepperTextSpeaker
import pcm_utils
import subtitles
from  oaichat_integrated import OaiChatIntegrated, Query
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
    
    def on_listening_state_change(listening):
        if listening:
            api.ALLeds.earLedsSetAngle(270, .01, True)
        else:
            api.ALLeds.earLedsSetAngle(90, .01, False)

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

    oai = OaiChatIntegrated(
        api_key=config.openai_api_key,
        conversation_prompt=config.get_prompt(),
        robot_action_names=["wave", "shake your head", "dance", "play air guitar"],
        robot_action_callback=perform_robot_action,
        image_capture_callback=get_head_cam_image
    )
    oai.query_update_callbacks.append(on_query_update)
    oai.intermediate_response_text_callbacks.append(pts.push_text)
    oai.listening_state_change_callbacks.append(on_listening_state_change)
    oai.silero.threshold = .5

    def muter():
        while True:
            if oai.state == oai.STATE_RECEIVING_RESPONSE or pts.speaking:
                mute_mic_a_while(.2)
            oai.set_listening(time.time() > mute_mic_until)
            time.sleep(.1)
    threading.Thread(target=muter, daemon=True).start()
    pcm_utils.listen_on_local_mic(24000,[oai.push_pcm16_frames])

    gui.run(oai)

if __name__ == "__main__":
    main()
