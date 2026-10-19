"""
ALTargetManager.
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
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
	return call_method("_ALTargetManager", "version", [])

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
	return call_method("_ALTargetManager", "ping", [])

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
	return call_method("_ALTargetManager", "getMethodList", [])

def getMethodHelp(methodName:str) -> Any:
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
	return call_method("_ALTargetManager", "getMethodHelp", [methodName])

def getModuleHelp() -> Any:
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
	return call_method("_ALTargetManager", "getModuleHelp", [])

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
	return call_method("_ALTargetManager", "getBrokerName", [])

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
	return call_method("_ALTargetManager", "getUsage", [name])

def start() -> None:
	"""
	Start the target manager. Subscribe to all extractors corresponding to targets setted.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "()",
	#     "description": "Start the target manager. Subscribe to all extractors corresponding to targets setted.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "start", [])

def stopManager() -> None:
	"""
	Stop target Manager. Unsubscribe to all extractors.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "stopManager",
	#     "parametersSignature": "()",
	#     "description": "Stop target Manager. Unsubscribe to all extractors.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "stopManager", [])

def addTarget(pTarget_name:str, pParam:Any) -> None:
	"""
	Add a predefined target. Subscribe to corresponding extractor if TargetManager is running.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name
	pParam:Any
		a target parameters. (RedBall: set diameter of ball.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "addTarget",
	#     "parametersSignature": "(sm)",
	#     "description": "Add a predefined target. Subscribe to corresponding extractor if TargetManager is running.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name"
	#         },
	#         {
	#             "name": "pParam",
	#             "description": "a target parameters. (RedBall: set diameter of ball."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "addTarget", [pTarget_name, pParam])

def removeTarget(pTarget_name:str) -> None:
	"""
	Remove target from manager and stop corresponding extractor.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "removeTarget",
	#     "parametersSignature": "(s)",
	#     "description": "Remove target from manager and stop corresponding extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "removeTarget", [pTarget_name])

def removeTargets(pTarget_name_array:List[str]) -> None:
	"""
	Remove targets from manager.
	
	Parameters
	----------
	pTarget_name_array:List[str]
		array with predefined targets names
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "removeTargets",
	#     "parametersSignature": "([s])",
	#     "description": "Remove targets from manager.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name array",
	#             "description": "array with predefined targets names"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "removeTargets", [pTarget_name_array])

def removeAllTargets() -> None:
	"""
	Remove all targets from manager except active target.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "removeAllTargets",
	#     "parametersSignature": "()",
	#     "description": "Remove all targets from manager except active target.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "removeAllTargets", [])

def setActiveTarget(pTarget_name:str) -> None:
	"""
	Active a target added before.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setActiveTarget",
	#     "parametersSignature": "(s)",
	#     "description": "Active a target added before.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "setActiveTarget", [pTarget_name])

def setActiveEvent(pTarget_name:str) -> None:
	"""
	Active a target added before.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "setActiveEvent",
	#     "parametersSignature": "(s)",
	#     "description": "Active a target added before.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "setActiveEvent", [pTarget_name])

def getActiveTarget() -> str:
	"""
	Return active target name.
	
	Returns
	----------
	Active target name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "s",
	#     "name": "getActiveTarget",
	#     "parametersSignature": "()",
	#     "description": "Return active target name.",
	#     "parameters": [],
	#     "returnDescription": "Active target name."
	# }
	return call_method("_ALTargetManager", "getActiveTarget", [])

def getActiveTargetPosition() -> List[float]:
	"""
	Return active target position.
	
	Returns
	----------
	Active target position.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "[f]",
	#     "name": "getActiveTargetPosition",
	#     "parametersSignature": "()",
	#     "description": "Return active target position.",
	#     "parameters": [],
	#     "returnDescription": "Active target position."
	# }
	return call_method("_ALTargetManager", "getActiveTargetPosition", [])

def getEventName() -> str:
	"""
	Return event name to subscribe.
	
	Returns
	----------
	Event name to subscribe.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "s",
	#     "name": "getEventName",
	#     "parametersSignature": "()",
	#     "description": "Return event name to subscribe.",
	#     "parameters": [],
	#     "returnDescription": "Event name to subscribe."
	# }
	return call_method("_ALTargetManager", "getEventName", [])

def getSecondEventName() -> str:
	"""
	Return second event name to subscribe.
	
	Returns
	----------
	Event name to subscribe.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "s",
	#     "name": "getSecondEventName",
	#     "parametersSignature": "()",
	#     "description": "Return second event name to subscribe.",
	#     "parameters": [],
	#     "returnDescription": "Event name to subscribe."
	# }
	return call_method("_ALTargetManager", "getSecondEventName", [])

def isTargetManaged(pTarget_name:str) -> bool:
	"""
	Return if a target was added.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name.
	
	Returns
	----------
	True if target name is managed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "isTargetManaged",
	#     "parametersSignature": "(s)",
	#     "description": "Return if a target was added.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name."
	#         }
	#     ],
	#     "returnDescription": "True if target name is managed."
	# }
	return call_method("_ALTargetManager", "isTargetManaged", [pTarget_name])

def getTargetIds(pTarget_name:str) -> List[int]:
	"""
	Return a list of target ids.
	
	Parameters
	----------
	pTarget_name:str
		a predefined target name.
	
	Returns
	----------
	List of target ids.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "[i]",
	#     "name": "getTargetIds",
	#     "parametersSignature": "(s)",
	#     "description": "Return a list of target ids.",
	#     "parameters": [
	#         {
	#             "name": "pTarget name",
	#             "description": "a predefined target name."
	#         }
	#     ],
	#     "returnDescription": "List of target ids."
	# }
	return call_method("_ALTargetManager", "getTargetIds", [pTarget_name])

def getSupportedTargets() -> List[str]:
	"""
	Return a list of all possible target names.
	
	Returns
	----------
	List of possible target names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "[s]",
	#     "name": "getSupportedTargets",
	#     "parametersSignature": "()",
	#     "description": "Return a list of all possible target names.",
	#     "parameters": [],
	#     "returnDescription": "List of possible target names."
	# }
	return call_method("_ALTargetManager", "getSupportedTargets", [])

def getRegisteredTargets() -> List[str]:
	"""
	Return a list of the currently registered targets names.
	
	Returns
	----------
	List of currently registered targets names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "[s]",
	#     "name": "getRegisteredTargets",
	#     "parametersSignature": "()",
	#     "description": "Return a list of the currently registered targets names.",
	#     "parameters": [],
	#     "returnDescription": "List of currently registered targets names."
	# }
	return call_method("_ALTargetManager", "getRegisteredTargets", [])

def setExtractorPeriod(pTarget:str, pPeriod:int) -> None:
	"""
	Set a period for the corresponding target name extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	pPeriod:int
		a period in milliseconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "setExtractorPeriod",
	#     "parametersSignature": "(si)",
	#     "description": "Set a period for the corresponding target name extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target name.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         },
	#         {
	#             "name": "pPeriod",
	#             "description": "a period in milliseconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "setExtractorPeriod", [pTarget, pPeriod])

def getExtractorPeriod(pTarget:str) -> int:
	"""
	Get the period of corresponding target name extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People"or  "Sound".
	
	Returns
	----------
	a period in milliseconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "i",
	#     "name": "getExtractorPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Get the period of corresponding target name extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target name.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\"or  \"Sound\"."
	#         }
	#     ],
	#     "returnDescription": "a period in milliseconds"
	# }
	return call_method("_ALTargetManager", "getExtractorPeriod", [pTarget])

def _raiseEvent(key:str, value:Any) -> None:
	"""
	callback method.
	
	Parameters
	----------
	key:str
		ALMemory key.
	value:Any
		ALValue of key.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_raiseEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "callback method.",
	#     "parameters": [
	#         {
	#             "name": "key",
	#             "description": "ALMemory key."
	#         },
	#         {
	#             "name": "value",
	#             "description": "ALValue of key."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "_raiseEvent", [key, value])

def _genericEvent(p0:str, p1:Any) -> None:
	"""
	generic event callback.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_genericEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "generic event callback.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALTargetManager", "_genericEvent", [p0, p1])

