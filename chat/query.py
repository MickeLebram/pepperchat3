import time

class Query:
    def __init__(self):
        self.start_time = time.time()
        self.response_text = ""
        self.response_done = False
        self.query_transcript:str = None
        self.done = False
        self.duration = 0
        self.canceled = False
        self.silent = False # The model decided the utterance was not directed at it
    def __str__(self):
        return str(self.__dict__)
    @property
    def query_text(self):
        return self.query_transcript
