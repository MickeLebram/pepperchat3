import json
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication, QDialog, QGridLayout,  QPushButton, QLineEdit, QLabel
import dirs

_config_fname = dirs.APP_DIR / "system.cfg"

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

    robot_server_ip = add_text("Robot Server IP", config.robot_server_ip)
    apikey = add_text("Openai API Key", config.openai_api_key)

    btn_apply = QPushButton("Apply")
    btn_cancel = QPushButton("Cancel")
    applied = False
    def apply():
        nonlocal applied
        config.robot_server_ip = robot_server_ip.text()
        config.openai_api_key = apikey.text()
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

