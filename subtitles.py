import atexit
from dataclasses import dataclass
import json
import os
import platform
import re
import socket
import threading
import time
import traceback
import binascii
import http.server
import socketserver
from typing import Callable, List, Tuple
import numpy as np
from syslogger import syslogger
import utils
from apidefs import api

htmlfile = os.path.dirname(os.path.realpath(__file__)) + "/subtitles.html"

class SubtitleServer:
    class HttpHandler(http.server.BaseHTTPRequestHandler):
        pending_text = "*"
        def do_GET(self):
            #print("getreq:", self.request)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Ignore favicon with an empty 200
            if "favicon" in self.path:
                content = b""
            else:
                with open(htmlfile, "rb") as f:
                    content = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        
        def do_POST(self):
            #print("postreq:", self.request)
            while not self.pending_text:
                time.sleep(.1)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.pending_text.encode("utf-8"))
            #self.pending_text = ""


        def log_message(self, format, *args):
            return
    
    _instance:"SubtitleServer" = None
    def __init__(self, http_port = 8088):
        if(SubtitleServer._instance):
            return
        SubtitleServer._instance = self
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        self.url = f"http://{s.getsockname()[0]}:{http_port}"
        s.close()
        def listen():
            socketserver.TCPServer.allow_reuse_address = True
            with socketserver.TCPServer(("", http_port), self.HttpHandler) as httpd:
                print(f"Serving on port {http_port}...")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\nShutting down server.")
                    httpd.server_close()
        threading.Thread(target=listen, daemon=True).start()
        self.setting_up_tablet = threading.Event()
        self._try_show_on_tablet()
    
    def _try_show_on_tablet(self):
        if not utils.has_tablet():
            syslogger.error("Tablet missing")
            return
        print("setup")
        if self.setting_up_tablet.is_set():
            print("nopes")
            return
        def doit():
            if utils.connect_tablet():
                done = False
                def cleanup():
                    try:
                        api.ALTabletService.hideWebview()
                    except:
                        pass
                
                while not done:
                    if api.ALTabletService.showWebview_2(self.url):
                        print(f"Opened subtitle URL {self.url} on tablet")
                        atexit.register(cleanup)
                        done = True
                    else:
                        print(f"Failed to open subtitle URL {self.url} on tablet. Will retry soon")
                        time.sleep(3)
            self.setting_up_tablet.clear()
        self.setting_up_tablet.set()
        threading.Thread(target=doit, daemon=True).start()


    def set_text(self, text:str):
        #print("set text:" + text)
        self.HttpHandler.pending_text = text

def try_show_on_tablet():
    print(SubtitleServer._instance)
    if SubtitleServer._instance:
        SubtitleServer._instance._try_show_on_tablet()

def split_into_sentences(text) -> List[str]:
    parts = re.split(r'([.?!])', text)
    out = []
    for i in range(0, len(parts)-1, 2):
        out.append(parts[i] + parts[i+1])
    return out

class AudioSynchronizedSubtitleProvider:
    def __init__(self):
        self.signal_threshold = 500
        self.duration_threshold = .1
        self._consecutive_silent_sample_cnt = 0
        self._sample_cnt = 0
        self._sample_rate = -1
        self._collected_text = ""
        self._last_pcm_time = 0
        self._start_time = 0
        self._cur_subtitle = ""
        self._server = SubtitleServer()
        self._silences:List[Tuple[float,float]] = [] 
        """(start, duration)"""
        def loop():
            while True:
                now = time.time()
                if self._sample_cnt > 0:
                    speech_dur = self._sample_cnt / self._sample_rate
                    play_time = now - self._start_time
                    remaining_time = speech_dur - play_time
                    pcm_input_done = time.time() - self._last_pcm_time > .5
                    if pcm_input_done and remaining_time < -3:
                        self.reset()
                    elif pcm_input_done and remaining_time <= 0:
                        self._set_subtitle(self._collected_text)
                    else:
                        if sentences := split_into_sentences(self._collected_text):
                            applicable_silence_cnt = min(len(self._silences), len(sentences)-1)
                            applicable_silences = sorted(self._silences, reverse=True, key=lambda silence: silence[1])[:applicable_silence_cnt]
                            number_of_texts_to_show = 1 + len([silence for silence in applicable_silences if (silence[0] + silence[1]) < play_time])
                            self._set_subtitle("".join([sentence.strip() for sentence in sentences[:number_of_texts_to_show]]))
                time.sleep(.2)
        threading.Thread(target=loop, daemon=True).start()

    def _set_subtitle(self, text):
        if text != self._cur_subtitle:
            print(text)
            self._cur_subtitle = text
            self._server.set_text(text)
            
    def reset(self):
        if self._sample_cnt > 0:
            self._set_subtitle("")
            self._collected_text = ""
            self._sample_cnt = 0
            self._silences = []
   

    def push_text(self, text:str):
        self._collected_text += text

    def push_pcm16_frames(self, sample_rate:int, channel_cnt:int, frames:np.ndarray):
        if channel_cnt > 1:
            return False
        self._last_pcm_time = time.time()
        self._sample_rate = sample_rate
        if self._sample_cnt == 0:
            self._start_time = time.time()
        abs_amplitudes = np.abs(frames)
        silent_sample_cnt_threshold = int(sample_rate * self.duration_threshold)
        for amp in abs_amplitudes:
            self._sample_cnt += 1
            if amp < self.signal_threshold:
                self._consecutive_silent_sample_cnt += 1
            else:
                if self._consecutive_silent_sample_cnt >= silent_sample_cnt_threshold:
                    self._silences.append((
                        (self._sample_cnt - self._consecutive_silent_sample_cnt) / sample_rate,
                        self._consecutive_silent_sample_cnt / sample_rate
                    ))
                self._consecutive_silent_sample_cnt = 0

