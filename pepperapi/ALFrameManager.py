from .gentypes import *
from .robot_client import send_mfc
import json
"""
Frame manager is used to play choregraphe projects in naoqi. It needs Choregraphe projects in input and will return an ID for each project. It can also only read a given box/timeline in a complex behavior.
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
	return send_mfc("ALFrameManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALFrameManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALFrameManager", "metaObject", [p0])

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
	return send_mfc("ALFrameManager", "terminate", [p0])

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
	return send_mfc("ALFrameManager", "property", [p0])

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
	return send_mfc("ALFrameManager", "setProperty", [p0, p1])

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
	return send_mfc("ALFrameManager", "properties", [])

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
	return send_mfc("ALFrameManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALFrameManager", "isStatsEnabled", [])

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
	return send_mfc("ALFrameManager", "enableStats", [p0])

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
	return send_mfc("ALFrameManager", "stats", [])

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
	return send_mfc("ALFrameManager", "clearStats", [])

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
	return send_mfc("ALFrameManager", "isTraceEnabled", [])

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
	return send_mfc("ALFrameManager", "enableTrace", [p0])

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
	return send_mfc("ALFrameManager", "version", [])

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
	return send_mfc("ALFrameManager", "ping", [])

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
	return send_mfc("ALFrameManager", "getMethodList", [])

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
	return send_mfc("ALFrameManager", "getMethodHelp", [methodName])

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
	return send_mfc("ALFrameManager", "getModuleHelp", [])

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
	return send_mfc("ALFrameManager", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALFrameManager", "wait", [id])

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
	return send_mfc("ALFrameManager", "isRunning", [id])

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
	return send_mfc("ALFrameManager", "stop", [id])

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
	return send_mfc("ALFrameManager", "getBrokerName", [])

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
	return send_mfc("ALFrameManager", "getUsage", [name])

def createBehavior(packageDir:str, behaviorPath:str, behName:str) -> str:
	"""
	Creates a new behavior, from a box found in an xml file stored in the robot.
	
	Parameters
	----------
	packageDir:str
		 the base directory of the behavior's package, eg: "/home/myApp".
	behaviorPath:str
		the relative path of the behavior inside the package, eg: "/behavior_1/behavior.xar".
	behName:str
		
	
	Returns
	----------
	return a unique identifier for the created box, that can be used by playBehavior
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "s",
	    "name": "createBehavior",
	    "parametersSignature": "(sss)",
	    "description": "Creates a new behavior, from a box found in an xml file stored in the robot.",
	    "parameters": [
	        {
	            "name": "packageDir",
	            "description": " the base directory of the behavior's package, eg: \"/home/myApp\"."
	        },
	        {
	            "name": "behaviorPath",
	            "description": "the relative path of the behavior inside the package, eg: \"/behavior_1/behavior.xar\"."
	        },
	        {
	            "name": "behName",
	            "description": ""
	        }
	    ],
	    "returnDescription": "return a unique identifier for the created box, that can be used by playBehavior"
	}
	'''
	"""
	return send_mfc("ALFrameManager", "createBehavior", [packageDir, behaviorPath, behName])

def completeBehavior(id:str) -> None:
	"""
	It will play a behavior and block until the behavior is finished. Note that it can block forever if the behavior output is never called.
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "completeBehavior",
	    "parametersSignature": "(s)",
	    "description": "It will play a behavior and block until the behavior is finished. Note that it can block forever if the behavior output is never called.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the box (the box URI)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "completeBehavior", [id])

def deleteBehavior(id:str) -> None:
	"""
	Deletes a behavior (meaning a box). Stop the whole behavior contained in this box first.
	
	Parameters
	----------
	id:str
		The id of the box to delete (the box URI).
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "deleteBehavior",
	    "parametersSignature": "(s)",
	    "description": "Deletes a behavior (meaning a box). Stop the whole behavior contained in this box first.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the box to delete (the box URI)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "deleteBehavior", [id])

def playBehavior(id:str) -> None:
	"""
	Starts a behavior
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "playBehavior",
	    "parametersSignature": "(s)",
	    "description": "Starts a behavior",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the box (the box URI)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "playBehavior", [id])

def exitBehavior(id:str) -> None:
	"""
	Exit the reading of a timeline contained in a given box
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "exitBehavior",
	    "parametersSignature": "(s)",
	    "description": "Exit the reading of a timeline contained in a given box",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the box (the box URI)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "exitBehavior", [id])

def isBehaviorRunning(id:str) -> bool:
	"""
	Tells whether the behavior is running
	
	Parameters
	----------
	id:str
		The id of the behavior to check (The URI of the root box).
	
	Returns
	----------
	True if the behavior is running, false otherwise
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "isBehaviorRunning",
	    "parametersSignature": "(s)",
	    "description": "Tells whether the behavior is running",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the behavior to check (The URI of the root box)."
	        }
	    ],
	    "returnDescription": "True if the behavior is running, false otherwise"
	}
	'''
	"""
	return send_mfc("ALFrameManager", "isBehaviorRunning", [id])

def cleanBehaviors() -> None:
	"""
	Stop playing any behavior in FrameManager, and delete all of them.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "cleanBehaviors",
	    "parametersSignature": "()",
	    "description": "Stop playing any behavior in FrameManager, and delete all of them.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "cleanBehaviors", [])

def getBehaviorPath(id:str) -> str:
	"""
	Returns a playing behavior absolute path.
	
	Parameters
	----------
	id:str
		The id of the behavior (The URI of the root box).
	
	Returns
	----------
	Returns the absolute path of given behavior.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "s",
	    "name": "getBehaviorPath",
	    "parametersSignature": "(s)",
	    "description": "Returns a playing behavior absolute path.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The id of the behavior (The URI of the root box)."
	        }
	    ],
	    "returnDescription": "Returns the absolute path of given behavior."
	}
	'''
	"""
	return send_mfc("ALFrameManager", "getBehaviorPath", [id])

def createTimeline(timelineContent:str) -> str:
	"""
	Creates a timeline.
	
	Parameters
	----------
	timelineContent:str
		The timeline content (in XML format).
	
	Returns
	----------
	return a unique identifier for the created box that contains the timeline. You must call deleteBehavior on it at some point. DEPRECATED since 1.14
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "s",
	    "name": "createTimeline",
	    "parametersSignature": "(s)",
	    "description": "Creates a timeline.",
	    "parameters": [
	        {
	            "name": "timelineContent",
	            "description": "The timeline content (in XML format)."
	        }
	    ],
	    "returnDescription": "return a unique identifier for the created box that contains the timeline. You must call deleteBehavior on it at some point. DEPRECATED since 1.14"
	}
	'''
	"""
	return send_mfc("ALFrameManager", "createTimeline", [timelineContent])

def behaviors() -> List[str]:
	"""
	List all behaviors currently handled by the frame manager.
	
	Returns
	----------
	a set listing all behavior ids
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[s]",
	    "name": "behaviors",
	    "parametersSignature": "()",
	    "description": "List all behaviors currently handled by the frame manager.",
	    "parameters": [],
	    "returnDescription": "a set listing all behavior ids"
	}
	'''
	"""
	return send_mfc("ALFrameManager", "behaviors", [])

def _dataChanged(dataName:str, data:object, message:str) -> None:
	"""
	Called by ALMemory when subcription data is updated. INTERNAL
	
	Parameters
	----------
	dataName:str
		Name of the subscribed data.
	data:object
		Value of the the subscribed data
	message:str
		The message give when subscribing.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "_dataChanged",
	    "parametersSignature": "(sms)",
	    "description": "Called by ALMemory when subcription data is updated. INTERNAL",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "Name of the subscribed data."
	        },
	        {
	            "name": "data",
	            "description": "Value of the the subscribed data"
	        },
	        {
	            "name": "message",
	            "description": "The message give when subscribing."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_dataChanged", [dataName, data, message])

def _subscribeBoxToEvent(eventName:str, boxName:str, message:str, callback:str, micro:bool) -> None:
	"""
	method called by almemory to inform framemanager that a box is subscribing to an event
	
	Parameters
	----------
	eventName:str
		the name of the event
	boxName:str
		the name of the box requesting it (the URI of the box).
	message:str
		the associated message
	callback:str
		the name of the box's callback to call
	micro:bool
		true if the subscription is to a micro event
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_subscribeBoxToEvent",
	    "parametersSignature": "(ssssb)",
	    "description": "method called by almemory to inform framemanager that a box is subscribing to an event",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "the name of the event"
	        },
	        {
	            "name": "boxName",
	            "description": "the name of the box requesting it (the URI of the box)."
	        },
	        {
	            "name": "message",
	            "description": "the associated message"
	        },
	        {
	            "name": "callback",
	            "description": "the name of the box's callback to call"
	        },
	        {
	            "name": "micro",
	            "description": "true if the subscription is to a micro event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_subscribeBoxToEvent", [eventName, boxName, message, callback, micro])

def _unsubscribeBoxToEvent(eventName:str, boxName:str, micro:bool) -> None:
	"""
	method called by almemory to inform framemanager that a box is unsubscribing from an event
	
	Parameters
	----------
	eventName:str
		the name of the event
	boxName:str
		the name of the box requesting it (the URI of the box).
	micro:bool
		true if the subscription is to a micro event
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_unsubscribeBoxToEvent",
	    "parametersSignature": "(ssb)",
	    "description": "method called by almemory to inform framemanager that a box is unsubscribing from an event",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "the name of the event"
	        },
	        {
	            "name": "boxName",
	            "description": "the name of the box requesting it (the URI of the box)."
	        },
	        {
	            "name": "micro",
	            "description": "true if the subscription is to a micro event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_unsubscribeBoxToEvent", [eventName, boxName, micro])

def _boxDataChanged(eventName:str, value:object, message:str) -> None:
	"""
	
	
	Parameters
	----------
	eventName:str
		
	value:object
		
	message:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_boxDataChanged",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": ""
	        },
	        {
	            "name": "value",
	            "description": ""
	        },
	        {
	            "name": "message",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_boxDataChanged", [eventName, value, message])

def _startBenchmark() -> None:
	"""
	Start recording some performance data.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_startBenchmark",
	    "parametersSignature": "()",
	    "description": "Start recording some performance data.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_startBenchmark", [])

def _stopBenchmark() -> str:
	"""
	Stop performance data recording, and return a summary.
	
	Returns
	----------
	Returns a textual report of the recorded performance data.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "s",
	    "name": "_stopBenchmark",
	    "parametersSignature": "()",
	    "description": "Stop performance data recording, and return a summary.",
	    "parameters": [],
	    "returnDescription": "Returns a textual report of the recorded performance data."
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_stopBenchmark", [])

def _newBoxFromFile(xmlFilePath:str, path:str) -> str:
	"""
	Creates a new box found in an xml file stored in the robot, without loading it, and without auto-delete on stop. (used by link box)
	
	Parameters
	----------
	xmlFilePath:str
		Path to Xml file, ex : "/home/youhou/mybehavior.xar".
	path:str
		The path to reach the box to instantiate in the project ("" if root).
	
	Returns
	----------
	return a unique identifier for the created box (the URI of the box), that can be used by playBehavior
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "s",
	    "name": "_newBoxFromFile",
	    "parametersSignature": "(ss)",
	    "description": "Creates a new box found in an xml file stored in the robot, without loading it, and without auto-delete on stop. (used by link box)",
	    "parameters": [
	        {
	            "name": "xmlFilePath",
	            "description": "Path to Xml file, ex : \"/home/youhou/mybehavior.xar\"."
	        },
	        {
	            "name": "path",
	            "description": "The path to reach the box to instantiate in the project (\"\" if root)."
	        }
	    ],
	    "returnDescription": "return a unique identifier for the created box (the URI of the box), that can be used by playBehavior"
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_newBoxFromFile", [xmlFilePath, path])

def _waitForStopped(fmid:str) -> None:
	"""
	wait for a previously started behavior is stopped
	
	Parameters
	----------
	fmid:str
		the unique identifier of the behavior to wait for (the URI of the root box)
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_waitForStopped",
	    "parametersSignature": "(s)",
	    "description": "wait for a previously started behavior is stopped",
	    "parameters": [
	        {
	            "name": "fmid",
	            "description": "the unique identifier of the behavior to wait for (the URI of the root box)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_waitForStopped", [fmid])

def _onPreferenceUpdated(key:str, value:object, message:str) -> None:
	"""
	callback for changes in the preference manager
	
	Parameters
	----------
	key:str
		ignored, used by ALMemory
	value:object
		the domain and the key of the preference that changed
	message:str
		ignored, used by ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "_onPreferenceUpdated",
	    "parametersSignature": "(sms)",
	    "description": "callback for changes in the preference manager",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "ignored, used by ALMemory"
	        },
	        {
	            "name": "value",
	            "description": "the domain and the key of the preference that changed"
	        },
	        {
	            "name": "message",
	            "description": "ignored, used by ALMemory"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_onPreferenceUpdated", [key, value, message])

def _onPreferencesSynchronized(key:str, value:object, message:str) -> None:
	"""
	callback for changes in the preference manager
	
	Parameters
	----------
	key:str
		ignored, used by ALMemory
	value:object
		the domain and the key of the preference that changed
	message:str
		ignored, used by ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "_onPreferencesSynchronized",
	    "parametersSignature": "(sms)",
	    "description": "callback for changes in the preference manager",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "ignored, used by ALMemory"
	        },
	        {
	            "name": "value",
	            "description": "the domain and the key of the preference that changed"
	        },
	        {
	            "name": "message",
	            "description": "ignored, used by ALMemory"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_onPreferencesSynchronized", [key, value, message])

def _reportError(fmid:str, boxid:str, error:str) -> None:
	"""
	called by behaviors when an error occured
	
	Parameters
	----------
	fmid:str
		the unique identifier of the behavior that failed (the URI of the root box)
	boxid:str
		the identifier of the box that failed (the URI of the box).
	error:str
		the error message
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "_reportError",
	    "parametersSignature": "(sss)",
	    "description": "called by behaviors when an error occured",
	    "parameters": [
	        {
	            "name": "fmid",
	            "description": "the unique identifier of the behavior that failed (the URI of the root box)"
	        },
	        {
	            "name": "boxid",
	            "description": "the identifier of the box that failed (the URI of the box)."
	        },
	        {
	            "name": "error",
	            "description": "the error message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "_reportError", [fmid, boxid, error])

def getBehaviorDebuggerFor(behavior:str) -> object:
	"""
	get an object tracking transitions in a behavior
	
	Parameters
	----------
	behavior:str
		name of the behavior (the URI of the root box)
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "o",
	    "name": "getBehaviorDebuggerFor",
	    "parametersSignature": "(s)",
	    "description": "get an object tracking transitions in a behavior",
	    "parameters": [
	        {
	            "name": "behavior",
	            "description": "name of the behavior (the URI of the root box)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "getBehaviorDebuggerFor", [behavior])

def getBox(box:str) -> object:
	"""
	get a box as an object
	
	Parameters
	----------
	box:str
		name of the box (the URI of the box).
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "o",
	    "name": "getBox",
	    "parametersSignature": "(s)",
	    "description": "get a box as an object",
	    "parameters": [
	        {
	            "name": "box",
	            "description": "name of the box (the URI of the box)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "getBox", [box])

def callBoxInput_1(box:str, method:str, arg:object) -> object:
	"""
	Note: This is one of the overloads of the original method (callBoxInput)
	
	call an input on a box
	
	Parameters
	----------
	box:str
		name of the box (the URI of the box).
	method:str
		name of the method
	arg:object
		input argument
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "m",
	    "name": "callBoxInput",
	    "parametersSignature": "(ssm)",
	    "description": "call an input on a box",
	    "parameters": [
	        {
	            "name": "box",
	            "description": "name of the box (the URI of the box)."
	        },
	        {
	            "name": "method",
	            "description": "name of the method"
	        },
	        {
	            "name": "arg",
	            "description": "input argument"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "callBoxInput", [box, method, arg])

def callBoxInput_2(box:str, method:str, arg1:object, arg2:object) -> object:
	"""
	Note: This is one of the overloads of the original method (callBoxInput)
	
	call an input on a box
	
	Parameters
	----------
	box:str
		name of the box (the URI of the box). A box URI is of the format 'behavior_name:/diagram_1/box_2'
	method:str
		name of the method
	arg1:object
		input argument
	arg2:object
		input argument
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "m",
	    "name": "callBoxInput",
	    "parametersSignature": "(ssmm)",
	    "description": "call an input on a box",
	    "parameters": [
	        {
	            "name": "box",
	            "description": "name of the box (the URI of the box). A box URI is of the format 'behavior_name:/diagram_1/box_2'"
	        },
	        {
	            "name": "method",
	            "description": "name of the method"
	        },
	        {
	            "name": "arg1",
	            "description": "input argument"
	        },
	        {
	            "name": "arg2",
	            "description": "input argument"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFrameManager", "callBoxInput", [box, method, arg1, arg2])

