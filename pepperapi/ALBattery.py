from .gentypes import *
from .robot_client import send_mfc
import json
"""
Deals with Battery informations.
A event name BatteryChargeCellVoltageMinChanged is raised when the cell voltage Min (int) of the battery changed.
A event name BatteryChargingFlagChanged is raised when the flag battery is charging (bool) changed.
A event name BatteryFullChargedFlagChanged is raised when the flag battery is full charged (bool) changed.
A event name BatteryDisChargingFlagChanged is raised when the flag battery is disCharging (bool) changed.
A event name BatteryChargeChanged is raised when the battery level percentage (int) changed.

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
	return send_mfc("ALBattery", "version", [])

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
	return send_mfc("ALBattery", "ping", [])

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
	return send_mfc("ALBattery", "getMethodList", [])

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
	return send_mfc("ALBattery", "getMethodHelp", [methodName])

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
	return send_mfc("ALBattery", "getModuleHelp", [])

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
	return send_mfc("ALBattery", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALBattery", "wait", [id])

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
	return send_mfc("ALBattery", "isRunning", [id])

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
	return send_mfc("ALBattery", "stop", [id])

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
	return send_mfc("ALBattery", "getBrokerName", [])

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
	return send_mfc("ALBattery", "getUsage", [name])

def enablePowerMonitoring(Enable:bool) -> None:
	"""
	Enable power monitoring
	
	Parameters
	----------
	Enable:bool
		True activate power monitoring
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "enablePowerMonitoring",
	    "parametersSignature": "(b)",
	    "description": "Enable power monitoring",
	    "parameters": [
	        {
	            "name": "Enable",
	            "description": "True activate power monitoring"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "enablePowerMonitoring", [Enable])

def getBatteryCharge() -> int:
	"""
	Get the battery charge in percents
	
	Returns
	----------
	the percentage of remaining power
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "i",
	    "name": "getBatteryCharge",
	    "parametersSignature": "()",
	    "description": "Get the battery charge in percents",
	    "parameters": [],
	    "returnDescription": "the percentage of remaining power"
	}
	'''
	"""
	return send_mfc("ALBattery", "getBatteryCharge", [])

def _setFirstWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the first warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_setFirstWarningPercent",
	    "parametersSignature": "(i)",
	    "description": "Internal set the battery level for the first warning.",
	    "parameters": [
	        {
	            "name": "Percent",
	            "description": "Percentage of battery."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "_setFirstWarningPercent", [Percent])

def _setWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the second warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_setWarningPercent",
	    "parametersSignature": "(i)",
	    "description": "Internal set the battery level for the second warning.",
	    "parameters": [
	        {
	            "name": "Percent",
	            "description": "Percentage of battery."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "_setWarningPercent", [Percent])

def _setLastWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the last warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_setLastWarningPercent",
	    "parametersSignature": "(i)",
	    "description": "Internal set the battery level for the last warning.",
	    "parameters": [
	        {
	            "name": "Percent",
	            "description": "Percentage of battery."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "_setLastWarningPercent", [Percent])

def _hasBattery() -> bool:
	"""
	Is battery detected.
	
	Returns
	----------
	Return true if battery is detected.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "_hasBattery",
	    "parametersSignature": "()",
	    "description": "Is battery detected.",
	    "parameters": [],
	    "returnDescription": "Return true if battery is detected."
	}
	'''
	"""
	return send_mfc("ALBattery", "_hasBattery", [])

def _getBatteryMode() -> int:
	"""
	Get current battery mode.
	
	Returns
	----------
	Return the current battery mode. (Local = 0, robot = 1, simulation = 2)
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "_getBatteryMode",
	    "parametersSignature": "()",
	    "description": "Get current battery mode.",
	    "parameters": [],
	    "returnDescription": "Return the current battery mode. (Local = 0, robot = 1, simulation = 2)"
	}
	'''
	"""
	return send_mfc("ALBattery", "_getBatteryMode", [])

def _getFullyChargedThreshold() -> int:
	"""
	Get current battery fully charged threshold.
	
	Returns
	----------
	the percentage of threshold for fully charged event.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "_getFullyChargedThreshold",
	    "parametersSignature": "()",
	    "description": "Get current battery fully charged threshold.",
	    "parameters": [],
	    "returnDescription": "the percentage of threshold for fully charged event."
	}
	'''
	"""
	return send_mfc("ALBattery", "_getFullyChargedThreshold", [])

def _setFullyChargedThreshold(threshold:int) -> None:
	"""
	Set battery fully charged threshold.
	
	Parameters
	----------
	threshold:int
		the percentage of threshold for fully charged event.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "_setFullyChargedThreshold",
	    "parametersSignature": "(i)",
	    "description": "Set battery fully charged threshold.",
	    "parameters": [
	        {
	            "name": "threshold",
	            "description": "the percentage of threshold for fully charged event."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "_setFullyChargedThreshold", [threshold])

def _setModeSlave(status:bool) -> None:
	"""
	Set mode slave status.
	
	Parameters
	----------
	status:bool
		Enables or disables mode slave.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_setModeSlave",
	    "parametersSignature": "(b)",
	    "description": "Set mode slave status.",
	    "parameters": [
	        {
	            "name": "status",
	            "description": "Enables or disables mode slave."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBattery", "_setModeSlave", [status])

