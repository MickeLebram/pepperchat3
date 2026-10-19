"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

@overload
def get(p0:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	get has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- get_1(str)
	- get_2(int, str)
	- get_3(str, str)
	- get_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def get(p0:int, p1:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	get has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- get_1(str)
	- get_2(int, str)
	- get_3(str, str)
	- get_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def get(p0:str, p1:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	get has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- get_1(str)
	- get_2(int, str)
	- get_3(str, str)
	- get_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def get(p0:str, p1:int, p2:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	get has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- get_1(str)
	- get_2(int, str)
	- get_3(str, str)
	- get_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def get(*args, **kwargs):
	"""
	Bridge notes
	------------
	get has 4 variants on the robot:
	- get(p0:str), explicitly get_1
	- get(p0:int, p1:str), explicitly get_2
	- get(p0:str, p1:str), explicitly get_3
	- get(p0:str, p1:int, p2:str), explicitly get_4
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo.get has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "get", list(args))

def get_1(p0:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	Explicit variant of get(str). Calling get instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "get", [p0])

def get_2(p0:int, p1:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	Explicit variant of get(int, str). Calling get instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "get", [p0, p1])

def get_3(p0:str, p1:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	Explicit variant of get(str, str). Calling get instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "get", [p0, p1])

def get_4(p0:str, p1:int, p2:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	Explicit variant of get(str, int, str). Calling get instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "get",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "get", [p0, p1, p2])

@overload
def _set(p0:str, p1:Any, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	
	Bridge notes
	------------
	_set has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "_set",
	#     "parametersSignature": "(sm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _set(p0:int, p1:str, p2:Any, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:Any
		
	
	Bridge notes
	------------
	_set has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "b",
	#     "name": "_set",
	#     "parametersSignature": "(ism)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _set(*args, **kwargs):
	"""
	Bridge notes
	------------
	_set has 2 variants on the robot:
	- _set(p0:str, p1:Any)
	- _set(p0:int, p1:str, p2:Any)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo._set has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "_set", list(args))

@overload
def set(p0:str, p1:str, p2:Any, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:Any
		
	
	Bridge notes
	------------
	set has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "b",
	#     "name": "set",
	#     "parametersSignature": "(ssm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def set(p0:str, p1:int, p2:str, p3:Any, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	p3:Any
		
	
	Bridge notes
	------------
	set has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "b",
	#     "name": "set",
	#     "parametersSignature": "(sism)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def set(*args, **kwargs):
	"""
	Bridge notes
	------------
	set has 2 variants on the robot:
	- set(p0:str, p1:str, p2:Any)
	- set(p0:str, p1:int, p2:str, p3:Any)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo.set has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "set", list(args))

@overload
def has(p0:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	has has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- has_1(str)
	- has_2(int, str)
	- has_3(str, str)
	- has_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def has(p0:int, p1:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	has has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- has_1(str)
	- has_2(int, str)
	- has_3(str, str)
	- has_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def has(p0:str, p1:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	has has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- has_1(str)
	- has_2(int, str)
	- has_3(str, str)
	- has_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def has(p0:str, p1:int, p2:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	has has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- has_1(str)
	- has_2(int, str)
	- has_3(str, str)
	- has_4(str, int, str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def has(*args, **kwargs):
	"""
	Bridge notes
	------------
	has has 4 variants on the robot:
	- has(p0:str), explicitly has_1
	- has(p0:int, p1:str), explicitly has_2
	- has(p0:str, p1:str), explicitly has_3
	- has(p0:str, p1:int, p2:str), explicitly has_4
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo.has has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "has", list(args))

def has_1(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	Explicit variant of has(str). Calling has instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "has", [p0])

def has_2(p0:int, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	Explicit variant of has(int, str). Calling has instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "has", [p0, p1])

def has_3(p0:str, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	Explicit variant of has(str, str). Calling has instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "has", [p0, p1])

def has_4(p0:str, p1:int, p2:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	Explicit variant of has(str, int, str). Calling has instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "b",
	#     "name": "has",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "has", [p0, p1, p2])

@overload
def _remove(p0:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	_remove has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "b",
	#     "name": "_remove",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _remove(p0:int, p1:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	_remove has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "b",
	#     "name": "_remove",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _remove(*args, **kwargs):
	"""
	Bridge notes
	------------
	_remove has 2 variants on the robot:
	- _remove(p0:str)
	- _remove(p0:int, p1:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo._remove has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "_remove", list(args))

@overload
def remove(p0:str, p1:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	remove has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "remove",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def remove(p0:str, p1:int, p2:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	remove has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "remove",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def remove(*args, **kwargs):
	"""
	Bridge notes
	------------
	remove has 2 variants on the robot:
	- remove(p0:str, p1:str)
	- remove(p0:str, p1:int, p2:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo.remove has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "remove", list(args))

@overload
def removeUser(p0:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	removeUser has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "removeUser",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def removeUser(p0:str, p1:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	Bridge notes
	------------
	removeUser has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "removeUser",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def removeUser(*args, **kwargs):
	"""
	Bridge notes
	------------
	removeUser has 2 variants on the robot:
	- removeUser(p0:str)
	- removeUser(p0:str, p1:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo.removeUser has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "removeUser", list(args))

@overload
def _removeUser() -> bool:
	"""
	
	
	Bridge notes
	------------
	_removeUser has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "_removeUser",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _removeUser(p0:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	_removeUser has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "_removeUser",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _removeUser(*args, **kwargs):
	"""
	Bridge notes
	------------
	_removeUser has 2 variants on the robot:
	- _removeUser()
	- _removeUser(p0:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserInfo._removeUser has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserInfo", "_removeUser", list(args))

def getType(p0:str, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "s",
	#     "name": "getType",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserInfo", "getType", [p0, p1])

class _Signals:
	userInfoEdited: Signal[[int, str, Any]] = Signal("ALUserInfo", "userInfoEdited")
	"""
	Bridge notes
	------------
	A signal sent by ALUserInfo on the robot.
	
	subscribe(callback) calls callback(int, str, Any) each time the robot sends it.
	"""
	userInfoRemoved: Signal[[int, str]] = Signal("ALUserInfo", "userInfoRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALUserInfo on the robot.
	
	subscribe(callback) calls callback(int, str) each time the robot sends it.
	"""
signals = _Signals()

