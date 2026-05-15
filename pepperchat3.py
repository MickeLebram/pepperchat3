from apidefs import api
import traceback
import dotenv
dotenv.load_dotenv()
import threading, time, json, os
from datetime import datetime
from pepper_text_speaker import PepperTextSpeaker
import pcm_utils
import subtitles
import utils
from  oaichat_integrated import OaiChatIntegrated, Query
from pathlib import Path
from platformdirs import user_data_dir
from config import config
ROBOT_SERVER_IP = "192.168.0.147" # Nao Mickes kontor
#ROBOT_SERVER_IP = "192.168.1.12" # Pepper lab
ROBOT_SERVER_IP = "192.168.2.106" # Pepper shc
api.robot_client.init(config.robot_server_ip)

LOGDIR = Path(user_data_dir("Pepperchat")) / "logs"

"""
GUI
Volym
Autonomous life på av
Apply postures
"""

def main():
    
    try:
        api.ALTextToSpeech.setLanguage(os.getenv('LANGUAGE', 'Swedish'))
    except:
        traceback.print_exc()

    pts = PepperTextSpeaker(subtitles.SubtitleServer())

    #pts.push_text("Det enda ja äter, är sill o puttäter. Sillsillsill och puttputtputtäter.")
    pts.push_text("Hej")
    mute_mic_until = 0
    def mute_mic_a_while(dur):
        nonlocal mute_mic_until
        mute_mic_until = max(mute_mic_until, time.time() + dur)
    def ontouch(data):
        for sensor in data:
            bodypart, touched = sensor[:2]
            if touched and bodypart == "Head":
                print("STFU")
                mute_mic_a_while(3)
                oai.cancel_current()
                pts.stop_talking()
    api.event.TouchChanged.subscribe(ontouch)

    logdir = os.path.join(os.path.dirname(__file__), 'logs')
    os.makedirs(logdir, exist_ok=True)
    logfile = os.path.join(logdir, datetime.now().strftime('dialogue_%Y-%m-%d_%H%M%S.log'))
    print('Logging to', logfile)

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
            print("USER:", query.query_text.strip())
        if query.done:
            print(query)
            log_query(query)
    
    def on_listening_state_change(listening):
        if listening:
            api.ALLeds.earLedsSetAngle(270, .01, True)
        else:
            api.ALLeds.earLedsSetAngle(90, .01, False)

    oai = OaiChatIntegrated(
        system_prompt=os.getenv('PROMPT', ''),
        query_update_callback = on_query_update,
        state_callback=print,
        intermediate_response_text_callback=pts.push_text,
        listening_state_change_callback=on_listening_state_change
    )
    oai.silero.threshold = .5
    

    def muter():
        while True:
            if oai.state == oai.STATE_RECEIVING_RESPONSE or pts.speaking:
                mute_mic_a_while(.2)
            oai.set_listening(time.time() > mute_mic_until)
            time.sleep(.1)
    threading.Thread(target=muter, daemon=True).start()
    pcm_utils.listen_on_local_mic(48000,[oai.push_pcm16_frames])
    def set_system_prompt(prompt:str):
        oai.system_prompt = prompt
        oai.start()

    import gui
    gui.run(set_system_prompt)
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     pass
    
if __name__ == "__main__":
    main()
