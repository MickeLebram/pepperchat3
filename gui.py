import math
import os
from pathlib import Path
import threading
import time
from typing import Callable
from PySide6.QtWidgets import (
    QApplication, QFileDialog, QGridLayout, QGroupBox, QLayout, QMessageBox, QWidget, QVBoxLayout,
    QPushButton, QComboBox, QSlider,
    QLineEdit, QLabel
)
from PySide6.QtCore import QObject, QThread, QTimer, Qt, Signal
import sys
from apidefs import api
import subtitles
from config import config
from config import show_config_dlg

class Task(QObject):
    done = Signal()
    def __init__(self, func, args):
        super().__init__()
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)
        self.done.emit()

def run_async_task(func, args, ondone):
    task = Task(func, args)
    thread = QThread()
    task.moveToThread(thread)
    thread.started.connect(task.run)
    def done():
        thread.quit()
        task.deleteLater()
        thread.deleteLater()
        ondone()
    task.done.connect(done)
    thread.start()


def show_msg(owner, msg:str):
    msgBox = QMessageBox(owner)
    msgBox.setText(msg)
    msgBox.exec()    

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PepperChat3")

        layout = QGridLayout(self)
        
        def add_combo(layout:QGridLayout, name:str, options:list, selected_option, onchange:Callable):

            combo = QComboBox()
            combo.addItems(options)
            def chg(idx):
                combo.setEnabled(False)
                run_async_task(onchange, [options[idx]], lambda: combo.setEnabled(True))
            combo.setCurrentIndex(options.index(selected_option) if selected_option in options else 0)
            combo.currentIndexChanged.connect(chg)
            row_idx = layout.rowCount() + 1
            layout.addWidget(QLabel(name),row_idx, 0)
            layout.addWidget(combo,row_idx, 1)
            return combo
        
        def add_button(layout:QGridLayout, caption, onclick, args=None):
            btn = QPushButton(caption)
            def click():
                if args is not None:
                    onclick(args)
                else:
                    onclick()
            btn.clicked.connect(click)
            layout.addWidget(btn)
            return btn
        
        def add_slider(layout:QGridLayout, name:str, val:int, min:int, max:int, onchange:Callable[[int],None]=None):
            label = QLabel()
            def update_label():
                label.setText(f"{name}: {slider.value()}")
            slider = QSlider(Qt.Horizontal)
            slider.setRange(min, max)
            slider.setValue(val)
            def change(v):
                if onchange:
                    onchange(v)
                update_label()
            update_label()
            slider.valueChanged.connect(change)
            row_idx = layout.rowCount() + 1
            layout.addWidget(label, row_idx, 0)
            layout.addWidget(slider, row_idx, 1)
            return slider

        def update_btn_prompt():
            caption = config.cur_prompt_file if os.path.exists(config.cur_prompt_file) else "Load prompt"
            maxlen = 40
            if len(caption) > maxlen:
                caption = "..." + caption[-maxlen:]
            btn_prompt.setText(caption)
        def browse_prompts():
            start_path = config.cur_prompt_file if config.cur_prompt_file else str(config.appdir.absolute())
            fname = QFileDialog.getOpenFileName(self, "Play Animation", start_path, "Text files (*.*)")[0]
            if not fname:
                return
            config.cur_prompt_file = fname
            config.save()
            update_btn_prompt()
            reload_prompt()
        btn_prompt = add_button(layout, "Load", browse_prompts)
        layout.addWidget(btn_prompt, 0,0,1,2)
        update_btn_prompt()
        self.cur_volume = api.ALAudioDevice.getOutputVolume()
        slide_volume = add_slider(layout, "Volume", self.cur_volume, 0, 100)        
        self.cur_tts_speed = api.ALTextToSpeech.getParameter("speed")
        slide_tts_speed = add_slider(layout, "Speech speed", self.cur_tts_speed, 50, 200)        
        add_combo(
            layout,
            "Speech Language", 
            api.ALTextToSpeech.getAvailableLanguages(),
            api.ALTextToSpeech.getLanguage(),
            lambda lang: api.ALTextToSpeech.setLanguage(lang)
        )

        add_combo(
            layout,
            "Autonomous Life State", 
            ["solitary", "interactive", "safeguard", "disabled"],
            api.ALAutonomousLife.getState(),
            lambda state: api.ALAutonomousLife.setState(state)
        )
        add_button(layout, "System config", show_config_dlg, self)
        add_button(layout, "Restart subtitles", subtitles.try_show_on_tablet)
        group_posture = QGroupBox("Postures")
        group_posture.setLayout(QVBoxLayout())
        layout.addWidget(group_posture)
        for posture in api.ALRobotPosture.getPostureList():
            def set_posture(p):
                group_posture.setEnabled(False)
                run_async_task(
                    api.ALRobotPosture.goToPosture,
                    [p,1],
                    lambda: group_posture.setEnabled(True)
                )
            add_button(
                group_posture.layout(),
                posture,
                lambda args: set_posture(args[0]),
                [posture]
            )
        group_motion = QGroupBox("Motion")
        group_motion.setLayout(QVBoxLayout())
        layout.addWidget(group_motion)
        add_button(group_motion.layout(), "Look straight", lambda: api.ALMotion.setAngles_1(['HeadYaw', 'HeadPitch'],[0,0],.25))
        def browse_animations():
            anim_root = os.path.abspath("animations")
            stand_path = os.path.abspath(anim_root+"/Stand")
            def valid(fname:str, show_reject_reason = False):
                print("fname",fname)
                p = Path(fname)
                reject = ""
                if not (p.exists() and Path(stand_path) in p.parents):
                    reject = "Invalid path, need to be child of\n" + stand_path
                elif "loop" in fname.lower():
                    reject = "Looped animations are currently not allowed"
                if reject:
                    if show_reject_reason:
                        show_msg(self, reject)
                    return False
                return True
                
            start_path = config.last_browsed_anim if valid(config.last_browsed_anim) else stand_path
            fname = QFileDialog.getOpenFileName(self, "Play Animation", start_path, "Animations (*.anim)")[0]
            if not fname:
                return
            fname = os.path.abspath(fname)
            if valid(fname, True):
                def run_anim(a):
                    try:
                        api.ALAnimationPlayer.run(a)
                        config.last_browsed_anim = fname
                        config.save()
                    except Exception as e:
                        show_msg(self,str(e))
                anim = fname.removeprefix(os.path.dirname(anim_root)).replace("\\","/").removesuffix(".anim")[1:]
                # run_anim(anim)
                btn_animations.setEnabled(False)
                run_async_task(run_anim, [anim], lambda: btn_animations.setEnabled(True))

        btn_animations = add_button(group_motion.layout(), "Animations...", browse_animations)

        def sparse_update():
            if self.cur_volume != slide_volume.value():
                self.cur_volume = slide_volume.value()
                api.ALAudioDevice.setOutputVolume(self.cur_volume)
            if self.cur_tts_speed != slide_tts_speed.value():
                self.cur_tts_speed = slide_tts_speed.value()
                api.ALTextToSpeech.setParameter("speed", self.cur_tts_speed)
        self.sparse_updater = QTimer(self)
        self.sparse_updater.timeout.connect(sparse_update)
        self.sparse_updater.start(100)

reload_prompt:Callable[[],None] = None
def run(reload_prompt_callback):
    global reload_prompt
    reload_prompt = reload_prompt_callback
    app = QApplication.instance() if QApplication.instance() else QApplication()
    window = App()
    window.show()
    sys.exit(app.exec())
    