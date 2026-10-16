"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def check_if_can_sleep() -> object:
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

def check_start_sleep(p0:object, p1:object, p2:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	p2:object
		
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

def sleep_mode() -> object:
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

