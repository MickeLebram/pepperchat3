from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module is dedicated to inform if the robot is touched [joints or button]
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
	return send_mfc("ALTouch", "version", [])

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
	return send_mfc("ALTouch", "ping", [])

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
	return send_mfc("ALTouch", "getMethodList", [])

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
	return send_mfc("ALTouch", "getMethodHelp", [methodName])

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
	return send_mfc("ALTouch", "getModuleHelp", [])

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
	return send_mfc("ALTouch", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALTouch", "wait", [id])

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
	return send_mfc("ALTouch", "isRunning", [id])

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
	return send_mfc("ALTouch", "stop", [id])

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
	return send_mfc("ALTouch", "getBrokerName", [])

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
	return send_mfc("ALTouch", "getUsage", [name])

def _setTouchConfig(config:object) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:object
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "_setTouchConfig",
	    "parametersSignature": "(m)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "config",
	            "description": "Internal: An array of ALValues [i][0]: name, [i][1]: value"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_setTouchConfig", [config])

def getSensorList() -> List[str]:
	"""
	Return the list of sensors managed by touch module and return by TouchChangedevent.
	
	Returns
	----------
	A vector<std::string> of sensor names manage by ALTouch.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "[s]",
	    "name": "getSensorList",
	    "parametersSignature": "()",
	    "description": "Return the list of sensors managed by touch module and return by TouchChangedevent.",
	    "parameters": [],
	    "returnDescription": "A vector<std::string> of sensor names manage by ALTouch."
	}
	'''
	"""
	return send_mfc("ALTouch", "getSensorList", [])

def getStatus() -> object:
	"""
	Return the current status of all Touch groups.
	
	Returns
	----------
	A vector of pair [name, bool], similar to TouchChanged event.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "getStatus",
	    "parametersSignature": "()",
	    "description": "Return the current status of all Touch groups.",
	    "parameters": [],
	    "returnDescription": "A vector of pair [name, bool], similar to TouchChanged event."
	}
	'''
	"""
	return send_mfc("ALTouch", "getStatus", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "_createGroup",
	    "parametersSignature": "(s[s])",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the group to create."
	        },
	        {
	            "name": "jointNames",
	            "description": "A vector of joint and actuator names constituting the group."
	        }
	    ],
	    "returnDescription": "true if the group was created, false otherwise."
	}
	'''
	"""
	return send_mfc("ALTouch", "_createGroup", [groupName, jointNames])

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
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "_deleteGroup",
	    "parametersSignature": "(s)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the group to delete"
	        }
	    ],
	    "returnDescription": "true if the group was deleted, false otherwise"
	}
	'''
	"""
	return send_mfc("ALTouch", "_deleteGroup", [groupName])

def _getGroupList() -> List[str]:
	"""
	Internal Use.
	
	Returns
	----------
	The list of groups used for sending touch events
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "[s]",
	    "name": "_getGroupList",
	    "parametersSignature": "()",
	    "description": "Internal Use.",
	    "parameters": [],
	    "returnDescription": "The list of groups used for sending touch events"
	}
	'''
	"""
	return send_mfc("ALTouch", "_getGroupList", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "s",
	    "name": "_getDetectionTypeName",
	    "parametersSignature": "(i)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "type",
	            "description": "Touch detection type enum"
	        }
	    ],
	    "returnDescription": "The name of a touch detection type"
	}
	'''
	"""
	return send_mfc("ALTouch", "_getDetectionTypeName", [type])

def _triggerMotionReflex(groupName:str) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the touched group
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_triggerMotionReflex",
	    "parametersSignature": "(s)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the touched group"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_triggerMotionReflex", [groupName])

def _notifyTouchStopped(groupName:str) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	groupName:str
		The name of the touched group
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "_notifyTouchStopped",
	    "parametersSignature": "(s)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the touched group"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_notifyTouchStopped", [groupName])

def _robotFallingCallback(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when robot is falling
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_robotFallingCallback",
	    "parametersSignature": "(smm)",
	    "description": "Callback when robot is falling",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_robotFallingCallback", [p0, p1, p2])

def _robotFallenCallback(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when robot has fallen
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_robotFallenCallback",
	    "parametersSignature": "(smm)",
	    "description": "Callback when robot has fallen",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_robotFallenCallback", [p0, p1, p2])

def _diagnosisCallback(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when diagnosis change.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_diagnosisCallback",
	    "parametersSignature": "(smm)",
	    "description": "Callback when diagnosis change.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_diagnosisCallback", [p0, p1, p2])

def _temperatureCallback(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when temperature diagnosis change.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "_temperatureCallback",
	    "parametersSignature": "(smm)",
	    "description": "Callback when temperature diagnosis change.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTouch", "_temperatureCallback", [p0, p1, p2])

