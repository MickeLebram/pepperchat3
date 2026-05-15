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
	return send_mfc("ALBasicAwareness", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALBasicAwareness", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALBasicAwareness", "metaObject", [p0])

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
	return send_mfc("ALBasicAwareness", "terminate", [p0])

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
	return send_mfc("ALBasicAwareness", "property", [p0])

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
	return send_mfc("ALBasicAwareness", "setProperty", [p0, p1])

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
	return send_mfc("ALBasicAwareness", "properties", [])

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
	return send_mfc("ALBasicAwareness", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALBasicAwareness", "isStatsEnabled", [])

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
	return send_mfc("ALBasicAwareness", "enableStats", [p0])

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
	return send_mfc("ALBasicAwareness", "stats", [])

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
	return send_mfc("ALBasicAwareness", "clearStats", [])

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
	return send_mfc("ALBasicAwareness", "isTraceEnabled", [])

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
	return send_mfc("ALBasicAwareness", "enableTrace", [p0])

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
	return send_mfc("ALBasicAwareness", "version", [])

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
	return send_mfc("ALBasicAwareness", "ping", [])

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
	return send_mfc("ALBasicAwareness", "getMethodList", [])

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
	return send_mfc("ALBasicAwareness", "getMethodHelp", [methodName])

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
	return send_mfc("ALBasicAwareness", "getModuleHelp", [])

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
	return send_mfc("ALBasicAwareness", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALBasicAwareness", "wait", [id])

def isRunning_1(id:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (isRunning)
	
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
	return send_mfc("ALBasicAwareness", "isRunning", [id])

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
	return send_mfc("ALBasicAwareness", "stop", [id])

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
	return send_mfc("ALBasicAwareness", "getBrokerName", [])

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
	return send_mfc("ALBasicAwareness", "getUsage", [name])

def _onPeopleDetected(name:str, populationUpdated:object, message:str) -> None:
	"""
	Population Updated (event: PeoplePerception/PopulationUpdated)
	
	Parameters
	----------
	name:str
		Name of the event
	populationUpdated:object
		Boolean value for people detection event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "_onPeopleDetected",
	    "parametersSignature": "(sms)",
	    "description": "Population Updated (event: PeoplePerception/PopulationUpdated)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "populationUpdated",
	            "description": "Boolean value for people detection event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onPeopleDetected", [name, populationUpdated, message])

def _onMovementDetected(name:str, movementDetected:object, message:str) -> None:
	"""
	Movement Detected (event: MovementDetection3D/MovementDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	movementDetected:object
		Boolean value for movement event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "_onMovementDetected",
	    "parametersSignature": "(sms)",
	    "description": "Movement Detected (event: MovementDetection3D/MovementDetected)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "movementDetected",
	            "description": "Boolean value for movement event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onMovementDetected", [name, movementDetected, message])

def _onNavigationMotionDetected(name:str, movementDetected:object, message:str) -> None:
	"""
	Navigation Motion Detected (event: Navigation/MotionDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	movementDetected:object
		Boolean value for movement event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_onNavigationMotionDetected",
	    "parametersSignature": "(sms)",
	    "description": "Navigation Motion Detected (event: Navigation/MotionDetected)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "movementDetected",
	            "description": "Boolean value for movement event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onNavigationMotionDetected", [name, movementDetected, message])

def _onCloseMovementDetected(name:str, closeMovementDetected:object, message:str) -> None:
	"""
	Close Movement Detected (event: WavingDetection/Waving)
	
	Parameters
	----------
	name:str
		Name of the event
	closeMovementDetected:object
		Boolean value for close movement event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_onCloseMovementDetected",
	    "parametersSignature": "(sms)",
	    "description": "Close Movement Detected (event: WavingDetection/Waving)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "closeMovementDetected",
	            "description": "Boolean value for close movement event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onCloseMovementDetected", [name, closeMovementDetected, message])

def _onSoundDetected(name:str, SoundLocated:object, message:str) -> None:
	"""
	Sound Detected (event: SoundLocated)
	
	Parameters
	----------
	name:str
		Name of the event
	SoundLocated:object
		Boolean value for movement event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_onSoundDetected",
	    "parametersSignature": "(sms)",
	    "description": "Sound Detected (event: SoundLocated)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "SoundLocated",
	            "description": "Boolean value for movement event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onSoundDetected", [name, SoundLocated, message])

def _onTouchDetected(name:str, touchDetected:object, message:str) -> None:
	"""
	Touch Detected (event: TouchDetection3D/TouchDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	touchDetected:object
		Boolean value for touch event
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "_onTouchDetected",
	    "parametersSignature": "(sms)",
	    "description": "Touch Detected (event: TouchDetection3D/TouchDetected)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "touchDetected",
	            "description": "Boolean value for touch event"
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onTouchDetected", [name, touchDetected, message])

def _onFastPersonTracking(name:str, tackerValue:object, message:str) -> None:
	"""
	Servoing event callback (event:ALTracker/FastPersonTracking)
	
	Parameters
	----------
	name:str
		Name of the event
	tackerValue:object
		Position to track.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "_onFastPersonTracking",
	    "parametersSignature": "(sms)",
	    "description": "Servoing event callback (event:ALTracker/FastPersonTracking)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "tackerValue",
	            "description": "Position to track."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onFastPersonTracking", [name, tackerValue, message])

def _onNoFastPersonFound(name:str, val:object, message:str) -> None:
	"""
	No person found by fast tracking callback (event:ALFastPersonTracking/TrackedPersonNotFound)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_onNoFastPersonFound",
	    "parametersSignature": "(sms)",
	    "description": "No person found by fast tracking callback (event:ALFastPersonTracking/TrackedPersonNotFound)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "val",
	            "description": "Content of the event."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onNoFastPersonFound", [name, val, message])

def _onHeadTracking(name:str, tackerValue:object, message:str) -> None:
	"""
	Servoing event callback (event:ALTracker/FindPersonHead)
	
	Parameters
	----------
	name:str
		Name of the event
	tackerValue:object
		Position to track.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "_onHeadTracking",
	    "parametersSignature": "(sms)",
	    "description": "Servoing event callback (event:ALTracker/FindPersonHead)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "tackerValue",
	            "description": "Position to track."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onHeadTracking", [name, tackerValue, message])

def _onHeadNotFound(name:str, val:object, message:str) -> None:
	"""
	HeadNotFound event callback (event:ALFindPersonHead/HeadNotFound)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_onHeadNotFound",
	    "parametersSignature": "(sms)",
	    "description": "HeadNotFound event callback (event:ALFindPersonHead/HeadNotFound)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "val",
	            "description": "Content of the event."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onHeadNotFound", [name, val, message])

def _onHeadReached(name:str, val:object, message:str) -> None:
	"""
	HeadReached event callback (event:ALFindPersonHead/HeadReached)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_onHeadReached",
	    "parametersSignature": "(sms)",
	    "description": "HeadReached event callback (event:ALFindPersonHead/HeadReached)",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "val",
	            "description": "Content of the event."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onHeadReached", [name, val, message])

def _onHeadTrackingStopped(name:str, val:object, message:str) -> None:
	"""
	tracking interruption
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_onHeadTrackingStopped",
	    "parametersSignature": "(sms)",
	    "description": "tracking interruption",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event"
	        },
	        {
	            "name": "val",
	            "description": "Content of the event."
	        },
	        {
	            "name": "message",
	            "description": "Event message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onHeadTrackingStopped", [name, val, message])

def setEnabled(enabled:bool) -> None:
	"""
	Enable/Disable BasicAwareness.
	
	Parameters
	----------
	enabled:bool
		True to enable BasicAwareness, False to disable BasicAwareness.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "setEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable/Disable BasicAwareness.",
	    "parameters": [
	        {
	            "name": "enabled",
	            "description": "True to enable BasicAwareness, False to disable BasicAwareness."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "setEnabled", [enabled])

def isEnabled() -> bool:
	"""
	Return whether BasicAwareness is enabled or not.
	
	Returns
	----------
	Boolean value, true if enabled else false
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "isEnabled",
	    "parametersSignature": "()",
	    "description": "Return whether BasicAwareness is enabled or not.",
	    "parameters": [],
	    "returnDescription": "Boolean value, true if enabled else false"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "isEnabled", [])

def isRunning_2() -> bool:
	"""
	Note: This is one of the overloads of the original method (isRunning)
	
	Return whether BasicAwareness is running.
	
	Returns
	----------
	Boolean value, true if running else false
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "isRunning",
	    "parametersSignature": "()",
	    "description": "Return whether BasicAwareness is running.",
	    "parameters": [],
	    "returnDescription": "Boolean value, true if running else false"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "isRunning", [])

def pauseAwareness() -> None:
	"""
	Pause BasicAwareness.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "pauseAwareness",
	    "parametersSignature": "()",
	    "description": "Pause BasicAwareness.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "pauseAwareness", [])

def resumeAwareness() -> None:
	"""
	Resume BasicAwareness.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "resumeAwareness",
	    "parametersSignature": "()",
	    "description": "Resume BasicAwareness.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "resumeAwareness", [])

def isAwarenessPaused() -> bool:
	"""
	Get the pause status of the module.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "b",
	    "name": "isAwarenessPaused",
	    "parametersSignature": "()",
	    "description": "Get the pause status of the module.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "isAwarenessPaused", [])

def setStimulusDetectionEnabled(stimulusName:str, isStimulusDetectionEnabled:bool) -> None:
	"""
	Enable/Disable Stimulus Detection.
	
	Parameters
	----------
	stimulusName:str
		Name of the stimulus to enable/disable
	isStimulusDetectionEnabled:bool
		Boolean value: true to enable, false to disable.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "setStimulusDetectionEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Enable/Disable Stimulus Detection.",
	    "parameters": [
	        {
	            "name": "stimulusName",
	            "description": "Name of the stimulus to enable/disable"
	        },
	        {
	            "name": "isStimulusDetectionEnabled",
	            "description": "Boolean value: true to enable, false to disable."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "setStimulusDetectionEnabled", [stimulusName, isStimulusDetectionEnabled])

def isStimulusDetectionEnabled(stimulusName:str) -> bool:
	"""
	Get status enabled/disabled for Stimulus Detection.
	
	Parameters
	----------
	stimulusName:str
		Name of the stimulus to check
	
	Returns
	----------
	Boolean value for status enabled/disabled
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "isStimulusDetectionEnabled",
	    "parametersSignature": "(s)",
	    "description": "Get status enabled/disabled for Stimulus Detection.",
	    "parameters": [
	        {
	            "name": "stimulusName",
	            "description": "Name of the stimulus to check"
	        }
	    ],
	    "returnDescription": "Boolean value for status enabled/disabled"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "isStimulusDetectionEnabled", [stimulusName])

def setParameter(paramName:str, newVal:object) -> None:
	"""
	Set the specified parameter 
	
	Parameters
	----------
	paramName:str
		"LookStimulusSpeed" : Speed of head moves when looking at a stimulus, as fraction of max speed
		 "LookBackSpeed" : Speed of head moves when looking back to previous position, as fraction of max speed
		 "NobodyFoundTimeOut" : timeout to send HumanLost event when no blob is found, in seconds
		 "MinTimeTracking" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds
		 "TimeSleepBeforeResumeMS" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds
		 "TimeOutResetHead" : Timeout to reset the head, in seconds
		 "AmplitudeYawTracking" : max absolute value for head yaw in tracking, in degrees
		 "PeoplePerceptionPeriod" : Period for people perception, in milliseconds
		 "SlowPeoplePerceptionPeriod" : Period for people perception in FullyEngaged mode, in milliseconds
		 "HeadThreshold" : Yaw threshold for tracking, in degrees
		 "BodyRotationThreshold" : Angular threshold for BodyRotation tracking mode, in degrees
		 "BodyRotationThresholdNao" : Angular threshold for BodyRotation tracking mode on Nao, in degrees
		 "MoveDistanceX" : X Distance for the Move tracking mode, in meters
		 "MoveDistanceY" : Y Distance for the Move tracking mode, in meters
		 "MoveAngleTheta" : Angle for the Move tracking mode, in degrees
		 "MoveThresholdX" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdY" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdTheta" : Theta Threshold for the Move tracking mode, in degrees
		 "MaxDistanceFullyEngaged" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters
		 "MaxDistanceNotFullyEngaged" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters
		 "MaxHumanSearchTime" : Maximum time to find a human after observing stimulus, in seconds
		 "DeltaPitchComfortZone" : Pitch width of the comfort zone, in degree
		 "CenterPitchComfortZone" : Pitch center of the confort zone, in degree
		 "SoundHeight" : Default Height for sound detection, in meters
		 "MoveSpeed" : Speed of the robot moves
		 "MC_Interactive_MinTime" : Minimum time between 2 contextual moves (when the robot is tracking somebody)
		 "MC_Interactive_MaxOffsetTime" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)
		 "MC_Interactive_DistanceXY" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody
		 "MC_Interactive_MinTheta" : Minimum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_MaxTheta" : Maximum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_DistanceHumanRobot" : Distance between the human and the robot
		 "MC_Interactive_MaxDistanceHumanRobot" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)
		 
	newVal:object
		"LookStimulusSpeed" : Float in range [0.01;1]
		 "LookBackSpeed" : Float in range [0.01;1]
		 "NobodyFoundTimeOut" : Float > 0
		 "MinTimeTracking" : Float in range [0;20]
		 "TimeSleepBeforeResumeMS" : Int > 0
		 "TimeOutResetHead" : Float in range [0;30]
		 "AmplitudeYawTracking" : Float in range [10;120]
		 "PeoplePerceptionPeriod" : Int > 1
		 "SlowPeoplePerceptionPeriod" : Int > 1
		 "HeadThreshold" : Float in range [0;180]
		 "BodyRotationThreshold" : Float in range [-180;180]
		 "BodyRotationThresholdNao" : Float in range [-180;180]
		 "MoveDistanceX" : Float in range [-5;5]
		 "MoveDistanceY" : Float in range [-5;5]
		 "MoveAngleTheta" : Float in range [-180;180]
		 "MoveThresholdX" : Float in range [0;5]
		 "MoveThresholdY" : Float in range [0;5]
		 "MoveThresholdTheta" : Float in range [-180;180]
		 "MaxDistanceFullyEngaged" : Float in range [0.5;5]
		 "MaxDistanceNotFullyEngaged" : Float in range [0.5;5]
		 "MaxHumanSearchTime" : Float in range [0.1;10]
		 "DeltaPitchComfortZone" : Float in range [0;90]
		 "CenterPitchComfortZone" : Float in range [-90;90]
		 "SoundHeight" : Float in range [0;2]
		 "MoveSpeed" : Float in range [0.1;0.55]
		 "MC_Interactive_MinTime" : Int in range [0;100]
		 "MC_Interactive_MaxOffsetTime" : Int in range [0;100]
		 "MC_Interactive_DistanceXY" : Float in range [0;1]
		 "MC_Interactive_MinTheta" : Float in range [-40;0]
		 "MC_Interactive_MaxTheta" : Float in range [0;40]
		 "MC_Interactive_DistanceHumanRobot" : Float in range [0.1;2]
		 "MC_Interactive_MaxDistanceHumanRobot" : Float in range [0.1;3]
		 
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "setParameter",
	    "parametersSignature": "(sm)",
	    "description": "Set the specified parameter ",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "\"LookStimulusSpeed\" : Speed of head moves when looking at a stimulus, as fraction of max speed\n \"LookBackSpeed\" : Speed of head moves when looking back to previous position, as fraction of max speed\n \"NobodyFoundTimeOut\" : timeout to send HumanLost event when no blob is found, in seconds\n \"MinTimeTracking\" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds\n \"TimeSleepBeforeResumeMS\" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds\n \"TimeOutResetHead\" : Timeout to reset the head, in seconds\n \"AmplitudeYawTracking\" : max absolute value for head yaw in tracking, in degrees\n \"PeoplePerceptionPeriod\" : Period for people perception, in milliseconds\n \"SlowPeoplePerceptionPeriod\" : Period for people perception in FullyEngaged mode, in milliseconds\n \"HeadThreshold\" : Yaw threshold for tracking, in degrees\n \"BodyRotationThreshold\" : Angular threshold for BodyRotation tracking mode, in degrees\n \"BodyRotationThresholdNao\" : Angular threshold for BodyRotation tracking mode on Nao, in degrees\n \"MoveDistanceX\" : X Distance for the Move tracking mode, in meters\n \"MoveDistanceY\" : Y Distance for the Move tracking mode, in meters\n \"MoveAngleTheta\" : Angle for the Move tracking mode, in degrees\n \"MoveThresholdX\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdY\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdTheta\" : Theta Threshold for the Move tracking mode, in degrees\n \"MaxDistanceFullyEngaged\" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters\n \"MaxDistanceNotFullyEngaged\" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters\n \"MaxHumanSearchTime\" : Maximum time to find a human after observing stimulus, in seconds\n \"DeltaPitchComfortZone\" : Pitch width of the comfort zone, in degree\n \"CenterPitchComfortZone\" : Pitch center of the confort zone, in degree\n \"SoundHeight\" : Default Height for sound detection, in meters\n \"MoveSpeed\" : Speed of the robot moves\n \"MC_Interactive_MinTime\" : Minimum time between 2 contextual moves (when the robot is tracking somebody)\n \"MC_Interactive_MaxOffsetTime\" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)\n \"MC_Interactive_DistanceXY\" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody\n \"MC_Interactive_MinTheta\" : Minimum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_MaxTheta\" : Maximum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_DistanceHumanRobot\" : Distance between the human and the robot\n \"MC_Interactive_MaxDistanceHumanRobot\" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)\n "
	        },
	        {
	            "name": "newVal",
	            "description": "\"LookStimulusSpeed\" : Float in range [0.01;1]\n \"LookBackSpeed\" : Float in range [0.01;1]\n \"NobodyFoundTimeOut\" : Float > 0\n \"MinTimeTracking\" : Float in range [0;20]\n \"TimeSleepBeforeResumeMS\" : Int > 0\n \"TimeOutResetHead\" : Float in range [0;30]\n \"AmplitudeYawTracking\" : Float in range [10;120]\n \"PeoplePerceptionPeriod\" : Int > 1\n \"SlowPeoplePerceptionPeriod\" : Int > 1\n \"HeadThreshold\" : Float in range [0;180]\n \"BodyRotationThreshold\" : Float in range [-180;180]\n \"BodyRotationThresholdNao\" : Float in range [-180;180]\n \"MoveDistanceX\" : Float in range [-5;5]\n \"MoveDistanceY\" : Float in range [-5;5]\n \"MoveAngleTheta\" : Float in range [-180;180]\n \"MoveThresholdX\" : Float in range [0;5]\n \"MoveThresholdY\" : Float in range [0;5]\n \"MoveThresholdTheta\" : Float in range [-180;180]\n \"MaxDistanceFullyEngaged\" : Float in range [0.5;5]\n \"MaxDistanceNotFullyEngaged\" : Float in range [0.5;5]\n \"MaxHumanSearchTime\" : Float in range [0.1;10]\n \"DeltaPitchComfortZone\" : Float in range [0;90]\n \"CenterPitchComfortZone\" : Float in range [-90;90]\n \"SoundHeight\" : Float in range [0;2]\n \"MoveSpeed\" : Float in range [0.1;0.55]\n \"MC_Interactive_MinTime\" : Int in range [0;100]\n \"MC_Interactive_MaxOffsetTime\" : Int in range [0;100]\n \"MC_Interactive_DistanceXY\" : Float in range [0;1]\n \"MC_Interactive_MinTheta\" : Float in range [-40;0]\n \"MC_Interactive_MaxTheta\" : Float in range [0;40]\n \"MC_Interactive_DistanceHumanRobot\" : Float in range [0.1;2]\n \"MC_Interactive_MaxDistanceHumanRobot\" : Float in range [0.1;3]\n "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "setParameter", [paramName, newVal])

def resetAllParameters() -> None:
	"""
	Reset all parameters, including enabled/disabled stimulus.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "resetAllParameters",
	    "parametersSignature": "()",
	    "description": "Reset all parameters, including enabled/disabled stimulus.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "resetAllParameters", [])

def getParameter(paramName:str) -> object:
	"""
	Get the specified parameter.
	
	Parameters
	----------
	paramName:str
		"LookStimulusSpeed" : Speed of head moves when looking at a stimulus, as fraction of max speed
		 "LookBackSpeed" : Speed of head moves when looking back to previous position, as fraction of max speed
		 "NobodyFoundTimeOut" : timeout to send HumanLost event when no blob is found, in seconds
		 "MinTimeTracking" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds
		 "TimeSleepBeforeResumeMS" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds
		 "TimeOutResetHead" : Timeout to reset the head, in seconds
		 "AmplitudeYawTracking" : max absolute value for head yaw in tracking, in degrees
		 "PeoplePerceptionPeriod" : Period for people perception, in milliseconds
		 "SlowPeoplePerceptionPeriod" : Period for people perception in FullyEngaged mode, in milliseconds
		 "HeadThreshold" : Yaw threshold for tracking, in degrees
		 "BodyRotationThreshold" : Angular threshold for BodyRotation tracking mode, in degrees
		 "BodyRotationThresholdNao" : Angular threshold for BodyRotation tracking mode on Nao, in degrees
		 "MoveDistanceX" : X Distance for the Move tracking mode, in meters
		 "MoveDistanceY" : Y Distance for the Move tracking mode, in meters
		 "MoveAngleTheta" : Angle for the Move tracking mode, in degrees
		 "MoveThresholdX" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdY" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdTheta" : Theta Threshold for the Move tracking mode, in degrees
		 "MaxDistanceFullyEngaged" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters
		 "MaxDistanceNotFullyEngaged" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters
		 "MaxHumanSearchTime" : Maximum time to find a human after observing stimulus, in seconds
		 "DeltaPitchComfortZone" : Pitch width of the comfort zone, in degree
		 "CenterPitchComfortZone" : Pitch center of the confort zone, in degree
		 "SoundHeight" : Default Height for sound detection, in meters
		 "MoveSpeed" : Speed of the robot moves
		 "MC_Interactive_MinTime" : Minimum time between 2 contextual moves (when the robot is tracking somebody)
		 "MC_Interactive_MaxOffsetTime" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)
		 "MC_Interactive_DistanceXY" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody
		 "MC_Interactive_MinTheta" : Minimum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_MaxTheta" : Maximum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_DistanceHumanRobot" : Distance between the human and the robot
		 "MC_Interactive_MaxDistanceHumanRobot" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)
		 
	
	Returns
	----------
	ALValue format for required parameter
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "m",
	    "name": "getParameter",
	    "parametersSignature": "(s)",
	    "description": "Get the specified parameter.",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "\"LookStimulusSpeed\" : Speed of head moves when looking at a stimulus, as fraction of max speed\n \"LookBackSpeed\" : Speed of head moves when looking back to previous position, as fraction of max speed\n \"NobodyFoundTimeOut\" : timeout to send HumanLost event when no blob is found, in seconds\n \"MinTimeTracking\" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds\n \"TimeSleepBeforeResumeMS\" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds\n \"TimeOutResetHead\" : Timeout to reset the head, in seconds\n \"AmplitudeYawTracking\" : max absolute value for head yaw in tracking, in degrees\n \"PeoplePerceptionPeriod\" : Period for people perception, in milliseconds\n \"SlowPeoplePerceptionPeriod\" : Period for people perception in FullyEngaged mode, in milliseconds\n \"HeadThreshold\" : Yaw threshold for tracking, in degrees\n \"BodyRotationThreshold\" : Angular threshold for BodyRotation tracking mode, in degrees\n \"BodyRotationThresholdNao\" : Angular threshold for BodyRotation tracking mode on Nao, in degrees\n \"MoveDistanceX\" : X Distance for the Move tracking mode, in meters\n \"MoveDistanceY\" : Y Distance for the Move tracking mode, in meters\n \"MoveAngleTheta\" : Angle for the Move tracking mode, in degrees\n \"MoveThresholdX\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdY\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdTheta\" : Theta Threshold for the Move tracking mode, in degrees\n \"MaxDistanceFullyEngaged\" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters\n \"MaxDistanceNotFullyEngaged\" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters\n \"MaxHumanSearchTime\" : Maximum time to find a human after observing stimulus, in seconds\n \"DeltaPitchComfortZone\" : Pitch width of the comfort zone, in degree\n \"CenterPitchComfortZone\" : Pitch center of the confort zone, in degree\n \"SoundHeight\" : Default Height for sound detection, in meters\n \"MoveSpeed\" : Speed of the robot moves\n \"MC_Interactive_MinTime\" : Minimum time between 2 contextual moves (when the robot is tracking somebody)\n \"MC_Interactive_MaxOffsetTime\" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)\n \"MC_Interactive_DistanceXY\" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody\n \"MC_Interactive_MinTheta\" : Minimum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_MaxTheta\" : Maximum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_DistanceHumanRobot\" : Distance between the human and the robot\n \"MC_Interactive_MaxDistanceHumanRobot\" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)\n "
	        }
	    ],
	    "returnDescription": "ALValue format for required parameter"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "getParameter", [paramName])

def setEngagementMode(modeName:str) -> None:
	"""
	Set engagement mode.
	
	Parameters
	----------
	modeName:str
		Name of the mode
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "setEngagementMode",
	    "parametersSignature": "(s)",
	    "description": "Set engagement mode.",
	    "parameters": [
	        {
	            "name": "modeName",
	            "description": "Name of the mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "setEngagementMode", [modeName])

def getEngagementMode() -> str:
	"""
	Set engagement mode.
	
	Returns
	----------
	Name of current engagement mode as a string
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "s",
	    "name": "getEngagementMode",
	    "parametersSignature": "()",
	    "description": "Set engagement mode.",
	    "parameters": [],
	    "returnDescription": "Name of current engagement mode as a string"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "getEngagementMode", [])

def _setCustomEngagementMode(checkStimWhenFocused:bool, stimuliWhenNotTracking:List[str], stimuliWhenTracking:List[str]) -> None:
	"""
	Set engagement mode.
	
	Parameters
	----------
	checkStimWhenFocused:bool
		when it is tracking someone, true makes the robot check a stimulus to see if it corresponds to a human, false makes it go back to the current track human just after watching in the stim direction (as in SemiEngaged mode)
	stimuliWhenNotTracking:List[str]
		stimuli enabled when the robot is tracking, as a stimuli names list
	stimuliWhenTracking:List[str]
		stimuli enabled when the robot is not tracking, as a stimuli names list
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_setCustomEngagementMode",
	    "parametersSignature": "(b[s][s])",
	    "description": "Set engagement mode.",
	    "parameters": [
	        {
	            "name": "checkStimWhenFocused",
	            "description": "when it is tracking someone, true makes the robot check a stimulus to see if it corresponds to a human, false makes it go back to the current track human just after watching in the stim direction (as in SemiEngaged mode)"
	        },
	        {
	            "name": "stimuliWhenNotTracking",
	            "description": "stimuli enabled when the robot is tracking, as a stimuli names list"
	        },
	        {
	            "name": "stimuliWhenTracking",
	            "description": "stimuli enabled when the robot is not tracking, as a stimuli names list"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_setCustomEngagementMode", [checkStimWhenFocused, stimuliWhenNotTracking, stimuliWhenTracking])

def setTrackingMode(modeName:str) -> None:
	"""
	Set tracking mode.
	
	Parameters
	----------
	modeName:str
		Name of the mode
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "setTrackingMode",
	    "parametersSignature": "(s)",
	    "description": "Set tracking mode.",
	    "parameters": [
	        {
	            "name": "modeName",
	            "description": "Name of the mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "setTrackingMode", [modeName])

def getTrackingMode() -> str:
	"""
	Set tracking mode.
	
	Returns
	----------
	Name of current tracking mode as a string
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "s",
	    "name": "getTrackingMode",
	    "parametersSignature": "()",
	    "description": "Set tracking mode.",
	    "parameters": [],
	    "returnDescription": "Name of current tracking mode as a string"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "getTrackingMode", [])

def engagePerson(engagePerson:int) -> bool:
	"""
	Force Engage Person.
	
	Parameters
	----------
	engagePerson:int
		ID of the person as found in PeoplePerception.
	
	Returns
	----------
	true if the robot succeeded to engage the person, else false.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "b",
	    "name": "engagePerson",
	    "parametersSignature": "(i)",
	    "description": "Force Engage Person.",
	    "parameters": [
	        {
	            "name": "engagePerson",
	            "description": "ID of the person as found in PeoplePerception."
	        }
	    ],
	    "returnDescription": "true if the robot succeeded to engage the person, else false."
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "engagePerson", [engagePerson])

def _setContextualMoveType(contextualMove:str) -> None:
	"""
	Set a new contextual moves type.
	
	Parameters
	----------
	contextualMove:str
		The contextual move, can be 'forward', 'backward', 'sides' and 'random'.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "_setContextualMoveType",
	    "parametersSignature": "(s)",
	    "description": "Set a new contextual moves type.",
	    "parameters": [
	        {
	            "name": "contextualMove",
	            "description": "The contextual move, can be 'forward', 'backward', 'sides' and 'random'."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_setContextualMoveType", [contextualMove])

def triggerStimulus(stimulusPosition:List[float]) -> int:
	"""
	Trigger a custom stimulus.
	
	Parameters
	----------
	stimulusPosition:List[float]
		Position of the stimulus, in Frame World
	
	Returns
	----------
	If someone was found, return value is its ID, else it's -1
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "i",
	    "name": "triggerStimulus",
	    "parametersSignature": "([f])",
	    "description": "Trigger a custom stimulus.",
	    "parameters": [
	        {
	            "name": "stimulusPosition",
	            "description": "Position of the stimulus, in Frame World"
	        }
	    ],
	    "returnDescription": "If someone was found, return value is its ID, else it's -1"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "triggerStimulus", [stimulusPosition])

def _useLedDebug(useLeds:bool) -> None:
	"""
	Use leds for debug
	
	Parameters
	----------
	useLeds:bool
		Boolean value: true to use leds.
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_useLedDebug",
	    "parametersSignature": "(b)",
	    "description": "Use leds for debug",
	    "parameters": [
	        {
	            "name": "useLeds",
	            "description": "Boolean value: true to use leds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_useLedDebug", [useLeds])

def _setLedGroup(ledGroupName:str) -> None:
	"""
	Set Led group
	
	Parameters
	----------
	ledGroupName:str
		Name of the led group.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "_setLedGroup",
	    "parametersSignature": "(s)",
	    "description": "Set Led group",
	    "parameters": [
	        {
	            "name": "ledGroupName",
	            "description": "Name of the led group."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_setLedGroup", [ledGroupName])

def _displayRobotViewDebug(useDisplay:bool) -> None:
	"""
	Use debug display in robot view
	
	Parameters
	----------
	useDisplay:bool
		Boolean value: true to use debug display in robot view.
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "v",
	    "name": "_displayRobotViewDebug",
	    "parametersSignature": "(b)",
	    "description": "Use debug display in robot view",
	    "parameters": [
	        {
	            "name": "useDisplay",
	            "description": "Boolean value: true to use debug display in robot view."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_displayRobotViewDebug", [useDisplay])

def _getParametersInfo() -> str:
	"""
	Get parameters documentation
	
	Returns
	----------
	Parameters info as string
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "s",
	    "name": "_getParametersInfo",
	    "parametersSignature": "()",
	    "description": "Get parameters documentation",
	    "parameters": [],
	    "returnDescription": "Parameters info as string"
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_getParametersInfo", [])

def _setEnableStimuliFromBehind(enable:bool) -> None:
	"""
	Allow the robot to detect stimuli coming from behind and to turnthe base up to 180 degrees to watch them. If it's disabled, thestimuli from behind won't be taken into account.
	
	Parameters
	----------
	enable:bool
		true to enable, false to disable
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "_setEnableStimuliFromBehind",
	    "parametersSignature": "(b)",
	    "description": "Allow the robot to detect stimuli coming from behind and to turnthe base up to 180 degrees to watch them. If it's disabled, thestimuli from behind won't be taken into account.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "true to enable, false to disable"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_setEnableStimuliFromBehind", [enable])

def _getEnableStimuliFromBehind() -> bool:
	"""
	To know if the robot can detect stimuli from behind
	
	Returns
	----------
	Boolean value: true if stimuli from behind are enabled, else false.
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "b",
	    "name": "_getEnableStimuliFromBehind",
	    "parametersSignature": "()",
	    "description": "To know if the robot can detect stimuli from behind",
	    "parameters": [],
	    "returnDescription": "Boolean value: true if stimuli from behind are enabled, else false."
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_getEnableStimuliFromBehind", [])

def _setEnableCheckLowStimuli(enable:bool) -> None:
	"""
	Allow the robot to check downwards for low stimuli if nobody's found.
	
	Parameters
	----------
	enable:bool
		true to enable, false to disable
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_setEnableCheckLowStimuli",
	    "parametersSignature": "(b)",
	    "description": "Allow the robot to check downwards for low stimuli if nobody's found.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "true to enable, false to disable"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_setEnableCheckLowStimuli", [enable])

def _getEnableCheckLowStimuli() -> bool:
	"""
	To know if the robot can detect stimuli from behind
	
	Returns
	----------
	Boolean value: true if low stimuli are enabled, else false.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "b",
	    "name": "_getEnableCheckLowStimuli",
	    "parametersSignature": "()",
	    "description": "To know if the robot can detect stimuli from behind",
	    "parameters": [],
	    "returnDescription": "Boolean value: true if low stimuli are enabled, else false."
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_getEnableCheckLowStimuli", [])

def _getHomeReferencePosition() -> List[float]:
	"""
	Get the position of home
	
	Returns
	----------
	Pose2D as vector: Pose2D of home.
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "[f]",
	    "name": "_getHomeReferencePosition",
	    "parametersSignature": "()",
	    "description": "Get the position of home",
	    "parameters": [],
	    "returnDescription": "Pose2D as vector: Pose2D of home."
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_getHomeReferencePosition", [])

def _onPreferenceUpdated(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "v",
	    "name": "_onPreferenceUpdated",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onPreferenceUpdated", [p1, p2, p3])

def _onPreferenceSynchronized(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "v",
	    "name": "_onPreferenceSynchronized",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBasicAwareness", "_onPreferenceSynchronized", [p1, p2, p3])

