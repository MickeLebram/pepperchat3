"""
Use ALTracker module to make the robot track an object or a person with head and arms or not.
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
	return call_method("ALTracker", "version", [])

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
	return call_method("ALTracker", "ping", [])

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
	return call_method("ALTracker", "getMethodList", [])

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
	return call_method("ALTracker", "getMethodHelp", [methodName])

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
	return call_method("ALTracker", "getModuleHelp", [])

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
	return call_method("ALTracker", "getBrokerName", [])

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
	return call_method("ALTracker", "getUsage", [name])

def getTargetPosition(pFrame:int) -> List[float]:
	"""
	Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.
	
	Parameters
	----------
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	
	Returns
	----------
	Vector of 3 floats corresponding to the target position 3D. 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "[f]",
	#     "name": "getTargetPosition",
	#     "parametersSignature": "(i)",
	#     "description": "Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.",
	#     "parameters": [
	#         {
	#             "name": "pFrame",
	#             "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	#         }
	#     ],
	#     "returnDescription": "Vector of 3 floats corresponding to the target position 3D. "
	# }
	return call_method("ALTracker", "getTargetPosition", [pFrame])

def getRobotPosition() -> List[float]:
	"""
	Only work with LandMarks target name. Returns the [x, y, z, wx, wy, wz] position of the robot in coordinate system setted with setMap API. This is done assuming an average target size, so it might not be very accurate.
	
	Returns
	----------
	Vector of 6 floats corresponding to the robot position 6D.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "[f]",
	#     "name": "getRobotPosition",
	#     "parametersSignature": "()",
	#     "description": "Only work with LandMarks target name. Returns the [x, y, z, wx, wy, wz] position of the robot in coordinate system setted with setMap API. This is done assuming an average target size, so it might not be very accurate.",
	#     "parameters": [],
	#     "returnDescription": "Vector of 6 floats corresponding to the robot position 6D."
	# }
	return call_method("ALTracker", "getRobotPosition", [])

def isActive() -> bool:
	"""
	Return true if Tracker is running.
	
	Returns
	----------
	True if Tracker is running.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "isActive",
	#     "parametersSignature": "()",
	#     "description": "Return true if Tracker is running.",
	#     "parameters": [],
	#     "returnDescription": "True if Tracker is running."
	# }
	return call_method("ALTracker", "isActive", [])

def isNewTargetDetected() -> bool:
	"""
	Return true if a new target was detected.
	
	Returns
	----------
	True if a new target was detected since the last getTargetPosition().
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "isNewTargetDetected",
	#     "parametersSignature": "()",
	#     "description": "Return true if a new target was detected.",
	#     "parameters": [],
	#     "returnDescription": "True if a new target was detected since the last getTargetPosition()."
	# }
	return call_method("ALTracker", "isNewTargetDetected", [])

def setRelativePosition(target:Any) -> None:
	"""
	Set the robot position relative to target in Move mode.
	
	Parameters
	----------
	target:Any
		Set the final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "setRelativePosition",
	#     "parametersSignature": "(m)",
	#     "description": "Set the robot position relative to target in Move mode.",
	#     "parameters": [
	#         {
	#             "name": "target",
	#             "description": "Set the final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz]."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setRelativePosition", [target])

def getRelativePosition() -> Any:
	"""
	Get the robot position relative to target in Move mode.
	
	Returns
	----------
	The final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "getRelativePosition",
	#     "parametersSignature": "()",
	#     "description": "Get the robot position relative to target in Move mode.",
	#     "parameters": [],
	#     "returnDescription": "The final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz]."
	# }
	return call_method("ALTracker", "getRelativePosition", [])

def setTargetCoordinates(pCoord:Any) -> None:
	"""
	Only work with LandMarks target name. Set objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]
	
	Parameters
	----------
	pCoord:Any
		objects coordinates.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setTargetCoordinates",
	#     "parametersSignature": "(m)",
	#     "description": "Only work with LandMarks target name. Set objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]",
	#     "parameters": [
	#         {
	#             "name": "pCoord",
	#             "description": "objects coordinates."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setTargetCoordinates", [pCoord])

def getTargetCoordinates() -> Any:
	"""
	Only work with LandMarks target name. Get objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]
	
	Returns
	----------
	objects coordinates.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "getTargetCoordinates",
	#     "parametersSignature": "()",
	#     "description": "Only work with LandMarks target name. Get objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]",
	#     "parameters": [],
	#     "returnDescription": "objects coordinates."
	# }
	return call_method("ALTracker", "getTargetCoordinates", [])

def setMode(pMode:str) -> None:
	"""
	Set the tracker in the predefined mode.Could be "Head", "WholeBody" or "Move".
	
	Parameters
	----------
	pMode:str
		a predefined mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setMode",
	#     "parametersSignature": "(s)",
	#     "description": "Set the tracker in the predefined mode.Could be \"Head\", \"WholeBody\" or \"Move\".",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "a predefined mode."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setMode", [pMode])

def getMode() -> str:
	"""
	Get the tracker current mode.
	
	Returns
	----------
	The current tracker mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getMode",
	#     "parametersSignature": "()",
	#     "description": "Get the tracker current mode.",
	#     "parameters": [],
	#     "returnDescription": "The current tracker mode."
	# }
	return call_method("ALTracker", "getMode", [])

def getAvailableModes() -> List[str]:
	"""
	Get the list of predefined mode.
	
	Returns
	----------
	List of predefined mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getAvailableModes",
	#     "parametersSignature": "()",
	#     "description": "Get the list of predefined mode.",
	#     "parameters": [],
	#     "returnDescription": "List of predefined mode."
	# }
	return call_method("ALTracker", "getAvailableModes", [])

def toggleSearch(pSearch:bool) -> None:
	"""
	Enables/disables the target search process. Target search process occurs only when the target is lost.
	
	Parameters
	----------
	pSearch:bool
		If true and if the target is lost, the robot moves the head in order to find the target. If false and if the target is lost the robot does not move.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "toggleSearch",
	#     "parametersSignature": "(b)",
	#     "description": "Enables/disables the target search process. Target search process occurs only when the target is lost.",
	#     "parameters": [
	#         {
	#             "name": "pSearch",
	#             "description": "If true and if the target is lost, the robot moves the head in order to find the target. If false and if the target is lost the robot does not move."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "toggleSearch", [pSearch])

def setSearchFractionMaxSpeed(pFractionMaxSpeed:float) -> None:
	"""
	Set search process fraction max speed.
	
	Parameters
	----------
	pFractionMaxSpeed:float
		a fraction max speed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "setSearchFractionMaxSpeed",
	#     "parametersSignature": "(f)",
	#     "description": "Set search process fraction max speed.",
	#     "parameters": [
	#         {
	#             "name": "pFractionMaxSpeed",
	#             "description": "a fraction max speed."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setSearchFractionMaxSpeed", [pFractionMaxSpeed])

def getSearchFractionMaxSpeed() -> float:
	"""
	Get search process fraction max speed.
	
	Returns
	----------
	a fraction max speed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "f",
	#     "name": "getSearchFractionMaxSpeed",
	#     "parametersSignature": "()",
	#     "description": "Get search process fraction max speed.",
	#     "parameters": [],
	#     "returnDescription": "a fraction max speed."
	# }
	return call_method("ALTracker", "getSearchFractionMaxSpeed", [])

def isSearchEnabled() -> bool:
	"""
	Return true if the target search process is enabled.
	
	Returns
	----------
	If true the target search process is enabled.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "isSearchEnabled",
	#     "parametersSignature": "()",
	#     "description": "Return true if the target search process is enabled.",
	#     "parameters": [],
	#     "returnDescription": "If true the target search process is enabled."
	# }
	return call_method("ALTracker", "isSearchEnabled", [])

def stopTracker() -> None:
	"""
	Stop the tracker.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "stopTracker",
	#     "parametersSignature": "()",
	#     "description": "Stop the tracker.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "stopTracker", [])

def isTargetLost() -> bool:
	"""
	Return true if the target was lost.
	
	Returns
	----------
	True if the target was lost.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "isTargetLost",
	#     "parametersSignature": "()",
	#     "description": "Return true if the target was lost.",
	#     "parameters": [],
	#     "returnDescription": "True if the target was lost."
	# }
	return call_method("ALTracker", "isTargetLost", [])

def track(pTarget:str) -> None:
	"""
	Set the predefided target to track and start the tracking process if not started.
	
	Parameters
	----------
	pTarget:str
		a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "track",
	#     "parametersSignature": "(s)",
	#     "description": "Set the predefided target to track and start the tracking process if not started.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target to track.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "track", [pTarget])

def trackEvent(pEventName:str) -> None:
	"""
	Track event and start the tracking process if not started.
	
	Parameters
	----------
	pEventName:str
		a event name to track.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "trackEvent",
	#     "parametersSignature": "(s)",
	#     "description": "Track event and start the tracking process if not started.",
	#     "parameters": [
	#         {
	#             "name": "pEventName",
	#             "description": "a event name to track."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "trackEvent", [pEventName])

def registerTarget(pTarget:str, pParams:Any) -> None:
	"""
	Register a predefined target. Subscribe to corresponding extractor if Tracker is running..
	
	Parameters
	----------
	pTarget:str
		a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	pParams:Any
		a target parameters. (RedBall : set diameter of ball.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "registerTarget",
	#     "parametersSignature": "(sm)",
	#     "description": "Register a predefined target. Subscribe to corresponding extractor if Tracker is running..",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target to track.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         },
	#         {
	#             "name": "pParams",
	#             "description": "a target parameters. (RedBall : set diameter of ball."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "registerTarget", [pTarget, pParams])

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
	#     "uid": 134,
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
	return call_method("ALTracker", "setExtractorPeriod", [pTarget, pPeriod])

def getExtractorPeriod(pTarget:str) -> int:
	"""
	Get the period of corresponding target name extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	
	Returns
	----------
	a period in milliseconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "i",
	#     "name": "getExtractorPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Get the period of corresponding target name extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target name.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         }
	#     ],
	#     "returnDescription": "a period in milliseconds"
	# }
	return call_method("ALTracker", "getExtractorPeriod", [pTarget])

def unregisterTarget(pTarget:str) -> None:
	"""
	Unregister target name and stop corresponding extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "unregisterTarget",
	#     "parametersSignature": "(s)",
	#     "description": "Unregister target name and stop corresponding extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target to remove.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "unregisterTarget", [pTarget])

def unregisterTargets(pTarget:List[str]) -> None:
	"""
	Unregister a list of target names and stop corresponding extractor.
	
	Parameters
	----------
	pTarget:List[str]
		a predefined target list to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "unregisterTargets",
	#     "parametersSignature": "([s])",
	#     "description": "Unregister a list of target names and stop corresponding extractor.",
	#     "parameters": [
	#         {
	#             "name": "pTarget",
	#             "description": "a predefined target list to remove.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "unregisterTargets", [pTarget])

def unregisterAllTargets() -> None:
	"""
	Unregister all targets except active target and stop corresponding extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "unregisterAllTargets",
	#     "parametersSignature": "()",
	#     "description": "Unregister all targets except active target and stop corresponding extractor.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "unregisterAllTargets", [])

def getActiveTarget() -> str:
	"""
	Return active target name.
	
	Returns
	----------
	Tracked target name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "s",
	#     "name": "getActiveTarget",
	#     "parametersSignature": "()",
	#     "description": "Return active target name.",
	#     "parameters": [],
	#     "returnDescription": "Tracked target name."
	# }
	return call_method("ALTracker", "getActiveTarget", [])

def getSupportedTargets() -> List[str]:
	"""
	Return a list of supported targets names.
	
	Returns
	----------
	Supported targets names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "[s]",
	#     "name": "getSupportedTargets",
	#     "parametersSignature": "()",
	#     "description": "Return a list of supported targets names.",
	#     "parameters": [],
	#     "returnDescription": "Supported targets names."
	# }
	return call_method("ALTracker", "getSupportedTargets", [])

def getRegisteredTargets() -> List[str]:
	"""
	Return a list of registered targets names.
	
	Returns
	----------
	Registered targets names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "[s]",
	#     "name": "getRegisteredTargets",
	#     "parametersSignature": "()",
	#     "description": "Return a list of registered targets names.",
	#     "parameters": [],
	#     "returnDescription": "Registered targets names."
	# }
	return call_method("ALTracker", "getRegisteredTargets", [])

def lookAt(pPosition:List[float], pFrame:int, pFractionMaxSpeed:float, pUseWholeBody:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "lookAt",
	#     "parametersSignature": "([f]ifb)",
	#     "description": "Look at the target position with head.\n",
	#     "parameters": [
	#         {
	#             "name": "pPosition",
	#             "description": "position 3D [x, y, z] x position must be striclty positif."
	#         },
	#         {
	#             "name": "pFrame",
	#             "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	#         },
	#         {
	#             "name": "pFractionMaxSpeed",
	#             "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	#         },
	#         {
	#             "name": "pUseWholeBody",
	#             "description": "If true, use whole body constraints."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "lookAt", [pPosition, pFrame, pFractionMaxSpeed, pUseWholeBody])

def pointAt(pEffector:str, pPosition:List[float], pFrame:int, pFractionMaxSpeed:float) -> None:
	"""
	Point at the target position with arms.
	
	
	Parameters
	----------
	pEffector:str
		effector name. Could be "Arms", "LArm", "RArm".
	pPosition:List[float]
		position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "pointAt",
	#     "parametersSignature": "(s[f]if)",
	#     "description": "Point at the target position with arms.\n",
	#     "parameters": [
	#         {
	#             "name": "pEffector",
	#             "description": "effector name. Could be \"Arms\", \"LArm\", \"RArm\"."
	#         },
	#         {
	#             "name": "pPosition",
	#             "description": "position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif."
	#         },
	#         {
	#             "name": "pFrame",
	#             "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	#         },
	#         {
	#             "name": "pFractionMaxSpeed",
	#             "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "pointAt", [pEffector, pPosition, pFrame, pFractionMaxSpeed])

def getMoveConfig() -> Any:
	"""
	Get the config for move modes.
	
	Returns
	----------
	ALMotion GaitConfig
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "m",
	#     "name": "getMoveConfig",
	#     "parametersSignature": "()",
	#     "description": "Get the config for move modes.",
	#     "parameters": [],
	#     "returnDescription": "ALMotion GaitConfig"
	# }
	return call_method("ALTracker", "getMoveConfig", [])

def setMoveConfig(config:Any) -> None:
	"""
	set a config for move modes.
	
	Parameters
	----------
	config:Any
		ALMotion GaitConfig
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "setMoveConfig",
	#     "parametersSignature": "(m)",
	#     "description": "set a config for move modes.",
	#     "parameters": [
	#         {
	#             "name": "config",
	#             "description": "ALMotion GaitConfig"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setMoveConfig", [config])

def getTimeOut() -> int:
	"""
	get the timeout parameter for target lost.
	
	Returns
	----------
	time in milliseconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "i",
	#     "name": "getTimeOut",
	#     "parametersSignature": "()",
	#     "description": "get the timeout parameter for target lost.",
	#     "parameters": [],
	#     "returnDescription": "time in milliseconds."
	# }
	return call_method("ALTracker", "getTimeOut", [])

def setTimeOut(pTimeMs:int) -> None:
	"""
	set the timeout parameter for target lost.
	
	Parameters
	----------
	pTimeMs:int
		time in milliseconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "setTimeOut",
	#     "parametersSignature": "(i)",
	#     "description": "set the timeout parameter for target lost.",
	#     "parameters": [
	#         {
	#             "name": "pTimeMs",
	#             "description": "time in milliseconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setTimeOut", [pTimeMs])

def getMaximumDistanceDetection() -> float:
	"""
	get the maximum distance for target detection in meter.
	
	Returns
	----------
	The maximum distance for target detection in meter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "f",
	#     "name": "getMaximumDistanceDetection",
	#     "parametersSignature": "()",
	#     "description": "get the maximum distance for target detection in meter.",
	#     "parameters": [],
	#     "returnDescription": "The maximum distance for target detection in meter."
	# }
	return call_method("ALTracker", "getMaximumDistanceDetection", [])

def setMaximumDistanceDetection(pMaxDistance:float) -> None:
	"""
	set the maximum target detection distance in meter.
	
	Parameters
	----------
	pMaxDistance:float
		The maximum distance for target detection in meter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "setMaximumDistanceDetection",
	#     "parametersSignature": "(f)",
	#     "description": "set the maximum target detection distance in meter.",
	#     "parameters": [
	#         {
	#             "name": "pMaxDistance",
	#             "description": "The maximum distance for target detection in meter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setMaximumDistanceDetection", [pMaxDistance])

def getEffector() -> str:
	"""
	Get active effector.
	
	Returns
	----------
	Active effector name. Could be: "Arms", "LArm", "RArm" or "None". 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "s",
	#     "name": "getEffector",
	#     "parametersSignature": "()",
	#     "description": "Get active effector.",
	#     "parameters": [],
	#     "returnDescription": "Active effector name. Could be: \"Arms\", \"LArm\", \"RArm\" or \"None\". "
	# }
	return call_method("ALTracker", "getEffector", [])

def setEffector(pEffector:str) -> None:
	"""
	Set an end-effector to move for tracking.
	
	Parameters
	----------
	pEffector:str
		Name of effector. Could be: "Arms", "LArm", "RArm" or "None". 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "setEffector",
	#     "parametersSignature": "(s)",
	#     "description": "Set an end-effector to move for tracking.",
	#     "parameters": [
	#         {
	#             "name": "pEffector",
	#             "description": "Name of effector. Could be: \"Arms\", \"LArm\", \"RArm\" or \"None\". "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setEffector", [pEffector])

def initialize() -> None:
	"""
	Initialize tracker parameters with default values.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "v",
	#     "name": "initialize",
	#     "parametersSignature": "()",
	#     "description": "Initialize tracker parameters with default values.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "initialize", [])

def setMaximumVelocity(pVelocity:float) -> None:
	"""
	Set the maximum velocity for tracking.
	
	Parameters
	----------
	pVelocity:float
		The maximum velocity in rad.s-1 .
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "v",
	#     "name": "setMaximumVelocity",
	#     "parametersSignature": "(f)",
	#     "description": "Set the maximum velocity for tracking.",
	#     "parameters": [
	#         {
	#             "name": "pVelocity",
	#             "description": "The maximum velocity in rad.s-1 ."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setMaximumVelocity", [pVelocity])

def getMaximumVelocity() -> float:
	"""
	Get the maximum velocity for tracking.
	
	Returns
	----------
	The maximum velocity in rad.s-1 .
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "f",
	#     "name": "getMaximumVelocity",
	#     "parametersSignature": "()",
	#     "description": "Get the maximum velocity for tracking.",
	#     "parameters": [],
	#     "returnDescription": "The maximum velocity in rad.s-1 ."
	# }
	return call_method("ALTracker", "getMaximumVelocity", [])

def setMaximumAcceleration(pAcceleration:float) -> None:
	"""
	Set the maximum acceleration for tracking.
	
	Parameters
	----------
	pAcceleration:float
		The maximum acceleration in rad.s-2 .
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "setMaximumAcceleration",
	#     "parametersSignature": "(f)",
	#     "description": "Set the maximum acceleration for tracking.",
	#     "parameters": [
	#         {
	#             "name": "pAcceleration",
	#             "description": "The maximum acceleration in rad.s-2 ."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "setMaximumAcceleration", [pAcceleration])

def getMaximumAcceleration() -> float:
	"""
	Get the maximum acceleration for tracking.
	
	Returns
	----------
	The maximum acceleration in rad.s-2 .
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "f",
	#     "name": "getMaximumAcceleration",
	#     "parametersSignature": "()",
	#     "description": "Get the maximum acceleration for tracking.",
	#     "parameters": [],
	#     "returnDescription": "The maximum acceleration in rad.s-2 ."
	# }
	return call_method("ALTracker", "getMaximumAcceleration", [])

def _pause() -> None:
	"""
	Pause the tracking process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "v",
	#     "name": "_pause",
	#     "parametersSignature": "()",
	#     "description": "Pause the tracking process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_pause", [])

def _restart() -> None:
	"""
	Restart the tracking process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "v",
	#     "name": "_restart",
	#     "parametersSignature": "()",
	#     "description": "Restart the tracking process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_restart", [])

def _setTrackerConfig(config:Any) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:Any
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "v",
	#     "name": "_setTrackerConfig",
	#     "parametersSignature": "(m)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "config",
	#             "description": "Internal: An array of ALValues [i][0]: name, [i][1]: value"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_setTrackerConfig", [config])

def _getTrackerConfig() -> Dict[str,float]:
	"""
	Get the tracker configuration.
	
	Returns
	----------
	map contraining all the information.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "{sf}",
	#     "name": "_getTrackerConfig",
	#     "parametersSignature": "()",
	#     "description": "Get the tracker configuration.",
	#     "parameters": [],
	#     "returnDescription": "map contraining all the information."
	# }
	return call_method("ALTracker", "_getTrackerConfig", [])

def _getTrackerConfigStr() -> str:
	"""
	Get the tracker configuration.
	
	Returns
	----------
	string contraining all the information.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "s",
	#     "name": "_getTrackerConfigStr",
	#     "parametersSignature": "()",
	#     "description": "Get the tracker configuration.",
	#     "parameters": [],
	#     "returnDescription": "string contraining all the information."
	# }
	return call_method("ALTracker", "_getTrackerConfigStr", [])

def _lostEvent() -> None:
	"""
	Lost event callback.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "v",
	#     "name": "_lostEvent",
	#     "parametersSignature": "()",
	#     "description": "Lost event callback.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_lostEvent", [])

def _detectedEvent(p0:str, p1:Any) -> None:
	"""
	Detected event callback.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "v",
	#     "name": "_detectedEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Detected event callback.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_detectedEvent", [p0, p1])

def _setDebugInView3D(p0:bool) -> None:
	"""
	Active debug in choregraphe 3D view.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "v",
	#     "name": "_setDebugInView3D",
	#     "parametersSignature": "(b)",
	#     "description": "Active debug in choregraphe 3D view.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_setDebugInView3D", [p0])

def _debugCallbackEvent(p0:str, p1:Any) -> None:
	"""
	debug event callback.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "v",
	#     "name": "_debugCallbackEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "debug event callback.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_debugCallbackEvent", [p0, p1])

def _lookAtWithMove(pPosition:List[float], pFractionMaxSpeed:float, pUseWholeBody:bool, pUseMove:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] to look in FRAME_TORSO.x position must be striclty positif.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use.Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	pUseMove:bool
		If true, use move to look at target behind.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "v",
	#     "name": "_lookAtWithMove",
	#     "parametersSignature": "([f]fbb)",
	#     "description": "Look at the target position with head.\n",
	#     "parameters": [
	#         {
	#             "name": "pPosition",
	#             "description": "position 3D [x, y, z] to look in FRAME_TORSO.x position must be striclty positif."
	#         },
	#         {
	#             "name": "pFractionMaxSpeed",
	#             "description": "The fraction of maximum speed to use.Must be between 0 and 1."
	#         },
	#         {
	#             "name": "pUseWholeBody",
	#             "description": "If true, use whole body constraints."
	#         },
	#         {
	#             "name": "pUseMove",
	#             "description": "If true, use move to look at target behind."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_lookAtWithMove", [pPosition, pFractionMaxSpeed, pUseWholeBody, pUseMove])

def _lookAtWithEffector(pPosition:List[float], pFrame:int, pEffectorId:int, pFractionMaxSpeed:float, pUseWholeBody:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pEffectorId:int
		effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "v",
	#     "name": "_lookAtWithEffector",
	#     "parametersSignature": "([f]iifb)",
	#     "description": "Look at the target position with head.\n",
	#     "parameters": [
	#         {
	#             "name": "pPosition",
	#             "description": "position 3D [x, y, z] x position must be striclty positif."
	#         },
	#         {
	#             "name": "pFrame",
	#             "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	#         },
	#         {
	#             "name": "pEffectorId",
	#             "description": "effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}."
	#         },
	#         {
	#             "name": "pFractionMaxSpeed",
	#             "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	#         },
	#         {
	#             "name": "pUseWholeBody",
	#             "description": "If true, use whole body constraints."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_lookAtWithEffector", [pPosition, pFrame, pEffectorId, pFractionMaxSpeed, pUseWholeBody])

def _stopLookAt() -> None:
	"""
	Stop current look at
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 179,
	#     "returnSignature": "v",
	#     "name": "_stopLookAt",
	#     "parametersSignature": "()",
	#     "description": "Stop current look at\n",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_stopLookAt", [])

def _stopPointAt() -> None:
	"""
	Stop current point at
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "v",
	#     "name": "_stopPointAt",
	#     "parametersSignature": "()",
	#     "description": "Stop current point at\n",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_stopPointAt", [])

def _searcherSetUseWholeBodyLookAt(p0:bool) -> None:
	"""
	Enable whole body look at during search
	
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "v",
	#     "name": "_searcherSetUseWholeBodyLookAt",
	#     "parametersSignature": "(b)",
	#     "description": "Enable whole body look at during search\n",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_searcherSetUseWholeBodyLookAt", [p0])

def _setMoveEvent(p0:str) -> None:
	"""
	Set a specific event for move.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "v",
	#     "name": "_setMoveEvent",
	#     "parametersSignature": "(s)",
	#     "description": "Set a specific event for move.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_setMoveEvent", [p0])

def _setMoveHysteresis(p0:List[float]) -> None:
	"""
	Set move hysteresis.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "v",
	#     "name": "_setMoveHysteresis",
	#     "parametersSignature": "([f])",
	#     "description": "Set move hysteresis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_setMoveHysteresis", [p0])

def _getMoveHysteresis() -> List[float]:
	"""
	Get move hysteresis.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "[f]",
	#     "name": "_getMoveHysteresis",
	#     "parametersSignature": "()",
	#     "description": "Get move hysteresis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTracker", "_getMoveHysteresis", [])

