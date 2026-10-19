"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def setEnabled(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "setEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALListeningMovement", "setEnabled", [p0])

def isEnabled() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "b",
	#     "name": "isEnabled",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALListeningMovement", "isEnabled", [])

def isRunning() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "isRunning",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALListeningMovement", "isRunning", [])

def _setEnabled(p0:bool, p1:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "_setEnabled",
	#     "parametersSignature": "(bs)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALListeningMovement", "_setEnabled", [p0, p1])

def _isEnabled(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "_isEnabled",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALListeningMovement", "_isEnabled", [p0])

