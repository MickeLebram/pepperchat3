from .gentypes import *
from .robot_client import send_mfc
import json
"""
Deals with motor temperature.
A event name HotJointDetected is raised when at least one motor has higher temperature.
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
	return send_mfc("ALBodyTemperature", "version", [])

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
	return send_mfc("ALBodyTemperature", "ping", [])

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
	return send_mfc("ALBodyTemperature", "getMethodList", [])

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
	return send_mfc("ALBodyTemperature", "getMethodHelp", [methodName])

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
	return send_mfc("ALBodyTemperature", "getModuleHelp", [])

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
	return send_mfc("ALBodyTemperature", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALBodyTemperature", "wait", [id])

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
	return send_mfc("ALBodyTemperature", "isRunning", [id])

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
	return send_mfc("ALBodyTemperature", "stop", [id])

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
	return send_mfc("ALBodyTemperature", "getBrokerName", [])

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
	return send_mfc("ALBodyTemperature", "getUsage", [name])

def getTemperatureDiagnosis() -> object:
	"""
	The actual state of the temperature diagnosis.
	
	Returns
	----------
	Return the current temperature diagnosis.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "m",
	    "name": "getTemperatureDiagnosis",
	    "parametersSignature": "()",
	    "description": "The actual state of the temperature diagnosis.",
	    "parameters": [],
	    "returnDescription": "Return the current temperature diagnosis."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "getTemperatureDiagnosis", [])

def setEnableNotifications(enable:bool) -> None:
	"""
	Enables / Disables temperature notifications.
	
	Parameters
	----------
	enable:bool
		If True enable temperature notifications. If False disable temperature notifications.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "setEnableNotifications",
	    "parametersSignature": "(b)",
	    "description": "Enables / Disables temperature notifications.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "If True enable temperature notifications. If False disable temperature notifications."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "setEnableNotifications", [enable])

def areNotificationsEnabled() -> bool:
	"""
	Return true if notifications are active.
	
	Returns
	----------
	Return True if notifications are active.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "areNotificationsEnabled",
	    "parametersSignature": "()",
	    "description": "Return true if notifications are active.",
	    "parameters": [],
	    "returnDescription": "Return True if notifications are active."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "areNotificationsEnabled", [])

def _getDeviceTemperature(deviceName:str) -> int:
	"""
	Return the current temperature of deviceName.
	
	Parameters
	----------
	deviceName:str
		A joint, actuator or sensor name.
	
	Returns
	----------
	Return the current temperature in degree celsius.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "_getDeviceTemperature",
	    "parametersSignature": "(s)",
	    "description": "Return the current temperature of deviceName.",
	    "parameters": [
	        {
	            "name": "deviceName",
	            "description": "A joint, actuator or sensor name."
	        }
	    ],
	    "returnDescription": "Return the current temperature in degree celsius."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "_getDeviceTemperature", [deviceName])

def _getDeviceStatus(deviceName:str) -> int:
	"""
	Return the current temperature status of deviceName.
	
	Parameters
	----------
	deviceName:str
		A joint, actuator or sensor name.
	
	Returns
	----------
	Return the current temperature status.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "i",
	    "name": "_getDeviceStatus",
	    "parametersSignature": "(s)",
	    "description": "Return the current temperature status of deviceName.",
	    "parameters": [
	        {
	            "name": "deviceName",
	            "description": "A joint, actuator or sensor name."
	        }
	    ],
	    "returnDescription": "Return the current temperature status."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "_getDeviceStatus", [deviceName])

def _getTemperatureStatus() -> object:
	"""
	The actual state of the temperature status.
	
	Returns
	----------
	Return the current temperature status.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "_getTemperatureStatus",
	    "parametersSignature": "()",
	    "description": "The actual state of the temperature status.",
	    "parameters": [],
	    "returnDescription": "Return the current temperature status."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "_getTemperatureStatus", [])

def _setEnableDump(status:bool) -> None:
	"""
	Enabled or disables file dump at temperature error.
	
	Parameters
	----------
	status:bool
		Enables or disables dump.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "_setEnableDump",
	    "parametersSignature": "(b)",
	    "description": "Enabled or disables file dump at temperature error.",
	    "parameters": [
	        {
	            "name": "status",
	            "description": "Enables or disables dump."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "_setEnableDump", [status])

def _isDumpEnabled() -> bool:
	"""
	Return true if dump to file is active.
	
	Returns
	----------
	Return true if dump is enable.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "_isDumpEnabled",
	    "parametersSignature": "()",
	    "description": "Return true if dump to file is active.",
	    "parameters": [],
	    "returnDescription": "Return true if dump is enable."
	}
	'''
	"""
	return send_mfc("ALBodyTemperature", "_isDumpEnabled", [])

