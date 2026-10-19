import time
from typing import List
from apidefs import api
from syslogger import syslogger
from config import config
import traceback
_has_tablet = None
def has_tablet():
    global _has_tablet
    if _has_tablet is None:
        try:
            api.ALTabletService._ping()
            _has_tablet = True
        except:
            _has_tablet =  False
    return _has_tablet

def tablet_connected():
    return api.ALTabletService.getWifiStatus() == "CONNECTED"

def connect_tablet():
    connected = tablet_connected()
    if not connected:

        if config.wifi_ssid and config.wifi_pwd:
            syslogger.info(f"Configuring tablet wifi: {config.wifi_ssid}")
            api.ALTabletService.configureWifi(
                config.wifi_security,
                config.wifi_ssid,
                config.wifi_pwd
            )
            t = time.time()
            while not connected and time.time() - t < 15:
                connected = tablet_connected()
                time.sleep(.2)
    if connected:
        syslogger.info("Tablet connected")
        return True
    syslogger.warning("Could not connect tablet. Check wifi credentials." )
    return False

class AnimationRunner:
    _current_anim: api.robot_client.RemoteFuture = None
    _animations: List[str] = []
    @classmethod
    def run(cls, path:str):
        cls.stop_current()
        def anim_done(fut):
            print("done", path)
        print("anim", path)
        cls._current_anim = api.robot_client.call_async(api.ALAnimationPlayer.run, path).on_done(anim_done)

    @classmethod
    def stop_current(cls):
        if cls._current_anim and cls._current_anim.is_running():
            cls._current_anim.cancel()
            print("canceling current")
            while cls._current_anim.is_running():
                print("waiting for current to stop running")
                time.sleep(.1)

    @classmethod
    def get_animations(cls) -> List[str]:
        if not cls._animations:
            cls._animations = api.ALAnimationPlayer._getAnimations()
        return cls._animations