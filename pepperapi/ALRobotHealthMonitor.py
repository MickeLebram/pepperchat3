from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALRobotHealthMonitor provides a simple API to robot health monitoring.


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
	return send_mfc("ALRobotHealthMonitor", "version", [])

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
	return send_mfc("ALRobotHealthMonitor", "ping", [])

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
	return send_mfc("ALRobotHealthMonitor", "getMethodList", [])

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
	return send_mfc("ALRobotHealthMonitor", "getMethodHelp", [methodName])

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
	return send_mfc("ALRobotHealthMonitor", "getModuleHelp", [])

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
	return send_mfc("ALRobotHealthMonitor", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALRobotHealthMonitor", "wait", [id])

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
	return send_mfc("ALRobotHealthMonitor", "isRunning", [id])

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
	return send_mfc("ALRobotHealthMonitor", "stop", [id])

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
	return send_mfc("ALRobotHealthMonitor", "getBrokerName", [])

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
	return send_mfc("ALRobotHealthMonitor", "getUsage", [name])

def _start() -> None:
	"""
	*Parsing issues:*
		*Mismatch between 'parameters' and 'parametersSignature'*
		
	start this module.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "_start",
	    "parametersSignature": "()",
	    "description": "start this module.",
	    "parameters": [
	        {
	            "name": "conffile",
	            "description": "Path to the configuration file."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_start", [])

def _stop() -> None:
	"""
	stop this module.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "_stop",
	    "parametersSignature": "()",
	    "description": "stop this module.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_stop", [])

def _mainThread() -> None:
	"""
	simple loop calling buffer update every "period" milliseconds
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_mainThread",
	    "parametersSignature": "()",
	    "description": "simple loop calling buffer update every \"period\" milliseconds",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_mainThread", [])

def _enableNetwork(p0:bool) -> None:
	"""
	enable storage of collected data on remote servers.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_enableNetwork",
	    "parametersSignature": "(b)",
	    "description": "enable storage of collected data on remote servers.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_enableNetwork", [p0])

def _setNetworkVerboseLevel(p0:int) -> None:
	"""
	used for debugging. Set verbose level.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_setNetworkVerboseLevel",
	    "parametersSignature": "(i)",
	    "description": "used for debugging. Set verbose level.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_setNetworkVerboseLevel", [p0])

def _setTimeInMinutePassiveDiagLoop(timeInMinutePassiveDiagLoop:int) -> None:
	"""
	Set passive diagnosis loop sleep duration in minute.
	
	Parameters
	----------
	timeInMinutePassiveDiagLoop:int
		Duration in minute.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "_setTimeInMinutePassiveDiagLoop",
	    "parametersSignature": "(i)",
	    "description": "Set passive diagnosis loop sleep duration in minute.",
	    "parameters": [
	        {
	            "name": "timeInMinutePassiveDiagLoop",
	            "description": "Duration in minute."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_setTimeInMinutePassiveDiagLoop", [timeInMinutePassiveDiagLoop])

def _getTimeInMinutePassiveDiagLoop() -> int:
	"""
	Get passive diagnosis loop sleep duration in minute.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "_getTimeInMinutePassiveDiagLoop",
	    "parametersSignature": "()",
	    "description": "Get passive diagnosis loop sleep duration in minute.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_getTimeInMinutePassiveDiagLoop", [])

def _setReportingEnabled(enabled:bool) -> None:
	"""
	Set the authorization to send data to the cloud
	
	Parameters
	----------
	enabled:bool
		boolean value if authorized or not
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_setReportingEnabled",
	    "parametersSignature": "(b)",
	    "description": "Set the authorization to send data to the cloud",
	    "parameters": [
	        {
	            "name": "enabled",
	            "description": "boolean value if authorized or not"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_setReportingEnabled", [enabled])

def _getReportingEnabled() -> bool:
	"""
	Get the authorization to send data to the cloud
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "_getReportingEnabled",
	    "parametersSignature": "()",
	    "description": "Get the authorization to send data to the cloud",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_getReportingEnabled", [])

def _onConnectivityChanged(string1:str, string2:object, string3:str) -> None:
	"""
	Internal callback
	
	Parameters
	----------
	string1:str
		variable
	string2:object
		value
	string3:str
		message
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_onConnectivityChanged",
	    "parametersSignature": "(sms)",
	    "description": "Internal callback",
	    "parameters": [
	        {
	            "name": "string",
	            "description": "variable"
	        },
	        {
	            "name": "string",
	            "description": "value"
	        },
	        {
	            "name": "string",
	            "description": "message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onConnectivityChanged", [string1, string2, string3])

def _onEventNotify(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when an event we have subscribed to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_onEventNotify",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when an event we have subscribed to has changed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onEventNotify", [dataName, dataValue, message])

def _onKeyAdded(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when an event we have subscribed to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_onKeyAdded",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when an event we have subscribed to has changed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onKeyAdded", [dataName, dataValue, message])

def _onKeyRemoved(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "_onKeyRemoved",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when a key is removed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onKeyRemoved", [dataName, dataValue, message])

def _onKeyTypeChanged(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when an event we have subscribe to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_onKeyTypeChanged",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when an event we have subscribe to has changed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onKeyTypeChanged", [dataName, dataValue, message])

def _onNetworkServiceAdded(eventName:str, serviceId:object, subscriberIdentifier:str) -> None:
	"""
	Called when a service is added to the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceAdded
	serviceId:object
		The service identifier of the added service.
	subscriberIdentifier:str
		-
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "_onNetworkServiceAdded",
	    "parametersSignature": "(sms)",
	    "description": "Called when a service is added to the service list.",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "NetworkServiceAdded"
	        },
	        {
	            "name": "serviceId",
	            "description": "The service identifier of the added service."
	        },
	        {
	            "name": "subscriberIdentifier",
	            "description": "-"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onNetworkServiceAdded", [eventName, serviceId, subscriberIdentifier])

def _onNetworkServiceRemoved(eventName:str, serviceId:object, subscriberIdentifier:str) -> None:
	"""
	Called when a service is removed from the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceRemoved
	serviceId:object
		The service identifier of the removed service.
	subscriberIdentifier:str
		-
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_onNetworkServiceRemoved",
	    "parametersSignature": "(sms)",
	    "description": "Called when a service is removed from the service list.",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "NetworkServiceRemoved"
	        },
	        {
	            "name": "serviceId",
	            "description": "The service identifier of the removed service."
	        },
	        {
	            "name": "subscriberIdentifier",
	            "description": "-"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onNetworkServiceRemoved", [eventName, serviceId, subscriberIdentifier])

def _onNetworkServiceStateChanged(eventName:str, serviceState:object, subscriberIdentifier:str) -> None:
	"""
	Called when a service is removed from the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceStateChanged
	serviceState:object
		A pair which contains the serviceId and the state of the service.
	subscriberIdentifier:str
		-
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "_onNetworkServiceStateChanged",
	    "parametersSignature": "(sms)",
	    "description": "Called when a service is removed from the service list.",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "NetworkServiceStateChanged"
	        },
	        {
	            "name": "serviceState",
	            "description": "A pair which contains the serviceId and the state of the service."
	        },
	        {
	            "name": "subscriberIdentifier",
	            "description": "-"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_onNetworkServiceStateChanged", [eventName, serviceState, subscriberIdentifier])

def _uploadActiveDiagnosis() -> None:
	"""
	Called when an active diagnosis error is triggered
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "_uploadActiveDiagnosis",
	    "parametersSignature": "()",
	    "description": "Called when an active diagnosis error is triggered",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_uploadActiveDiagnosis", [])

def _sendKPIAtStartup() -> None:
	"""
	Called when an active diagnosis error is triggered
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_sendKPIAtStartup",
	    "parametersSignature": "()",
	    "description": "Called when an active diagnosis error is triggered",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotHealthMonitor", "_sendKPIAtStartup", [])

