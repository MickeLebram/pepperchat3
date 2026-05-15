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
	return send_mfc("ALWorldRepresentation", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALWorldRepresentation", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALWorldRepresentation", "metaObject", [p0])

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
	return send_mfc("ALWorldRepresentation", "terminate", [p0])

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
	return send_mfc("ALWorldRepresentation", "property", [p0])

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
	return send_mfc("ALWorldRepresentation", "setProperty", [p0, p1])

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
	return send_mfc("ALWorldRepresentation", "properties", [])

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
	return send_mfc("ALWorldRepresentation", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALWorldRepresentation", "isStatsEnabled", [])

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
	return send_mfc("ALWorldRepresentation", "enableStats", [p0])

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
	return send_mfc("ALWorldRepresentation", "stats", [])

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
	return send_mfc("ALWorldRepresentation", "clearStats", [])

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
	return send_mfc("ALWorldRepresentation", "isTraceEnabled", [])

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
	return send_mfc("ALWorldRepresentation", "enableTrace", [p0])

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
	return send_mfc("ALWorldRepresentation", "version", [])

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
	return send_mfc("ALWorldRepresentation", "ping", [])

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
	return send_mfc("ALWorldRepresentation", "getMethodList", [])

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
	return send_mfc("ALWorldRepresentation", "getMethodHelp", [methodName])

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
	return send_mfc("ALWorldRepresentation", "getModuleHelp", [])

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
	return send_mfc("ALWorldRepresentation", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALWorldRepresentation", "wait", [id])

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
	return send_mfc("ALWorldRepresentation", "isRunning", [id])

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
	return send_mfc("ALWorldRepresentation", "stop", [id])

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
	return send_mfc("ALWorldRepresentation", "getBrokerName", [])

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
	return send_mfc("ALWorldRepresentation", "getUsage", [name])

def addAttributeToCategory(p0:str, p1:str, p2:object) -> int:
	"""
	Add an attribute to a category.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "i",
	    "name": "addAttributeToCategory",
	    "parametersSignature": "(ssm)",
	    "description": "Add an attribute to a category.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "addAttributeToCategory", [p0, p1, p2])

def clearObject(p0:str) -> int:
	"""
	Clear an object.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "i",
	    "name": "clearObject",
	    "parametersSignature": "(s)",
	    "description": "Clear an object.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "clearObject", [p0])

def clearOldPositions(p0:str, p1:int) -> int:
	"""
	Clear recording of old positions.
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "i",
	    "name": "clearOldPositions",
	    "parametersSignature": "(si)",
	    "description": "Clear recording of old positions.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "clearOldPositions", [p0, p1])

def createObjectCategory(p0:str, p1:bool) -> int:
	"""
	Create a new object category
	
	Parameters
	----------
	p0:str
		
	p1:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "createObjectCategory",
	    "parametersSignature": "(sb)",
	    "description": "Create a new object category",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "createObjectCategory", [p0, p1])

def removeObjectCategory(p0:str) -> int:
	"""
	Remove an object category
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "i",
	    "name": "removeObjectCategory",
	    "parametersSignature": "(s)",
	    "description": "Remove an object category",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "removeObjectCategory", [p0])

def objectCategoryExists(p0:str) -> bool:
	"""
	Tells if an object category exists
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "objectCategoryExists",
	    "parametersSignature": "(s)",
	    "description": "Tells if an object category exists",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "objectCategoryExists", [p0])

def deleteObjectAttribute(p0:str, p1:str, p2:str) -> int:
	"""
	Delete an object attribute
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "deleteObjectAttribute",
	    "parametersSignature": "(sss)",
	    "description": "Delete an object attribute",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "deleteObjectAttribute", [p0, p1, p2])

def findObject(p0:str) -> bool:
	"""
	Check that an object is present.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "findObject",
	    "parametersSignature": "(s)",
	    "description": "Check that an object is present.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "findObject", [p0])

def load() -> int:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "load",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "load", [])

def getAttributesFromCategory(p0:str) -> object:
	"""
	Get all attributes from a category if it exists.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "getAttributesFromCategory",
	    "parametersSignature": "(s)",
	    "description": "Get all attributes from a category if it exists.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getAttributesFromCategory", [p0])

def getChildrenNames(p0:str) -> List[str]:
	"""
	Get the direct children of an object.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "[s]",
	    "name": "getChildrenNames",
	    "parametersSignature": "(s)",
	    "description": "Get the direct children of an object.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getChildrenNames", [p0])

def getObjectNames() -> List[str]:
	"""
	Get the name of the objects.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "[s]",
	    "name": "getObjectNames",
	    "parametersSignature": "()",
	    "description": "Get the name of the objects.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectNames", [])

def getObjectAttributes(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "m",
	    "name": "getObjectAttributes",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectAttributes", [p0])

def getObjectAttributeValues(p0:str, p1:str, p2:int) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "m",
	    "name": "getObjectAttributeValues",
	    "parametersSignature": "(ssi)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectAttributeValues", [p0, p1, p2])

def getObjectLatestAttributes(p0:str, p1:int) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "m",
	    "name": "getObjectLatestAttributes",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectLatestAttributes", [p0, p1])

def getObjectParentName(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "s",
	    "name": "getObjectParentName",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectParentName", [p0])

def getObjectsInCategory(p0:str) -> List[str]:
	"""
	Get the name of the objects stored in the database.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[s]",
	    "name": "getObjectsInCategory",
	    "parametersSignature": "(s)",
	    "description": "Get the name of the objects stored in the database.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectsInCategory", [p0])

def getObjectCategory(p0:str) -> str:
	"""
	Get the name of the database where the object is stored.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "s",
	    "name": "getObjectCategory",
	    "parametersSignature": "(s)",
	    "description": "Get the name of the database where the object is stored.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getObjectCategory", [p0])

def getPosition(p0:str, p1:str) -> object:
	"""
	Get the position of an object with quaternion / translation.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "m",
	    "name": "getPosition",
	    "parametersSignature": "(ss)",
	    "description": "Get the position of an object with quaternion / translation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getPosition", [p0, p1])

def getPosition6D(p0:str, p1:str) -> List[float]:
	"""
	Get the position from one object to another.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "[f]",
	    "name": "getPosition6D",
	    "parametersSignature": "(ss)",
	    "description": "Get the position from one object to another.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getPosition6D", [p0, p1])

def getPosition6DAtTime(p0:str, p1:str, p2:int, p3:int) -> List[float]:
	"""
	Get the interpolated position of an object
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:int
		
	p3:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "[f]",
	    "name": "getPosition6DAtTime",
	    "parametersSignature": "(ssii)",
	    "description": "Get the interpolated position of an object",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getPosition6DAtTime", [p0, p1, p2, p3])

def getRootName() -> str:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "s",
	    "name": "getRootName",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "getRootName", [])

def save() -> int:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "i",
	    "name": "save",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "save", [])

def select(p0:str, p1:str, p2:str, p3:str) -> object:
	"""
	Select information from a database.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "m",
	    "name": "select",
	    "parametersSignature": "(ssss)",
	    "description": "Select information from a database.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "select", [p0, p1, p2, p3])

def selectWithOrder(p0:str, p1:str, p2:str, p3:str, p4:str) -> object:
	"""
	Select ordered information from a database.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	p4:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "m",
	    "name": "selectWithOrder",
	    "parametersSignature": "(sssss)",
	    "description": "Select ordered information from a database.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "selectWithOrder", [p0, p1, p2, p3, p4])

def storeObject(p0:str, p1:str, p2:List[float], p3:str, p4:object) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:List[float]
		
	p3:str
		
	p4:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "i",
	    "name": "storeObject",
	    "parametersSignature": "(ss[f]sm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "storeObject", [p0, p1, p2, p3, p4])

def storeObjectWithReference(p0:str, p1:str, p2:str, p3:List[float], p4:str, p5:object) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:List[float]
		
	p4:str
		
	p5:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "i",
	    "name": "storeObjectWithReference",
	    "parametersSignature": "(sss[f]sm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "storeObjectWithReference", [p0, p1, p2, p3, p4, p5])

def storeObjectAttribute(p0:str, p1:str, p2:object) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "i",
	    "name": "storeObjectAttribute",
	    "parametersSignature": "(ssm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "storeObjectAttribute", [p0, p1, p2])

def updatePosition(p0:str, p1:List[float], p2:bool) -> int:
	"""
	Update the position of an object.
	
	Parameters
	----------
	p0:str
		
	p1:List[float]
		
	p2:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "i",
	    "name": "updatePosition",
	    "parametersSignature": "(s[f]b)",
	    "description": "Update the position of an object.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "updatePosition", [p0, p1, p2])

def updatePositionWithReference(p0:str, p1:str, p2:List[float], p3:bool) -> int:
	"""
	Update the position of an object relative to another.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:List[float]
		
	p3:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "i",
	    "name": "updatePositionWithReference",
	    "parametersSignature": "(ss[f]b)",
	    "description": "Update the position of an object relative to another.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "updatePositionWithReference", [p0, p1, p2, p3])

def updateAttribute(p0:str, p1:str, p2:str, p3:object) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "i",
	    "name": "updateAttribute",
	    "parametersSignature": "(sssm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "updateAttribute", [p0, p1, p2, p3])

def _startMemoryCheck(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "_startMemoryCheck",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "_startMemoryCheck", [p0])

def _stopMemoryCheck() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "_stopMemoryCheck",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "_stopMemoryCheck", [])

def _beginTransaction(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "i",
	    "name": "_beginTransaction",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "_beginTransaction", [p0])

def _endTransaction(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "i",
	    "name": "_endTransaction",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALWorldRepresentation", "_endTransaction", [p0])

