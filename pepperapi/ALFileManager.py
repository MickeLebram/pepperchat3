from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALFileManager manages the user files stored in a shared folder.
Note that FileManager starts to look in the shared folder, and if it does not find anything,
then it looks in the data folder.
Shared folder can be changed on the fly, and module will then be able to say which
files are available in this folder, as well as return their complete path.
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
	return send_mfc("ALFileManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALFileManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALFileManager", "metaObject", [p0])

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
	return send_mfc("ALFileManager", "terminate", [p0])

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
	return send_mfc("ALFileManager", "property", [p0])

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
	return send_mfc("ALFileManager", "setProperty", [p0, p1])

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
	return send_mfc("ALFileManager", "properties", [])

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
	return send_mfc("ALFileManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALFileManager", "isStatsEnabled", [])

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
	return send_mfc("ALFileManager", "enableStats", [p0])

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
	return send_mfc("ALFileManager", "stats", [])

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
	return send_mfc("ALFileManager", "clearStats", [])

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
	return send_mfc("ALFileManager", "isTraceEnabled", [])

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
	return send_mfc("ALFileManager", "enableTrace", [p0])

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
	return send_mfc("ALFileManager", "version", [])

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
	return send_mfc("ALFileManager", "ping", [])

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
	return send_mfc("ALFileManager", "getMethodList", [])

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
	return send_mfc("ALFileManager", "getMethodHelp", [methodName])

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
	return send_mfc("ALFileManager", "getModuleHelp", [])

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
	return send_mfc("ALFileManager", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALFileManager", "wait", [id])

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
	return send_mfc("ALFileManager", "isRunning", [id])

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
	return send_mfc("ALFileManager", "stop", [id])

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
	return send_mfc("ALFileManager", "getBrokerName", [])

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
	return send_mfc("ALFileManager", "getUsage", [name])

def setUserSharedFolderPath(fileName:str) -> None:
	"""
	Set a new value of the user shared folder path.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "setUserSharedFolderPath",
	    "parametersSignature": "(s)",
	    "description": "Set a new value of the user shared folder path.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associate to the preference."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFileManager", "setUserSharedFolderPath", [fileName])

def getUserSharedFolderPath() -> str:
	"""
	Get the current user shared folder path.
	
	Returns
	----------
	User shared folder path string.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "s",
	    "name": "getUserSharedFolderPath",
	    "parametersSignature": "()",
	    "description": "Get the current user shared folder path.",
	    "parameters": [],
	    "returnDescription": "User shared folder path string."
	}
	'''
	"""
	return send_mfc("ALFileManager", "getUserSharedFolderPath", [])

def getSystemSharedFolderPath() -> str:
	"""
	Get the current system shared folder path.
	
	Returns
	----------
	System shared folder path string.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "s",
	    "name": "getSystemSharedFolderPath",
	    "parametersSignature": "()",
	    "description": "Get the current system shared folder path.",
	    "parameters": [],
	    "returnDescription": "System shared folder path string."
	}
	'''
	"""
	return send_mfc("ALFileManager", "getSystemSharedFolderPath", [])

def fileExists(fileName:str) -> bool:
	"""
	Try to find if this file does exist on robot or not.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	
	Returns
	----------
	True upon success
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "fileExists",
	    "parametersSignature": "(s)",
	    "description": "Try to find if this file does exist on robot or not.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associate to the preference."
	        }
	    ],
	    "returnDescription": "True upon success"
	}
	'''
	"""
	return send_mfc("ALFileManager", "fileExists", [fileName])

def dataFileExists(fileName:str) -> bool:
	"""
	Try to find if this file does exist on robot or not.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	
	Returns
	----------
	True upon success
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "dataFileExists",
	    "parametersSignature": "(s)",
	    "description": "Try to find if this file does exist on robot or not.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associate to the preference."
	        }
	    ],
	    "returnDescription": "True upon success"
	}
	'''
	"""
	return send_mfc("ALFileManager", "dataFileExists", [fileName])

def getFileCompletePath(prefs:str) -> str:
	"""
	Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.
	
	Parameters
	----------
	prefs:str
		array reprenting the whole file.
	
	Returns
	----------
	True upon success
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "s",
	    "name": "getFileCompletePath",
	    "parametersSignature": "(s)",
	    "description": "Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.",
	    "parameters": [
	        {
	            "name": "prefs",
	            "description": "array reprenting the whole file."
	        }
	    ],
	    "returnDescription": "True upon success"
	}
	'''
	"""
	return send_mfc("ALFileManager", "getFileCompletePath", [prefs])

def getFileContents(prefs:str) -> object:
	"""
	Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.
	
	Parameters
	----------
	prefs:str
		array reprenting the whole file.
	
	Returns
	----------
	True upon success
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "getFileContents",
	    "parametersSignature": "(s)",
	    "description": "Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.",
	    "parameters": [
	        {
	            "name": "prefs",
	            "description": "array reprenting the whole file."
	        }
	    ],
	    "returnDescription": "True upon success"
	}
	'''
	"""
	return send_mfc("ALFileManager", "getFileContents", [prefs])

def _getBehaviorsPath() -> str:
	"""
	Returns the path to the directory where behaviors are stored on the robot.
	
	Returns
	----------
	The behaviors path, as an UTF-8 encoded string.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "s",
	    "name": "_getBehaviorsPath",
	    "parametersSignature": "()",
	    "description": "Returns the path to the directory where behaviors are stored on the robot.",
	    "parameters": [],
	    "returnDescription": "The behaviors path, as an UTF-8 encoded string."
	}
	'''
	"""
	return send_mfc("ALFileManager", "_getBehaviorsPath", [])

def _getBoxLibrariesPath() -> str:
	"""
	Returns the path to the directory where box libraries are stored on the robot.
	
	Returns
	----------
	The box libraries path, as an UTF-8 encoded string.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "s",
	    "name": "_getBoxLibrariesPath",
	    "parametersSignature": "()",
	    "description": "Returns the path to the directory where box libraries are stored on the robot.",
	    "parameters": [],
	    "returnDescription": "The box libraries path, as an UTF-8 encoded string."
	}
	'''
	"""
	return send_mfc("ALFileManager", "_getBoxLibrariesPath", [])

