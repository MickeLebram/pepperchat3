from .gentypes import *
from .robot_client import send_mfc
import json
"""
Manage robot resources: Synchronize movement, led, sound. Run specific actions when another behavior wants your resources
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
	return send_mfc("ALResourceManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALResourceManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALResourceManager", "metaObject", [p0])

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
	return send_mfc("ALResourceManager", "terminate", [p0])

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
	return send_mfc("ALResourceManager", "property", [p0])

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
	return send_mfc("ALResourceManager", "setProperty", [p0, p1])

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
	return send_mfc("ALResourceManager", "properties", [])

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
	return send_mfc("ALResourceManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALResourceManager", "isStatsEnabled", [])

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
	return send_mfc("ALResourceManager", "enableStats", [p0])

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
	return send_mfc("ALResourceManager", "stats", [])

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
	return send_mfc("ALResourceManager", "clearStats", [])

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
	return send_mfc("ALResourceManager", "isTraceEnabled", [])

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
	return send_mfc("ALResourceManager", "enableTrace", [p0])

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
	return send_mfc("ALResourceManager", "version", [])

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
	return send_mfc("ALResourceManager", "ping", [])

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
	return send_mfc("ALResourceManager", "getMethodList", [])

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
	return send_mfc("ALResourceManager", "getMethodHelp", [methodName])

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
	return send_mfc("ALResourceManager", "getModuleHelp", [])

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
	return send_mfc("ALResourceManager", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALResourceManager", "wait", [id])

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
	return send_mfc("ALResourceManager", "isRunning", [id])

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
	return send_mfc("ALResourceManager", "stop", [id])

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
	return send_mfc("ALResourceManager", "getBrokerName", [])

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
	return send_mfc("ALResourceManager", "getUsage", [name])

def waitForResource(resourceName:str, ownerName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	ownerName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "waitForResource",
	    "parametersSignature": "(sssi)",
	    "description": "Wait resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        },
	        {
	            "name": "ownerName",
	            "description": "Module name"
	        },
	        {
	            "name": "callbackName",
	            "description": "callback name"
	        },
	        {
	            "name": "timeoutSeconds",
	            "description": "Timeout in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "waitForResource", [resourceName, ownerName, callbackName, timeoutSeconds])

def acquireResource(resourceName:str, moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait and acquire a resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "acquireResource",
	    "parametersSignature": "(sssi)",
	    "description": "Wait and acquire a resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        },
	        {
	            "name": "moduleName",
	            "description": "Module name"
	        },
	        {
	            "name": "callbackName",
	            "description": "callback name"
	        },
	        {
	            "name": "timeoutSeconds",
	            "description": "Timeout in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "acquireResource", [resourceName, moduleName, callbackName, timeoutSeconds])

def waitForOptionalResourcesTree(p0:List[str], p1:str, p2:str, p3:int, p4:List[str]) -> List[str]:
	"""
	Wait resource
	
	Parameters
	----------
	p0:List[str]
		
	p1:str
		
	p2:str
		
	p3:int
		
	p4:List[str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "[s]",
	    "name": "waitForOptionalResourcesTree",
	    "parametersSignature": "([s]ssi[s])",
	    "description": "Wait resource",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "waitForOptionalResourcesTree", [p0, p1, p2, p3, p4])

def waitForResourcesTree(resourceName:List[str], moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait for resource tree. Parent and children are not in conflict. Local function
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "waitForResourcesTree",
	    "parametersSignature": "([s]ssi)",
	    "description": "Wait for resource tree. Parent and children are not in conflict. Local function",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        },
	        {
	            "name": "moduleName",
	            "description": "Module name"
	        },
	        {
	            "name": "callbackName",
	            "description": "callback name"
	        },
	        {
	            "name": "timeoutSeconds",
	            "description": "Timeout in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "waitForResourcesTree", [resourceName, moduleName, callbackName, timeoutSeconds])

def acquireResourcesTree(resourceName:List[str], moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait for resource tree. Parent and children are not in conflict. Local function
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "acquireResourcesTree",
	    "parametersSignature": "([s]ssi)",
	    "description": "Wait for resource tree. Parent and children are not in conflict. Local function",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        },
	        {
	            "name": "moduleName",
	            "description": "Module name"
	        },
	        {
	            "name": "callbackName",
	            "description": "callback name"
	        },
	        {
	            "name": "timeoutSeconds",
	            "description": "Timeout in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "acquireResourcesTree", [resourceName, moduleName, callbackName, timeoutSeconds])

def areResourcesOwnedBy(resourceNameList:List[str], ownerName:str) -> bool:
	"""
	True if all the specified resources are owned by the owner
	
	Parameters
	----------
	resourceNameList:List[str]
		Resource name
	ownerName:str
		Owner pointer with hierarchy
	
	Returns
	----------
	True if all the specify resources are owned by the owner
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "areResourcesOwnedBy",
	    "parametersSignature": "([s]s)",
	    "description": "True if all the specified resources are owned by the owner",
	    "parameters": [
	        {
	            "name": "resourceNameList",
	            "description": "Resource name"
	        },
	        {
	            "name": "ownerName",
	            "description": "Owner pointer with hierarchy"
	        }
	    ],
	    "returnDescription": "True if all the specify resources are owned by the owner"
	}
	'''
	"""
	return send_mfc("ALResourceManager", "areResourcesOwnedBy", [resourceNameList, ownerName])

def releaseResource(resourceName:str, ownerName:str) -> None:
	"""
	Release resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	ownerName:str
		Existing owner name
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "releaseResource",
	    "parametersSignature": "(ss)",
	    "description": "Release resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        },
	        {
	            "name": "ownerName",
	            "description": "Existing owner name"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "releaseResource", [resourceName, ownerName])

def releaseResources(resourceNames:List[str], ownerName:str) -> None:
	"""
	Release  resources list
	
	Parameters
	----------
	resourceNames:List[str]
		Resource names
	ownerName:str
		Owner name
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "releaseResources",
	    "parametersSignature": "([s]s)",
	    "description": "Release  resources list",
	    "parameters": [
	        {
	            "name": "resourceNames",
	            "description": "Resource names"
	        },
	        {
	            "name": "ownerName",
	            "description": "Owner name"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "releaseResources", [resourceNames, ownerName])

def enableStateResource(resourceName:str, enabled:bool) -> None:
	"""
	Enable or disable a state resource
	
	Parameters
	----------
	resourceName:str
		The name of the resource that you wish enable of disable. e.g. Standing
	enabled:bool
		True to enable, false to disable
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "enableStateResource",
	    "parametersSignature": "(sb)",
	    "description": "Enable or disable a state resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "The name of the resource that you wish enable of disable. e.g. Standing"
	        },
	        {
	            "name": "enabled",
	            "description": "True to enable, false to disable"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "enableStateResource", [resourceName, enabled])

def checkStateResourceFree(resourceName:List[str]) -> bool:
	"""
	check if all the state resource in the list are free
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "b",
	    "name": "checkStateResourceFree",
	    "parametersSignature": "([s])",
	    "description": "check if all the state resource in the list are free",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "checkStateResourceFree", [resourceName])

def areResourcesFree(resourceNames:List[str]) -> bool:
	"""
	True if all resources are free
	
	Parameters
	----------
	resourceNames:List[str]
		Resource names
	
	Returns
	----------
	True if all the specify resources are free
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "b",
	    "name": "areResourcesFree",
	    "parametersSignature": "([s])",
	    "description": "True if all resources are free",
	    "parameters": [
	        {
	            "name": "resourceNames",
	            "description": "Resource names"
	        }
	    ],
	    "returnDescription": "True if all the specify resources are free"
	}
	'''
	"""
	return send_mfc("ALResourceManager", "areResourcesFree", [resourceNames])

def isResourceFree(resourceNames:str) -> bool:
	"""
	True if the resource is free
	
	Parameters
	----------
	resourceNames:str
		Resource name
	
	Returns
	----------
	True if the specify resources is free
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "b",
	    "name": "isResourceFree",
	    "parametersSignature": "(s)",
	    "description": "True if the resource is free",
	    "parameters": [
	        {
	            "name": "resourceNames",
	            "description": "Resource name"
	        }
	    ],
	    "returnDescription": "True if the specify resources is free"
	}
	'''
	"""
	return send_mfc("ALResourceManager", "isResourceFree", [resourceNames])

def createResource(resourceName:str, parentResourceName:str) -> None:
	"""
	Create a resource
	
	Parameters
	----------
	resourceName:str
		Resource name to create
	parentResourceName:str
		Parent resource name or empty string for root resource
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "createResource",
	    "parametersSignature": "(ss)",
	    "description": "Create a resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name to create"
	        },
	        {
	            "name": "parentResourceName",
	            "description": "Parent resource name or empty string for root resource"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "createResource", [resourceName, parentResourceName])

def deleteResource(resourceName:str, deleteChildResources:bool) -> None:
	"""
	Delete a root resource
	
	Parameters
	----------
	resourceName:str
		Resource name to delete
	deleteChildResources:bool
		DEPRECATED: Delete child resources if true
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "deleteResource",
	    "parametersSignature": "(sb)",
	    "description": "Delete a root resource",
	    "parameters": [
	        {
	            "name": "resourceName",
	            "description": "Resource name to delete"
	        },
	        {
	            "name": "deleteChildResources",
	            "description": "DEPRECATED: Delete child resources if true"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "deleteResource", [resourceName, deleteChildResources])

def isInGroup(resourceGroupName:str, resourceName:str) -> bool:
	"""
	True if a resource is in another parent resource
	
	Parameters
	----------
	resourceGroupName:str
		Group name. Ex: Arm
	resourceName:str
		Resource name
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "isInGroup",
	    "parametersSignature": "(ss)",
	    "description": "True if a resource is in another parent resource",
	    "parameters": [
	        {
	            "name": "resourceGroupName",
	            "description": "Group name. Ex: Arm"
	        },
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "isInGroup", [resourceGroupName, resourceName])

def createResourcesList(resourceGroupName:List[str], resourceName:str) -> None:
	"""
	True if a resource is in another parent resource
	
	Parameters
	----------
	resourceGroupName:List[str]
		Group name. Ex: Arm
	resourceName:str
		Resource name
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "createResourcesList",
	    "parametersSignature": "([s]s)",
	    "description": "True if a resource is in another parent resource",
	    "parameters": [
	        {
	            "name": "resourceGroupName",
	            "description": "Group name. Ex: Arm"
	        },
	        {
	            "name": "resourceName",
	            "description": "Resource name"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "createResourcesList", [resourceGroupName, resourceName])

def getResources() -> object:
	"""
	Get tree of resources
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "m",
	    "name": "getResources",
	    "parametersSignature": "()",
	    "description": "Get tree of resources",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "getResources", [])

def ownersGet() -> object:
	"""
	The tree of the resources owners.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "m",
	    "name": "ownersGet",
	    "parametersSignature": "()",
	    "description": "The tree of the resources owners.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALResourceManager", "ownersGet", [])

