"""
This module raises an event about the position of tracked person. This event can then be used as input of the function trackEvent of ALTracker.
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
	return call_method("_ALFastPersonTracking", "version", [])

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
	return call_method("_ALFastPersonTracking", "ping", [])

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
	return call_method("_ALFastPersonTracking", "getMethodList", [])

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
	return call_method("_ALFastPersonTracking", "getMethodHelp", [methodName])

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
	return call_method("_ALFastPersonTracking", "getModuleHelp", [])

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
	return call_method("_ALFastPersonTracking", "getBrokerName", [])

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
	return call_method("_ALFastPersonTracking", "getUsage", [name])

@overload
def startTracking() -> None:
	"""
	Starts the module's process, the events are then raised.
	
	Bridge notes
	------------
	startTracking has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startTracking",
	#     "parametersSignature": "()",
	#     "description": "Starts the module's process, the events are then raised.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def startTracking(position:List[float], /) -> None:
	"""
	Starts the module's process, the events are then raised.
	
	Parameters
	----------
	position:List[float]
		Position to start the tracking.
	
	Bridge notes
	------------
	startTracking has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "startTracking",
	#     "parametersSignature": "([f])",
	#     "description": "Starts the module's process, the events are then raised.",
	#     "parameters": [
	#         {
	#             "name": "position",
	#             "description": "Position to start the tracking."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def startTracking(*args, **kwargs):
	"""
	Bridge notes
	------------
	startTracking has 2 variants on the robot:
	- startTracking()
	- startTracking(position:List[float])
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_ALFastPersonTracking.startTracking has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_ALFastPersonTracking", "startTracking", list(args))

def stopTracking() -> None:
	"""
	Stops the module's process, the events are not raised anymore.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "stopTracking",
	#     "parametersSignature": "()",
	#     "description": "Stops the module's process, the events are not raised anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALFastPersonTracking", "stopTracking", [])

def isTracking() -> bool:
	"""
	Tells if the module is running or not.
	
	Returns
	----------
	True if the module is running, False if not.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "isTracking",
	#     "parametersSignature": "()",
	#     "description": "Tells if the module is running or not.",
	#     "parameters": [],
	#     "returnDescription": "True if the module is running, False if not."
	# }
	return call_method("_ALFastPersonTracking", "isTracking", [])

def setTrackingDistance(distance:float) -> None:
	"""
	Sets the distance (in meters) for the tracking
	
	Parameters
	----------
	distance:float
		New value (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "setTrackingDistance",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the distance (in meters) for the tracking",
	#     "parameters": [
	#         {
	#             "name": "distance",
	#             "description": "New value (in meters)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALFastPersonTracking", "setTrackingDistance", [distance])

def getTrackingDistance() -> float:
	"""
	Gets the distance (in meters) for the tracking
	
	Returns
	----------
	Current tracking distance (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "f",
	#     "name": "getTrackingDistance",
	#     "parametersSignature": "()",
	#     "description": "Gets the distance (in meters) for the tracking",
	#     "parameters": [],
	#     "returnDescription": "Current tracking distance (in meters)"
	# }
	return call_method("_ALFastPersonTracking", "getTrackingDistance", [])

def setTrackingPosition(x:float, y:float, z:float) -> None:
	"""
	Sets the position (in world frame) for the tracking
	
	Parameters
	----------
	x:float
		X coordinate in world frame (in meters)
	y:float
		Y coordinate in world frame (in meters)
	z:float
		Z coordinate in world frame (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setTrackingPosition",
	#     "parametersSignature": "(fff)",
	#     "description": "Sets the position (in world frame) for the tracking",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "X coordinate in world frame (in meters)"
	#         },
	#         {
	#             "name": "y",
	#             "description": "Y coordinate in world frame (in meters)"
	#         },
	#         {
	#             "name": "z",
	#             "description": "Z coordinate in world frame (in meters)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALFastPersonTracking", "setTrackingPosition", [x, y, z])

def getTrackingPosition() -> Any:
	"""
	Gets the position (in world frame) for the tracking
	
	Returns
	----------
	Current tracking postion [x,y,z] in world frame
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "getTrackingPosition",
	#     "parametersSignature": "()",
	#     "description": "Gets the position (in world frame) for the tracking",
	#     "parameters": [],
	#     "returnDescription": "Current tracking postion [x,y,z] in world frame"
	# }
	return call_method("_ALFastPersonTracking", "getTrackingPosition", [])

def _setDetectionMode(mode:str) -> None:
	"""
	Sets the mode (2D/3D) used for the tracking.
	
	Parameters
	----------
	mode:str
		Mode to use.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "_setDetectionMode",
	#     "parametersSignature": "(s)",
	#     "description": "Sets the mode (2D/3D) used for the tracking.",
	#     "parameters": [
	#         {
	#             "name": "mode",
	#             "description": "Mode to use."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALFastPersonTracking", "_setDetectionMode", [mode])

def _getDetectionMode() -> str:
	"""
	Gets the mode (2D/3D) used for the tracking.
	
	Returns
	----------
	Current mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "_getDetectionMode",
	#     "parametersSignature": "()",
	#     "description": "Gets the mode (2D/3D) used for the tracking.",
	#     "parameters": [],
	#     "returnDescription": "Current mode."
	# }
	return call_method("_ALFastPersonTracking", "_getDetectionMode", [])

def getDefaultPeriod() -> int:
	"""
	Get the default running period
	
	Returns
	----------
	Default period in ms.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "getDefaultPeriod",
	#     "parametersSignature": "()",
	#     "description": "Get the default running period",
	#     "parameters": [],
	#     "returnDescription": "Default period in ms."
	# }
	return call_method("_ALFastPersonTracking", "getDefaultPeriod", [])

