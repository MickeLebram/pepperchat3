"""
Notification manager: Handle all notifications on the robot.
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
	return call_method("ALNotificationManager", "version", [])

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
	return call_method("ALNotificationManager", "ping", [])

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
	return call_method("ALNotificationManager", "getMethodList", [])

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
	return call_method("ALNotificationManager", "getMethodHelp", [methodName])

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
	return call_method("ALNotificationManager", "getModuleHelp", [])

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
	return call_method("ALNotificationManager", "getBrokerName", [])

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
	return call_method("ALNotificationManager", "getUsage", [name])

def add(notification:object) -> int:
	"""
	Add a notification.
	
	Parameters
	----------
	notification:object
		Contain information for the notification
	
	Returns
	----------
	Notification ID.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "i",
	#     "name": "add",
	#     "parametersSignature": "(m)",
	#     "description": "Add a notification.",
	#     "parameters": [
	#         {
	#             "name": "notification",
	#             "description": "Contain information for the notification"
	#         }
	#     ],
	#     "returnDescription": "Notification ID."
	# }
	return call_method("ALNotificationManager", "add", [notification])

def remove(notificationId:int) -> None:
	"""
	Remove a notification.
	
	Parameters
	----------
	notificationId:int
		Notification ID to remove.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "remove",
	#     "parametersSignature": "(i)",
	#     "description": "Remove a notification.",
	#     "parameters": [
	#         {
	#             "name": "notificationId",
	#             "description": "Notification ID to remove."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNotificationManager", "remove", [notificationId])

def notifications() -> object:
	"""
	Get the all array of pending notifications.
	
	Returns
	----------
	An array of pending notification.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "notifications",
	#     "parametersSignature": "()",
	#     "description": "Get the all array of pending notifications.",
	#     "parameters": [],
	#     "returnDescription": "An array of pending notification."
	# }
	return call_method("ALNotificationManager", "notifications", [])

def notification(notificationId:int) -> object:
	"""
	Get one notification.
	
	Parameters
	----------
	notificationId:int
		Notification ID.
	
	Returns
	----------
	ALValue containing a Notification.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "notification",
	#     "parametersSignature": "(i)",
	#     "description": "Get one notification.",
	#     "parameters": [
	#         {
	#             "name": "notificationId",
	#             "description": "Notification ID."
	#         }
	#     ],
	#     "returnDescription": "ALValue containing a Notification."
	# }
	return call_method("ALNotificationManager", "notification", [notificationId])

def _internalNotifications() -> object:
	"""
	
	
	Returns
	----------
	An array of pending notification.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "_internalNotifications",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": "An array of pending notification."
	# }
	return call_method("ALNotificationManager", "_internalNotifications", [])

def _internalNotification(notificationId:int) -> object:
	"""
	
	
	Parameters
	----------
	notificationId:int
		Notification ID.
	
	Returns
	----------
	ALValue containing a Notification.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "_internalNotification",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "notificationId",
	#             "description": "Notification ID."
	#         }
	#     ],
	#     "returnDescription": "ALValue containing a Notification."
	# }
	return call_method("ALNotificationManager", "_internalNotification", [notificationId])

def _severity() -> int:
	"""
	
	
	Returns
	----------
	Maximal Notification severity.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "_severity",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": "Maximal Notification severity."
	# }
	return call_method("ALNotificationManager", "_severity", [])

def _read(int:int) -> None:
	"""
	
	
	Parameters
	----------
	int:int
		Notification ID.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_read",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "int",
	#             "description": "Notification ID."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNotificationManager", "_read", [int])

def _isImmediate(notificationId:int) -> bool:
	"""
	
	
	Parameters
	----------
	notificationId:int
		Notification ID.
	
	Returns
	----------
	True if the notification is immediate, false otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "_isImmediate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "notificationId",
	#             "description": "Notification ID."
	#         }
	#     ],
	#     "returnDescription": "True if the notification is immediate, false otherwise."
	# }
	return call_method("ALNotificationManager", "_isImmediate", [notificationId])

