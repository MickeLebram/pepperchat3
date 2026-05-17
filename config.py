from dataclasses import dataclass
import json
import os
from pathlib import Path
import traceback
import platformdirs
from PySide6.QtWidgets import (
    QApplication, QDialog, QGridLayout, QGroupBox, QLayout, QWidget, QVBoxLayout,
    QPushButton, QComboBox, QSlider,
    QLineEdit, QLabel
)
from PySide6.QtCore import QObject, QThread, QTimer, Qt, Signal

_appdir = Path(platformdirs.user_data_dir("PepperChat3"))
_logdir = _appdir / "logs"
for d in (_appdir, _logdir):
    d.mkdir(parents=True, exist_ok=True)

_config_fname = _appdir / "config.txt"

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
        self.robot_server_ip = "192.168.2.106"
        self.openai_api_key = ""
        self.last_browsed_anim = ""
    def save(self):
        _save_to_file(self, _config_fname)
    def get_prompt(self):
        if os.path.exists(self.cur_prompt_file):
            with open(self.cur_prompt_file,"r",encoding="utf8") as f:
                return f.read()
        return ""
    @property
    def logdir(self):
        return _logdir
    @property
    def appdir(self):
        return _appdir

config = Config()

try:
    _assign_from_file(config, _config_fname)
except:
    pass
    #traceback.print_exc()

print(config.__dict__)

def show_config_dlg(parent=None):
    print("show config")
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

    robot_server_ip = add_text("Robot Server IP", config.robot_server_ip)
    apikey = add_text("Openai API Key", config.openai_api_key)

    btn_apply = QPushButton("Apply")
    btn_cancel = QPushButton("Cancel")
    def apply():
        config.robot_server_ip = robot_server_ip.text()
        config.openai_api_key = apikey.text()
        config.save()
        dlg.close()
    btn_apply.clicked.connect(apply)
    btn_cancel.clicked.connect(dlg.close)

    layout.addWidget(btn_apply)
    layout.addWidget(btn_cancel)
    


    if standalone:
        dlg.show()
        standalone.exec()
    else:
        dlg.exec()

#show_config_dlg()