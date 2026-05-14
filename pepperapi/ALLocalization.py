from .gentypes import *
from .robot_client import send_mfc
import json
"""

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
	return send_mfc("ALLocalization", "version", [])

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
	return send_mfc("ALLocalization", "ping", [])

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
	return send_mfc("ALLocalization", "getMethodList", [])

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
	return send_mfc("ALLocalization", "getMethodHelp", [methodName])

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
	return send_mfc("ALLocalization", "getModuleHelp", [])

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
	return send_mfc("ALLocalization", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALLocalization", "wait", [id])

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
	return send_mfc("ALLocalization", "isRunning", [id])

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
	return send_mfc("ALLocalization", "stop", [id])

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
	return send_mfc("ALLocalization", "getBrokerName", [])

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
	return send_mfc("ALLocalization", "getUsage", [name])

def stopAll() -> None:
	"""
	Stop all robot movements.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "stopAll",
	    "parametersSignature": "()",
	    "description": "Stop all robot movements.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "stopAll", [])

def learnHome() -> int:
	"""
	Learn the robot home.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "learnHome",
	    "parametersSignature": "()",
	    "description": "Learn the robot home.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "learnHome", [])

def isInCurrentHome() -> bool:
	"""
	Is the robot in its home?
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "isInCurrentHome",
	    "parametersSignature": "()",
	    "description": "Is the robot in its home?",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "isInCurrentHome", [])

def getCurrentPanoramaDescriptor() -> object:
	"""
	Get some information about the current panorama.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getCurrentPanoramaDescriptor",
	    "parametersSignature": "()",
	    "description": "Get some information about the current panorama.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getCurrentPanoramaDescriptor", [])

def getFrame(p0:int, p1:str) -> object:
	"""
	Get a frame buffer.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "getFrame",
	    "parametersSignature": "(is)",
	    "description": "Get a frame buffer.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getFrame", [p0, p1])

def clear(pDirectory:str) -> int:
	"""
	Delete all panoramas in a directory.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "clear",
	    "parametersSignature": "(s)",
	    "description": "Delete all panoramas in a directory.",
	    "parameters": [
	        {
	            "name": "pDirectory",
	            "description": "Name of the directory"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "clear", [pDirectory])

def load(pDirectory:str) -> int:
	"""
	Loads panoramas from a directory in the default one.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "load",
	    "parametersSignature": "(s)",
	    "description": "Loads panoramas from a directory in the default one.",
	    "parameters": [
	        {
	            "name": "pDirectory",
	            "description": "Name of the directory"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "load", [pDirectory])

def save(pDirectory:str) -> int:
	"""
	Save the temporary panoramas in a directory from the default one.
	
	Parameters
	----------
	pDirectory:str
		Name of the directory
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "i",
	    "name": "save",
	    "parametersSignature": "(s)",
	    "description": "Save the temporary panoramas in a directory from the default one.",
	    "parameters": [
	        {
	            "name": "pDirectory",
	            "description": "Name of the directory"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "save", [pDirectory])

def getRobotPosition_1() -> List[float]:
	"""
	Note: This is one of the overloads of the original method (getRobotPosition)
	
	Get the robot position in world navigation.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "[f]",
	    "name": "getRobotPosition",
	    "parametersSignature": "()",
	    "description": "Get the robot position in world navigation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getRobotPosition", [])

def getRobotPosition_2(p0:bool) -> List[float]:
	"""
	Note: This is one of the overloads of the original method (getRobotPosition)
	
	Get the robot position in world navigation.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "[f]",
	    "name": "getRobotPosition",
	    "parametersSignature": "(b)",
	    "description": "Get the robot position in world navigation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getRobotPosition", [p0])

def getRobotOrientation_1(p0:bool) -> object:
	"""
	Note: This is one of the overloads of the original method (getRobotOrientation)
	
	Get the robot orientation.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "m",
	    "name": "getRobotOrientation",
	    "parametersSignature": "(b)",
	    "description": "Get the robot orientation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getRobotOrientation", [p0])

def getRobotOrientation_2() -> object:
	"""
	Note: This is one of the overloads of the original method (getRobotOrientation)
	
	Get the robot orientation.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "m",
	    "name": "getRobotOrientation",
	    "parametersSignature": "()",
	    "description": "Get the robot orientation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "getRobotOrientation", [])

def goToHome() -> int:
	"""
	Go to the robot home.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "i",
	    "name": "goToHome",
	    "parametersSignature": "()",
	    "description": "Go to the robot home.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "goToHome", [])

def goToPosition(p0:List[float]) -> int:
	"""
	Go to a given position.
	
	Parameters
	----------
	p0:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "i",
	    "name": "goToPosition",
	    "parametersSignature": "([f])",
	    "description": "Go to a given position.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "goToPosition", [p0])

def _getSavingDirectories() -> List[str]:
	"""
	Return the list of saving directories
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "[s]",
	    "name": "_getSavingDirectories",
	    "parametersSignature": "()",
	    "description": "Return the list of saving directories",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "_getSavingDirectories", [])

def _getLoadedDirectory() -> str:
	"""
	Return the current loaded directory name. Will be empty if there is no active panorama or if it has not been saved to a directory yet
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "s",
	    "name": "_getLoadedDirectory",
	    "parametersSignature": "()",
	    "description": "Return the current loaded directory name. Will be empty if there is no active panorama or if it has not been saved to a directory yet",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLocalization", "_getLoadedDirectory", [])

