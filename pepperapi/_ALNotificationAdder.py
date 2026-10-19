"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

@overload
def _add(p0:int, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	_add has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "i",
	#     "name": "_add",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _add(p0:int, p1:List[str], /) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[str]
		
	
	Bridge notes
	------------
	_add has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "i",
	#     "name": "_add",
	#     "parametersSignature": "(i[s])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _add(*args, **kwargs):
	"""
	Bridge notes
	------------
	_add has 2 variants on the robot:
	- _add(p0:int)
	- _add(p0:int, p1:List[str])
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_ALNotificationAdder._add has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_ALNotificationAdder", "_add", list(args))

@overload
def _get(p0:int, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	_get has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "_get",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _get(p0:int, p1:List[str], /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[str]
		
	
	Bridge notes
	------------
	_get has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "_get",
	#     "parametersSignature": "(i[s])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _get(*args, **kwargs):
	"""
	Bridge notes
	------------
	_get has 2 variants on the robot:
	- _get(p0:int)
	- _get(p0:int, p1:List[str])
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_ALNotificationAdder._get has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_ALNotificationAdder", "_get", list(args))

