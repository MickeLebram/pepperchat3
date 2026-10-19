"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method

@dataclass
class SpeakingMovementConfig:
	"""NAOqi signature: (bi{s[s]}b)<SpeakingMovementConfig,enabled,speakingMovementMode,wordsToTags,inputMode2>"""
	enabled: bool
	speakingMovementMode: int
	wordsToTags: Dict[str,List[str]]
	inputMode2: bool


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
	return call_method("ALSpeakingMovement", "setEnabled", [p0])

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
	return call_method("ALSpeakingMovement", "isEnabled", [])

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
	return call_method("ALSpeakingMovement", "isRunning", [])

def setMode(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "setMode",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "setMode", [p0])

def getMode() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "s",
	#     "name": "getMode",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "getMode", [])

def addTagsToWords(p0:Any) -> None:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "addTagsToWords",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "addTagsToWords", [p0])

def resetTagsToWords() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "resetTagsToWords",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "resetTagsToWords", [])

def _reset() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "_reset",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "_reset", [])

def _getConfig() -> SpeakingMovementConfig:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "(bi{s[s]}b)<SpeakingMovementConfig,enabled,speakingMovementMode,wordsToTags,inputMode2>",
	#     "name": "_getConfig",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeakingMovement", "_getConfig", [], returns=SpeakingMovementConfig)

