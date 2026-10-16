"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
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
	return call_method("ALAutonomousBlinking", "setEnabled", [p0])

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
	return call_method("ALAutonomousBlinking", "isEnabled", [])

