from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def registerEvent(p0:int, p1:int, p2:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 0,
	    "returnSignature": "L",
	    "name": "registerEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "registerEvent", [p0, p1, p2])

def unregisterEvent(p0:int, p1:int, p2:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 1,
	    "returnSignature": "v",
	    "name": "unregisterEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "unregisterEvent", [p0, p1, p2])

def metaObject(p0:int) -> MetaObject:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 2,
	    "returnSignature": "({I(Issss[(ss)<MetaMethodParameter,name,description>]s)<MetaMethod,uid,returnSignature,name,parametersSignature,description,parameters,returnDescription>}{I(Iss)<MetaSignal,uid,name,signature>}{I(Iss)<MetaProperty,uid,name,signature>}s)<MetaObject,methods,signals,properties,description>",
	    "name": "metaObject",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "metaObject", [p0])

def terminate(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 3,
	    "returnSignature": "v",
	    "name": "terminate",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "terminate", [p0])

def property(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 5,
	    "returnSignature": "m",
	    "name": "property",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "property", [p0])

def setProperty(p0:object, p1:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 6,
	    "returnSignature": "v",
	    "name": "setProperty",
	    "parametersSignature": "(mm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "setProperty", [p0, p1])

def properties() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 7,
	    "returnSignature": "[s]",
	    "name": "properties",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "properties", [])

def registerEventWithSignature(p0:int, p1:int, p2:int, p3:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 8,
	    "returnSignature": "L",
	    "name": "registerEventWithSignature",
	    "parametersSignature": "(IILs)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "registerEventWithSignature", [p0, p1, p2, p3])

def isStatsEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 80,
	    "returnSignature": "b",
	    "name": "isStatsEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "isStatsEnabled", [])

def enableStats(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 81,
	    "returnSignature": "v",
	    "name": "enableStats",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "enableStats", [p0])

def stats() -> Dict[int,MethodStatistics]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 82,
	    "returnSignature": "{I(I(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>)<MethodStatistics,count,wall,user,system>}",
	    "name": "stats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "stats", [])

def clearStats() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 83,
	    "returnSignature": "v",
	    "name": "clearStats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "clearStats", [])

def isTraceEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 84,
	    "returnSignature": "b",
	    "name": "isTraceEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "isTraceEnabled", [])

def enableTrace(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 85,
	    "returnSignature": "v",
	    "name": "enableTrace",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "enableTrace", [p0])

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
	return send_mfc("ALSystem", "version", [])

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
	return send_mfc("ALSystem", "ping", [])

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
	return send_mfc("ALSystem", "getMethodList", [])

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
	return send_mfc("ALSystem", "getMethodHelp", [methodName])

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
	return send_mfc("ALSystem", "getModuleHelp", [])

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
	return send_mfc("ALSystem", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALSystem", "wait", [id])

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
	return send_mfc("ALSystem", "isRunning", [id])

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
	return send_mfc("ALSystem", "stop", [id])

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
	return send_mfc("ALSystem", "getBrokerName", [])

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
	return send_mfc("ALSystem", "getUsage", [name])

def appBackupInfo() -> List[AppBackupInfo]:
	"""
	Get the backup information of applications
	
	Returns
	----------
	A vector with all application backup infos
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "[(sss[s][s])<AppBackupInfo,applicationName,userDataPath,userConfPath,dataBackupPaths,confBackupPaths>]",
	    "name": "appBackupInfo",
	    "parametersSignature": "()",
	    "description": "Get the backup information of applications",
	    "parameters": [],
	    "returnDescription": "A vector with all application backup infos"
	}
	'''
	"""
	return send_mfc("ALSystem", "appBackupInfo", [])

def diskFree(all:bool) -> List[PartitionInfo]:
	"""
	Display free disk space
	
	Parameters
	----------
	all:bool
		Show all mount partions.
	
	Returns
	----------
	A vector with all partions' infos
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "[(ssLL)<PartitionInfo,filesystem,path,size,free>]",
	    "name": "diskFree",
	    "parametersSignature": "(b)",
	    "description": "Display free disk space",
	    "parameters": [
	        {
	            "name": "all",
	            "description": "Show all mount partions."
	        }
	    ],
	    "returnDescription": "A vector with all partions' infos"
	}
	'''
	"""
	return send_mfc("ALSystem", "diskFree", [all])

def robotName() -> str:
	"""
	System hostname
	
	Returns
	----------
	name of the robot
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "s",
	    "name": "robotName",
	    "parametersSignature": "()",
	    "description": "System hostname",
	    "parameters": [],
	    "returnDescription": "name of the robot"
	}
	'''
	"""
	return send_mfc("ALSystem", "robotName", [])

def setRobotName(name:str) -> bool:
	"""
	Set system hostname
	
	Parameters
	----------
	name:str
		name to use
	
	Returns
	----------
	whether the operation was successful
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "setRobotName",
	    "parametersSignature": "(s)",
	    "description": "Set system hostname",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "name to use"
	        }
	    ],
	    "returnDescription": "whether the operation was successful"
	}
	'''
	"""
	return send_mfc("ALSystem", "setRobotName", [name])

def robotIcon_1(p0:int) -> object:
	"""
	Note: This is one of the overloads of the original method (robotIcon)
	
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "o",
	    "name": "robotIcon",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "robotIcon", [p0])

def robotIcon_2() -> object:
	"""
	Note: This is one of the overloads of the original method (robotIcon)
	
	
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "robotIcon",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "robotIcon", [])

def shutdown() -> None:
	"""
	Shutdown robot
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "shutdown",
	    "parametersSignature": "()",
	    "description": "Shutdown robot",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "shutdown", [])

def reboot() -> None:
	"""
	Reboot robot
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "reboot",
	    "parametersSignature": "()",
	    "description": "Reboot robot",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "reboot", [])

def systemVersion() -> str:
	"""
	Running system version
	
	Returns
	----------
	running system version
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "s",
	    "name": "systemVersion",
	    "parametersSignature": "()",
	    "description": "Running system version",
	    "parameters": [],
	    "returnDescription": "running system version"
	}
	'''
	"""
	return send_mfc("ALSystem", "systemVersion", [])

def systemInfo() -> SystemInfo:
	"""
	Running system version
	
	Returns
	----------
	information about the system version
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "(ssss)<SystemInfo,systemVersion,buildDate,buildID,buildTag>",
	    "name": "systemInfo",
	    "parametersSignature": "()",
	    "description": "Running system version",
	    "parameters": [],
	    "returnDescription": "information about the system version"
	}
	'''
	"""
	return send_mfc("ALSystem", "systemInfo", [])

def freeMemory() -> int:
	"""
	Amount of available memory in heap
	
	Returns
	----------
	amount of available memory in heap
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "i",
	    "name": "freeMemory",
	    "parametersSignature": "()",
	    "description": "Amount of available memory in heap",
	    "parameters": [],
	    "returnDescription": "amount of available memory in heap"
	}
	'''
	"""
	return send_mfc("ALSystem", "freeMemory", [])

def totalMemory() -> int:
	"""
	Amount of total memory in heap
	
	Returns
	----------
	amount of total memory in heap
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "i",
	    "name": "totalMemory",
	    "parametersSignature": "()",
	    "description": "Amount of total memory in heap",
	    "parameters": [],
	    "returnDescription": "amount of total memory in heap"
	}
	'''
	"""
	return send_mfc("ALSystem", "totalMemory", [])

def timezone() -> str:
	"""
	Current timezone
	
	Returns
	----------
	current timezone
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "s",
	    "name": "timezone",
	    "parametersSignature": "()",
	    "description": "Current timezone",
	    "parameters": [],
	    "returnDescription": "current timezone"
	}
	'''
	"""
	return send_mfc("ALSystem", "timezone", [])

def setTimezone(timezone:str) -> bool:
	"""
	Set current timezone
	
	Parameters
	----------
	timezone:str
		timezone to use
	
	Returns
	----------
	whether the operation was successful
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "setTimezone",
	    "parametersSignature": "(s)",
	    "description": "Set current timezone",
	    "parameters": [
	        {
	            "name": "timezone",
	            "description": "timezone to use"
	        }
	    ],
	    "returnDescription": "whether the operation was successful"
	}
	'''
	"""
	return send_mfc("ALSystem", "setTimezone", [timezone])

def setRobotIcon(imageFile:object) -> int:
	"""
	Set current robot icon
	
	Parameters
	----------
	imageFile:object
		Image file to use as a robot icon
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "i",
	    "name": "setRobotIcon",
	    "parametersSignature": "(o)",
	    "description": "Set current robot icon",
	    "parameters": [
	        {
	            "name": "imageFile",
	            "description": "Image file to use as a robot icon"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "setRobotIcon", [imageFile])

def previousSystemVersion() -> str:
	"""
	Previous system version before software update (empty if this is not the 1st boot after a software update)
	
	Returns
	----------
	Previous system version before software update.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "s",
	    "name": "previousSystemVersion",
	    "parametersSignature": "()",
	    "description": "Previous system version before software update (empty if this is not the 1st boot after a software update)",
	    "parameters": [],
	    "returnDescription": "Previous system version before software update."
	}
	'''
	"""
	return send_mfc("ALSystem", "previousSystemVersion", [])

def changePassword(old_password:str, new_password:str) -> None:
	"""
	Change the user password.
	
	Parameters
	----------
	old_password:str
		The current password of the user.
	new_password:str
		The new user password.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "changePassword",
	    "parametersSignature": "(ss)",
	    "description": "Change the user password.",
	    "parameters": [
	        {
	            "name": "old password",
	            "description": "The current password of the user."
	        },
	        {
	            "name": "new password",
	            "description": "The new user password."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "changePassword", [old_password, new_password])

def upgrade(image:str, checksum:str) -> None:
	"""
	Flash the system image.
	
	Parameters
	----------
	image:str
		Local path to a valid image.
	checksum:str
		Local path to a md5 checksum file, or empty string for no verification
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "upgrade",
	    "parametersSignature": "(ss)",
	    "description": "Flash the system image.",
	    "parameters": [
	        {
	            "name": "image",
	            "description": "Local path to a valid image."
	        },
	        {
	            "name": "checksum",
	            "description": "Local path to a md5 checksum file, or empty string for no verification"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "upgrade", [image, checksum])

def factoryReset(image:str, checksum:str) -> None:
	"""
	Flash the system image and erase the user data
	
	Parameters
	----------
	image:str
		Local path to a valid image.
	checksum:str
		Local path to a md5 checksum file, or empty string for no verification
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "factoryReset",
	    "parametersSignature": "(ss)",
	    "description": "Flash the system image and erase the user data",
	    "parameters": [
	        {
	            "name": "image",
	            "description": "Local path to a valid image."
	        },
	        {
	            "name": "checksum",
	            "description": "Local path to a md5 checksum file, or empty string for no verification"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "factoryReset", [image, checksum])

def _setStatusLed(state:int) -> None:
	"""
	Set the robot status LED
	
	Parameters
	----------
	state:int
		state to set
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "_setStatusLed",
	    "parametersSignature": "(i)",
	    "description": "Set the robot status LED",
	    "parameters": [
	        {
	            "name": "state",
	            "description": "state to set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "_setStatusLed", [state])

def _initializeSystemNotification() -> None:
	"""
	Load system notification and data
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "_initializeSystemNotification",
	    "parametersSignature": "()",
	    "description": "Load system notification and data",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "_initializeSystemNotification", [])

def _boardFirmwareUpdateError() -> List[str]:
	"""
	List of the faulty boards
	
	Returns
	----------
	A vector with the name of the faulty boards
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "[s]",
	    "name": "_boardFirmwareUpdateError",
	    "parametersSignature": "()",
	    "description": "List of the faulty boards",
	    "parameters": [],
	    "returnDescription": "A vector with the name of the faulty boards"
	}
	'''
	"""
	return send_mfc("ALSystem", "_boardFirmwareUpdateError", [])

def _prepareNaoqiStop() -> None:
	"""
	Execute operations for safe naoqi stop
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_prepareNaoqiStop",
	    "parametersSignature": "()",
	    "description": "Execute operations for safe naoqi stop",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSystem", "_prepareNaoqiStop", [])

