import json
import socket
import struct
import threading
import time
import traceback
from typing import Callable, Dict, Generic, List, Optional, ParamSpec, TypeVar
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

class FutureCanceledException(Exception):
    pass

  
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
        if not self.running.is_set():
            # The connection was lost after the first check, and _recv_loop won't release us
            self.pending_requests.pop(msg.id, None)
            return None
        try:
            with self.sock_lock:
                send_dict(self.sock, msg.__dict__)
        except Exception as e:
            self.pending_requests.pop(msg.id, None)
            if not self.closing.is_set():
                _logger.error(f"Could not send to robot server: {e}")
            return None
        req.lock.acquire()
        if req.response is None:
            return None # Connection lost while waiting
        if error:=req.response.get("error"):
            if isinstance(msg, (MsgModuleFunctionCall, MsgFutureCommand)):
                raise FunctionCallException(error)
        return req.response.get("result")        

    def _recv_loop(self):
        try:
            while self.running.is_set():
                response = read_dict(self.sock)
                req = self.pending_requests.pop(response.get("msg_id"), None)
                if req:
                    req.response = response
                    req.lock.release()
                else:
                    _logger.warning(f"Unmatched reply: {response}")
        except Exception as e:
            if not self.closing.is_set():
                _logger.error(f"Lost connection to robot server: {e}")
        finally:
            self.running.clear()
            # Wake up calls still waiting for a reply. They get response None
            while self.pending_requests:
                _, req = self.pending_requests.popitem()
                req.lock.release()

    def close(self):
        self.running.clear()
        self.closing.set()
        try:
            self.recv_thread.join(timeout=1)
        except:
            pass
        _close_sock(self.sock)


_client:_MessageClient = None

T = TypeVar("T")
P = ParamSpec("P")

class RemoteFuture(Generic[T]):
    """
    Handle to a qi.Future on the robot, created by call_async.
    Once the call has finished, the final state is kept here and the robot forgets the future.
    """
    def __init__(self, future_id:str):
        self.id = future_id
        self._state = {"state": "running"}

    def _command(self, cmd:str, timeout_ms:Optional[int] = None) -> str:
        if self._state["state"] == "running":
            state = _client.send_msg(MsgFutureCommand(self.id, cmd, timeout_ms)) if _client else None
            if state is None:
                raise ConnectionError("Lost connection to the robot server")
            self._state = state
        return self._state["state"]

    def cancel(self):
        """Asks the robot to cancel the call. It may take a moment before the call has actually stopped."""
        self._command(MsgFutureCommand.CANCEL)

    def wait(self, timeout_ms:Optional[int] = None) -> bool:
        """Waits for the call to finish. Returns False if timeout_ms passed first."""
        return self._command(MsgFutureCommand.WAIT, timeout_ms) != "running"

    def value(self, timeout_ms:Optional[int] = None) -> T:
        """Waits for the call to finish and returns its result. Raises if the call failed or was canceled."""
        state = self._command(MsgFutureCommand.WAIT, timeout_ms)
        if state == "running":
            raise TimeoutError(f"Future {self.id} did not finish within {timeout_ms} ms")
        if state == "canceled":
            raise FutureCanceledException(f"Future {self.id} was canceled")
        if state == "error":
            raise FunctionCallException(self._state.get("error"))
        return self._state.get("value")

    def is_running(self) -> bool:
        return self._command(MsgFutureCommand.GET_STATE) == "running"

    def is_finished(self) -> bool:
        return not self.is_running()

    def is_canceled(self) -> bool:
        return self._command(MsgFutureCommand.GET_STATE) == "canceled"

    def has_error(self) -> bool:
        return self._command(MsgFutureCommand.GET_STATE) == "error"

    def error(self) -> Optional[str]:
        self._command(MsgFutureCommand.GET_STATE)
        return self._state.get("error")

# Set by call_async so that the next send_mfc on this thread runs asynchronously on the robot.
# __init__ runs once per thread, so every thread starts with active = False
class _AsyncCallFlag(threading.local):
    def __init__(self):
        self.active = False

_async_call = _AsyncCallFlag()

def robot_connected():
    return _client and _client.running.is_set()

def send_mfc(module_name, func_name, func_args = []):
    if not _client:
        return None
    run_async = _async_call.active
    _async_call.active = False
    msg = MsgModuleFunctionCall(
        module_name=module_name,
        func_name=func_name,
        func_args=func_args,
        run_async=run_async
    )
    result = _client.send_msg(msg)
    if run_async:
        if result is None and not robot_connected():
            raise ConnectionError("Not connected to the robot server")
        if not isinstance(result, dict) or "future_id" not in result:
            raise FunctionCallException("The robot server does not support async calls. Please update robot_server.py and robot_comm_common.py on the robot.")
        return RemoteFuture(result["future_id"])
    return result

def call_async(func:Callable[P, T], *args:P.args, **kwargs:P.kwargs) -> RemoteFuture[T]:
    """
    Starts a robot function call without waiting for it to finish, e.g.
        fut = call_async(ALAnimationPlayer.run, "animations/Stand/Gestures/Hey_1")
        fut.cancel()
    """
    _async_call.active = True
    try:
        fut = func(*args, **kwargs)
    finally:
        _async_call.active = False
    if fut is None and not robot_connected():
        raise ConnectionError("Not connected to the robot server")
    if not isinstance(fut, RemoteFuture):
        raise TypeError(f"{getattr(func, '__name__', func)} did not call the robot, so it can't be used with call_async")
    return fut

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

