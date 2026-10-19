"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def check_if_can_sleep() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "m",
	#     "name": "check_if_can_sleep",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALGoToSleepALD", "check_if_can_sleep", [])

def check_start_sleep(p0:Any, p1:Any, p2:Any) -> Any:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "check_start_sleep",
	#     "parametersSignature": "(mmm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALGoToSleepALD", "check_start_sleep", [p0, p1, p2])

def sleep_mode() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "sleep_mode",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALGoToSleepALD", "sleep_mode", [])

