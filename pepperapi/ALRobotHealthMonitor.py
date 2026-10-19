"""
ALRobotHealthMonitor provides a simple API to robot health monitoring.


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
	return call_method("ALRobotHealthMonitor", "version", [])

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
	return call_method("ALRobotHealthMonitor", "ping", [])

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
	return call_method("ALRobotHealthMonitor", "getMethodList", [])

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
	return call_method("ALRobotHealthMonitor", "getMethodHelp", [methodName])

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
	return call_method("ALRobotHealthMonitor", "getModuleHelp", [])

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
	return call_method("ALRobotHealthMonitor", "getBrokerName", [])

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
	return call_method("ALRobotHealthMonitor", "getUsage", [name])

def _start() -> None:
	"""
	start this module.
	
	Bridge notes
	------------
	NAOqi's documentation lists a parameter (conffile) that the method's signature doesn't have. This function follows the signature and takes no arguments.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_start",
	#     "parametersSignature": "()",
	#     "description": "start this module.",
	#     "parameters": [
	#         {
	#             "name": "conffile",
	#             "description": "Path to the configuration file."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_start", [])

def _stop() -> None:
	"""
	stop this module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "_stop",
	#     "parametersSignature": "()",
	#     "description": "stop this module.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_stop", [])

def _mainThread() -> None:
	"""
	simple loop calling buffer update every "period" milliseconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_mainThread",
	#     "parametersSignature": "()",
	#     "description": "simple loop calling buffer update every \"period\" milliseconds",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_mainThread", [])

def _enableNetwork(p0:bool) -> None:
	"""
	enable storage of collected data on remote servers.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_enableNetwork",
	#     "parametersSignature": "(b)",
	#     "description": "enable storage of collected data on remote servers.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_enableNetwork", [p0])

def _setNetworkVerboseLevel(p0:int) -> None:
	"""
	used for debugging. Set verbose level.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_setNetworkVerboseLevel",
	#     "parametersSignature": "(i)",
	#     "description": "used for debugging. Set verbose level.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_setNetworkVerboseLevel", [p0])

def _setTimeInMinutePassiveDiagLoop(timeInMinutePassiveDiagLoop:int) -> None:
	"""
	Set passive diagnosis loop sleep duration in minute.
	
	Parameters
	----------
	timeInMinutePassiveDiagLoop:int
		Duration in minute.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_setTimeInMinutePassiveDiagLoop",
	#     "parametersSignature": "(i)",
	#     "description": "Set passive diagnosis loop sleep duration in minute.",
	#     "parameters": [
	#         {
	#             "name": "timeInMinutePassiveDiagLoop",
	#             "description": "Duration in minute."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_setTimeInMinutePassiveDiagLoop", [timeInMinutePassiveDiagLoop])

def _getTimeInMinutePassiveDiagLoop() -> int:
	"""
	Get passive diagnosis loop sleep duration in minute.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "_getTimeInMinutePassiveDiagLoop",
	#     "parametersSignature": "()",
	#     "description": "Get passive diagnosis loop sleep duration in minute.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_getTimeInMinutePassiveDiagLoop", [])

def _setReportingEnabled(enabled:bool) -> None:
	"""
	Set the authorization to send data to the cloud
	
	Parameters
	----------
	enabled:bool
		boolean value if authorized or not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_setReportingEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Set the authorization to send data to the cloud",
	#     "parameters": [
	#         {
	#             "name": "enabled",
	#             "description": "boolean value if authorized or not"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_setReportingEnabled", [enabled])

def _getReportingEnabled() -> bool:
	"""
	Get the authorization to send data to the cloud
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "_getReportingEnabled",
	#     "parametersSignature": "()",
	#     "description": "Get the authorization to send data to the cloud",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_getReportingEnabled", [])

def _onConnectivityChanged(string1:str, string2:Any, string3:str) -> None:
	"""
	Internal callback
	
	Parameters
	----------
	string1:str
		variable
	string2:Any
		value
	string3:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_onConnectivityChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Internal callback",
	#     "parameters": [
	#         {
	#             "name": "string",
	#             "description": "variable"
	#         },
	#         {
	#             "name": "string",
	#             "description": "value"
	#         },
	#         {
	#             "name": "string",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onConnectivityChanged", [string1, string2, string3])

def _onEventNotify(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when an event we have subscribed to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_onEventNotify",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when an event we have subscribed to has changed in ALMemory",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "name of the data"
	#         },
	#         {
	#             "name": "dataValue",
	#             "description": "value of the data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "callback message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onEventNotify", [dataName, dataValue, message])

def _onKeyAdded(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when an event we have subscribed to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_onKeyAdded",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when an event we have subscribed to has changed in ALMemory",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "name of the data"
	#         },
	#         {
	#             "name": "dataValue",
	#             "description": "value of the data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "callback message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onKeyAdded", [dataName, dataValue, message])

def _onKeyRemoved(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_onKeyRemoved",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when a key is removed in ALMemory",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "name of the data"
	#         },
	#         {
	#             "name": "dataValue",
	#             "description": "value of the data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "callback message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onKeyRemoved", [dataName, dataValue, message])

def _onKeyTypeChanged(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when an event we have subscribe to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_onKeyTypeChanged",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when an event we have subscribe to has changed in ALMemory",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "name of the data"
	#         },
	#         {
	#             "name": "dataValue",
	#             "description": "value of the data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "callback message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onKeyTypeChanged", [dataName, dataValue, message])

def _onNetworkServiceAdded(eventName:str, serviceId:Any, subscriberIdentifier:str) -> None:
	"""
	Called when a service is added to the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceAdded
	serviceId:Any
		The service identifier of the added service.
	subscriberIdentifier:str
		-
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "_onNetworkServiceAdded",
	#     "parametersSignature": "(sms)",
	#     "description": "Called when a service is added to the service list.",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "NetworkServiceAdded"
	#         },
	#         {
	#             "name": "serviceId",
	#             "description": "The service identifier of the added service."
	#         },
	#         {
	#             "name": "subscriberIdentifier",
	#             "description": "-"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onNetworkServiceAdded", [eventName, serviceId, subscriberIdentifier])

def _onNetworkServiceRemoved(eventName:str, serviceId:Any, subscriberIdentifier:str) -> None:
	"""
	Called when a service is removed from the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceRemoved
	serviceId:Any
		The service identifier of the removed service.
	subscriberIdentifier:str
		-
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_onNetworkServiceRemoved",
	#     "parametersSignature": "(sms)",
	#     "description": "Called when a service is removed from the service list.",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "NetworkServiceRemoved"
	#         },
	#         {
	#             "name": "serviceId",
	#             "description": "The service identifier of the removed service."
	#         },
	#         {
	#             "name": "subscriberIdentifier",
	#             "description": "-"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onNetworkServiceRemoved", [eventName, serviceId, subscriberIdentifier])

def _onNetworkServiceStateChanged(eventName:str, serviceState:Any, subscriberIdentifier:str) -> None:
	"""
	Called when a service is removed from the service list.
	
	Parameters
	----------
	eventName:str
		NetworkServiceStateChanged
	serviceState:Any
		A pair which contains the serviceId and the state of the service.
	subscriberIdentifier:str
		-
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_onNetworkServiceStateChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Called when a service is removed from the service list.",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "NetworkServiceStateChanged"
	#         },
	#         {
	#             "name": "serviceState",
	#             "description": "A pair which contains the serviceId and the state of the service."
	#         },
	#         {
	#             "name": "subscriberIdentifier",
	#             "description": "-"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_onNetworkServiceStateChanged", [eventName, serviceState, subscriberIdentifier])

def _uploadActiveDiagnosis() -> None:
	"""
	Called when an active diagnosis error is triggered
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "_uploadActiveDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "Called when an active diagnosis error is triggered",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_uploadActiveDiagnosis", [])

def _sendKPIAtStartup() -> None:
	"""
	Called when an active diagnosis error is triggered
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_sendKPIAtStartup",
	#     "parametersSignature": "()",
	#     "description": "Called when an active diagnosis error is triggered",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRobotHealthMonitor", "_sendKPIAtStartup", [])

