import contextlib
import socket
import threading
import time
from typing import Callable, Dict, Generic, List, Optional, ParamSpec, Tuple, TypeVar
import uuid
import queue
from . robot_comm_common import *
import os
import sys
import __main__
import logging
import dataclasses
import functools
import typing
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
# When set (debugging without a robot), robot calls without a connection are skipped and return None
# instead of raising ConnectionError. Each skipped call is logged once, see _MessageClient._not_connected
_ignore_disconnected = False
_skip_warned:set = set()

def init(robot_server_ip:str, robot_server_port = ROBOT_SERVER_PORT, logger:logging.Logger = None, ignore_disconnected = False):
    """
    Connects to the robot server. Raises ConnectionError if it can't be reached, unless ignore_disconnected is set.
    ignore_disconnected is meant for testing without a robot: robot calls are then skipped and return None,
    with one log warning per skipped function.
    """
    global _logger, _client, _ignore_disconnected
    if logger:
        _logger = logger
    if not _logger:
        _logger = logging.getLogger("clientdummylogger")
        # Shared by every generated API's copy of this module, so only the first one adds the output
        if not _logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(logging.Formatter(
                fmt="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            ))
            _logger.addHandler(handler)
    if _client:
        close()
    _ignore_disconnected = ignore_disconnected
    _skip_warned.clear()
    _client = _MessageClient(robot_server_ip, robot_server_port)
    if not _client.running.is_set():
        reason = f"Could not connect to robot server on {robot_server_ip}:{robot_server_port} ({_client.connect_error})"
        if not ignore_disconnected:
            raise ConnectionError(reason)
        _logger.warning(f"{reason}. Continuing without a robot, since ignore_disconnected is set.")
        return
    _check_naoqi_version()

def _check_naoqi_version():
    """
    Warns if the robot runs another NAOqi version than the one this API was built from (NAOQI_VERSION in the
    generated package). Using it anyway is allowed, e.g. the Pepper's API with a Nao, at your own discretion
    """
    package = sys.modules.get(__package__) if __package__ else None
    built = getattr(package, "NAOQI_VERSION", None)
    if not built:
        return
    try:
        with timeout(INTERNAL_REQUEST_TIMEOUT_SECONDS):
            actual = _client.send_message(MsgMethodCall("ALSystem", "systemVersion", []))
    except Exception:
        return # Not worth failing init() for
    if actual and actual != built:
        _logger.warning(f"This API was built from NAOqi {built}, but the robot runs NAOqi {actual}. It can be used "
                        "anyway, but methods the robot doesn't have, or has with other arguments, fail with a RobotError.")


# time.time() on Windows (before Python 3.13) may only advance every 15.6 ms, too coarse for timing events.
# perf_counter() is precise but has no fixed zero, so it's anchored to time.time() once
_time_anchor = time.time() - time.perf_counter()

def precise_time() -> float:
    """This PC's time in seconds since 1970, like time.time(), but with a fine resolution on every platform"""
    return _time_anchor + time.perf_counter()

HEARTBEAT_SECONDS = 2 # How often the client pings the robot server
CONNECTION_DEAD_SECONDS = 10 # Without any sign of life from the robot server for this long, the connection is closed
INTERNAL_REQUEST_TIMEOUT_SECONDS = 10 # For the bridge's own short requests, see _MessageClient._reply_timeout
WAIT_SLICE_SECONDS = 0.5 # Waits are done in slices of this, so Ctrl+C can interrupt them on Windows

def _wait_in_slices(wait_once:Callable[[float], bool], timeout_seconds:Optional[float] = None) -> bool:
    """
    Calls wait_once(seconds), e.g. event.wait, until it returns True or timeout_seconds
    have passed (None: no limit). Returns whether it succeeded. On Windows, a wait without a timeout
    can't be interrupted by Ctrl+C, so this waits in short slices
    """
    deadline = None if timeout_seconds is None else time.monotonic() + timeout_seconds
    while True:
        seconds = WAIT_SLICE_SECONDS if deadline is None else min(WAIT_SLICE_SECONDS, deadline - time.monotonic())
        if seconds <= 0:
            return False
        if wait_once(seconds):
            return True

class _CallTimeout(threading.local):
    def __init__(self):
        self.seconds:Optional[float] = None # Set by timeout(), for the calling thread only

_call_timeout = _CallTimeout()

@contextlib.contextmanager
def timeout(seconds:float):
    """
    Limits how long the robot calls in a with-block wait for their reply, e.g.
        with robot_client.timeout(5):
            ALTextToSpeech.say("Hello")
    raises TimeoutError if the reply takes longer than 5 s. The call keeps running on the robot, since a
    synchronous call can't be stopped from here (use call_async and cancel() for that). Applies to the
    calling thread only. Without it, method calls wait as long as they run, and the heartbeat detects
    a lost connection
    """
    previous = _call_timeout.seconds
    _call_timeout.seconds = seconds
    try:
        yield
    finally:
        _call_timeout.seconds = previous

class _Request:
    def __init__(self):
        self.lock = threading.Lock()
        self.response = None

class RobotError(Exception):
    """
    An error reported by the robot side: a failed method call, subscription or property access
    (with NAOqi's message), or a robot server too old for what was asked
    """
    def __init__(self, *args):
        super().__init__(*args)

class FutureCanceledError(Exception):
    pass

class RobotClientNotInitializedError(RuntimeError):
    """A programming mistake, kept apart from ConnectionError so code handling connection problems can't hide it"""
    pass

def _require_init(action:str):
    if not _client:
        raise RobotClientNotInitializedError(f"robot_client.init() must be called before {action}")

  
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
        # Small messages go out at once instead of waiting for TCP's Nagle algorithm, e.g. several requests
        # from different threads at once (the robot server does the same for events, where it was measured)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.id = ""
        self.connect_error:Exception = None # Reported by init()
        self.last_received = time.monotonic() # Any message from the server counts as a sign of life
        self.discarded_replies:set = set() # Ids of requests whose reply nobody waits for: pings and timed-out calls
        self.dead_reason = "" # Set by the heartbeat when it closes the connection
        self.heartbeat_thread = threading.Thread(target=self._heartbeat_loop, daemon=True)
        self.event_sock:socket.socket = None # The second connection, for events only, see _open_event_connection
        try:
            _logger.info("Connecting")
            self.sock.connect((self.server_ip, self.server_port))
            _logger.info("Connected")
            # The script's name, for the robot server's log. There's none with python -c, or interactively
            script_file = getattr(__main__, "__file__", None)
            program = os.path.splitext(os.path.basename(script_file))[0] if script_file else "unknown"
            self.id = f"{int(time.time()*1000) % 100000}[{program}@{self.sock.getsockname()[0]}]"
            self.running.set()
            self.recv_thread.start()
            self.heartbeat_thread.start()
            self.send_message(MsgSystemCommand(MsgSystemCommand.GET_SERVICE_NAMES)) # The server now knows our id
            self._open_event_connection()
        except Exception as e:
            self.running.clear()
            self.connect_error = e

    def _open_event_connection(self):
        """
        Opens a second connection to the server, for events only, so a large reply on the main connection
        (e.g. a camera image, ~0.5 s for 640x480 on Wi-Fi) doesn't hold them up. If the server is too old for
        it, the events simply come over the main connection, as before
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            sock.settimeout(INTERNAL_REQUEST_TIMEOUT_SECONDS)
            sock.connect((self.server_ip, self.server_port))
            msg = MsgEventChannel()
            msg.id = str(uuid.uuid4())
            msg.client_id = self.id
            send_dict(sock, msg.__dict__)
            reply = read_dict(sock)
            sock.settimeout(None)
        except Exception as e:
            _close_sock(sock)
            _logger.warning(f"Couldn't open the event connection ({e}), so events come over the main connection.")
            return
        result = reply.get("result")
        if not (isinstance(result, dict) and result.get("event_channel")):
            _close_sock(sock)
            _logger.info("The robot server has no separate event connection (an older version), so events come over the main connection.")
            return
        self.event_sock = sock
        threading.Thread(target=self._event_loop, daemon=True).start()

    def _event_loop(self):
        """Receives the events on the event connection. If it breaks, the whole connection counts as lost"""
        try:
            while self.running.is_set():
                event = json_to_binary(read_dict(self.event_sock))
                self.last_received = time.monotonic()
                if event.get("type") == MsgEvent.__name__:
                    self._pass_on_event(event)
        except Exception as e:
            if not self.closing.is_set() and self.running.is_set():
                # Often the whole server is gone, and this connection just noticed first
                self.dead_reason = f"the connection was closed (noticed on the event connection: {e})"
                _close_sock(self.sock) # Ends _recv_loop, which fails the calls waiting for a reply

    @staticmethod
    def _describe(msg:MsgBase) -> str:
        """What a request does, for error and log messages"""
        if isinstance(msg, MsgMethodCall):
            return f"calling {msg.service_name}.{msg.method_name}"
        if isinstance(msg, MsgEventSubscription):
            return f"{'subscribing to' if msg.subscribe else 'unsubscribing from'} {event_key(msg.service_name, msg.event_name)}"
        if isinstance(msg, MsgPropertyAccess):
            return f"{'setting' if msg.set_value else 'reading'} {msg.service_name}.{msg.property_name}"
        if isinstance(msg, MsgFutureCommand):
            return f"the future command {msg.command}"
        return f"the system command {getattr(msg, 'command', type(msg).__name__)}"

    @staticmethod
    def _reply_timeout(msg:MsgBase) -> Optional[float]:
        """How long send_message waits for the reply to msg. None: as long as it takes"""
        if isinstance(msg, MsgFutureCommand) and msg.command == MsgFutureCommand.WAIT:
            return None # The waiter thread waits as long as the method runs on the robot
        if _call_timeout.seconds is not None:
            return _call_timeout.seconds
        if isinstance(msg, MsgMethodCall) and not msg.run_async:
            return None # Methods may legitimately run for minutes. The heartbeat detects a lost connection
        # The bridge's own requests (subscriptions, properties, starting an async call, system commands)
        # should answer at once, but could hang on the robot, e.g. if a NAOqi service has crashed
        return INTERNAL_REQUEST_TIMEOUT_SECONDS

    def _not_connected(self, msg:MsgBase, reason:str):
        """Raises ConnectionError, or with ignore_disconnected skips the call (returns None) and logs it once"""
        action = self._describe(msg)
        if not _ignore_disconnected:
            raise ConnectionError(f"{reason} ({action})")
        if action not in _skip_warned:
            _skip_warned.add(action)
            _logger.warning(f"{reason}, so {action} is skipped. ignore_disconnected is set, so further skips of it aren't logged.")
        return None

    def send_message(self, msg:MsgBase):
        if not self.running.is_set():
            return self._not_connected(msg, "Not connected to the robot server")
        msg.id = str(uuid.uuid4())
        msg.client_id = self.id
        req = _Request()
        req.lock.acquire()
        self.pending_requests[msg.id] = req
        if not self.running.is_set():
            # The connection was lost after the first check, and _recv_loop won't release us
            self.pending_requests.pop(msg.id, None)
            return self._not_connected(msg, "Not connected to the robot server")
        try:
            with self.sock_lock:
                send_dict(self.sock, binary_to_json(msg.__dict__)) # bytes arguments go as base64, see BYTES_MARKER
        except Exception as e:
            self.pending_requests.pop(msg.id, None)
            return self._not_connected(msg, f"Could not send to the robot server: {e}")
        timeout_seconds = self._reply_timeout(msg)
        try:
            # timeout= by keyword: acquire's first parameter is blocking, so acquire(0.5) would wait forever
            replied = _wait_in_slices(lambda seconds: req.lock.acquire(timeout=seconds), timeout_seconds)
        except BaseException:
            # E.g. Ctrl+C (KeyboardInterrupt) while waiting: nobody wants the reply any more
            self._give_up(msg.id)
            raise
        if not replied:
            self._give_up(msg.id)
            raise TimeoutError(f"No reply from the robot within {timeout_seconds} s ({self._describe(msg)}). "
                               "It may still be running on the robot.")
        if req.response is None:
            return self._not_connected(msg, "Lost connection to the robot server while waiting for the reply")
        if error:=req.response.get("error"):
            if isinstance(msg, (MsgMethodCall, MsgFutureCommand, MsgEventSubscription, MsgPropertyAccess)):
                raise RobotError(error)
        return req.response.get("result")        

    def _give_up(self, message_id:str):
        """Stops waiting for a reply. If it still arrives, it's dropped silently"""
        self.pending_requests.pop(message_id, None)
        self.discarded_replies.add(message_id)

    def _send_without_reply(self, msg:MsgBase):
        """Sends msg without waiting for the reply, which is dropped when it arrives"""
        msg.id = str(uuid.uuid4())
        msg.client_id = self.id
        self.discarded_replies.add(msg.id)
        with self.sock_lock:
            send_dict(self.sock, msg.__dict__)

    def _heartbeat_loop(self):
        """
        Pings the server every HEARTBEAT_SECONDS. If nothing at all (replies, events, pings answered) has
        arrived for CONNECTION_DEAD_SECONDS, the connection is closed, which fails the waiting calls
        """
        last_round = time.monotonic()
        while not self.closing.wait(HEARTBEAT_SECONDS) and self.running.is_set():
            now = time.monotonic()
            if now - last_round > 3 * HEARTBEAT_SECONDS:
                # This program was paused (e.g. in a debugger) or the PC slept, so the silence says nothing
                # about the robot. Start counting again
                self.last_received = now
            last_round = now
            if now - self.last_received > CONNECTION_DEAD_SECONDS:
                self.dead_reason = f"no sign of life from the robot server for {CONNECTION_DEAD_SECONDS} s"
                _close_sock(self.sock) # Ends _recv_loop, which fails the calls waiting for a reply
                return
            try:
                self._send_without_reply(MsgSystemCommand(MsgSystemCommand.PING))
            except Exception:
                pass # _recv_loop notices the broken connection

    def _recv_loop(self):
        try:
            while self.running.is_set():
                response = json_to_binary(read_dict(self.sock)) # Binary data (e.g. camera images) becomes bytes
                self.last_received = time.monotonic()
                if response.get("type") == MsgEvent.__name__:
                    self._pass_on_event(response)
                    continue
                message_id = response.get("message_id")
                req = self.pending_requests.pop(message_id, None)
                if req:
                    req.response = response
                    req.lock.release()
                elif message_id in self.discarded_replies:
                    self.discarded_replies.discard(message_id)
                else:
                    _logger.warning(f"Unmatched reply: {response}")
        except Exception as e:
            if not self.closing.is_set():
                _logger.error(f"Lost connection to robot server: {self.dead_reason or e}")
        finally:
            self.running.clear()
            if self.event_sock is not None:
                _close_sock(self.event_sock) # Ends _event_loop
            # Wake up calls still waiting for a reply. They get response None
            while self.pending_requests:
                _, req = self.pending_requests.popitem()
                req.lock.release()

    def _pass_on_event(self, event:dict):
        """
        Passes an event the robot pushed to its listener. Runs on the receive thread, so it must never call
        the callbacks itself: a callback that calls the robot would wait for a reply only this thread can read
        """
        event["received_time"] = precise_time() # For EventInfo
        if event.get("dropped"):
            _logger.warning(f"The robot dropped {event['dropped']} events before this one, because this program "
                            "didn't read them in time (e.g. paused in a debugger, or a stalled network).")
        listener = EventListener.instances_by_key.get(event_key(event.get("service_name", ""), event.get("event_name", "")))
        if listener:
            listener.add_event(event)
        # Otherwise it was sent before an unsubscribe reached the robot, and nobody wants it

    def close(self):
        self.running.clear()
        self.closing.set()
        try:
            self.recv_thread.join(timeout=1)
        except:
            pass
        _close_sock(self.sock)
        if self.event_sock is not None:
            _close_sock(self.event_sock)


_client:_MessageClient = None

T = TypeVar("T")
P = ParamSpec("P")

class RemoteFuture(Generic[T]):
    """
    Handle to a method running on the robot, created by call_async (a qi.Future on the robot).
    call_async returns as soon as the robot has started the method. Once the method has stopped,
    the final state is kept here and the robot forgets the future.
    The state is what NAOqi reports. Some services report a canceled call as finished
    (e.g. ALAnimationPlayer.run), so cancel_requested tells whether cancel() was called here.
    If the method fails and no on_error handler is attached, a warning is logged, so errors never vanish silently.
    """
    def __init__(self, future_id:str, description:str = "", value_type = None):
        self.id = future_id
        self.description = description # E.g. "ALTextToSpeech.say", used in log messages
        self._value_type = value_type # The return type where it involves structs, see _dicts_to_structs
        self.cancel_requested = False # Set by cancel(), whatever NAOqi then reports
        # Only the waiter thread asks the robot about this future (one WAIT, see _wait_until_done).
        # It stores the final state and then sets _done. Everything else reads that locally, so a
        # future never has more than one waiting point on the robot, and threads can't race each other
        self._state = {"state": "running"}
        self._waiter_error:Exception = None # E.g. a ConnectionError while waiting for the call to finish
        self._done = threading.Event()
        # Callbacks waiting for the waiter thread to see the call finish. Several are common,
        # since on_error is built on on_done. Callbacks added after the call is done are called at once instead
        self._callbacks:List[Callable[["RemoteFuture[T]"], None]] = []
        self._callbacks_lock = threading.Lock()
        self._waiter:threading.Thread = None
        self._has_error_handler = False # Set by on_error. Without it, a failure is logged as a warning

    # The state of a call skipped by ignore_disconnected: finished, with None as value like a skipped normal call
    _SKIPPED_STATE = {"state": "finished", "value": None}

    @classmethod
    def _skipped(cls) -> "RemoteFuture":
        future = cls("")
        future._state = cls._SKIPPED_STATE
        future._done.set()
        return future

    def cancel(self):
        """
        Asks the robot to cancel the call. It may take a moment before the call has actually stopped.
        Sets cancel_requested, since some services report a canceled call as finished rather than canceled.
        Doesn't wait for the robot: is_canceled() and the other states update once it confirms, so call wait()
        first if you need the outcome. Does nothing if the method has already stopped.
        """
        self.cancel_requested = True
        if self._done.is_set():
            return
        try:
            # Raises ConnectionError when disconnected, or does nothing if ignore_disconnected is set
            _client.send_message(MsgFutureCommand(self.id, MsgFutureCommand.CANCEL))
        except RobotError:
            # The method may have stopped just before the cancel arrived, so the robot no longer knew the
            # future. Then the waiter's answer is already on its way. Anything else is a real error
            if not self._done.wait(5):
                raise

    def on_done(self, callback:Callable[["RemoteFuture[T]"], None]) -> "RemoteFuture[T]":
        """
        Calls callback(future) once the method has stopped running on the robot: finished, failed or canceled.
        It's called whatever the outcome, so it doesn't mean the method succeeded. Check the future in the
        callback (has_error(), is_canceled(), value()), or use on_error for failures.
        Returns the future itself, so calls can be chained: call_async(...).on_done(a).on_error(b)
        The callback runs on a background thread, so GUI code must pass the work on to its own thread.
        If the method has already stopped, the callback is called at once, on the calling thread.
        If the connection is lost while waiting, the callback is still called, and value() then raises the error.
        on_done doesn't count as handling errors: use on_error for that, or a failure is logged as a warning.
        """
        with self._callbacks_lock:
            if not self._done.is_set():
                self._callbacks.append(callback)
                return self
        self._run_callback(callback)
        return self

    def on_error(self, callback:Callable[[Exception], None]) -> "RemoteFuture[T]":
        """
        Calls callback(exception) if the method fails on the robot: a RobotError with the robot's message,
        or a ConnectionError if the connection was lost while waiting. A canceled call isn't an error.
        Attaching on_error means the application handles errors, so no warning is logged.
        Returns the future itself, like on_done, and the same rules apply.
        """
        def call_if_failed(future:"RemoteFuture[T]"):
            failure = future._failure()
            if failure:
                callback(failure)
        with self._callbacks_lock:
            self._has_error_handler = True
        return self.on_done(call_if_failed)

    def _watch(self):
        """Starts the waiter thread. Done by call_async for every future"""
        with self._callbacks_lock:
            if not self._waiter and not self._done.is_set():
                self._waiter = threading.Thread(target=self._wait_until_done, daemon=True)
                self._waiter.start()

    def _failure(self) -> Optional[Exception]:
        if self._waiter_error:
            return self._waiter_error
        if self._state["state"] == "error":
            return RobotError(self._state.get("error"))
        return None

    def _wait_until_done(self):
        """The waiter thread: the only place that asks the robot about this future"""
        try:
            # Blocks until the method has stopped on the robot. Raises ConnectionError when the
            # connection is lost, or returns None if ignore_disconnected is set
            state = _client.send_message(MsgFutureCommand(self.id, MsgFutureCommand.WAIT))
            if state is not None and state.get("state") == "finished" and self._value_type is not None:
                state = dict(state, value=_dicts_to_structs(self._value_type, state.get("value")))
            self._state = state if state is not None else self._SKIPPED_STATE
        except Exception as e:
            self._waiter_error = e
        with self._callbacks_lock:
            # The state is complete before _done is set, so every thread waiting for _done sees it
            self._done.set()
            callbacks, self._callbacks = self._callbacks, []
            has_error_handler = self._has_error_handler
        failure = self._failure()
        if failure and not has_error_handler:
            # Without this, the error of a call nobody handles would vanish silently
            message = " ".join(str(failure).split()) # NAOqi's messages contain line breaks and tabs
            _logger.warning(f"call_async({self.description}) failed and has no on_error handler: {message}")
        for callback in callbacks:
            self._run_callback(callback)

    def _run_callback(self, callback):
        try:
            callback(self)
        except Exception as e:
            _logger.exception(e)

    def wait(self, timeout_ms:Optional[int] = None) -> bool:
        """
        Waits for the method to stop on the robot. Returns False if timeout_ms passed first.
        Raises the error (e.g. ConnectionError) if the connection was lost while waiting, since it's then unknown
        whether the method stopped. After cancel(), wait() is the way to know when the robot has confirmed it.
        """
        if not _wait_in_slices(self._done.wait, None if timeout_ms is None else timeout_ms / 1000):
            return False
        if self._waiter_error:
            raise self._waiter_error
        return True

    def value(self, timeout_ms:Optional[int] = None) -> T:
        """
        Waits for the method to stop and returns its result.
        Raises if it failed, was canceled, or the connection was lost while waiting.
        """
        if not self.wait(timeout_ms): # Raises the error if the connection was lost
            raise TimeoutError(f"Future {self.id} did not finish within {timeout_ms} ms")
        state = self._state["state"]
        if state == "canceled":
            raise FutureCanceledError(f"Future {self.id} was canceled")
        if state == "error":
            raise RobotError(self._state.get("error"))
        return self._state.get("value")

    def is_running(self) -> bool:
        return not self._done.is_set()

    def is_finished(self) -> bool:
        return self._done.is_set()

    def is_canceled(self) -> bool:
        return self._done.is_set() and self._state["state"] == "canceled"

    def has_error(self) -> bool:
        return self._done.is_set() and self._state["state"] == "error"

    def error(self) -> Optional[str]:
        return self._state.get("error") if self._done.is_set() else None

# Set by call_async so that the next call_method on this thread runs asynchronously on the robot.
# __init__ runs once per thread, so every thread starts with active = False
class _AsyncCallFlag(threading.local):
    def __init__(self):
        self.active = False

_async_call = _AsyncCallFlag()

def robot_connected() -> bool:
    return bool(_client and _client.running.is_set())

def _server_command(command:str, args:list, result_key:str):
    """A system command that the robot server answers with a dict holding result_key"""
    _require_init(f"the system command {command}")
    # Raises ConnectionError when disconnected, or returns None if ignore_disconnected is set
    result = _client.send_message(MsgSystemCommand(command, args))
    if result is None and _ignore_disconnected:
        return None
    if not isinstance(result, dict) or result_key not in result:
        # An old server answers commands it doesn't know with an empty result
        raise RobotError("The robot server is too old for this. Please update robot_server.py and robot_comm_common.py on the robot.")
    return result[result_key]

def set_server_debug(on:bool) -> None:
    """
    Switches the robot server's log between DEBUG (also every event and every message received) and INFO.
    The setting is the server's, so it applies to all connected programs, until it's changed again or the
    server restarts (it then starts at INFO). See get_server_log
    """
    _server_command(MsgSystemCommand.SET_LOG_LEVEL, ["DEBUG" if on else "INFO"], "log_level")

def get_server_log(lines:int = 200) -> Optional[str]:
    """
    The last lines of the robot server's log, up to a limit set in robot_server.py. The log is kept in log/
    next to robot_server.py on the robot. It rolls over: the oldest lines are removed by themselves, so it
    only reaches back a limited time
    """
    log_lines = _server_command(MsgSystemCommand.GET_LOG, [lines], "lines")
    return None if log_lines is None else "\n".join(log_lines)

# Structs: the generated API has a dataclass per struct, while the robot sends and accepts dicts
# with the field names as keys (tested on Nao and Pepper). These two convert between them

@functools.lru_cache(maxsize=None)
def _struct_fields(struct_class) -> Tuple:
    """(Python name, dict key, type) for each field. The key differs where the robot's name isn't valid Python"""
    types = typing.get_type_hints(struct_class)
    return tuple((f.name, f.metadata.get("key", f.name), types[f.name]) for f in dataclasses.fields(struct_class))

def _dicts_to_structs(value_type, value):
    """
    Converts dicts received from the robot into the struct classes that value_type describes, also inside
    lists, dicts and tuples. Anything without a struct type, or not shaped as expected, is returned unchanged
    """
    if value is None or value_type is None:
        return value
    if dataclasses.is_dataclass(value_type) and isinstance(value, dict):
        return value_type(**{name: _dicts_to_structs(field_type, value.get(key))
                             for name, key, field_type in _struct_fields(value_type)})
    origin, type_args = typing.get_origin(value_type), typing.get_args(value_type)
    if origin is list and type_args and isinstance(value, (list, tuple)):
        return [_dicts_to_structs(type_args[0], item) for item in value]
    if origin is dict and len(type_args) == 2 and isinstance(value, dict):
        return {key: _dicts_to_structs(type_args[1], item) for key, item in value.items()}
    if origin is tuple and type_args and isinstance(value, (list, tuple)):
        return tuple(_dicts_to_structs(item_type, item) for item_type, item in zip(type_args, value))
    return value

def _structs_to_dicts(value):
    """Converts struct objects into the dicts the robot accepts, also inside lists, tuples and dicts"""
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return {key: _structs_to_dicts(getattr(value, name)) for name, key, _ in _struct_fields(type(value))}
    if isinstance(value, list):
        return [_structs_to_dicts(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_structs_to_dicts(item) for item in value)
    if isinstance(value, dict):
        return {key: _structs_to_dicts(item) for key, item in value.items()}
    return value

def call_method(service_name, method_name, args = [], returns = None):
    """
    Calls a method of a service on the robot. The generated API functions are built on this.
    returns is the return type, given where it involves structs, so the result is converted into them
    """
    _require_init(f"calling {service_name}.{method_name}")
    run_async = _async_call.active
    _async_call.active = False
    msg = MsgMethodCall(
        service_name=service_name,
        method_name=method_name,
        args=[_structs_to_dicts(arg) for arg in args],
        run_async=run_async
    )
    result = _client.send_message(msg) # Raises ConnectionError when disconnected, unless ignore_disconnected is set
    if run_async:
        if result is None and not robot_connected():
            return RemoteFuture._skipped() # ignore_disconnected is set
        if not isinstance(result, dict) or "future_id" not in result:
            raise RobotError("The robot server does not support async calls. Please update robot_server.py and robot_comm_common.py on the robot.")
        future = RemoteFuture(result["future_id"], f"{service_name}.{method_name}", returns)
        future._watch()
        return future
    return _dicts_to_structs(returns, result)

def call_async(func:Callable[P, T], *args:P.args, **kwargs:P.kwargs) -> RemoteFuture[T]:
    """
    Starts a robot function call without waiting for it to finish, e.g.
        future = call_async(ALAnimationPlayer.run, "animations/Stand/Gestures/Hey_1")
        future.cancel()
    """
    _async_call.active = True
    try:
        future = func(*args, **kwargs)
    finally:
        _async_call.active = False
    if not isinstance(future, RemoteFuture):
        raise TypeError(f"{getattr(func, '__name__', func)} did not call the robot, so it can't be used with call_async")
    return future

def close():
    for listener in list(EventListener.instances_by_key.values()): # A copy, since stop() removes the listener
        #listener.listener_thread.join(timeout=1)
        listener.stop()
    if _client:
        _client.close()

EVENT_QUEUE_WARNING_SIZE = 100 # Events waiting for one listener's callbacks before a warning is logged

@dataclasses.dataclass(frozen=True)
class EventInfo:
    """Details of the event being handled. Read-only. See get_event_info"""
    event_name:str # e.g. "valence", or "TouchChanged" for an ALMemory event
    service_name:str # e.g. "ALMood", empty for an ALMemory event
    robot_time:float # time.time() on the robot when the robot server received the event
    received_time:float # precise_time() on this PC when the event arrived. A different clock than robot_time
    seq:int # Numbers this program's events in the order the robot sent them. Gaps mean dropped events

# The event each dispatcher thread is handling, see get_event_info
_current_event = threading.local()

def get_event_info() -> Optional[EventInfo]:
    """
    Details of the event being handled, such as the robot's time when it happened. Call it inside an event,
    signal or property callback; elsewhere it returns None. A callback that passes the work on to another
    thread must call it first and pass the result along
    """
    return getattr(_current_event, "info", None)

class EventListener:
    """
    One per ALMemory event or service signal, shared by all its subscriptions.
    The robot pushes the events over the main connection, the receive thread passes them on with add_event,
    and a dispatcher thread calls the callbacks, so a slow callback only holds up its own event.
    ALMemory event callbacks get the event's value, signal callbacks get the signal's arguments
    """
    instances_by_key:Dict[str, "EventListener"] = {} # Keyed by event_key()
    def __init__(self, event_name:str, service_name:str = ""):
        self.event_name = event_name
        self.service_name = service_name
        self.key = event_key(service_name, event_name)
        self.callbacks = []
        self.alive = threading.Event()
        self._pending_events = queue.Queue()
        self._warning_size = EVENT_QUEUE_WARNING_SIZE # Doubles with each warning, so the log isn't flooded

        def dispatcher():
            while self.alive.is_set():
                event = self._pending_events.get()
                if event == "die":
                    return
                args = event.get("args", [])
                # Shared by all callbacks for this event, on this thread only
                _current_event.info = EventInfo(self.event_name, self.service_name, event.get("ts"),
                                                event.get("received_time"), event.get("seq"))
                for callback in list(self.callbacks):
                    try:
                        if self.service_name:
                            callback(*args)
                        else:
                            callback(args[0] if args else None)
                    except Exception as e:
                        _logger.exception(e)
                _current_event.info = None
                if self._pending_events.empty():
                    self._warning_size = EVENT_QUEUE_WARNING_SIZE

        # Registered before subscribing, since the robot can push the first event before its reply arrives
        self.instances_by_key[self.key] = self
        self.alive.set()
        try:
            # Raises ConnectionError when disconnected, or returns None if ignore_disconnected is set
            response = _client.send_message(MsgEventSubscription(event_name, True, service_name))
        except Exception:
            self._forget()
            raise
        if not response:
            self.alive.clear()
            return
        if response.get("delivery") != "push":
            # An old server, which answers with a port to poll
            self._forget()
            _client.send_message(MsgEventSubscription(event_name, False, service_name))
            raise RobotError("The robot server is too old for this client. Please update robot_server.py and robot_comm_common.py on the robot.")
        threading.Thread(target=dispatcher, daemon=True).start()

    def add_event(self, event:dict):
        """Called by the receive thread for each event the robot pushes"""
        if not self.alive.is_set():
            return
        self._pending_events.put(event)
        waiting = self._pending_events.qsize()
        if waiting >= self._warning_size:
            self._warning_size *= 2
            _logger.warning(f"The callbacks for {self.key} aren't keeping up: {waiting} events are waiting.")

    def _forget(self):
        """So a later subscription to the same event creates a new listener"""
        self.alive.clear()
        if self.instances_by_key.get(self.key) is self:
            self.instances_by_key.pop(self.key)

    def stop(self):
        self._forget()
        self._pending_events.put("die") # Wakes up the dispatcher thread so it can end
        # Cleanup never raises: without a connection there's nothing to unsubscribe from
        if robot_connected():
            try:
                _client.send_message(MsgEventSubscription(self.event_name, False, self.service_name))
            except Exception:
                pass

class EventSubscription:
    """
    A subscription to an ALMemory event, or to a signal or property of a service when service_name is given.
    Usually created through event.<name>.subscribe() or <Service>.<signal>.subscribe().
    The callback runs on a background thread, one per event. Inside it, get_event_info() gives details
    of the event, such as the robot's time when it happened
    """
    def __init__(self, event_name, callback, service_name = ""):
        key = event_key(service_name, event_name)
        _require_init(f"subscribing to {key}")
        self._listener = EventListener.instances_by_key.get(key)
        if not self._listener:
            self._listener = EventListener(event_name, service_name)
        self._callback = callback
        self._listener.callbacks.append(callback)
    def unsubscribe(self):
        self._listener.callbacks.remove(self._callback)
        if not self._listener.callbacks:
            self._listener.stop()

class Signal(Generic[P]):
    """
    A signal of a robot service, e.g. ALBehaviorManager.signals.behaviorStarted.
    The callback is called with the signal's arguments.
    """
    def __init__(self, service_name:str, name:str, types:Tuple = None):
        self.service_name = service_name
        self.name = name
        self._types = types # The argument types, given where they involve structs, see _dicts_to_structs
    def subscribe(self, callback:Callable[P, None]) -> EventSubscription:
        """
        Calls callback with the signal's arguments each time the robot sends it, on a background thread.
        Inside the callback, get_event_info() gives details such as the robot's time when it happened
        """
        if self._types:
            original = callback
            def callback(*args):
                original(*[_dicts_to_structs(arg_type, arg) for arg_type, arg in zip(self._types, args)])
        return EventSubscription(self.name, callback, self.service_name)

class Property(Generic[T]):
    """
    A property of a robot service, e.g. ALMood.properties.ambiance: a value on the robot.
    get() returns it, set(value) changes it, and subscribe(callback) calls callback(value)
    each time the robot sets it. Some properties are set regularly even when the value doesn't change
    (e.g. ALMood.ambiance every second). Where a matching ...Changed signal exists
    (e.g. ALMood.signals.ambianceChanged), see its description.
    """
    def __init__(self, service_name:str, name:str, value_type = None):
        self.service_name = service_name
        self.name = name
        self._value_type = value_type # Given where the value involves structs, see _dicts_to_structs
    def get(self) -> T:
        _require_init(f"reading {self.service_name}.{self.name}")
        return _dicts_to_structs(self._value_type, _client.send_message(MsgPropertyAccess(self.service_name, self.name)))
    def set(self, value:T) -> None:
        _require_init(f"setting {self.service_name}.{self.name}")
        _client.send_message(MsgPropertyAccess(self.service_name, self.name, True, _structs_to_dicts(value)))
    def subscribe(self, callback:Callable[[T], None]) -> EventSubscription:
        """
        Calls callback with the value each time the robot sets it, on a background thread.
        Inside the callback, get_event_info() gives details such as the robot's time when it was set
        """
        if self._value_type is not None:
            original = callback
            def callback(value):
                original(_dicts_to_structs(self._value_type, value))
        return EventSubscription(self.name, callback, self.service_name)

