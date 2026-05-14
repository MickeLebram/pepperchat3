from .gentypes import *
from .robot_client import send_mfc
import json
"""
Notification manager: Handle all notifications on the robot.
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
	return send_mfc("ALNotificationManager", "version", [])

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
	return send_mfc("ALNotificationManager", "ping", [])

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
	return send_mfc("ALNotificationManager", "getMethodList", [])

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
	return send_mfc("ALNotificationManager", "getMethodHelp", [methodName])

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
	return send_mfc("ALNotificationManager", "getModuleHelp", [])

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
	return send_mfc("ALNotificationManager", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALNotificationManager", "wait", [id])

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
	return send_mfc("ALNotificationManager", "isRunning", [id])

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
	return send_mfc("ALNotificationManager", "stop", [id])

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
	return send_mfc("ALNotificationManager", "getBrokerName", [])

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
	return send_mfc("ALNotificationManager", "getUsage", [name])

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
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "i",
	    "name": "add",
	    "parametersSignature": "(m)",
	    "description": "Add a notification.",
	    "parameters": [
	        {
	            "name": "notification",
	            "description": "Contain information for the notification"
	        }
	    ],
	    "returnDescription": "Notification ID."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "add", [notification])

def remove(notificationId:int) -> None:
	"""
	Remove a notification.
	
	Parameters
	----------
	notificationId:int
		Notification ID to remove.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "remove",
	    "parametersSignature": "(i)",
	    "description": "Remove a notification.",
	    "parameters": [
	        {
	            "name": "notificationId",
	            "description": "Notification ID to remove."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "remove", [notificationId])

def notifications() -> object:
	"""
	Get the all array of pending notifications.
	
	Returns
	----------
	An array of pending notification.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "notifications",
	    "parametersSignature": "()",
	    "description": "Get the all array of pending notifications.",
	    "parameters": [],
	    "returnDescription": "An array of pending notification."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "notifications", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "m",
	    "name": "notification",
	    "parametersSignature": "(i)",
	    "description": "Get one notification.",
	    "parameters": [
	        {
	            "name": "notificationId",
	            "description": "Notification ID."
	        }
	    ],
	    "returnDescription": "ALValue containing a Notification."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "notification", [notificationId])

def _internalNotifications() -> object:
	"""
	
	
	Returns
	----------
	An array of pending notification.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "_internalNotifications",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": "An array of pending notification."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "_internalNotifications", [])

def _internalNotification(notificationId:int) -> object:
	"""
	
	
	Parameters
	----------
	notificationId:int
		Notification ID.
	
	Returns
	----------
	ALValue containing a Notification.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "_internalNotification",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "notificationId",
	            "description": "Notification ID."
	        }
	    ],
	    "returnDescription": "ALValue containing a Notification."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "_internalNotification", [notificationId])

def _severity() -> int:
	"""
	
	
	Returns
	----------
	Maximal Notification severity.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "_severity",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": "Maximal Notification severity."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "_severity", [])

def _read(int:int) -> None:
	"""
	
	
	Parameters
	----------
	int:int
		Notification ID.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_read",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "int",
	            "description": "Notification ID."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "_read", [int])

def _isImmediate(notificationId:int) -> bool:
	"""
	
	
	Parameters
	----------
	notificationId:int
		Notification ID.
	
	Returns
	----------
	True if the notification is immediate, false otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "_isImmediate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "notificationId",
	            "description": "Notification ID."
	        }
	    ],
	    "returnDescription": "True if the notification is immediate, false otherwise."
	}
	'''
	"""
	return send_mfc("ALNotificationManager", "_isImmediate", [notificationId])

