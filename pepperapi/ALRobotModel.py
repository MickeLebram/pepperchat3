from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module gives access to configuration of the robot defined in xml format

"""
def version() -> str:
	"""
	Returns the version of the module.
	
	Returns
	----------
	A string containing the version of the module.
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "s",
	    "name": "version",
	    "parametersSignature": "()",
	    "description": "Returns the version of the module.",
	    "parameters": [],
	    "returnDescription": "A string containing the version of the module."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "version", [])

def ping() -> bool:
	"""
	Just a ping. Always returns true
	
	Returns
	----------
	returns true
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "b",
	    "name": "ping",
	    "parametersSignature": "()",
	    "description": "Just a ping. Always returns true",
	    "parameters": [],
	    "returnDescription": "returns true"
	}
	'''
	"""
	return send_mfc("ALRobotModel", "ping", [])

def getMethodList() -> List[str]:
	"""
	Retrieves the module's method list.
	
	Returns
	----------
	An array of method names.
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "[s]",
	    "name": "getMethodList",
	    "parametersSignature": "()",
	    "description": "Retrieves the module's method list.",
	    "parameters": [],
	    "returnDescription": "An array of method names."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getMethodList", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "m",
	    "name": "getMethodHelp",
	    "parametersSignature": "(s)",
	    "description": "Retrieves a method's description.",
	    "parameters": [
	        {
	            "name": "methodName",
	            "description": "The name of the method."
	        }
	    ],
	    "returnDescription": "A structure containing the method's description."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getMethodHelp", [methodName])

def getModuleHelp() -> object:
	"""
	Retrieves the module's description.
	
	Returns
	----------
	A structure describing the module.
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "m",
	    "name": "getModuleHelp",
	    "parametersSignature": "()",
	    "description": "Retrieves the module's description.",
	    "parameters": [],
	    "returnDescription": "A structure describing the module."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getModuleHelp", [])

def wait_1(id:int, timeoutPeriod:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (wait)
	
	Wait for the end of a long running method that was called using 'post'
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	timeoutPeriod:int
		The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
	
	Returns
	----------
	True if the timeout period terminated. False if the method returned.
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "b",
	    "name": "wait",
	    "parametersSignature": "(ii)",
	    "description": "Wait for the end of a long running method that was called using 'post'",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        },
	        {
	            "name": "timeoutPeriod",
	            "description": "The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero."
	        }
	    ],
	    "returnDescription": "True if the timeout period terminated. False if the method returned."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "wait", [id, timeoutPeriod])

def wait_2(id:int) -> None:
	"""
	Note: This is one of the overloads of the original method (wait)
	
	Wait for the end of a long running method that was called using 'post', returns a cancelable future
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "v",
	    "name": "wait",
	    "parametersSignature": "(i)",
	    "description": "Wait for the end of a long running method that was called using 'post', returns a cancelable future",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotModel", "wait", [id])

def isRunning(id:int) -> bool:
	"""
	Returns true if the method is currently running.
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	
	Returns
	----------
	True if the method is currently running
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "b",
	    "name": "isRunning",
	    "parametersSignature": "(i)",
	    "description": "Returns true if the method is currently running.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        }
	    ],
	    "returnDescription": "True if the method is currently running"
	}
	'''
	"""
	return send_mfc("ALRobotModel", "isRunning", [id])

def stop(id:int) -> None:
	"""
	returns true if the method is currently running
	
	Parameters
	----------
	id:int
		the ID of the method to wait for
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "stop",
	    "parametersSignature": "(i)",
	    "description": "returns true if the method is currently running",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "the ID of the method to wait for"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotModel", "stop", [id])

def getBrokerName() -> str:
	"""
	Gets the name of the parent broker.
	
	Returns
	----------
	The name of the parent broker.
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "s",
	    "name": "getBrokerName",
	    "parametersSignature": "()",
	    "description": "Gets the name of the parent broker.",
	    "parameters": [],
	    "returnDescription": "The name of the parent broker."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getBrokerName", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "s",
	    "name": "getUsage",
	    "parametersSignature": "(s)",
	    "description": "Gets the method usage string. This summarises how to use the method.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the method."
	        }
	    ],
	    "returnDescription": "A string that summarises the usage of the method."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getUsage", [name])

def getConfig() -> str:
	"""
	Return the RobotConfig key/value pairs serialized in xml format
	
	Returns
	----------
	the RobotConfig key/value pairs in xml format
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "s",
	    "name": "getConfig",
	    "parametersSignature": "()",
	    "description": "Return the RobotConfig key/value pairs serialized in xml format",
	    "parameters": [],
	    "returnDescription": "the RobotConfig key/value pairs in xml format"
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getConfig", [])

def _getConfigMap() -> Dict[str,object]:
	"""
	Return the RobotConfig key/value pairs
	
	Returns
	----------
	the RobotConfig key/value pairs in a  std::map<std::string, AL::ALValue>
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "{sm}",
	    "name": "_getConfigMap",
	    "parametersSignature": "()",
	    "description": "Return the RobotConfig key/value pairs",
	    "parameters": [],
	    "returnDescription": "the RobotConfig key/value pairs in a  std::map<std::string, AL::ALValue>"
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_getConfigMap", [])

def _isRobocup() -> bool:
	"""
	Determine if the robot is a robocup version.
	
	Returns
	----------
	True if the robot is a robocup version.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "_isRobocup",
	    "parametersSignature": "()",
	    "description": "Determine if the robot is a robocup version.",
	    "parameters": [],
	    "returnDescription": "True if the robot is a robocup version."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_isRobocup", [])

def _getRobotModel() -> int:
	"""
	Get the robot model. Could be: ROBOT_MODEL_NAO_H25, ROBOT_MODEL_NAO_H21, ....
	
	Returns
	----------
	The robot model.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "_getRobotModel",
	    "parametersSignature": "()",
	    "description": "Get the robot model. Could be: ROBOT_MODEL_NAO_H25, ROBOT_MODEL_NAO_H21, ....",
	    "parameters": [],
	    "returnDescription": "The robot model."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_getRobotModel", [])

def _getRobotType() -> int:
	"""
	Get the robot type. Could be: ROBOT_TYPE_NAO, ROBOT_TYPE_ROMEO ....
	
	Returns
	----------
	The robot type.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "i",
	    "name": "_getRobotType",
	    "parametersSignature": "()",
	    "description": "Get the robot type. Could be: ROBOT_TYPE_NAO, ROBOT_TYPE_ROMEO ....",
	    "parameters": [],
	    "returnDescription": "The robot type."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_getRobotType", [])

def getRobotType() -> str:
	"""
	Get the robot type. Could be: Nao, Romeo, Juliette....
	
	Returns
	----------
	The robot type.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "s",
	    "name": "getRobotType",
	    "parametersSignature": "()",
	    "description": "Get the robot type. Could be: Nao, Romeo, Juliette....",
	    "parameters": [],
	    "returnDescription": "The robot type."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "getRobotType", [])

def hasArms() -> bool:
	"""
	Determine if the robot has arms.
	
	Returns
	----------
	True if the robot has arms.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "hasArms",
	    "parametersSignature": "()",
	    "description": "Determine if the robot has arms.",
	    "parameters": [],
	    "returnDescription": "True if the robot has arms."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "hasArms", [])

def hasHands() -> bool:
	"""
	Determine if the robot has hands.
	
	Returns
	----------
	True if the robot has hands.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "hasHands",
	    "parametersSignature": "()",
	    "description": "Determine if the robot has hands.",
	    "parameters": [],
	    "returnDescription": "True if the robot has hands."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "hasHands", [])

def hasLegs() -> bool:
	"""
	Determine if the robot has legs.
	
	Returns
	----------
	True if the robot has legs.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "b",
	    "name": "hasLegs",
	    "parametersSignature": "()",
	    "description": "Determine if the robot has legs.",
	    "parameters": [],
	    "returnDescription": "True if the robot has legs."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "hasLegs", [])

def _setConfigFromConfigXml(fileName:str) -> None:
	"""
	Set config from model type name 
	
	
	Parameters
	----------
	fileName:str
		the file name of config XML (NAOT2V32.xml, NAOH25V40.xml, ...)
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_setConfigFromConfigXml",
	    "parametersSignature": "(s)",
	    "description": "Set config from model type name \n",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "the file name of config XML (NAOT2V32.xml, NAOH25V40.xml, ...)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_setConfigFromConfigXml", [fileName])

def _getMicrophoneConfig() -> int:
	"""
	Get microphone configuration.
	
	Returns
	----------
	Integer value representing the config.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "i",
	    "name": "_getMicrophoneConfig",
	    "parametersSignature": "()",
	    "description": "Get microphone configuration.",
	    "parameters": [],
	    "returnDescription": "Integer value representing the config."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_getMicrophoneConfig", [])

def _hasTouchSensorInHands() -> bool:
	"""
	Determine if the robot has touch sensor in the hands.
	
	Returns
	----------
	True if the robot has the sensors.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "b",
	    "name": "_hasTouchSensorInHands",
	    "parametersSignature": "()",
	    "description": "Determine if the robot has touch sensor in the hands.",
	    "parameters": [],
	    "returnDescription": "True if the robot has the sensors."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_hasTouchSensorInHands", [])

def _hasTablet() -> bool:
	"""
	Determine if the robot has a tablet.
	
	Returns
	----------
	True if the robot has the tablet.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "_hasTablet",
	    "parametersSignature": "()",
	    "description": "Determine if the robot has a tablet.",
	    "parameters": [],
	    "returnDescription": "True if the robot has the tablet."
	}
	'''
	"""
	return send_mfc("ALRobotModel", "_hasTablet", [])

