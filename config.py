import json
import os
from pathlib import Path
from typing import Callable
from PySide6.QtWidgets import QApplication, QComboBox, QDialog, QGridLayout,  QPushButton, QLineEdit, QLabel
import defs
import wifi

_config_fname = defs.APP_DIR / "system.cfg"

def _assign_from_file(obj:object, filename:str):
    with open(filename, "r", encoding="utf-8") as f:
        dct = json.loads(f.read())
        for key, val in obj.__dict__.items():
            obj.__dict__[key] = dct.get(key, val)
    return obj

def _save_to_file(obj:object, filename:str):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(obj.__dict__, indent=4))

class Config:
    def __init__(self):
        self.cur_prompt_file = ""
        self.robot_server_ip = ""
        self.openai_api_key = ""
        self.last_browsed_anim = ""
        self.wifi_ssid = ""
        self.wifi_security = ""
        self.wifi_pwd = ""
    def save(self):
        _save_to_file(self, _config_fname)
    def get_prompt(self):
        if os.path.exists(self.cur_prompt_file):
            with open(self.cur_prompt_file,"r",encoding="utf8") as f:
                return f.read()
        return ""
    @property
    def file(self):
        return _config_fname

config = Config()

try:
    _assign_from_file(config, _config_fname)
except:
    pass
    #traceback.print_exc()

def show_config_dlg(parent=None):
    standalone = QApplication() if not QApplication.instance() else None
    dlg = QDialog(parent=parent)
    layout = QGridLayout(dlg)
    dlg.setWindowTitle("Config")
    def add_text(caption, cur_text):
        ret = QLineEdit(text=cur_text)
        row_idx = layout.rowCount()+1
        layout.addWidget(QLabel(caption),row_idx,0)
        layout.addWidget(ret,row_idx,1)
        return ret
        
    def add_combo(name:str, options:list, selected_option, onchange:Callable[[int], None] = None):
        combo = QComboBox()
        combo.addItems(options)
        combo.setCurrentIndex(options.index(selected_option) if selected_option in options else 0)
        if onchange:
            combo.currentIndexChanged.connect(onchange)
        row_idx = layout.rowCount() + 1
        layout.addWidget(QLabel(name),row_idx, 0)
        layout.addWidget(combo,row_idx, 1)
        return combo
    robot_server_ip = add_text("Robot Server IP", config.robot_server_ip)
    apikey = add_text("Openai API Key", config.openai_api_key)
    wifis = wifi.list_wifi_networks()
    if config.wifi_ssid not in wifis:
        wifis.insert(0, config.wifi_ssid)
    combo_wifi_ssid = add_combo("Wifi ssid", wifis, config.wifi_ssid)
    combo_wifi_ssid.setEditable(True)
    combo_wifi_security = add_combo("Wifi security", ["wpa","wep","open"], config.wifi_security)
    txt_wifi_pwd = add_text("Wifi pwd", config.wifi_pwd)
    txt_wifi_pwd.setEchoMode(QLineEdit.Password)
    btn_apply = QPushButton("Apply")
    btn_cancel = QPushButton("Cancel")
    applied = False
    def apply():
        nonlocal applied
        config.robot_server_ip = robot_server_ip.text()
        config.openai_api_key = apikey.text()
        config.wifi_ssid = combo_wifi_ssid.currentText()
        config.wifi_security = combo_wifi_security.currentText()
        config.wifi_pwd = txt_wifi_pwd.text()
        config.save()
        dlg.close()
        applied = True
    btn_apply.clicked.connect(apply)
    btn_cancel.clicked.connect(dlg.close)

    layout.addWidget(btn_apply)
    layout.addWidget(btn_cancel)
    


    if standalone:
        dlg.show()
        standalone.exec()
    else:
        dlg.exec()
    return applied

if __name__ == "__main__":
    show_config_dlg()