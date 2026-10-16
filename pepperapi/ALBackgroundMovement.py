"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method

@dataclass
class IdleDefinition:
	"""NAOqi signature: ([s][s])<IdleDefinition,idleBases,idleBreaks>"""
	idleBases: List[str]
	idleBreaks: List[str]


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
	return call_method("ALBackgroundMovement", "setEnabled", [p0])

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
	return call_method("ALBackgroundMovement", "isEnabled", [])

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
	return call_method("ALBackgroundMovement", "isRunning", [])

def _setMode(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "_setMode",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_setMode", [p0])

def _getMode() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "s",
	#     "name": "_getMode",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_getMode", [])

def _setAwakeMode(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_setAwakeMode",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_setAwakeMode", [p0])

def _getAwakeMode() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "i",
	#     "name": "_getAwakeMode",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_getAwakeMode", [])

def _setDefaultIdle(p0:List[str], p1:List[str]) -> None:
	"""
	
	
	Parameters
	----------
	p0:List[str]
		
	p1:List[str]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "_setDefaultIdle",
	#     "parametersSignature": "([s][s])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_setDefaultIdle", [p0, p1])

def _resetDefaultIdle() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "v",
	#     "name": "_resetDefaultIdle",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_resetDefaultIdle", [])

def _getDefaultIdle() -> IdleDefinition:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "([s][s])<IdleDefinition,idleBases,idleBreaks>",
	#     "name": "_getDefaultIdle",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_getDefaultIdle", [], returns=IdleDefinition)

def _setExpressiveIdle(p0:str, p1:List[str], p2:List[str]) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:List[str]
		
	p2:List[str]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "v",
	#     "name": "_setExpressiveIdle",
	#     "parametersSignature": "(s[s][s])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_setExpressiveIdle", [p0, p1, p2])

def _getExpressiveIdle(p0:str) -> IdleDefinition:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "([s][s])<IdleDefinition,idleBases,idleBreaks>",
	#     "name": "_getExpressiveIdle",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBackgroundMovement", "_getExpressiveIdle", [p0], returns=IdleDefinition)

