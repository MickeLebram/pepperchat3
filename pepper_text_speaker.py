import atexit
import traceback
import subtitles

import threading
import time
from apidefs import api
import utils

            
class PepperTextSpeaker:
    class Worker:
        def __init__(self, pepper_speak:"PepperTextSpeaker"):
            self.pepper_speak = pepper_speak
            self.sentences = []
            self.unsentenced_text = ""
            self.last_text_receive_time = 0
            self.done = False
            def loop():
                next_sentence_idx = 0
                while not self.done:
                    if self.last_text_receive_time > 0:
                        sentence_cnt = len(self.sentences)
                        got_all_text = time.time() - self.last_text_receive_time > .5
                        if sentence_cnt <= next_sentence_idx:
                            if got_all_text:
                                if self.unsentenced_text:
                                    self.sentences.append(self.unsentenced_text)
                                    self.unsentenced_text = ""
                                else:
                                    self.done = True

                        elif not pepper_speak.speaking:
                            sentences = self.sentences.copy()
                            sentence = sentences[next_sentence_idx]
                            threading.Thread(target=pepper_speak.say, args=[sentence], daemon=True).start()
                            #print("say:",sentence)
                            next_sentence_idx += 1
                            if pepper_speak.subtitle_server:
                                pepper_speak.subtitle_server.set_text("".join(sentences[:next_sentence_idx]))
                    time.sleep(.2)
            threading.Thread(target=loop, daemon=True).start()
        
        def push_text(self, text:str):
            self.last_text_receive_time = time.time()
            self.unsentenced_text += text
            if sentences := subtitles.split_into_sentences(self.unsentenced_text):
                self.unsentenced_text = self.unsentenced_text.removeprefix("".join(sentences))
                self.sentences += sentences

    def __init__(self, subtitle_server:subtitles.SubtitleServer=None):
        self.subtitle_server = subtitle_server
        self.worker = PepperTextSpeaker.Worker(self)
        self._speaking = threading.Event()
        self.tts = api.ALAnimatedSpeech

    def stop_talking(self):
        self.worker.done = True
        api.ALTextToSpeech.stopAll()

    @property
    def speaking(self):
        return self._speaking.is_set()
    
    def say(self, text:str):
        self._speaking.set()
        api.ALAnimatedSpeech.say_1(text)
        self._speaking.clear()

    def push_text(self, text:str):
        if self.worker.done:
            self.worker = PepperTextSpeaker.Worker(self)
        self.worker.push_text(text)
