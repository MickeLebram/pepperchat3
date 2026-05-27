import os
import time
from apidefs import api
from syslogger import syslogger
from config import config

def has_tablet():
    try:
        api.ALTabletService._ping()
    except api.robot_client.FunctionCallException:
        return False
    return True

def connect_tablet():
    def connected():
        return api.ALTabletService.getWifiStatus() == "CONNECTED"
    if not connected():

        if config.wifi_ssid and config.wifi_pwd:
            syslogger.info(f"Configuring tablet wifi: {config.wifi_ssid}")
            api.ALTabletService.configureWifi(
                config.wifi_security,
                config.wifi_ssid,
                config.wifi_pwd
            )
            t = time.time()
            while not connected() and time.time() - t < 15:
                time.sleep(.2)
    if connected():
        syslogger.info("Tablet connected")
        return True
    syslogger.warning("Could not connect tablet. Check environment variables TABLET_WIFI_SSID, TABLET_WIFI_PWD and TABLET_WIFI_SECURITY" )
    return False

