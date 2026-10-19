"""
This module gives access to configuration of the robot defined in xml format

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
	return call_method("ALRobotModel", "version", [])

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
	return call_method("ALRobotModel", "ping", [])

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
	return call_method("ALRobotModel", "getMethodList", [])

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
	return call_method("ALRobotModel", "getMethodHelp", [methodName])

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
	return call_method("ALRobotModel", "getModuleHelp", [])

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
	return call_method("ALRobotModel", "getBrokerName", [])

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
	return call_method("ALRobotModel", "getUsage", [name])

def getConfig() -> str:
	"""
	Return the RobotConfig key/value pairs serialized in xml format
	
	Returns
	----------
	the RobotConfig key/value pairs in xml format
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "s",
	#     "name": "getConfig",
	#     "parametersSignature": "()",
	#     "description": "Return the RobotConfig key/value pairs serialized in xml format",
	#     "parameters": [],
	#     "returnDescription": "the RobotConfig key/value pairs in xml format"
	# }
	return call_method("ALRobotModel", "getConfig", [])

def _getConfigMap() -> Dict[str,Any]:
	"""
	Return the RobotConfig key/value pairs
	
	Returns
	----------
	the RobotConfig key/value pairs in a  std::map<std::string, AL::ALValue>
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "{sm}",
	#     "name": "_getConfigMap",
	#     "parametersSignature": "()",
	#     "description": "Return the RobotConfig key/value pairs",
	#     "parameters": [],
	#     "returnDescription": "the RobotConfig key/value pairs in a  std::map<std::string, AL::ALValue>"
	# }
	return call_method("ALRobotModel", "_getConfigMap", [])

def _isRobocup() -> bool:
	"""
	Determine if the robot is a robocup version.
	
	Returns
	----------
	True if the robot is a robocup version.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "_isRobocup",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot is a robocup version.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot is a robocup version."
	# }
	return call_method("ALRobotModel", "_isRobocup", [])

def _getRobotModel() -> int:
	"""
	Get the robot model. Could be: ROBOT_MODEL_NAO_H25, ROBOT_MODEL_NAO_H21, ....
	
	Returns
	----------
	The robot model.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "_getRobotModel",
	#     "parametersSignature": "()",
	#     "description": "Get the robot model. Could be: ROBOT_MODEL_NAO_H25, ROBOT_MODEL_NAO_H21, ....",
	#     "parameters": [],
	#     "returnDescription": "The robot model."
	# }
	return call_method("ALRobotModel", "_getRobotModel", [])

def _getRobotType() -> int:
	"""
	Get the robot type. Could be: ROBOT_TYPE_NAO, ROBOT_TYPE_ROMEO ....
	
	Returns
	----------
	The robot type.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "i",
	#     "name": "_getRobotType",
	#     "parametersSignature": "()",
	#     "description": "Get the robot type. Could be: ROBOT_TYPE_NAO, ROBOT_TYPE_ROMEO ....",
	#     "parameters": [],
	#     "returnDescription": "The robot type."
	# }
	return call_method("ALRobotModel", "_getRobotType", [])

def getRobotType() -> str:
	"""
	Get the robot type. Could be: Nao, Romeo, Juliette....
	
	Returns
	----------
	The robot type.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "s",
	#     "name": "getRobotType",
	#     "parametersSignature": "()",
	#     "description": "Get the robot type. Could be: Nao, Romeo, Juliette....",
	#     "parameters": [],
	#     "returnDescription": "The robot type."
	# }
	return call_method("ALRobotModel", "getRobotType", [])

def hasArms() -> bool:
	"""
	Determine if the robot has arms.
	
	Returns
	----------
	True if the robot has arms.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "hasArms",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot has arms.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot has arms."
	# }
	return call_method("ALRobotModel", "hasArms", [])

def hasHands() -> bool:
	"""
	Determine if the robot has hands.
	
	Returns
	----------
	True if the robot has hands.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "hasHands",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot has hands.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot has hands."
	# }
	return call_method("ALRobotModel", "hasHands", [])

def hasLegs() -> bool:
	"""
	Determine if the robot has legs.
	
	Returns
	----------
	True if the robot has legs.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "b",
	#     "name": "hasLegs",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot has legs.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot has legs."
	# }
	return call_method("ALRobotModel", "hasLegs", [])

def _setConfigFromConfigXml(fileName:str) -> None:
	"""
	Set config from model type name 
	
	
	Parameters
	----------
	fileName:str
		the file name of config XML (NAOT2V32.xml, NAOH25V40.xml, ...)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_setConfigFromConfigXml",
	#     "parametersSignature": "(s)",
	#     "description": "Set config from model type name \n",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "the file name of config XML (NAOT2V32.xml, NAOH25V40.xml, ...)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotModel", "_setConfigFromConfigXml", [fileName])

def _getMicrophoneConfig() -> int:
	"""
	Get microphone configuration.
	
	Returns
	----------
	Integer value representing the config.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "_getMicrophoneConfig",
	#     "parametersSignature": "()",
	#     "description": "Get microphone configuration.",
	#     "parameters": [],
	#     "returnDescription": "Integer value representing the config."
	# }
	return call_method("ALRobotModel", "_getMicrophoneConfig", [])

def _hasTouchSensorInHands() -> bool:
	"""
	Determine if the robot has touch sensor in the hands.
	
	Returns
	----------
	True if the robot has the sensors.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "_hasTouchSensorInHands",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot has touch sensor in the hands.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot has the sensors."
	# }
	return call_method("ALRobotModel", "_hasTouchSensorInHands", [])

def _hasTablet() -> bool:
	"""
	Determine if the robot has a tablet.
	
	Returns
	----------
	True if the robot has the tablet.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "_hasTablet",
	#     "parametersSignature": "()",
	#     "description": "Determine if the robot has a tablet.",
	#     "parameters": [],
	#     "returnDescription": "True if the robot has the tablet."
	# }
	return call_method("ALRobotModel", "_hasTablet", [])

