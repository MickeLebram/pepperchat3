import os
import time
from apidefs import api

def connect_tablet():
    def connected():
        return api.ALTabletService.getWifiStatus() == "CONNECTED"
    if not connected():
        wifi_ssid = os.getenv('TABLET_WIFI_SSID')
        if wifi_ssid:
            print("Configuring tablet wifi:", wifi_ssid)
            api.ALTabletService.configureWifi(
                os.getenv('TABLET_WIFI_SECURITY', 'wpa'),
                wifi_ssid,
                os.getenv('TABLET_WIFI_PWD', '')
            )
            t = time.time()
            while not connected() and time.time() - t < 15:
                print(api.ALTabletService.getWifiStatus())
                time.sleep(.2)
    if connected():
        print("Tablet connected")
        return True
    print("Could not connect tablet. Check environment variables TABLET_WIFI_SSID, TABLET_WIFI_PWD and TABLET_WIFI_SECURITY" )
    return False
