"""

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
	return call_method("ALRecharge", "version", [])

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
	return call_method("ALRecharge", "ping", [])

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
	return call_method("ALRecharge", "getMethodList", [])

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
	return call_method("ALRecharge", "getMethodHelp", [methodName])

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
	return call_method("ALRecharge", "getModuleHelp", [])

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
	return call_method("ALRecharge", "getBrokerName", [])

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
	return call_method("ALRecharge", "getUsage", [name])

def goToStation() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "i",
	#     "name": "goToStation",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "goToStation", [])

def leaveStation() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "i",
	#     "name": "leaveStation",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "leaveStation", [])

def getStationPosition() -> List[float]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "[f]",
	#     "name": "getStationPosition",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "getStationPosition", [])

def stopAll() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "stopAll",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "stopAll", [])

def subscribe() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "subscribe", [])

def unsubscribe() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "unsubscribe", [])

def getStatus() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "getStatus",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "getStatus", [])

def lookForStation() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "lookForStation",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "lookForStation", [])

def moveInFrontOfStation() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "moveInFrontOfStation",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "moveInFrontOfStation", [])

def dockOnStation() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "i",
	#     "name": "dockOnStation",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "dockOnStation", [])

def setUseTrackerSearcher(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "setUseTrackerSearcher",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "setUseTrackerSearcher", [p0])

def getUseTrackerSearcher() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "b",
	#     "name": "getUseTrackerSearcher",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "getUseTrackerSearcher", [])

def setMaxNumberOfTries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "setMaxNumberOfTries",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "setMaxNumberOfTries", [p0])

def getMaxNumberOfTries() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "i",
	#     "name": "getMaxNumberOfTries",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "getMaxNumberOfTries", [])

@overload
def adjustDockingPosition() -> int:
	"""
	.
	
	Bridge notes
	------------
	adjustDockingPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "i",
	#     "name": "adjustDockingPosition",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def adjustDockingPosition(p0:List[List[float]], /) -> int:
	"""
	.
	
	Parameters
	----------
	p0:List[List[float]]
		
	
	Bridge notes
	------------
	adjustDockingPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "i",
	#     "name": "adjustDockingPosition",
	#     "parametersSignature": "([[f]])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def adjustDockingPosition(*args, **kwargs):
	"""
	Bridge notes
	------------
	adjustDockingPosition has 2 variants on the robot:
	- adjustDockingPosition()
	- adjustDockingPosition(p0:List[List[float]])
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALRecharge.adjustDockingPosition has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALRecharge", "adjustDockingPosition", list(args))

def _stop() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_stop",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_stop", [])

def _getConfidenceIndex() -> float:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "f",
	#     "name": "_getConfidenceIndex",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getConfidenceIndex", [])

def _allowTrackerNavigateTo(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_allowTrackerNavigateTo",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_allowTrackerNavigateTo", [p0])

def _setFinalApproachDistance(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_setFinalApproachDistance",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setFinalApproachDistance", [p0])

def _getFinalApproachDistance() -> float:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "f",
	#     "name": "_getFinalApproachDistance",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getFinalApproachDistance", [])

def _setFinalApproachYOffset(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "_setFinalApproachYOffset",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setFinalApproachYOffset", [p0])

def _getFinalApproachYOffset() -> float:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "f",
	#     "name": "_getFinalApproachYOffset",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getFinalApproachYOffset", [])

def _setFinalApproachThreshold(p0:List[float]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_setFinalApproachThreshold",
	#     "parametersSignature": "([f])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setFinalApproachThreshold", [p0])

def _getFinalApproachThreshold() -> List[float]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "[f]",
	#     "name": "_getFinalApproachThreshold",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getFinalApproachThreshold", [])

def _setStationDetectionConfidenceThreshold(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_setStationDetectionConfidenceThreshold",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setStationDetectionConfidenceThreshold", [p0])

def _getStationDetectionConfidenceThreshold() -> float:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "f",
	#     "name": "_getStationDetectionConfidenceThreshold",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getStationDetectionConfidenceThreshold", [])

def _startLogging() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "_startLogging",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_startLogging", [])

def _stopLogging() -> str:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "s",
	#     "name": "_stopLogging",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_stopLogging", [])

def _cancelLogging() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "_cancelLogging",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_cancelLogging", [])

def _getFinalConnectionMoves() -> List[List[float]]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "[[f]]",
	#     "name": "_getFinalConnectionMoves",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getFinalConnectionMoves", [])

def _setFinalConnectionMoves(p0:List[List[float]]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[List[float]]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "_setFinalConnectionMoves",
	#     "parametersSignature": "([[f]])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setFinalConnectionMoves", [p0])

def _setFinalConnectionMovesDelay(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "_setFinalConnectionMovesDelay",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setFinalConnectionMovesDelay", [p0])

def _getFinalConnectionMovesDelay() -> float:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "f",
	#     "name": "_getFinalConnectionMovesDelay",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getFinalConnectionMovesDelay", [])

def _setEnableCheckDisconnectionTask(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "_setEnableCheckDisconnectionTask",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setEnableCheckDisconnectionTask", [p0])

def _getEnableCheckDisconnectionTask() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "b",
	#     "name": "_getEnableCheckDisconnectionTask",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getEnableCheckDisconnectionTask", [])

def _getLastHopeMaxRetries() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "I",
	#     "name": "_getLastHopeMaxRetries",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getLastHopeMaxRetries", [])

def _setLastHopeMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "_setLastHopeMaxRetries",
	#     "parametersSignature": "(I)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setLastHopeMaxRetries", [p0])

def _getDockingMaxRetries() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "I",
	#     "name": "_getDockingMaxRetries",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getDockingMaxRetries", [])

def _setDockingMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "v",
	#     "name": "_setDockingMaxRetries",
	#     "parametersSignature": "(I)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setDockingMaxRetries", [p0])

def _getLookMaxRetries() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "I",
	#     "name": "_getLookMaxRetries",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_getLookMaxRetries", [])

def _setLookMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "_setLookMaxRetries",
	#     "parametersSignature": "(I)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_setLookMaxRetries", [p0])

def _updateStationDetection(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "v",
	#     "name": "_updateStationDetection",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_updateStationDetection", [p0, p1, p2])

def _eventTrackerSearcherLoopCallback() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "_eventTrackerSearcherLoopCallback",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventTrackerSearcherLoopCallback", [])

def _eventTrackerTargetReachedCallback() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "_eventTrackerTargetReachedCallback",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventTrackerTargetReachedCallback", [])

def _eventTrackerTargetLostCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "v",
	#     "name": "_eventTrackerTargetLostCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventTrackerTargetLostCallback", [p0, p1, p2])

def _eventTrackerActiveTargetChangedCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "v",
	#     "name": "_eventTrackerActiveTargetChangedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventTrackerActiveTargetChangedCallback", [p0, p1, p2])

def _eventTrackerSearcherScanStartedCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "v",
	#     "name": "_eventTrackerSearcherScanStartedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventTrackerSearcherScanStartedCallback", [p0, p1, p2])

def _eventMoveFailedCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "v",
	#     "name": "_eventMoveFailedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventMoveFailedCallback", [p0, p1, p2])

def _eventBatteryConnectedToChargingStationCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "v",
	#     "name": "_eventBatteryConnectedToChargingStationCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventBatteryConnectedToChargingStationCallback", [p0, p1, p2])

def _eventNavigationStatusChangedCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "v",
	#     "name": "_eventNavigationStatusChangedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventNavigationStatusChangedCallback", [p0, p1, p2])

def _eventSlopeDetectedChangedCallback(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "v",
	#     "name": "_eventSlopeDetectedChangedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRecharge", "_eventSlopeDetectedChangedCallback", [p0, p1, p2])

