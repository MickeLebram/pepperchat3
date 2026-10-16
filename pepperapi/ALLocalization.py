"""

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
	return call_method("ALLocalization", "version", [])

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
	return call_method("ALLocalization", "ping", [])

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
	return call_method("ALLocalization", "getMethodList", [])

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
	return call_method("ALLocalization", "getMethodHelp", [methodName])

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
	return call_method("ALLocalization", "getModuleHelp", [])

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
	return call_method("ALLocalization", "getBrokerName", [])

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
	return call_method("ALLocalization", "getUsage", [name])

def getMessageFromErrorCode(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "s",
	#     "name": "getMessageFromErrorCode",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "getMessageFromErrorCode", [p0])

def stopAll() -> None:
	"""
	Stop all robot movements.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "stopAll",
	#     "parametersSignature": "()",
	#     "description": "Stop all robot movements.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "stopAll", [])

def _safetyStop() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_safetyStop",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "_safetyStop", [])

def learnHome() -> int:
	"""
	Learn the robot home.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "learnHome",
	#     "parametersSignature": "()",
	#     "description": "Learn the robot home.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "learnHome", [])

def isInCurrentHome() -> bool:
	"""
	Is the robot in its home?
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "isInCurrentHome",
	#     "parametersSignature": "()",
	#     "description": "Is the robot in its home?",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "isInCurrentHome", [])

def getCurrentPanoramaDescriptor() -> object:
	"""
	Get some information about the current panorama.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "getCurrentPanoramaDescriptor",
	#     "parametersSignature": "()",
	#     "description": "Get some information about the current panorama.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "getCurrentPanoramaDescriptor", [])

def getFrame(p0:int, p1:str) -> object:
	"""
	Get a frame buffer.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "m",
	#     "name": "getFrame",
	#     "parametersSignature": "(is)",
	#     "description": "Get a frame buffer.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "getFrame", [p0, p1])

def clear(pDirectory:str) -> int:
	"""
	Delete all panoramas in a directory.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "clear",
	#     "parametersSignature": "(s)",
	#     "description": "Delete all panoramas in a directory.",
	#     "parameters": [
	#         {
	#             "name": "pDirectory",
	#             "description": "Name of the directory"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "clear", [pDirectory])

def load(pDirectory:str) -> int:
	"""
	Loads panoramas from a directory in the default one.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "load",
	#     "parametersSignature": "(s)",
	#     "description": "Loads panoramas from a directory in the default one.",
	#     "parameters": [
	#         {
	#             "name": "pDirectory",
	#             "description": "Name of the directory"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "load", [pDirectory])

def save(pDirectory:str) -> int:
	"""
	Save the temporary panoramas in a directory from the default one.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "i",
	#     "name": "save",
	#     "parametersSignature": "(s)",
	#     "description": "Save the temporary panoramas in a directory from the default one.",
	#     "parameters": [
	#         {
	#             "name": "pDirectory",
	#             "description": "Name of the directory"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "save", [pDirectory])

def isRelocalizationRequired() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "b",
	#     "name": "isRelocalizationRequired",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "isRelocalizationRequired", [])

def getDriftPercentages() -> List[float]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[f]",
	#     "name": "getDriftPercentages",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "getDriftPercentages", [])

def isDataAvailable() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "isDataAvailable",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "isDataAvailable", [])

@overload
def getRobotPosition() -> List[float]:
	"""
	Get the robot position in world navigation.
	
	Bridge notes
	------------
	getRobotPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "[f]",
	#     "name": "getRobotPosition",
	#     "parametersSignature": "()",
	#     "description": "Get the robot position in world navigation.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def getRobotPosition(p0:bool, /) -> List[float]:
	"""
	Get the robot position in world navigation.
	
	Parameters
	----------
	p0:bool
		
	
	Bridge notes
	------------
	getRobotPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "[f]",
	#     "name": "getRobotPosition",
	#     "parametersSignature": "(b)",
	#     "description": "Get the robot position in world navigation.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def getRobotPosition(*args, **kwargs):
	"""
	Bridge notes
	------------
	getRobotPosition has 2 variants on the robot:
	- getRobotPosition()
	- getRobotPosition(p0:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALLocalization.getRobotPosition has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALLocalization", "getRobotPosition", list(args))

@overload
def getRobotOrientation() -> object:
	"""
	Get the robot orientation.
	
	Bridge notes
	------------
	getRobotOrientation has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "m",
	#     "name": "getRobotOrientation",
	#     "parametersSignature": "()",
	#     "description": "Get the robot orientation.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def getRobotOrientation(p0:bool, /) -> object:
	"""
	Get the robot orientation.
	
	Parameters
	----------
	p0:bool
		
	
	Bridge notes
	------------
	getRobotOrientation has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "m",
	#     "name": "getRobotOrientation",
	#     "parametersSignature": "(b)",
	#     "description": "Get the robot orientation.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def getRobotOrientation(*args, **kwargs):
	"""
	Bridge notes
	------------
	getRobotOrientation has 2 variants on the robot:
	- getRobotOrientation()
	- getRobotOrientation(p0:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALLocalization.getRobotOrientation has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALLocalization", "getRobotOrientation", list(args))

def isInGivenZone(p0:float, p1:float, p2:float, p3:float) -> object:
	"""
	
	
	Parameters
	----------
	p0:float
		
	p1:float
		
	p2:float
		
	p3:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "m",
	#     "name": "isInGivenZone",
	#     "parametersSignature": "(ffff)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "isInGivenZone", [p0, p1, p2, p3])

def _launchLocalization() -> List[float]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "[f]",
	#     "name": "_launchLocalization",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "_launchLocalization", [])

def goToHome() -> int:
	"""
	Go to the robot home.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "i",
	#     "name": "goToHome",
	#     "parametersSignature": "()",
	#     "description": "Go to the robot home.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "goToHome", [])

def goToPosition(p0:List[float]) -> int:
	"""
	Go to a given position.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "i",
	#     "name": "goToPosition",
	#     "parametersSignature": "([f])",
	#     "description": "Go to a given position.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "goToPosition", [p0])

def _getSavingDirectories() -> List[str]:
	"""
	Return the list of saving directories
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "[s]",
	#     "name": "_getSavingDirectories",
	#     "parametersSignature": "()",
	#     "description": "Return the list of saving directories",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "_getSavingDirectories", [])

def _getLoadedDirectory() -> str:
	"""
	Return the current loaded directory name. Will be empty if there is no active panorama or if it has not been saved to a directory yet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "s",
	#     "name": "_getLoadedDirectory",
	#     "parametersSignature": "()",
	#     "description": "Return the current loaded directory name. Will be empty if there is no active panorama or if it has not been saved to a directory yet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "_getLoadedDirectory", [])

def _handlePush() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_handlePush",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLocalization", "_handlePush", [])

