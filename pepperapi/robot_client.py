import json
import socket
import struct
import threading
import time
import traceback
from typing import Callable, Dict, List
import uuid
import queue
from . robot_comm_common import *
import os
import sys
import __main__
import logging
def _close_sock(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except:
        pass
    try:
        sock.close()
    except:
        pass

_logger:logging.Logger = None

def init(robot_server_ip:str, robot_server_port = ROBOT_SERVER_PORT, logger:logging.Logger = None):
    global _logger, _client
    if logger:
        _logger = logger
    if not _logger:
        _logger = logging.getLogger("clientdummylogger")
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))
        _logger.addHandler(handler)
    if _client:
        close()
    _client = _MessageClient(robot_server_ip, robot_server_port)


class _Request:
    def __init__(self):
        self.lock = threading.Lock()
        self.response = None

class FunctionCallException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

  
class _MessageClient:
    def __init__(self, server_ip, server_port):
        self.sock:socket.socket = None
        self.pending_requests:dict[str,_Request] = {}
        self.sock_lock = threading.Lock()
        self.running = threading.Event()
        self.closing = threading.Event()
        self.recv_thread = threading.Thread(target=self._recv_loop, daemon=True)
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = ""
        try:
            _logger.info("Connecting")
            self.sock.connect((self.server_ip, self.server_port))
            _logger.info("Connected")
            self.id = f"{int(time.time()*1000) % 100000}[{os.path.splitext(os.path.basename(__main__.__file__))[0]}@{self.sock.getsockname()[0]}]"
            self.running.set()
            self.recv_thread.start()
            self.send_msg(MsgSystemCommand(MsgSystemCommand.GET_MODULE_NAMES))
        except Exception as e:
            if not self.closing.is_set():
                _logger.error(f"Could not connect to robot server on {server_ip}:{server_port}. {e}")

    def send_msg(self, msg:MsgBase):
        # if not self.server_ip or not self.server_port:
        #     raise(Exception("robot_client.init must be called before this operation"))
        if not self.running.is_set():
            return None
        msg.id = str(uuid.uuid4())
        msg.client_id = self.id
        req = _Request()
        req.lock.acquire()
        self.pending_requests[msg.id] = req
        with self.sock_lock:
            send_dict(self.sock, msg.__dict__)
        req.lock.acquire()
        if error:=req.response.get("error"):
            if isinstance(msg, MsgModuleFunctionCall):
                raise FunctionCallException(error)
        return req.response.get("result")        

    def _recv_loop(self):
        while self.running.is_set():
            response = read_dict(self.sock)
            req = self.pending_requests.pop(response.get("msg_id"), None)
            if req:
                req.response = response
                req.lock.release_lock()
            else:
                _logger.warning(f"Unmatched reply: {response}")

    def close(self):
        self.running.clear()
        self.closing.set()
        try:
            self.recv_thread.join(timeout=1)
        except:
            pass
        _close_sock(self.sock)


_client:_MessageClient = None
def robot_connected():
    return _client and _client.running.is_set()

def send_mfc(module_name, func_name, func_args = []):
    if not _client:
        return None
    msg = MsgModuleFunctionCall(
        module_name=module_name,
        func_name=func_name,
        func_args=func_args
    )
    return _client.send_msg(msg)

def close():
    for el in EventListener.instances_by_event_name.values():
        #el.listener_thread.join(timeout=1)
        el.stop()
    if _client:
        _client.close()

class EventListener:
    instances_by_event_name:Dict[str, "EventListener"] = {}
    def __init__(self, event_name:str):
        self.event_name = event_name
        self.callbacks = []
        self.instances_by_event_name[event_name] = self
        self.alive = threading.Event()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #sock.settimeout(10)
        msg_poll = MsgEventPoll()
        msg_poll.client_id = _client.id if _client else None
        pending_events = queue.Queue()

        def dispatcher():
            while self.alive.is_set():
                evt = pending_events.get()
                if evt == "die":
                    return
                for cb in self.callbacks:
                    try:
                        cb(evt["data"])
                    except Exception as e:
                        _logger.exception(e)
        def listen():
            while self.alive.is_set():
                try:
                    send_dict(self.sock, msg_poll.__dict__)
                    evt_bytes = read_packet(self.sock)   
                    if evt_bytes:
                        pending_events.put(json.loads(evt_bytes.decode("utf8")))
                except ConnectionResetError as e:
                    _logger.error(f"{self.event_name} connection was closed by server.")
                    self.alive.clear()
                except Exception as e:
                    if self.alive.is_set():
                        _logger.exception(e)
            _close_sock(self.sock)
        
        self.listener_thread= threading.Thread(target=listen, daemon=True)
        if robot_connected():
            resp = _client.send_msg(MsgEventSubscription(event_name, True))
            self.sock.connect((_client.server_ip, resp["port"]))
            self.alive.set()
            threading.Thread(target=dispatcher, daemon=True).start()
            self.listener_thread.start()

    def stop(self):
        self.alive.clear()
        if _client:
            _client.send_msg(MsgEventSubscription(self.event_name, False))
        _close_sock(self.sock)

class EventSubscription:
    def __init__(self, event_name, callback):
        self._listener = EventListener.instances_by_event_name.get(event_name, EventListener(event_name))
        self._callback = callback
        self._listener.callbacks.append(callback)
    def unsubscribe(self):
        self._listener.callbacks.remove(self._callback)
        if not self._listener.callbacks:
            self._listener.stop()

