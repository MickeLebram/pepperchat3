import math
from pathlib import Path
import threading
import time
from typing import Callable
from PySide6.QtWidgets import (
    QApplication, QGroupBox, QLayout, QWidget, QVBoxLayout,
    QPushButton, QComboBox, QSlider,
    QLineEdit, QLabel
)
from PySide6.QtCore import QObject, QThread, QTimer, Qt, Signal
import sys
from apidefs import api
import subtitles
SAVE_FILE = Path("settings.txt")

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

joint_names = []
def get_joint_angs():
    if not joint_names:
        joint_names.extend(api.ALMotion.getBodyNames("JointActuators"))
    angs = api.ALMotion.getAngles(joint_names, False)
    dct = {}
    for i, joint_name in enumerate(joint_names):
        dct[joint_name] = angs[i]
    return dct


class App(QWidget):
    def __init__(self):
        super().__init__()
        print(get_joint_angs())

        self.setWindowTitle("Qt Controls Example")

        self.name = QLineEdit()
        self.name.setPlaceholderText("Your name")
        layout = QVBoxLayout(self)
        
        def add_combo(layout:QLayout, name:str, options:list, selected_option, onchange:Callable):

            combo = QComboBox()
            combo.addItems(options)
            def chg(idx):
                combo.setEnabled(False)
                run_async_task(onchange, [options[idx]], lambda: combo.setEnabled(True))
            combo.setCurrentIndex(options.index(selected_option) if selected_option in options else 0)
            combo.currentIndexChanged.connect(chg)
            layout.addWidget(QLabel(name))
            layout.addWidget(combo)
            return combo
        def add_button(layout:QLayout, caption, onclick, args=None):
            btn = QPushButton(caption)
            def click():
                if args is not None:
                    onclick(args)
                else:
                    onclick()
            btn.clicked.connect(click)
            layout.addWidget(btn)
            return btn
        
        def add_slider(layout:QLayout, name:str, val:int, min:int, max:int, onchange:Callable[[int],None]=None):
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
            layout.addWidget(label)
            layout.addWidget(slider)
            return slider

        add_button(layout, "Apa", set_prompt, "You are a friendly monkey. Speak swedish.")
        add_button(layout, "Einstein", set_prompt, "You are a mad scientist. Speak swedish.")
        self.cur_volume = api.ALAudioDevice.getOutputVolume()
        slide_volume = add_slider(layout, "Volume", self.cur_volume, 0, 100)        

        add_combo(
            layout,
            "Autonomous Life State", 
            ["solitary", "interactive", "safeguard", "disabled"],
            api.ALAutonomousLife.getState(),
            lambda state: api.ALAutonomousLife.setState(state)
        )
        add_combo(
            layout,
            "Speech Language", 
            api.ALTextToSpeech.getAvailableLanguages(),
            api.ALTextToSpeech.getLanguage(),
            lambda lang: api.ALTextToSpeech.setLanguage(lang)
        )
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
        # print(api.ALMotion.s .getPostureList())
        add_button(layout, "Look straight", lambda: api.ALMotion.setAngles_1(['HeadYaw', 'HeadPitch'],[0,0],.25))
        for side in ("Right", "Left"):
            add_button(layout, f"Raise {side} Arm", lambda joint: api.ALMotion.setAngles_1(joint, -1.3, .25), side[0] + "ShoulderPitch")
            add_button(layout, f"Lower {side} Arm", lambda joint: api.ALMotion.setAngles_1(joint, 1.6, .25), side[0] + "ShoulderPitch")
        
        add_button(layout, "Restart subtitles", subtitles.try_show_on_tablet)
        if 0:
            label_joint_angs = QLabel()
            def update_joint_angs():
                lines = [f"{j}: {ang:.2f}" for j, ang in get_joint_angs().items()]
                label_joint_angs.setText("\n".join(lines))
            
            layout.addWidget(label_joint_angs)
            update_joint_angs()
            self.state_timer = QTimer(self)
            self.state_timer.timeout.connect(update_joint_angs)
            self.state_timer.start(500)

        def sparse_update():
            if self.cur_volume != slide_volume.value():
                self.cur_volume = slide_volume.value()
                api.ALAudioDevice.setOutputVolume(self.cur_volume)
        self.sparse_updater = QTimer(self)
        self.sparse_updater.timeout.connect(sparse_update)
        self.sparse_updater.start(100)

        save_button = QPushButton("Save")
        clear_button = QPushButton("Clear")


        save_button.clicked.connect(self.save)
        clear_button.clicked.connect(self.clear)

        layout.addWidget(self.name)
        layout.addWidget(save_button)
        layout.addWidget(clear_button)



    def save(self):
        pass
        # SAVE_FILE.write_text(
        #     f"name={self.name.text()}\n"
        #     f"color={self.combo_autonomous_life.currentText()}\n"
        #     f"volume={self.slider.value()}\n"
        # )

    def clear(self):
        self.name.clear()

        self.slider.setValue(50)

set_prompt:Callable[[str],None] = None
def run(set_prompt_callback):
    global set_prompt
    set_prompt = set_prompt_callback
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    api.robot_client.init("192.168.1.12")
    run()