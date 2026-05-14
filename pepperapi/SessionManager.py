import traceback
from typing import List
try:
    import qi
except:
    print("qi is needed for robot communication")
from .ALMemory import ALMemory
class EventSubscription:
    active_instances:List["EventSubscription"] = []
    def __init__(self, memory:ALMemory, event:str, callback):
        self.memory = memory
        self.event = event
        self.callback = callback
        self.start()

    def start(self):
        if self not in self.active_instances:
            print(f"starting {self.event} subscription")
            self.sub = self.memory.subscriber(self.event)
            self.link = self.sub.signal.connect(self.callback)
            self.active_instances.append(self)
        else:
            print(f"{self.event} subscription is already active")
    
    def stop(self):
        if self in self.active_instances:
            print(f"stopping {self.event} subscription")
            try:
                self.sub.signal.disconnect(self.link)
            except:
                traceback.print_exc()
            self.active_instances.remove(self)
        else:
            print(f"{self.event} subscription is not active")
    

class SessionManager:
    def __init__(self, robot_ip:str, robot_port = 9559):
        self.session=qi.Session()
        self.session.connect(f"tcp://{robot_ip}:{robot_port}")
        self.memory = ALMemory(self.session)
        self.service = self.session.service
    def create_event_subscription(self, event:str, callback):
        return EventSubscription(self.memory, event, callback)
    
    def stop(self):
        for evtsub in EventSubscription.active_instances:
            evtsub.stop()
