from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module is intended to manage behaviors. With this module, you can load, start, stop behaviors, add default behaviors or remove them. 

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
	return send_mfc("ALBehaviorManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALBehaviorManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALBehaviorManager", "metaObject", [p0])

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
	return send_mfc("ALBehaviorManager", "terminate", [p0])

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
	return send_mfc("ALBehaviorManager", "property", [p0])

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
	return send_mfc("ALBehaviorManager", "setProperty", [p0, p1])

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
	return send_mfc("ALBehaviorManager", "properties", [])

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
	return send_mfc("ALBehaviorManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALBehaviorManager", "isStatsEnabled", [])

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
	return send_mfc("ALBehaviorManager", "enableStats", [p0])

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
	return send_mfc("ALBehaviorManager", "stats", [])

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
	return send_mfc("ALBehaviorManager", "clearStats", [])

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
	return send_mfc("ALBehaviorManager", "isTraceEnabled", [])

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
	return send_mfc("ALBehaviorManager", "enableTrace", [p0])

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
	return send_mfc("ALBehaviorManager", "version", [])

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
	return send_mfc("ALBehaviorManager", "ping", [])

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
	return send_mfc("ALBehaviorManager", "getMethodList", [])

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
	return send_mfc("ALBehaviorManager", "getMethodHelp", [methodName])

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
	return send_mfc("ALBehaviorManager", "getModuleHelp", [])

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
	return send_mfc("ALBehaviorManager", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALBehaviorManager", "wait", [id])

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
	return send_mfc("ALBehaviorManager", "isRunning", [id])

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
	return send_mfc("ALBehaviorManager", "stop", [id])

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
	return send_mfc("ALBehaviorManager", "getBrokerName", [])

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
	return send_mfc("ALBehaviorManager", "getUsage", [name])

def preloadBehavior(behavior:str) -> bool:
	"""
	Load a behavior
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	Returns
	----------
	Returns true if it was successfully loaded.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "preloadBehavior",
	    "parametersSignature": "(s)",
	    "description": "Load a behavior",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": "Returns true if it was successfully loaded."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "preloadBehavior", [behavior])

def startBehavior(behavior:str) -> None:
	"""
	Starts a behavior, returns when started.
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "startBehavior",
	    "parametersSignature": "(s)",
	    "description": "Starts a behavior, returns when started.",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "startBehavior", [behavior])

def runBehavior(behavior:str) -> None:
	"""
	Runs a behavior, returns when finished
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "runBehavior",
	    "parametersSignature": "(s)",
	    "description": "Runs a behavior, returns when finished",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "runBehavior", [behavior])

def stopBehavior(behavior:str) -> None:
	"""
	Stop a behavior
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "stopBehavior",
	    "parametersSignature": "(s)",
	    "description": "Stop a behavior",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "stopBehavior", [behavior])

def stopAllBehaviors() -> None:
	"""
	Stop all behaviors
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "stopAllBehaviors",
	    "parametersSignature": "()",
	    "description": "Stop all behaviors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "stopAllBehaviors", [])

def isBehaviorInstalled(name:str) -> bool:
	"""
	Tell if supplied name corresponds to a behavior that has been installed
	
	Parameters
	----------
	name:str
		The behavior directory name
	
	Returns
	----------
	Returns true if it is a valid behavior
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "isBehaviorInstalled",
	    "parametersSignature": "(s)",
	    "description": "Tell if supplied name corresponds to a behavior that has been installed",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The behavior directory name"
	        }
	    ],
	    "returnDescription": "Returns true if it is a valid behavior"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "isBehaviorInstalled", [name])

def isBehaviorPresent(prefixedBehavior:str) -> bool:
	"""
	Tell if the supplied namecorresponds to an existing behavior.
	
	Parameters
	----------
	prefixedBehavior:str
		Prefixed behavior or just behavior's name (latter usage deprecated, in this case the behavior is searched for amongst user's behaviors, then in system behaviors) DEPRECATED in favor of ALBehaviorManager.isBehaviorInstalled.
	
	Returns
	----------
	Returns true if it is an existing behavior
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "b",
	    "name": "isBehaviorPresent",
	    "parametersSignature": "(s)",
	    "description": "Tell if the supplied namecorresponds to an existing behavior.",
	    "parameters": [
	        {
	            "name": "prefixedBehavior",
	            "description": "Prefixed behavior or just behavior's name (latter usage deprecated, in this case the behavior is searched for amongst user's behaviors, then in system behaviors) DEPRECATED in favor of ALBehaviorManager.isBehaviorInstalled."
	        }
	    ],
	    "returnDescription": "Returns true if it is an existing behavior"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "isBehaviorPresent", [prefixedBehavior])

def getBehaviorNames() -> List[str]:
	"""
	Get behaviors
	
	Returns
	----------
	Returns the list of behaviors prefixed by their type (User/ or System/). DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[s]",
	    "name": "getBehaviorNames",
	    "parametersSignature": "()",
	    "description": "Get behaviors",
	    "parameters": [],
	    "returnDescription": "Returns the list of behaviors prefixed by their type (User/ or System/). DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getBehaviorNames", [])

def getUserBehaviorNames() -> List[str]:
	"""
	Get user's behaviors
	
	Returns
	----------
	Returns the list of user's behaviors prefixed by User/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "[s]",
	    "name": "getUserBehaviorNames",
	    "parametersSignature": "()",
	    "description": "Get user's behaviors",
	    "parameters": [],
	    "returnDescription": "Returns the list of user's behaviors prefixed by User/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getUserBehaviorNames", [])

def getSystemBehaviorNames() -> List[str]:
	"""
	Get system behaviors
	
	Returns
	----------
	Returns the list of system behaviors prefixed by System/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "[s]",
	    "name": "getSystemBehaviorNames",
	    "parametersSignature": "()",
	    "description": "Get system behaviors",
	    "parameters": [],
	    "returnDescription": "Returns the list of system behaviors prefixed by System/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getSystemBehaviorNames", [])

def getInstalledBehaviors() -> List[str]:
	"""
	Get installed behaviors directories names
	
	Returns
	----------
	Returns the behaviors list
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "[s]",
	    "name": "getInstalledBehaviors",
	    "parametersSignature": "()",
	    "description": "Get installed behaviors directories names",
	    "parameters": [],
	    "returnDescription": "Returns the behaviors list"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getInstalledBehaviors", [])

def getBehaviorsByTag(tag:str) -> List[str]:
	"""
	Get installed behaviors directories names and filter it by tag.
	
	Parameters
	----------
	tag:str
		A tag to filter the list with.
	
	Returns
	----------
	Returns the behaviors list
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "[s]",
	    "name": "getBehaviorsByTag",
	    "parametersSignature": "(s)",
	    "description": "Get installed behaviors directories names and filter it by tag.",
	    "parameters": [
	        {
	            "name": "tag",
	            "description": "A tag to filter the list with."
	        }
	    ],
	    "returnDescription": "Returns the behaviors list"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getBehaviorsByTag", [tag])

def isBehaviorRunning(behavior:str) -> bool:
	"""
	Tell if supplied name corresponds to a running behavior
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	Returns
	----------
	Returns true if it is a running behavior
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "b",
	    "name": "isBehaviorRunning",
	    "parametersSignature": "(s)",
	    "description": "Tell if supplied name corresponds to a running behavior",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": "Returns true if it is a running behavior"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "isBehaviorRunning", [behavior])

def isBehaviorLoaded(behavior:str) -> bool:
	"""
	Tell if supplied name corresponds to a loaded behavior
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	Returns
	----------
	Returns true if it is a loaded behavior
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "isBehaviorLoaded",
	    "parametersSignature": "(s)",
	    "description": "Tell if supplied name corresponds to a loaded behavior",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": "Returns true if it is a loaded behavior"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "isBehaviorLoaded", [behavior])

def getRunningBehaviors() -> List[str]:
	"""
	Get running behaviors
	
	Returns
	----------
	Return running behaviors
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "[s]",
	    "name": "getRunningBehaviors",
	    "parametersSignature": "()",
	    "description": "Get running behaviors",
	    "parameters": [],
	    "returnDescription": "Return running behaviors"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getRunningBehaviors", [])

def getLoadedBehaviors() -> List[str]:
	"""
	Get loaded behaviors
	
	Returns
	----------
	Return loaded behaviors
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "[s]",
	    "name": "getLoadedBehaviors",
	    "parametersSignature": "()",
	    "description": "Get loaded behaviors",
	    "parameters": [],
	    "returnDescription": "Return loaded behaviors"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getLoadedBehaviors", [])

def getTagList() -> List[str]:
	"""
	Get tags found on installed behaviors.
	
	Returns
	----------
	The list of tags found.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[s]",
	    "name": "getTagList",
	    "parametersSignature": "()",
	    "description": "Get tags found on installed behaviors.",
	    "parameters": [],
	    "returnDescription": "The list of tags found."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getTagList", [])

def getBehaviorTags(behavior:str) -> List[str]:
	"""
	Get tags found on the given behavior.
	
	Parameters
	----------
	behavior:str
		The local path towards a behavior or a directory.
	
	Returns
	----------
	The list of tags found.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "[s]",
	    "name": "getBehaviorTags",
	    "parametersSignature": "(s)",
	    "description": "Get tags found on the given behavior.",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "The local path towards a behavior or a directory."
	        }
	    ],
	    "returnDescription": "The list of tags found."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getBehaviorTags", [behavior])

def getBehaviorNature(behavior:str) -> str:
	"""
	Get the nature of the given behavior.
	
	Parameters
	----------
	behavior:str
		The local path towards a behavior or a directory.
	
	Returns
	----------
	The nature of the behavior.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "s",
	    "name": "getBehaviorNature",
	    "parametersSignature": "(s)",
	    "description": "Get the nature of the given behavior.",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "The local path towards a behavior or a directory."
	        }
	    ],
	    "returnDescription": "The nature of the behavior."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getBehaviorNature", [behavior])

def _getBehaviorRelativePath(behaviorId:str) -> str:
	"""
	Get the relative path of a running behavior inside its package.
	
	Parameters
	----------
	behaviorId:str
		The ID of the behavior.
	
	Returns
	----------
	The relative path of the behavior.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "s",
	    "name": "_getBehaviorRelativePath",
	    "parametersSignature": "(s)",
	    "description": "Get the relative path of a running behavior inside its package.",
	    "parameters": [
	        {
	            "name": "behaviorId",
	            "description": "The ID of the behavior."
	        }
	    ],
	    "returnDescription": "The relative path of the behavior."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "_getBehaviorRelativePath", [behaviorId])

def _getPackageUid(behaviorId:str) -> str:
	"""
	Get the package UID of a running behavior.
	
	Parameters
	----------
	behaviorId:str
		The ID of the behavior.
	
	Returns
	----------
	The package UID of the behavior.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "s",
	    "name": "_getPackageUid",
	    "parametersSignature": "(s)",
	    "description": "Get the package UID of a running behavior.",
	    "parameters": [
	        {
	            "name": "behaviorId",
	            "description": "The ID of the behavior."
	        }
	    ],
	    "returnDescription": "The package UID of the behavior."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "_getPackageUid", [behaviorId])

def addDefaultBehavior(behavior:str) -> None:
	"""
	Set the given behavior as default
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "addDefaultBehavior",
	    "parametersSignature": "(s)",
	    "description": "Set the given behavior as default",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "addDefaultBehavior", [behavior])

def removeDefaultBehavior(behavior:str) -> None:
	"""
	Remove the given behavior from the default behaviors
	
	Parameters
	----------
	behavior:str
		Behavior name 
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "removeDefaultBehavior",
	    "parametersSignature": "(s)",
	    "description": "Remove the given behavior from the default behaviors",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "Behavior name "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "removeDefaultBehavior", [behavior])

def getDefaultBehaviors() -> List[str]:
	"""
	Get default behaviors
	
	Returns
	----------
	Return default behaviors
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "[s]",
	    "name": "getDefaultBehaviors",
	    "parametersSignature": "()",
	    "description": "Get default behaviors",
	    "parameters": [],
	    "returnDescription": "Return default behaviors"
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "getDefaultBehaviors", [])

def playDefaultProject() -> None:
	"""
	Play default behaviors
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "playDefaultProject",
	    "parametersSignature": "()",
	    "description": "Play default behaviors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "playDefaultProject", [])

def _onDataChanged(dataName:str, dataValue:object, message:str) -> None:
	"""
	Be notified when something we have subscribe to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:str
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_onDataChanged",
	    "parametersSignature": "(sms)",
	    "description": "Be notified when something we have subscribe to has changed in ALMemory",
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
	return send_mfc("ALBehaviorManager", "_onDataChanged", [dataName, dataValue, message])

def _getBehaviorFrameManagerId(name:str) -> str:
	"""
	get the FrameManagerID. INTERNAL
	
	Parameters
	----------
	name:str
		name of choregraphe project
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "s",
	    "name": "_getBehaviorFrameManagerId",
	    "parametersSignature": "(s)",
	    "description": "get the FrameManagerID. INTERNAL",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "name of choregraphe project"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "_getBehaviorFrameManagerId", [name])

def resolveBehaviorName(name:str) -> str:
	"""
	Find out the actual <package>/<behavior> path behind a behavior name.
	
	Parameters
	----------
	name:str
		name of a behavior
	
	Returns
	----------
	The actual <package>/<behavior> path if found, else an empty string. Throws an ALERROR if two behavior names conflicted.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "s",
	    "name": "resolveBehaviorName",
	    "parametersSignature": "(s)",
	    "description": "Find out the actual <package>/<behavior> path behind a behavior name.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "name of a behavior"
	        }
	    ],
	    "returnDescription": "The actual <package>/<behavior> path if found, else an empty string. Throws an ALERROR if two behavior names conflicted."
	}
	'''
	"""
	return send_mfc("ALBehaviorManager", "resolveBehaviorName", [name])

