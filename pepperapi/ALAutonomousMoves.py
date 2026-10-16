"""
Module that manage the background moves automatically started by the robot.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def version() -> str:
	"""
	Returns the version of the module.
	
	Returns
	----------
	A string containing the version of the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "s",
	#     "name": "version",
	#     "parametersSignature": "()",
	#     "description": "Returns the version of the module.",
	#     "parameters": [],
	#     "returnDescription": "A string containing the version of the module."
	# }
	return call_method("ALAutonomousMoves", "version", [])

def ping() -> bool:
	"""
	Just a ping. Always returns true
	
	Returns
	----------
	returns true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "ping",
	#     "parametersSignature": "()",
	#     "description": "Just a ping. Always returns true",
	#     "parameters": [],
	#     "returnDescription": "returns true"
	# }
	return call_method("ALAutonomousMoves", "ping", [])

def getMethodList() -> List[str]:
	"""
	Retrieves the module's method list.
	
	Returns
	----------
	An array of method names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[s]",
	#     "name": "getMethodList",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's method list.",
	#     "parameters": [],
	#     "returnDescription": "An array of method names."
	# }
	return call_method("ALAutonomousMoves", "getMethodList", [])

def getMethodHelp(methodName:str) -> object:
	"""
	Retrieves a method's description.
	
	Parameters
	----------
	methodName:str
		The name of the method.
	
	Returns
	----------
	A structure containing the method's description.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "m",
	#     "name": "getMethodHelp",
	#     "parametersSignature": "(s)",
	#     "description": "Retrieves a method's description.",
	#     "parameters": [
	#         {
	#             "name": "methodName",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A structure containing the method's description."
	# }
	return call_method("ALAutonomousMoves", "getMethodHelp", [methodName])

def getModuleHelp() -> object:
	"""
	Retrieves the module's description.
	
	Returns
	----------
	A structure describing the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "m",
	#     "name": "getModuleHelp",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's description.",
	#     "parameters": [],
	#     "returnDescription": "A structure describing the module."
	# }
	return call_method("ALAutonomousMoves", "getModuleHelp", [])

def getBrokerName() -> str:
	"""
	Gets the name of the parent broker.
	
	Returns
	----------
	The name of the parent broker.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "s",
	#     "name": "getBrokerName",
	#     "parametersSignature": "()",
	#     "description": "Gets the name of the parent broker.",
	#     "parameters": [],
	#     "returnDescription": "The name of the parent broker."
	# }
	return call_method("ALAutonomousMoves", "getBrokerName", [])

def getUsage(name:str) -> str:
	"""
	Gets the method usage string. This summarises how to use the method.
	
	Parameters
	----------
	name:str
		The name of the method.
	
	Returns
	----------
	A string that summarises the usage of the method.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "s",
	#     "name": "getUsage",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the method usage string. This summarises how to use the method.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A string that summarises the usage of the method."
	# }
	return call_method("ALAutonomousMoves", "getUsage", [name])

def _moveForward() -> None:
	"""
	Move forward.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_moveForward",
	#     "parametersSignature": "()",
	#     "description": "Move forward.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_moveForward", [])

def _moveBackward() -> None:
	"""
	Move backward.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_moveBackward",
	#     "parametersSignature": "()",
	#     "description": "Move backward.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_moveBackward", [])

def _moveSides() -> None:
	"""
	Move sides.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_moveSides",
	#     "parametersSignature": "()",
	#     "description": "Move sides.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_moveSides", [])

def _moveRandomly() -> None:
	"""
	Move randomly.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_moveRandomly",
	#     "parametersSignature": "()",
	#     "description": "Move randomly.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_moveRandomly", [])

def setBackgroundStrategy(strategy:str) -> None:
	"""
	The background strategy.
	
	Parameters
	----------
	strategy:str
		The autonomous background posture strategy. ("none" or "backToNeutral")
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setBackgroundStrategy",
	#     "parametersSignature": "(s)",
	#     "description": "The background strategy.",
	#     "parameters": [
	#         {
	#             "name": "strategy",
	#             "description": "The autonomous background posture strategy. (\"none\" or \"backToNeutral\")"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "setBackgroundStrategy", [strategy])

def getBackgroundStrategy() -> str:
	"""
	Gets the background strategy.
	
	Returns
	----------
	The autonomous background posture strategy. ("none" or "backToNeutral")
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getBackgroundStrategy",
	#     "parametersSignature": "()",
	#     "description": "Gets the background strategy.",
	#     "parameters": [],
	#     "returnDescription": "The autonomous background posture strategy. (\"none\" or \"backToNeutral\")"
	# }
	return call_method("ALAutonomousMoves", "getBackgroundStrategy", [])

def _enableJapaneseBackgroundPosture() -> None:
	"""
	Apply a new reset posture.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_enableJapaneseBackgroundPosture",
	#     "parametersSignature": "()",
	#     "description": "Apply a new reset posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_enableJapaneseBackgroundPosture", [])

def _enableDefaultBackgroundPosture() -> None:
	"""
	Apply a new reset posture.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_enableDefaultBackgroundPosture",
	#     "parametersSignature": "()",
	#     "description": "Apply a new reset posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_enableDefaultBackgroundPosture", [])

def _disableBackgroundPosture() -> None:
	"""
	Apply a new reset posture.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_disableBackgroundPosture",
	#     "parametersSignature": "()",
	#     "description": "Apply a new reset posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousMoves", "_disableBackgroundPosture", [])

