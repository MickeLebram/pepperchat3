from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module tries to detect emotions in the voice of the speaker.

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
	return send_mfc("ALVoiceEmotionAnalysis", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALVoiceEmotionAnalysis", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALVoiceEmotionAnalysis", "metaObject", [p0])

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
	return send_mfc("ALVoiceEmotionAnalysis", "terminate", [p0])

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
	return send_mfc("ALVoiceEmotionAnalysis", "property", [p0])

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
	return send_mfc("ALVoiceEmotionAnalysis", "setProperty", [p0, p1])

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
	return send_mfc("ALVoiceEmotionAnalysis", "properties", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALVoiceEmotionAnalysis", "isStatsEnabled", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "enableStats", [p0])

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
	return send_mfc("ALVoiceEmotionAnalysis", "stats", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "clearStats", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "isTraceEnabled", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "enableTrace", [p0])

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
	return send_mfc("ALVoiceEmotionAnalysis", "version", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "ping", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getMethodList", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getMethodHelp", [methodName])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getModuleHelp", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALVoiceEmotionAnalysis", "wait", [id])

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
	return send_mfc("ALVoiceEmotionAnalysis", "isRunning", [id])

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
	return send_mfc("ALVoiceEmotionAnalysis", "stop", [id])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getBrokerName", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getUsage", [name])

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
	return send_mfc("ALVoiceEmotionAnalysis", "subscribe", [name, period, precision])

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
	return send_mfc("ALVoiceEmotionAnalysis", "subscribe", [name])

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
	return send_mfc("ALVoiceEmotionAnalysis", "unsubscribe", [name])

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
	return send_mfc("ALVoiceEmotionAnalysis", "updatePeriod", [name, period])

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
	return send_mfc("ALVoiceEmotionAnalysis", "updatePrecision", [name, precision])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getCurrentPeriod", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getCurrentPrecision", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getMyPeriod", [name])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getMyPrecision", [name])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getSubscribersInfo", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getOutputNames", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getEventList", [])

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
	return send_mfc("ALVoiceEmotionAnalysis", "getMemoryKeyList", [])

def _onSpeechDetected(key:str, value:object) -> None:
	"""
	sound detected callback
	
	Parameters
	----------
	key:str
		ALMemory key.
	value:object
		ALValue of key.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_onSpeechDetected",
	    "parametersSignature": "(sm)",
	    "description": "sound detected callback",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "ALMemory key."
	        },
	        {
	            "name": "value",
	            "description": "ALValue of key."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVoiceEmotionAnalysis", "_onSpeechDetected", [key, value])

def setParameter(parameter:str, value:object) -> None:
	"""
	Set the specified parameter.
	
	Parameters
	----------
	parameter:str
		Name of the parameter. "MinSignalLength" Minimum length (in seconds, positive) required for the analysis of a voice signal
	value:object
		"MinSignalLength" : int > 0.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "setParameter",
	    "parametersSignature": "(sm)",
	    "description": "Set the specified parameter.",
	    "parameters": [
	        {
	            "name": "parameter",
	            "description": "Name of the parameter. \"MinSignalLength\" Minimum length (in seconds, positive) required for the analysis of a voice signal"
	        },
	        {
	            "name": "value",
	            "description": "\"MinSignalLength\" : int > 0."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVoiceEmotionAnalysis", "setParameter", [parameter, value])

