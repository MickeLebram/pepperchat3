from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALPreferences allows access to xml preference files. 
A preference is defined as follows : 
pParams[0] Name of the preference; 
pParams[1] Description of the preference; 
pParams[2] The value of the preference (can contain other preferences); 
pParams[3] (optional) The name of the data when inserted into memory.
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
	return send_mfc("ALPreferences", "version", [])

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
	return send_mfc("ALPreferences", "ping", [])

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
	return send_mfc("ALPreferences", "getMethodList", [])

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
	return send_mfc("ALPreferences", "getMethodHelp", [methodName])

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
	return send_mfc("ALPreferences", "getModuleHelp", [])

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
	return send_mfc("ALPreferences", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALPreferences", "wait", [id])

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
	return send_mfc("ALPreferences", "isRunning", [id])

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
	return send_mfc("ALPreferences", "stop", [id])

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
	return send_mfc("ALPreferences", "getBrokerName", [])

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
	return send_mfc("ALPreferences", "getUsage", [name])

def readPrefFile(fileName:str, autoGenerateMemoryNames:bool) -> object:
	"""
	Reads all preferences from an xml files and stores them in an ALValue.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	autoGenerateMemoryNames:bool
		If true a memory name will be generated for each non-array preference.
	
	Returns
	----------
	array reprenting the whole file.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "m",
	    "name": "readPrefFile",
	    "parametersSignature": "(sb)",
	    "description": "Reads all preferences from an xml files and stores them in an ALValue.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associated to the preference."
	        },
	        {
	            "name": "autoGenerateMemoryNames",
	            "description": "If true a memory name will be generated for each non-array preference."
	        }
	    ],
	    "returnDescription": "array reprenting the whole file."
	}
	'''
	"""
	return send_mfc("ALPreferences", "readPrefFile", [fileName, autoGenerateMemoryNames])

def writePrefFile(fileName:str, prefs:object, ignoreMemoryNames:bool) -> None:
	"""
	Writes all preferences from ALValue to an xml file.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	prefs:object
		array reprenting the whole file.
	ignoreMemoryNames:bool
		If true all memory names will be removed before saving.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "writePrefFile",
	    "parametersSignature": "(smb)",
	    "description": "Writes all preferences from ALValue to an xml file.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associated to the preference."
	        },
	        {
	            "name": "prefs",
	            "description": "array reprenting the whole file."
	        },
	        {
	            "name": "ignoreMemoryNames",
	            "description": "If true all memory names will be removed before saving."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferences", "writePrefFile", [fileName, prefs, ignoreMemoryNames])

def removePrefFile(fileName:str) -> None:
	"""
	Remove the xml file.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "removePrefFile",
	    "parametersSignature": "(s)",
	    "description": "Remove the xml file.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the module associated to the preference."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferences", "removePrefFile", [fileName])

def saveToMemory(prefs:object) -> bool:
	"""
	Writes all preferences from ALValue to an xml file.
	
	Parameters
	----------
	prefs:object
		array representing the whole file.
	
	Returns
	----------
	True upon success.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "saveToMemory",
	    "parametersSignature": "(m)",
	    "description": "Writes all preferences from ALValue to an xml file.",
	    "parameters": [
	        {
	            "name": "prefs",
	            "description": "array representing the whole file."
	        }
	    ],
	    "returnDescription": "True upon success."
	}
	'''
	"""
	return send_mfc("ALPreferences", "saveToMemory", [prefs])

