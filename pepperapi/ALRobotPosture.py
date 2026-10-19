"""
Use ALRobotPosture module to make the robot go tothe asked posture.
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
	return call_method("ALRobotPosture", "version", [])

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
	return call_method("ALRobotPosture", "ping", [])

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
	return call_method("ALRobotPosture", "getMethodList", [])

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
	return call_method("ALRobotPosture", "getMethodHelp", [methodName])

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
	return call_method("ALRobotPosture", "getModuleHelp", [])

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
	return call_method("ALRobotPosture", "getBrokerName", [])

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
	return call_method("ALRobotPosture", "getUsage", [name])

def getPostureFamily() -> str:
	"""
	Returns the posture family for example Standing, LyingBelly,...
	
	Returns
	----------
	Returns the posture family, e.g. Standing.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "s",
	#     "name": "getPostureFamily",
	#     "parametersSignature": "()",
	#     "description": "Returns the posture family for example Standing, LyingBelly,...",
	#     "parameters": [],
	#     "returnDescription": "Returns the posture family, e.g. Standing."
	# }
	return call_method("ALRobotPosture", "getPostureFamily", [])

def goToPosture(postureName:str, maxSpeedFraction:float) -> bool:
	"""
	Make the robot go to the choosenposture.
	
	Parameters
	----------
	postureName:str
		Name of the desired posture. Use getPostureList to get the list of posture name available.
	maxSpeedFraction:float
		A fraction.
	
	Returns
	----------
	Returns if the posture was reached or not.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "goToPosture",
	#     "parametersSignature": "(sf)",
	#     "description": "Make the robot go to the choosenposture.",
	#     "parameters": [
	#         {
	#             "name": "postureName",
	#             "description": "Name of the desired posture. Use getPostureList to get the list of posture name available."
	#         },
	#         {
	#             "name": "maxSpeedFraction",
	#             "description": "A fraction."
	#         }
	#     ],
	#     "returnDescription": "Returns if the posture was reached or not."
	# }
	return call_method("ALRobotPosture", "goToPosture", [postureName, maxSpeedFraction])

def applyPosture(postureName:str, maxSpeedFraction:float) -> bool:
	"""
	Set the angle of the joints of the  robot to the choosen posture.
	
	Parameters
	----------
	postureName:str
		Name of the desired posture. Use getPostureList to get the list of posture name available.
	maxSpeedFraction:float
		A fraction.
	
	Returns
	----------
	Returns if the posture was reached or not.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "applyPosture",
	#     "parametersSignature": "(sf)",
	#     "description": "Set the angle of the joints of the  robot to the choosen posture.",
	#     "parameters": [
	#         {
	#             "name": "postureName",
	#             "description": "Name of the desired posture. Use getPostureList to get the list of posture name available."
	#         },
	#         {
	#             "name": "maxSpeedFraction",
	#             "description": "A fraction."
	#         }
	#     ],
	#     "returnDescription": "Returns if the posture was reached or not."
	# }
	return call_method("ALRobotPosture", "applyPosture", [postureName, maxSpeedFraction])

def stopMove() -> None:
	"""
	Stop the posture move.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "stopMove",
	#     "parametersSignature": "()",
	#     "description": "Stop the posture move.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "stopMove", [])

def getPostureList() -> List[str]:
	"""
	Get the list of posture names available.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "[s]",
	#     "name": "getPostureList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of posture names available.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "getPostureList", [])

def getPostureFamilyList() -> List[str]:
	"""
	Get the list of posture family names available.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "[s]",
	#     "name": "getPostureFamilyList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of posture family names available.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "getPostureFamilyList", [])

def setMaxTryNumber(pMaxTryNumber:int) -> None:
	"""
	Set maximum of tries ongoToPosture fail.
	
	Parameters
	----------
	pMaxTryNumber:int
		Number of retry if goToPosture fail.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setMaxTryNumber",
	#     "parametersSignature": "(i)",
	#     "description": "Set maximum of tries ongoToPosture fail.",
	#     "parameters": [
	#         {
	#             "name": "pMaxTryNumber",
	#             "description": "Number of retry if goToPosture fail."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "setMaxTryNumber", [pMaxTryNumber])

def getPosture() -> str:
	"""
	Determine posture.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "s",
	#     "name": "getPosture",
	#     "parametersSignature": "()",
	#     "description": "Determine posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "getPosture", [])

def _isRobotInPosture(p0:str, p1:float, p2:float) -> Any:
	"""
	Articular distance
	
	Parameters
	----------
	p0:str
		
	p1:float
		
	p2:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "m",
	#     "name": "_isRobotInPosture",
	#     "parametersSignature": "(sff)",
	#     "description": "Articular distance",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_isRobotInPosture", [p0, p1, p2])

def _isRobotInPostureId(p0:int, p1:float, p2:float) -> bool:
	"""
	Articular distance
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	p2:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "b",
	#     "name": "_isRobotInPostureId",
	#     "parametersSignature": "(iff)",
	#     "description": "Articular distance",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_isRobotInPostureId", [p0, p1, p2])

def _getPosture() -> Any:
	"""
	Determine posture id.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "_getPosture",
	#     "parametersSignature": "()",
	#     "description": "Determine posture id.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getPosture", [])

def _setPostureId(p0:int, p1:float) -> bool:
	"""
	Set the angle of the joints.
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "b",
	#     "name": "_setPostureId",
	#     "parametersSignature": "(if)",
	#     "description": "Set the angle of the joints.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setPostureId", [p0, p1])

def _goToPostureId(p0:int, p1:float) -> bool:
	"""
	Set the angle of thejoints and of the inertial unit
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "_goToPostureId",
	#     "parametersSignature": "(if)",
	#     "description": "Set the angle of thejoints and of the inertial unit",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_goToPostureId", [p0, p1])

def _namePosture(p0:int, p1:str) -> bool:
	"""
	Name posture from id.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "_namePosture",
	#     "parametersSignature": "(is)",
	#     "description": "Name posture from id.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_namePosture", [p0, p1])

def _renamePosture(p0:str, p1:str) -> bool:
	"""
	Rename posture from name.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "_renamePosture",
	#     "parametersSignature": "(ss)",
	#     "description": "Rename posture from name.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_renamePosture", [p0, p1])

def _resavePosture(p0:int) -> bool:
	"""
	Resave posture joints, inertial, family. Keep neighbours.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "b",
	#     "name": "_resavePosture",
	#     "parametersSignature": "(i)",
	#     "description": "Resave posture joints, inertial, family. Keep neighbours.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_resavePosture", [p0])

def _setSlowFactor(p0:int, p1:int, p2:float) -> bool:
	"""
	Set slow factorbetween two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "_setSlowFactor",
	#     "parametersSignature": "(iif)",
	#     "description": "Set slow factorbetween two postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setSlowFactor", [p0, p1, p2])

def _setAntiCollision(p0:int, p1:bool) -> bool:
	"""
	Set anti collisionbetween two postures.
	
	Parameters
	----------
	p0:int
		
	p1:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "_setAntiCollision",
	#     "parametersSignature": "(ib)",
	#     "description": "Set anti collisionbetween two postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setAntiCollision", [p0, p1])

def _setUseAntiCollision(enable:bool) -> None:
	"""
	Enables/Disables anti collision management by RobotPosture.
	
	Parameters
	----------
	enable:bool
		A bool that enable anticollision management.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_setUseAntiCollision",
	#     "parametersSignature": "(b)",
	#     "description": "Enables/Disables anti collision management by RobotPosture.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "A bool that enable anticollision management."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setUseAntiCollision", [enable])

def _setUseAutoBalance(enable:bool) -> None:
	"""
	Enables/Disables auto balance management by RobotPosture.
	
	Parameters
	----------
	enable:bool
		A bool that enable auto balance management.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_setUseAutoBalance",
	#     "parametersSignature": "(b)",
	#     "description": "Enables/Disables auto balance management by RobotPosture.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "A bool that enable auto balance management."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setUseAutoBalance", [enable])

def _setCost(p0:int, p1:float) -> bool:
	"""
	Set cost between two postures.
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "b",
	#     "name": "_setCost",
	#     "parametersSignature": "(if)",
	#     "description": "Set cost between two postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_setCost", [p0, p1])

def _saveCurrentPosture(p0:int) -> bool:
	"""
	Save current posture.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "_saveCurrentPosture",
	#     "parametersSignature": "(i)",
	#     "description": "Save current posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_saveCurrentPosture", [p0])

def _saveCurrentPostureWithName(p0:int, p1:str) -> bool:
	"""
	Save with a namecurrent posture.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "_saveCurrentPostureWithName",
	#     "parametersSignature": "(is)",
	#     "description": "Save with a namecurrent posture.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_saveCurrentPostureWithName", [p0, p1])

def _applyPostures(p0:List[int], p1:float, p2:bool, p3:bool) -> bool:
	"""
	Apply postures.
	
	Parameters
	----------
	p0:List[int]
		
	p1:float
		
	p2:bool
		
	p3:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "b",
	#     "name": "_applyPostures",
	#     "parametersSignature": "([i]fbb)",
	#     "description": "Apply postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_applyPostures", [p0, p1, p2, p3])

def _eraseAllPostures() -> bool:
	"""
	Erase all postures.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "b",
	#     "name": "_eraseAllPostures",
	#     "parametersSignature": "()",
	#     "description": "Erase all postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_eraseAllPostures", [])

def _bindPostures(p0:int, p1:int, p2:float, p3:float) -> bool:
	"""
	Bind two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	p3:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "_bindPostures",
	#     "parametersSignature": "(iiff)",
	#     "description": "Bind two postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_bindPostures", [p0, p1, p2, p3])

def _addNeighbourToPosture(p0:int, p1:int, p2:float) -> bool:
	"""
	Add a neighbour to a postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "_addNeighbourToPosture",
	#     "parametersSignature": "(iif)",
	#     "description": "Add a neighbour to a postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_addNeighbourToPosture", [p0, p1, p2])

def _removeNeighbourFromPosture(p0:int, p1:int) -> bool:
	"""
	Remove a neighbour from postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "b",
	#     "name": "_removeNeighbourFromPosture",
	#     "parametersSignature": "(ii)",
	#     "description": "Remove a neighbour from postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_removeNeighbourFromPosture", [p0, p1])

def _unBindPostures(p0:int, p1:int) -> bool:
	"""
	Unbind two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "b",
	#     "name": "_unBindPostures",
	#     "parametersSignature": "(ii)",
	#     "description": "Unbind two postures.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_unBindPostures", [p0, p1])

def _erasePosture(p0:int) -> bool:
	"""
	Erase the posture and unBind theneighbours.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "b",
	#     "name": "_erasePosture",
	#     "parametersSignature": "(i)",
	#     "description": "Erase the posture and unBind theneighbours.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_erasePosture", [p0])

def _getLibrarySize() -> int:
	"""
	Get library size.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "i",
	#     "name": "_getLibrarySize",
	#     "parametersSignature": "()",
	#     "description": "Get library size.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getLibrarySize", [])

def _loadPostureLibraryFromName(p0:str) -> bool:
	"""
	Load a new library file.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "b",
	#     "name": "_loadPostureLibraryFromName",
	#     "parametersSignature": "(s)",
	#     "description": "Load a new library file.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_loadPostureLibraryFromName", [p0])

def _getCurrentPath() -> List[float]:
	"""
	Get current graph path.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "[f]",
	#     "name": "_getCurrentPath",
	#     "parametersSignature": "()",
	#     "description": "Get current graph path.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getCurrentPath", [])

def _isStandCallBack(p0:str, p1:Any, p2:str) -> None:
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
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "_isStandCallBack",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_isStandCallBack", [p0, p1, p2])

def _savePostureLibrary(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "b",
	#     "name": "_savePostureLibrary",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_savePostureLibrary", [p0])

def _getArticularDistanceToPosture(p0:int) -> float:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "f",
	#     "name": "_getArticularDistanceToPosture",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getArticularDistanceToPosture", [p0])

def _getCartesianDistanceToPosture(p0:int) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "m",
	#     "name": "_getCartesianDistanceToPosture",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getCartesianDistanceToPosture", [p0])

def _getCartesianDistanceVector(p0:int) -> List[float]:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "[f]",
	#     "name": "_getCartesianDistanceVector",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getCartesianDistanceVector", [p0])

def _getPostureIdList() -> List[int]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "[i]",
	#     "name": "_getPostureIdList",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getPostureIdList", [])

def _isReachable(p0:int) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "b",
	#     "name": "_isReachable",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_isReachable", [p0])

def _generateCartesianMap() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "v",
	#     "name": "_generateCartesianMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_generateCartesianMap", [])

def _getPostureZ(p0:float) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "m",
	#     "name": "_getPostureZ",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getPostureZ", [p0])

def _getPostureNoZ() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "m",
	#     "name": "_getPostureNoZ",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getPostureNoZ", [])

def _getIdFromName(p0:str) -> int:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "i",
	#     "name": "_getIdFromName",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_getIdFromName", [p0])

def _activeDiagnosisCallBack(p0:str, p1:Any, p2:str) -> None:
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
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "_activeDiagnosisCallBack",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_activeDiagnosisCallBack", [p0, p1, p2])

def _eraseFamily(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "b",
	#     "name": "_eraseFamily",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotPosture", "_eraseFamily", [p0])

