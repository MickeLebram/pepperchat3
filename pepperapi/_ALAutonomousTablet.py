"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

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
	return call_method("_ALAutonomousTablet", "setEnabled", [p0])

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
	return call_method("_ALAutonomousTablet", "isEnabled", [])

def setEmotionState(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "setEmotionState",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALAutonomousTablet", "setEmotionState", [p0])

def setFocusedActivity(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "setFocusedActivity",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALAutonomousTablet", "setFocusedActivity", [p0])

def setMode(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "setMode",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALAutonomousTablet", "setMode", [p0])

def getMode() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "s",
	#     "name": "getMode",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALAutonomousTablet", "getMode", [])

def showBubblesView() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "showBubblesView",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALAutonomousTablet", "showBubblesView", [])

class _Signals:
	mode: Signal[[str]] = Signal("_ALAutonomousTablet", "mode")
	"""
	Bridge notes
	------------
	A signal sent by _ALAutonomousTablet on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
signals = _Signals()

