# -*- coding: utf-8 -*-
import json
import struct


ROBOT_SERVER_PORT = 5556

class MsgBase(object):
    def __init__(self):
        self.type = self.__class__.__name__
        self.client_id = ""
        self.id = ""

class MsgModuleFunctionCall(MsgBase):
    def __init__(self, module_name="", func_name="", func_args=[], run_async=False):
        MsgBase.__init__(self)
        self.module_name = module_name
        self.func_name = func_name
        self.func_args = func_args
        self.run_async = run_async # If True, the server replies with a future_id instead of the result

class MsgFutureCommand(MsgBase):
    # Operations on a qi.Future that was started by an async MsgModuleFunctionCall
    CANCEL = "CANCEL"
    WAIT = "WAIT"
    GET_STATE = "GET_STATE"
    def __init__(self, future_id="", cmd="", timeout_ms=None):
        MsgBase.__init__(self)
        self.future_id = future_id
        self.cmd = cmd
        self.timeout_ms = timeout_ms # Only used by WAIT. None means wait forever

class MsgEventSubscription(MsgBase):
    def __init__(self, event_name="", subscribe=False):
        MsgBase.__init__(self)
        self.event_name = event_name
        self.subscribe = subscribe

class MsgSystemCommand(MsgBase):
    GET_MODULE_NAMES = "GET_MODULES"
    def __init__(self, cmd="", args=[]):
        MsgBase.__init__(self)
        self.cmd = cmd
        self.args = args

class MsgEventPoll(MsgBase):
    def __init__(self, timeout = 5):
        MsgBase.__init__(self)
        self.timeout = timeout


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
