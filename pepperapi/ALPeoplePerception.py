from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module controls the People Perception flow and pushes information about detected people in ALMemory.
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
	return send_mfc("ALPeoplePerception", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALPeoplePerception", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALPeoplePerception", "metaObject", [p0])

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
	return send_mfc("ALPeoplePerception", "terminate", [p0])

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
	return send_mfc("ALPeoplePerception", "property", [p0])

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
	return send_mfc("ALPeoplePerception", "setProperty", [p0, p1])

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
	return send_mfc("ALPeoplePerception", "properties", [])

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
	return send_mfc("ALPeoplePerception", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALPeoplePerception", "isStatsEnabled", [])

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
	return send_mfc("ALPeoplePerception", "enableStats", [p0])

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
	return send_mfc("ALPeoplePerception", "stats", [])

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
	return send_mfc("ALPeoplePerception", "clearStats", [])

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
	return send_mfc("ALPeoplePerception", "isTraceEnabled", [])

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
	return send_mfc("ALPeoplePerception", "enableTrace", [p0])

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
	return send_mfc("ALPeoplePerception", "version", [])

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
	return send_mfc("ALPeoplePerception", "ping", [])

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
	return send_mfc("ALPeoplePerception", "getMethodList", [])

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
	return send_mfc("ALPeoplePerception", "getMethodHelp", [methodName])

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
	return send_mfc("ALPeoplePerception", "getModuleHelp", [])

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
	return send_mfc("ALPeoplePerception", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALPeoplePerception", "wait", [id])

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
	return send_mfc("ALPeoplePerception", "isRunning", [id])

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
	return send_mfc("ALPeoplePerception", "stop", [id])

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
	return send_mfc("ALPeoplePerception", "getBrokerName", [])

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
	return send_mfc("ALPeoplePerception", "getUsage", [name])

def subscribe_1(name:str, period:int, precision:float) -> None:
	"""
	Note: This is one of the overloads of the original method (subscribe)
	
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "subscribe",
	    "parametersSignature": "(sif)",
	    "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which subscribes."
	        },
	        {
	            "name": "period",
	            "description": "Refresh period (in milliseconds) if relevant."
	        },
	        {
	            "name": "precision",
	            "description": "Precision of the extractor if relevant."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "subscribe", [name, period, precision])

def subscribe_2(name:str) -> None:
	"""
	Note: This is one of the overloads of the original method (subscribe)
	
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "subscribe",
	    "parametersSignature": "(s)",
	    "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which subscribes."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "subscribe", [name])

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "unsubscribe",
	    "parametersSignature": "(s)",
	    "description": "Unsubscribes from the extractor.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which had subscribed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "updatePeriod",
	    "parametersSignature": "(si)",
	    "description": "Updates the period if relevant.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        },
	        {
	            "name": "period",
	            "description": "Refresh period (in milliseconds)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "updatePrecision",
	    "parametersSignature": "(sf)",
	    "description": "Updates the precision if relevant.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        },
	        {
	            "name": "precision",
	            "description": "Precision of the extractor."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "i",
	    "name": "getCurrentPeriod",
	    "parametersSignature": "()",
	    "description": "Gets the current period.",
	    "parameters": [],
	    "returnDescription": "Refresh period (in milliseconds)."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "f",
	    "name": "getCurrentPrecision",
	    "parametersSignature": "()",
	    "description": "Gets the current precision.",
	    "parameters": [],
	    "returnDescription": "Precision of the extractor."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getCurrentPrecision", [])

def getMyPeriod(name:str) -> int:
	"""
	Gets the period for a specific subscription.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	
	Returns
	----------
	Refresh period (in milliseconds).
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "getMyPeriod",
	    "parametersSignature": "(s)",
	    "description": "Gets the period for a specific subscription.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        }
	    ],
	    "returnDescription": "Refresh period (in milliseconds)."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMyPeriod", [name])

def getMyPrecision(name:str) -> float:
	"""
	Gets the precision for a specific subscription.
	
	Parameters
	----------
	name:str
		name of the module which has subscribed
	
	Returns
	----------
	precision of the extractor
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "f",
	    "name": "getMyPrecision",
	    "parametersSignature": "(s)",
	    "description": "Gets the precision for a specific subscription.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "name of the module which has subscribed"
	        }
	    ],
	    "returnDescription": "precision of the extractor"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMyPrecision", [name])

def getSubscribersInfo() -> object:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "getSubscribersInfo",
	    "parametersSignature": "()",
	    "description": "Gets the parameters given by the module.",
	    "parameters": [],
	    "returnDescription": "Array of names and parameters of all subscribers."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "[s]",
	    "name": "getOutputNames",
	    "parametersSignature": "()",
	    "description": "Get the list of values updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of values updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "[s]",
	    "name": "getEventList",
	    "parametersSignature": "()",
	    "description": "Get the list of events updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of events updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "[s]",
	    "name": "getMemoryKeyList",
	    "parametersSignature": "()",
	    "description": "Get the list of events updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of events updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMemoryKeyList", [])

def isPaused() -> bool:
	"""
	Gets extractor pause status
	
	Returns
	----------
	True if the extractor is paused, False if not
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "isPaused",
	    "parametersSignature": "()",
	    "description": "Gets extractor pause status",
	    "parameters": [],
	    "returnDescription": "True if the extractor is paused, False if not"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isPaused", [])

def pause(status:bool) -> None:
	"""
	Changes the pause status of the extractor
	
	Parameters
	----------
	status:bool
		New pause satus
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "pause",
	    "parametersSignature": "(b)",
	    "description": "Changes the pause status of the extractor",
	    "parameters": [
	        {
	            "name": "status",
	            "description": "New pause satus"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "pause", [status])

def isProcessing() -> bool:
	"""
	Gets extractor running status
	
	Returns
	----------
	True if the extractor is currently processing images, False if not
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "b",
	    "name": "isProcessing",
	    "parametersSignature": "()",
	    "description": "Gets extractor running status",
	    "parameters": [],
	    "returnDescription": "True if the extractor is currently processing images, False if not"
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isProcessing", [])

def getMaximumDetectionRange() -> float:
	"""
	Gets the current maximum detection and tracking range.
	
	Returns
	----------
	Maximum range in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "f",
	    "name": "getMaximumDetectionRange",
	    "parametersSignature": "()",
	    "description": "Gets the current maximum detection and tracking range.",
	    "parameters": [],
	    "returnDescription": "Maximum range in meters."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMaximumDetectionRange", [])

def getMinimumBodyHeight() -> float:
	"""
	Gets the current minimum body height used for human detection (3D mode only).
	
	Returns
	----------
	Minimum height in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "f",
	    "name": "getMinimumBodyHeight",
	    "parametersSignature": "()",
	    "description": "Gets the current minimum body height used for human detection (3D mode only).",
	    "parameters": [],
	    "returnDescription": "Minimum height in meters."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMinimumBodyHeight", [])

def getMaximumBodyHeight() -> float:
	"""
	Gets the current maximum body height used for human detection (3D mode only).
	
	Returns
	----------
	Maximum height in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "f",
	    "name": "getMaximumBodyHeight",
	    "parametersSignature": "()",
	    "description": "Gets the current maximum body height used for human detection (3D mode only).",
	    "parameters": [],
	    "returnDescription": "Maximum height in meters."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getMaximumBodyHeight", [])

def getTimeBeforePersonDisappears() -> float:
	"""
	Gets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.
	
	Returns
	----------
	Time in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "f",
	    "name": "getTimeBeforePersonDisappears",
	    "parametersSignature": "()",
	    "description": "Gets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.",
	    "parameters": [],
	    "returnDescription": "Time in seconds."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getTimeBeforePersonDisappears", [])

def getTimeBeforeVisiblePersonDisappears() -> float:
	"""
	Gets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.
	
	Returns
	----------
	Time in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "f",
	    "name": "getTimeBeforeVisiblePersonDisappears",
	    "parametersSignature": "()",
	    "description": "Gets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.",
	    "parameters": [],
	    "returnDescription": "Time in seconds."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "getTimeBeforeVisiblePersonDisappears", [])

def isFaceDetectionEnabled() -> bool:
	"""
	Gets the current status of face detection.
	
	Returns
	----------
	True if face detection is enabled, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "isFaceDetectionEnabled",
	    "parametersSignature": "()",
	    "description": "Gets the current status of face detection.",
	    "parameters": [],
	    "returnDescription": "True if face detection is enabled, False otherwise."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isFaceDetectionEnabled", [])

def isFastModeEnabled() -> bool:
	"""
	Gets the current status of fast mode.
	
	Returns
	----------
	True if fast mode is enabled, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "isFastModeEnabled",
	    "parametersSignature": "()",
	    "description": "Gets the current status of fast mode.",
	    "parameters": [],
	    "returnDescription": "True if fast mode is enabled, False otherwise."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isFastModeEnabled", [])

def isGraphicalDisplayEnabled() -> bool:
	"""
	Gets the current status of graphical display in Choregraphe.
	
	Returns
	----------
	True if graphical display is enabled, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "b",
	    "name": "isGraphicalDisplayEnabled",
	    "parametersSignature": "()",
	    "description": "Gets the current status of graphical display in Choregraphe.",
	    "parameters": [],
	    "returnDescription": "True if graphical display is enabled, False otherwise."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isGraphicalDisplayEnabled", [])

def isMovementDetectionEnabled() -> bool:
	"""
	Gets the current status of movement detection in Choregraphe.
	
	Returns
	----------
	True if movement detection is enabled, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "b",
	    "name": "isMovementDetectionEnabled",
	    "parametersSignature": "()",
	    "description": "Gets the current status of movement detection in Choregraphe.",
	    "parameters": [],
	    "returnDescription": "True if movement detection is enabled, False otherwise."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "isMovementDetectionEnabled", [])

def resetPopulation() -> None:
	"""
	Empties the tracked population.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "resetPopulation",
	    "parametersSignature": "()",
	    "description": "Empties the tracked population.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "resetPopulation", [])

def setFastModeEnabled(enable:bool) -> None:
	"""
	Turns fast mode on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "setFastModeEnabled",
	    "parametersSignature": "(b)",
	    "description": "Turns fast mode on or off.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True to turn it on, False to turn it off."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setFastModeEnabled", [enable])

def setGraphicalDisplayEnabled(enable:bool) -> None:
	"""
	Turns graphical display in Choregraphe on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "setGraphicalDisplayEnabled",
	    "parametersSignature": "(b)",
	    "description": "Turns graphical display in Choregraphe on or off.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True to turn it on, False to turn it off."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setGraphicalDisplayEnabled", [enable])

def setMaximumDetectionRange(range:float) -> None:
	"""
	Sets the maximum range for human detection and tracking.
	
	Parameters
	----------
	range:float
		Maximum range in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "setMaximumDetectionRange",
	    "parametersSignature": "(f)",
	    "description": "Sets the maximum range for human detection and tracking.",
	    "parameters": [
	        {
	            "name": "range",
	            "description": "Maximum range in meters."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setMaximumDetectionRange", [range])

def setMinimumBodyHeight(height:float) -> None:
	"""
	Sets the minimum human body height (3D mode only).
	
	Parameters
	----------
	height:float
		Minimum height in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "setMinimumBodyHeight",
	    "parametersSignature": "(f)",
	    "description": "Sets the minimum human body height (3D mode only).",
	    "parameters": [
	        {
	            "name": "height",
	            "description": "Minimum height in meters."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setMinimumBodyHeight", [height])

def setMaximumBodyHeight(height:float) -> None:
	"""
	Sets the maximum human body height (3D mode only).
	
	Parameters
	----------
	height:float
		Maximum height in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "setMaximumBodyHeight",
	    "parametersSignature": "(f)",
	    "description": "Sets the maximum human body height (3D mode only).",
	    "parameters": [
	        {
	            "name": "height",
	            "description": "Maximum height in meters."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setMaximumBodyHeight", [height])

def setMovementDetectionEnabled(enable:bool) -> None:
	"""
	Turns movement detection on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "setMovementDetectionEnabled",
	    "parametersSignature": "(b)",
	    "description": "Turns movement detection on or off.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True to turn it on, False to turn it off."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setMovementDetectionEnabled", [enable])

def setTimeBeforePersonDisappears(seconds:float) -> None:
	"""
	Sets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.
	
	Parameters
	----------
	seconds:float
		Time in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "setTimeBeforePersonDisappears",
	    "parametersSignature": "(f)",
	    "description": "Sets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.",
	    "parameters": [
	        {
	            "name": "seconds",
	            "description": "Time in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setTimeBeforePersonDisappears", [seconds])

def setTimeBeforeVisiblePersonDisappears(seconds:float) -> None:
	"""
	Sets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.
	
	Parameters
	----------
	seconds:float
		Time in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "setTimeBeforeVisiblePersonDisappears",
	    "parametersSignature": "(f)",
	    "description": "Sets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.",
	    "parameters": [
	        {
	            "name": "seconds",
	            "description": "Time in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setTimeBeforeVisiblePersonDisappears", [seconds])

def _getDetectionMode() -> str:
	"""
	Gets the mode (2D/3D) used for the people detection.
	
	Returns
	----------
	Current mode.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "s",
	    "name": "_getDetectionMode",
	    "parametersSignature": "()",
	    "description": "Gets the mode (2D/3D) used for the people detection.",
	    "parameters": [],
	    "returnDescription": "Current mode."
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "_getDetectionMode", [])

def _setDetectionMode(mode:str) -> None:
	"""
	Sets the mode (2D/3D) used for the people detection.
	
	Parameters
	----------
	mode:str
		Mode to use.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "_setDetectionMode",
	    "parametersSignature": "(s)",
	    "description": "Sets the mode (2D/3D) used for the people detection.",
	    "parameters": [
	        {
	            "name": "mode",
	            "description": "Mode to use."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "_setDetectionMode", [mode])

def setFaceDetectionEnabled(enable:bool) -> None:
	"""
	Turns face detection on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "setFaceDetectionEnabled",
	    "parametersSignature": "(b)",
	    "description": "Turns face detection on or off.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True to turn it on, False to turn it off."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPeoplePerception", "setFaceDetectionEnabled", [enable])

