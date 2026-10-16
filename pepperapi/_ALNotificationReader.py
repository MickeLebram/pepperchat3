"""
Notification reader: Read the notifications pending on the robot.
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
	return call_method("_ALNotificationReader", "version", [])

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
	return call_method("_ALNotificationReader", "ping", [])

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
	return call_method("_ALNotificationReader", "getMethodList", [])

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
	return call_method("_ALNotificationReader", "getMethodHelp", [methodName])

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
	return call_method("_ALNotificationReader", "getModuleHelp", [])

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
	return call_method("_ALNotificationReader", "getBrokerName", [])

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
	return call_method("_ALNotificationReader", "getUsage", [name])

def _read(notificationId:int) -> None:
	"""
	Read a pending notification.
	
	Parameters
	----------
	notificationId:int
		ID of the notification to read.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_read",
	#     "parametersSignature": "(i)",
	#     "description": "Read a pending notification.",
	#     "parameters": [
	#         {
	#             "name": "notificationId",
	#             "description": "ID of the notification to read."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALNotificationReader", "_read", [notificationId])

def _readAll() -> None:
	"""
	Read all pending notifications.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "_readAll",
	#     "parametersSignature": "()",
	#     "description": "Read all pending notifications.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNotificationReader", "_readAll", [])

def _readAllSos() -> None:
	"""
	Read all pending notifications with SOS IP presentation if needed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_readAllSos",
	#     "parametersSignature": "()",
	#     "description": "Read all pending notifications with SOS IP presentation if needed.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNotificationReader", "_readAllSos", [])

def _skip() -> bool:
	"""
	Skip the reading of the current notification.
	
	Returns
	----------
	True if there was reading running (and so reading to skip), false otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "_skip",
	#     "parametersSignature": "()",
	#     "description": "Skip the reading of the current notification.",
	#     "parameters": [],
	#     "returnDescription": "True if there was reading running (and so reading to skip), false otherwise."
	# }
	return call_method("_ALNotificationReader", "_skip", [])

def _stopReading() -> None:
	"""
	Stop the reading of the notifications.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_stopReading",
	#     "parametersSignature": "()",
	#     "description": "Stop the reading of the notifications.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNotificationReader", "_stopReading", [])

def _onPreferenceChanged(p0:str, p1:object, p2:object) -> None:
	"""
	Update the value of preferences.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceChanged",
	#     "parametersSignature": "(smm)",
	#     "description": "Update the value of preferences.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNotificationReader", "_onPreferenceChanged", [p0, p1, p2])

