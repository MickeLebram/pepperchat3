import logging
import math
import os
from pathlib import Path
import threading
import time
import traceback
from typing import Callable
from PySide6.QtWidgets import (
    QApplication, QDialog, QFileDialog, QGridLayout, QGroupBox, QLayout, QMessageBox, QPlainTextEdit, QTextEdit, QTreeView, QWidget, QVBoxLayout,
    QPushButton, QComboBox, QSlider,
    QLineEdit, QLabel
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QObject, QThread, QTimer, Qt, Signal, Slot
import sys
from apidefs import api
import defs
import subtitles
from config import config
from config import show_config_dlg
from oaichat_integrated import OaiChatIntegrated, Query
from syslogger import syslogger
_active_tasks = []


class Task(QObject):
    done = Signal()
    error = Signal(Exception)

    def __init__(self, func, args=()):
        super().__init__()
        self.func = func
        self.args = args

    @Slot()
    def run(self):
        try:
            self.func(*self.args)
        except Exception as e:
            self.error.emit(e)
            traceback.print_exc()
        finally:
            self.done.emit()


def run_async_task(func, args=(), ondone=None, onerror=None):
    task = Task(func, args)
    thread = QThread()

    # keep both alive
    _active_tasks.append((thread, task))

    task.moveToThread(thread)

    thread.started.connect(task.run)

    def handle_done():
        if ondone:
            ondone()
        thread.quit()

    def handle_error(e):
        if onerror:
            onerror(e)
        else:
            print("Task error:", e)

    def cleanup():
        try:
            _active_tasks.remove((thread, task))
        except ValueError:
            pass

    task.done.connect(handle_done)
    task.error.connect(handle_error)

    thread.finished.connect(task.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.finished.connect(cleanup)

    thread.start()
    return thread

def show_msg(owner, msg:str):
    msgBox = QMessageBox(owner)
    msgBox.setText(msg)
    msgBox.exec()    


class ChatDisplay(QTextEdit):
    class QueryWorker(QObject):
        signal_query = Signal(Query)
    def __init__(self, oai:OaiChatIntegrated):
        super().__init__()
        self.worker = ChatDisplay.QueryWorker()
        self.worker.moveToThread(self.thread())

        def append(q:Query):
            if q.done:
                self.append(f"<i>{q.query_text}</i>")
                self.append(f"{q.response_text}\n")
        self.worker.signal_query.connect(append)
        oai.query_update_callbacks.append(lambda q:self.worker.signal_query.emit(q))

class LogEmitter(QObject):
    log_message = Signal(str)

class LogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.emitter = LogEmitter()

    def emit(self, record):
        try:
            msg = self.format(record)
            self.emitter.log_message.emit(msg)
        except Exception:
            self.handleError(record)


class LogViewer(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logs")

        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.log_view)
        handler = LogHandler()
        handler.setFormatter(logging.Formatter(
            "%(asctime)s.%(msecs)03d "
            "[%(filename)s:%(lineno)d] "
            "%(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))
        syslogger.addHandler(handler)
        handler.emitter.log_message.connect(self.log_view.appendPlainText)

class AnimationBrowser(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setWindowTitle("Animation Browser")
        layout = QVBoxLayout(self)
        self.tree = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Animations"])

        self.tree.setModel(self.model)
        self.tree.clicked.connect(self.on_item_clicked)
        self.tree.doubleClicked.connect(self.on_item_doubleclicked)
        layout.addWidget(self.tree)
        self.btn_play = QPushButton("Play")
        self.btn_play.clicked.connect(self.play_selected)
        layout.addWidget(self.btn_play)
        self.resize(600,400)
        def populate():
            root = self.model.invisibleRootItem()
            nodes = {}
            # Skip loops until we know how to terminate them without robot reboot
            def allowed(anim_path:str):
                name = anim_path.split("/")[-1]
                if "loop" in name.lower():
                    return False
                return True

            for anim_path in api.ALAnimationPlayer._getAnimations_1():
                if allowed(anim_path):
                    parent = root
                    current_path = ""
                    for part in anim_path.split("/"):
                        current_path = f"{current_path}/{part}" if current_path else part

                        if current_path not in nodes:
                            item = QStandardItem(part)
                            item.setEditable(False)
                            item.setData(current_path, Qt.UserRole)

                            parent.appendRow(item)
                            nodes[current_path] = item

                        parent = nodes[current_path]
        populate()
        self.tree.expandToDepth(1)
    
    def play_selected(self):
        if not self.tree.selectedIndexes():
            return
        item = self.model.itemFromIndex(self.tree.selectedIndexes()[0])
        if item.rowCount() != 0:
            return
        path = item.data(Qt.UserRole)
        def doit(a):
            try:
                api.ALAnimationPlayer.run(a)
                config.last_browsed_anim = path
                config.save()
            except Exception as e:
                show_msg(self,str(e))
        self.setEnabled(False)
        run_async_task(doit, [path], lambda: self.setEnabled(True))  
    
    def on_item_clicked(self, index):
        self.btn_play.setEnabled(self.model.itemFromIndex(index).rowCount() == 0)
    
    def on_item_doubleclicked(self, index):
        if self.model.itemFromIndex(index).rowCount() == 0:
            self.play_selected()

class MainWindow(QWidget):
    def __init__(self, oai:OaiChatIntegrated):
        super().__init__()
        self.oai = oai
        robot_connected = api.robot_client.robot_connected()
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
            start_path = config.cur_prompt_file if os.path.exists(config.cur_prompt_file) else str(defs.APP_DIR.absolute())
            fname = QFileDialog.getOpenFileName(self, "Play Animation", start_path, "Text files (*.*)")[0]
            if not fname:
                return
            if Path(fname) == Path(config.file):
                print(fname, config.file)
                show_msg(self, "Never share this file")
                return
            config.cur_prompt_file = fname
            config.save()
            update_btn_prompt()
            oai.set_system_prompt(config.get_prompt())
        btn_prompt = add_button(layout, "Load", browse_prompts)
        layout.addWidget(btn_prompt, 0,0,1,2)
        update_btn_prompt()
        self.cur_volume = api.ALAudioDevice.getOutputVolume() if robot_connected else 0
        slide_volume = add_slider(layout, "Volume", self.cur_volume, 0, 100)        
        self.cur_tts_speed = api.ALTextToSpeech.getParameter("speed") if robot_connected else 0
        slide_tts_speed = add_slider(layout, "Speech speed", self.cur_tts_speed, 50, 200)        
        add_combo(
            layout,
            "Speech Language", 
            api.ALTextToSpeech.getAvailableLanguages() if robot_connected else [],
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
        self.logview = LogViewer()
        add_button(layout, "System config", show_config_dlg, self)
        add_button(layout, "Log viewer", self.logview.show)
        add_button(layout, "Restart subtitles", subtitles.try_show_on_tablet)
        group_posture = QGroupBox("Postures")
        group_posture.setLayout(QVBoxLayout())
        layout.addWidget(group_posture)
        if robot_connected:
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
                AnimationBrowser(self).show()

            add_button(group_motion.layout(), "Animations...", browse_animations)

        chat_display = ChatDisplay(oai)
        # chat_display.append('<span style="color:green">Connected</span>')
        # chat_display.append('<span style="color:red">Connection failed</span>')
        # chat_display.append('<b>Downloading...</b>')
        chat_display.setMinimumWidth(500)
        layout.addWidget(chat_display, 0, 3, 20, 1)
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

def run(oai:OaiChatIntegrated):
    app = QApplication.instance() if QApplication.instance() else QApplication()
    window = MainWindow(oai)
    window.show()
    sys.exit(app.exec())
    
def show_init_dialog():
    syslogger.debug("1")
    app = QApplication.instance() if QApplication.instance() else QApplication()
    while not config.openai_api_key or not config.robot_server_ip:
        if not show_config_dlg():
            exit()

    dlg = QDialog()
    layout = QGridLayout(dlg)
    dlg.setWindowTitle(defs.APP_NAME)
    status = QLabel()
    layout.addWidget(status)
    done = threading.Event()
    def on_done():
        try:
            done.set()
            dlg.deleteLater()
        except:
            traceback.print_exc()
    connect_thread:QThread = None
    def connect():
        nonlocal connect_thread
        status.setText(f"Trying to connect to robot on {config.robot_server_ip}...")
        def doit():
            api.robot_client.init(config.robot_server_ip, logger=syslogger)
            api.ALMotion.ping()
            if api.robot_client.robot_connected():
                on_done()
            else:
                try:
                    status.setText(f"Could not connect to robot on {config.robot_server_ip}")
                except:
                    pass
        connect_thread = run_async_task(doit, ())
    
    btn_no_robot = QPushButton("Continue without robot")
    btn_no_robot.clicked.connect(on_done)
    layout.addWidget(btn_no_robot)
    def on_cfg():
        if show_config_dlg(dlg):
            # api.robot_client.close()
            connect()
    btn_config= QPushButton("System config")
    btn_config.clicked.connect(on_cfg)
    layout.addWidget(btn_config)
    syslogger.debug("2")

    connect()
    

    dlg.exec()
    if not done.is_set():
        try:
            connect_thread.deleteLater()
        except:
            pass
        exit()
    
        
