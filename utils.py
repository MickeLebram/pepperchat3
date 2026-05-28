import os
import time
from apidefs import api
from syslogger import syslogger
from config import config

_has_tablet = None
def has_tablet():
    global _has_tablet
    if has_tablet is None:
        try:
            api.ALTabletService._ping()
            _has_tablet = True
        except api.robot_client.FunctionCallException:
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

