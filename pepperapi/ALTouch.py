"""
This module is dedicated to inform if the robot is touched [joints or button]
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
	return call_method("ALTouch", "version", [])

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
	return call_method("ALTouch", "ping", [])

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
	return call_method("ALTouch", "getMethodList", [])

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
	return call_method("ALTouch", "getMethodHelp", [methodName])

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
	return call_method("ALTouch", "getModuleHelp", [])

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
	return call_method("ALTouch", "getBrokerName", [])

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
	return call_method("ALTouch", "getUsage", [name])

def _setTouchConfig(config:Any) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:Any
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_setTouchConfig",
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
	return call_method("ALTouch", "_setTouchConfig", [config])

def getSensorList() -> List[str]:
	"""
	Return the list of sensors managed by touch module and return by TouchChangedevent.
	
	Returns
	----------
	A vector<std::string> of sensor names manage by ALTouch.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "[s]",
	#     "name": "getSensorList",
	#     "parametersSignature": "()",
	#     "description": "Return the list of sensors managed by touch module and return by TouchChangedevent.",
	#     "parameters": [],
	#     "returnDescription": "A vector<std::string> of sensor names manage by ALTouch."
	# }
	return call_method("ALTouch", "getSensorList", [])

def getStatus() -> Any:
	"""
	Return the current status of all Touch groups.
	
	Returns
	----------
	A vector of pair [name, bool], similar to TouchChanged event.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "getStatus",
	#     "parametersSignature": "()",
	#     "description": "Return the current status of all Touch groups.",
	#     "parameters": [],
	#     "returnDescription": "A vector of pair [name, bool], similar to TouchChanged event."
	# }
	return call_method("ALTouch", "getStatus", [])

def _createGroup(groupName:str, jointNames:List[str]) -> bool:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the group to create.
	jointNames:List[str]
		A vector of joint and actuator names constituting the group.
	
	Returns
	----------
	true if the group was created, false otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "_createGroup",
	#     "parametersSignature": "(s[s])",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the group to create."
	#         },
	#         {
	#             "name": "jointNames",
	#             "description": "A vector of joint and actuator names constituting the group."
	#         }
	#     ],
	#     "returnDescription": "true if the group was created, false otherwise."
	# }
	return call_method("ALTouch", "_createGroup", [groupName, jointNames])

def _deleteGroup(groupName:str) -> bool:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the group to delete
	
	Returns
	----------
	true if the group was deleted, false otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "_deleteGroup",
	#     "parametersSignature": "(s)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the group to delete"
	#         }
	#     ],
	#     "returnDescription": "true if the group was deleted, false otherwise"
	# }
	return call_method("ALTouch", "_deleteGroup", [groupName])

def _getGroupList() -> List[str]:
	"""
	Internal Use.
	
	Returns
	----------
	The list of groups used for sending touch events
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "[s]",
	#     "name": "_getGroupList",
	#     "parametersSignature": "()",
	#     "description": "Internal Use.",
	#     "parameters": [],
	#     "returnDescription": "The list of groups used for sending touch events"
	# }
	return call_method("ALTouch", "_getGroupList", [])

def _getDetectionTypeName(type:int) -> str:
	"""
	Internal Use.
	
	Parameters
	----------
	type:int
		Touch detection type enum
	
	Returns
	----------
	The name of a touch detection type
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "s",
	#     "name": "_getDetectionTypeName",
	#     "parametersSignature": "(i)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "type",
	#             "description": "Touch detection type enum"
	#         }
	#     ],
	#     "returnDescription": "The name of a touch detection type"
	# }
	return call_method("ALTouch", "_getDetectionTypeName", [type])

def _triggerMotionReflex(groupName:str) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the touched group
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_triggerMotionReflex",
	#     "parametersSignature": "(s)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the touched group"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_triggerMotionReflex", [groupName])

def _notifyTouchStopped(groupName:str) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the touched group
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "_notifyTouchStopped",
	#     "parametersSignature": "(s)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the touched group"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_notifyTouchStopped", [groupName])

def _robotFallingCallback(p0:str, p1:Any, p2:Any) -> None:
	"""
	Callback when robot is falling
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_robotFallingCallback",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when robot is falling",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_robotFallingCallback", [p0, p1, p2])

def _robotFallenCallback(p0:str, p1:Any, p2:Any) -> None:
	"""
	Callback when robot has fallen
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_robotFallenCallback",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when robot has fallen",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_robotFallenCallback", [p0, p1, p2])

def _diagnosisCallback(p0:str, p1:Any, p2:Any) -> None:
	"""
	Callback when diagnosis change.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_diagnosisCallback",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when diagnosis change.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_diagnosisCallback", [p0, p1, p2])

def _temperatureCallback(p0:str, p1:Any, p2:Any) -> None:
	"""
	Callback when temperature diagnosis change.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_temperatureCallback",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when temperature diagnosis change.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTouch", "_temperatureCallback", [p0, p1, p2])

