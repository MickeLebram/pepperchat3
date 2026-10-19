# -*- coding: utf-8 -*-
import base64
import json
import struct


ROBOT_SERVER_PORT = 5556

# The date of the last change to the protocol: the message classes and their fields, and the system commands.
# A second change on the same day gets a suffix: "2026-10-19.2". Change it by hand with every protocol change,
# and only then. The client compares the robot server's with its own at init() (MsgSystemCommand.GET_VERSION).
# Servers from before 2026-10-19 can't report theirs
PROTOCOL_VERSION = "2026-10-19"

# Binary data (camera images, raw buffers) can't go into JSON as it is. It travels as base64 text in a dict
# with this single key, at any depth of a value. NAOqi's Python 2 binding gives raw data as bytearray
BYTES_MARKER = "__naoqibridge_bytes__"

def _is_binary(value):
    # In Python 2, str is also text, so only bytearray counts there. In Python 3, bytes counts too
    return isinstance(value, bytearray) or (bytes is not str and isinstance(value, bytes))

def binary_to_json(value):
    """Replaces binary data at any depth of value with {BYTES_MARKER: base64 text}, so json can send it"""
    if _is_binary(value):
        return {BYTES_MARKER: base64.b64encode(bytes(value)).decode("ascii")}
    if isinstance(value, (list, tuple)):
        return [binary_to_json(item) for item in value]
    if isinstance(value, dict):
        return dict((key, binary_to_json(item)) for key, item in value.items())
    return value

def json_to_binary(value):
    """Turns the {BYTES_MARKER: ...} dicts back into binary data: bytearray in Python 2 (as NAOqi uses), bytes in Python 3"""
    if isinstance(value, dict):
        if len(value) == 1 and BYTES_MARKER in value:
            data = base64.b64decode(str(value[BYTES_MARKER])) # str: in Python 2, json gives unicode; base64 is ASCII
            return bytearray(data) if bytes is str else data
        return dict((key, json_to_binary(item)) for key, item in value.items())
    if isinstance(value, list):
        return [json_to_binary(item) for item in value]
    return value

class MsgBase(object):
    def __init__(self):
        self.type = self.__class__.__name__
        self.client_id = ""
        self.id = ""

class MsgMethodCall(MsgBase):
    # Calls a method of a service on the robot
    def __init__(self, service_name="", method_name="", args=[], run_async=False):
        MsgBase.__init__(self)
        self.service_name = service_name
        self.method_name = method_name
        self.args = args
        self.run_async = run_async # If True, the server replies with a future_id instead of the result

class MsgFutureCommand(MsgBase):
    # Operations on a qi.Future that was started by an async MsgMethodCall
    CANCEL = "CANCEL"
    WAIT = "WAIT"
    GET_STATE = "GET_STATE"
    def __init__(self, future_id="", command="", timeout_ms=None):
        MsgBase.__init__(self)
        self.future_id = future_id
        self.command = command
        self.timeout_ms = timeout_ms # Only used by WAIT. None means wait forever

class MsgEventSubscription(MsgBase):
    def __init__(self, event_name="", subscribe=False, service_name=""):
        MsgBase.__init__(self)
        self.event_name = event_name
        self.subscribe = subscribe
        self.service_name = service_name # Empty: an ALMemory event. Otherwise a signal or property of that service

def event_key(service_name, event_name):
    """One name for an ALMemory event or a service's signal, e.g. "TouchChanged" or "ALBehaviorManager.behaviorStarted" """
    return service_name + "." + event_name if service_name else event_name

class MsgPropertyAccess(MsgBase):
    # Reads a property of a service, or sets it when set_value is True
    def __init__(self, service_name="", property_name="", set_value=False, value=None):
        MsgBase.__init__(self)
        self.service_name = service_name
        self.property_name = property_name
        self.set_value = set_value
        self.value = value

class MsgSystemCommand(MsgBase):
    GET_SERVICE_NAMES = "GET_SERVICES"
    PING = "PING" # The client's heartbeat. Any reply shows the server is alive
    GET_TIME = "GET_TIME" # The robot's time.time(), to estimate the offset between the robot's and the PC's clocks
    SET_LOG_LEVEL = "SET_LOG_LEVEL" # args: ["DEBUG"] or ["INFO"]. For the whole server, until it restarts
    GET_LOG = "GET_LOG" # args: [number of lines]. The end of the server's log
    CANCEL_ALL_FUTURES = "CANCEL_ALL_FUTURES" # Cancels the running calls started with call_async, of every client
    GET_VERSION = "GET_VERSION" # The server's PROTOCOL_VERSION
    def __init__(self, command="", args=[]):
        MsgBase.__init__(self)
        self.command = command
        self.args = args

class MsgEventChannel(MsgBase):
    # The first message on a client's second connection: from then on the server sends that client's events
    # there, so a large reply on the main connection (e.g. a camera image) doesn't hold them up
    def __init__(self):
        MsgBase.__init__(self)

class MsgEvent(MsgBase):
    # Sent by the server, unasked, on the main connection: one event that the client subscribed to
    def __init__(self, event_name="", service_name="", args=[], ts=0.0, seq=0, dropped=0):
        MsgBase.__init__(self)
        self.event_name = event_name
        self.service_name = service_name # Empty for an ALMemory event, as in MsgEventSubscription
        self.args = args # ALMemory events have one (the value), signals and properties 0 or more
        self.ts = ts # The robot's time.time() when the server received the event
        self.seq = seq # Numbers the events sent to this client, in the order they were queued
        self.dropped = dropped # Events dropped just before this one, because the client didn't read them in time


def read_packet(sock):
    def read_bytes(cnt):
        ba = bytearray()
        read_cnt = 0
        while read_cnt < cnt:
            chunk = sock.recv(cnt - read_cnt)
            if not chunk:
                raise EOFError("Connection closed by peer")
            ba.extend(chunk)
            read_cnt += len(chunk)
        return ba
    payload_len = struct.unpack("!I", read_bytes(4))[0]
    return read_bytes(payload_len)


def send_packet(sock, packet_bytes):
    sock.sendall(struct.pack("!I", len(packet_bytes)) + packet_bytes)

def send_dict(sock, dct):
    jsn = json.dumps(dct)
    packet_bytes = jsn.encode("utf-8")
    send_packet(sock, packet_bytes)

def read_dict(sock):
    packet_bytes = read_packet(sock)
    return json.loads(packet_bytes.decode("utf-8"))
