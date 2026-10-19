"""
Frame manager is used to play choregraphe projects in naoqi. It needs Choregraphe projects in input and will return an ID for each project. It can also only read a given box/timeline in a complex behavior.
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def version() -> str:
	"""
	Returns the version of the module.
	
	Returns
	----------
	A string containing the version of the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "s",
	#     "name": "version",
	#     "parametersSignature": "()",
	#     "description": "Returns the version of the module.",
	#     "parameters": [],
	#     "returnDescription": "A string containing the version of the module."
	# }
	return call_method("ALFrameManager", "version", [])

def ping() -> bool:
	"""
	Just a ping. Always returns true
	
	Returns
	----------
	returns true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "ping",
	#     "parametersSignature": "()",
	#     "description": "Just a ping. Always returns true",
	#     "parameters": [],
	#     "returnDescription": "returns true"
	# }
	return call_method("ALFrameManager", "ping", [])

def getMethodList() -> List[str]:
	"""
	Retrieves the module's method list.
	
	Returns
	----------
	An array of method names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[s]",
	#     "name": "getMethodList",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's method list.",
	#     "parameters": [],
	#     "returnDescription": "An array of method names."
	# }
	return call_method("ALFrameManager", "getMethodList", [])

def getMethodHelp(methodName:str) -> Any:
	"""
	Retrieves a method's description.
	
	Parameters
	----------
	methodName:str
		The name of the method.
	
	Returns
	----------
	A structure containing the method's description.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "m",
	#     "name": "getMethodHelp",
	#     "parametersSignature": "(s)",
	#     "description": "Retrieves a method's description.",
	#     "parameters": [
	#         {
	#             "name": "methodName",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A structure containing the method's description."
	# }
	return call_method("ALFrameManager", "getMethodHelp", [methodName])

def getModuleHelp() -> Any:
	"""
	Retrieves the module's description.
	
	Returns
	----------
	A structure describing the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "m",
	#     "name": "getModuleHelp",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's description.",
	#     "parameters": [],
	#     "returnDescription": "A structure describing the module."
	# }
	return call_method("ALFrameManager", "getModuleHelp", [])

def getBrokerName() -> str:
	"""
	Gets the name of the parent broker.
	
	Returns
	----------
	The name of the parent broker.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "s",
	#     "name": "getBrokerName",
	#     "parametersSignature": "()",
	#     "description": "Gets the name of the parent broker.",
	#     "parameters": [],
	#     "returnDescription": "The name of the parent broker."
	# }
	return call_method("ALFrameManager", "getBrokerName", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "s",
	#     "name": "getUsage",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the method usage string. This summarises how to use the method.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A string that summarises the usage of the method."
	# }
	return call_method("ALFrameManager", "getUsage", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "s",
	#     "name": "createBehavior",
	#     "parametersSignature": "(sss)",
	#     "description": "Creates a new behavior, from a box found in an xml file stored in the robot.",
	#     "parameters": [
	#         {
	#             "name": "packageDir",
	#             "description": " the base directory of the behavior's package, eg: \"/home/myApp\"."
	#         },
	#         {
	#             "name": "behaviorPath",
	#             "description": "the relative path of the behavior inside the package, eg: \"/behavior_1/behavior.xar\"."
	#         },
	#         {
	#             "name": "behName",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": "return a unique identifier for the created box, that can be used by playBehavior"
	# }
	return call_method("ALFrameManager", "createBehavior", [packageDir, behaviorPath, behName])

def completeBehavior(id:str) -> None:
	"""
	It will play a behavior and block until the behavior is finished. Note that it can block forever if the behavior output is never called.
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "completeBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "It will play a behavior and block until the behavior is finished. Note that it can block forever if the behavior output is never called.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the box (the box URI)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "completeBehavior", [id])

def deleteBehavior(id:str) -> None:
	"""
	Deletes a behavior (meaning a box). Stop the whole behavior contained in this box first.
	
	Parameters
	----------
	id:str
		The id of the box to delete (the box URI).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "deleteBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Deletes a behavior (meaning a box). Stop the whole behavior contained in this box first.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the box to delete (the box URI)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "deleteBehavior", [id])

def playBehavior(id:str) -> None:
	"""
	Starts a behavior
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "playBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Starts a behavior",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the box (the box URI)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "playBehavior", [id])

def exitBehavior(id:str) -> None:
	"""
	Exit the reading of a timeline contained in a given box
	
	Parameters
	----------
	id:str
		The id of the box (the box URI).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "exitBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Exit the reading of a timeline contained in a given box",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the box (the box URI)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "exitBehavior", [id])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "isBehaviorRunning",
	#     "parametersSignature": "(s)",
	#     "description": "Tells whether the behavior is running",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the behavior to check (The URI of the root box)."
	#         }
	#     ],
	#     "returnDescription": "True if the behavior is running, false otherwise"
	# }
	return call_method("ALFrameManager", "isBehaviorRunning", [id])

def cleanBehaviors() -> None:
	"""
	Stop playing any behavior in FrameManager, and delete all of them.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "cleanBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Stop playing any behavior in FrameManager, and delete all of them.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "cleanBehaviors", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getBehaviorPath",
	#     "parametersSignature": "(s)",
	#     "description": "Returns a playing behavior absolute path.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "The id of the behavior (The URI of the root box)."
	#         }
	#     ],
	#     "returnDescription": "Returns the absolute path of given behavior."
	# }
	return call_method("ALFrameManager", "getBehaviorPath", [id])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "s",
	#     "name": "createTimeline",
	#     "parametersSignature": "(s)",
	#     "description": "Creates a timeline.",
	#     "parameters": [
	#         {
	#             "name": "timelineContent",
	#             "description": "The timeline content (in XML format)."
	#         }
	#     ],
	#     "returnDescription": "return a unique identifier for the created box that contains the timeline. You must call deleteBehavior on it at some point. DEPRECATED since 1.14"
	# }
	return call_method("ALFrameManager", "createTimeline", [timelineContent])

def behaviors() -> List[str]:
	"""
	List all behaviors currently handled by the frame manager.
	
	Returns
	----------
	a set listing all behavior ids
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "[s]",
	#     "name": "behaviors",
	#     "parametersSignature": "()",
	#     "description": "List all behaviors currently handled by the frame manager.",
	#     "parameters": [],
	#     "returnDescription": "a set listing all behavior ids"
	# }
	return call_method("ALFrameManager", "behaviors", [])

def _dataChanged(dataName:str, data:Any, message:str) -> None:
	"""
	Called by ALMemory when subcription data is updated. INTERNAL
	
	Parameters
	----------
	dataName:str
		Name of the subscribed data.
	data:Any
		Value of the the subscribed data
	message:str
		The message give when subscribing.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "_dataChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Called by ALMemory when subcription data is updated. INTERNAL",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "Name of the subscribed data."
	#         },
	#         {
	#             "name": "data",
	#             "description": "Value of the the subscribed data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message give when subscribing."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_dataChanged", [dataName, data, message])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "_subscribeBoxToEvent",
	#     "parametersSignature": "(ssssb)",
	#     "description": "method called by almemory to inform framemanager that a box is subscribing to an event",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "the name of the event"
	#         },
	#         {
	#             "name": "boxName",
	#             "description": "the name of the box requesting it (the URI of the box)."
	#         },
	#         {
	#             "name": "message",
	#             "description": "the associated message"
	#         },
	#         {
	#             "name": "callback",
	#             "description": "the name of the box's callback to call"
	#         },
	#         {
	#             "name": "micro",
	#             "description": "true if the subscription is to a micro event"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_subscribeBoxToEvent", [eventName, boxName, message, callback, micro])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_unsubscribeBoxToEvent",
	#     "parametersSignature": "(ssb)",
	#     "description": "method called by almemory to inform framemanager that a box is unsubscribing from an event",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "the name of the event"
	#         },
	#         {
	#             "name": "boxName",
	#             "description": "the name of the box requesting it (the URI of the box)."
	#         },
	#         {
	#             "name": "micro",
	#             "description": "true if the subscription is to a micro event"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_unsubscribeBoxToEvent", [eventName, boxName, micro])

def _boxDataChanged(eventName:str, value:Any, message:str) -> None:
	"""
	
	
	Parameters
	----------
	eventName:str
		
	value:Any
		
	message:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "_boxDataChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": ""
	#         },
	#         {
	#             "name": "value",
	#             "description": ""
	#         },
	#         {
	#             "name": "message",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_boxDataChanged", [eventName, value, message])

def _startBenchmark() -> None:
	"""
	Start recording some performance data.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_startBenchmark",
	#     "parametersSignature": "()",
	#     "description": "Start recording some performance data.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_startBenchmark", [])

def _stopBenchmark() -> str:
	"""
	Stop performance data recording, and return a summary.
	
	Returns
	----------
	Returns a textual report of the recorded performance data.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "s",
	#     "name": "_stopBenchmark",
	#     "parametersSignature": "()",
	#     "description": "Stop performance data recording, and return a summary.",
	#     "parameters": [],
	#     "returnDescription": "Returns a textual report of the recorded performance data."
	# }
	return call_method("ALFrameManager", "_stopBenchmark", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "s",
	#     "name": "_newBoxFromFile",
	#     "parametersSignature": "(ss)",
	#     "description": "Creates a new box found in an xml file stored in the robot, without loading it, and without auto-delete on stop. (used by link box)",
	#     "parameters": [
	#         {
	#             "name": "xmlFilePath",
	#             "description": "Path to Xml file, ex : \"/home/youhou/mybehavior.xar\"."
	#         },
	#         {
	#             "name": "path",
	#             "description": "The path to reach the box to instantiate in the project (\"\" if root)."
	#         }
	#     ],
	#     "returnDescription": "return a unique identifier for the created box (the URI of the box), that can be used by playBehavior"
	# }
	return call_method("ALFrameManager", "_newBoxFromFile", [xmlFilePath, path])

def _waitForStopped(fmid:str) -> None:
	"""
	wait for a previously started behavior is stopped
	
	Parameters
	----------
	fmid:str
		the unique identifier of the behavior to wait for (the URI of the root box)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "_waitForStopped",
	#     "parametersSignature": "(s)",
	#     "description": "wait for a previously started behavior is stopped",
	#     "parameters": [
	#         {
	#             "name": "fmid",
	#             "description": "the unique identifier of the behavior to wait for (the URI of the root box)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_waitForStopped", [fmid])

def _onPreferenceUpdated(key:str, value:Any, message:str) -> None:
	"""
	callback for changes in the preference manager
	
	Parameters
	----------
	key:str
		ignored, used by ALMemory
	value:Any
		the domain and the key of the preference that changed
	message:str
		ignored, used by ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceUpdated",
	#     "parametersSignature": "(sms)",
	#     "description": "callback for changes in the preference manager",
	#     "parameters": [
	#         {
	#             "name": "key",
	#             "description": "ignored, used by ALMemory"
	#         },
	#         {
	#             "name": "value",
	#             "description": "the domain and the key of the preference that changed"
	#         },
	#         {
	#             "name": "message",
	#             "description": "ignored, used by ALMemory"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_onPreferenceUpdated", [key, value, message])

def _onPreferencesSynchronized(key:str, value:Any, message:str) -> None:
	"""
	callback for changes in the preference manager
	
	Parameters
	----------
	key:str
		ignored, used by ALMemory
	value:Any
		the domain and the key of the preference that changed
	message:str
		ignored, used by ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "_onPreferencesSynchronized",
	#     "parametersSignature": "(sms)",
	#     "description": "callback for changes in the preference manager",
	#     "parameters": [
	#         {
	#             "name": "key",
	#             "description": "ignored, used by ALMemory"
	#         },
	#         {
	#             "name": "value",
	#             "description": "the domain and the key of the preference that changed"
	#         },
	#         {
	#             "name": "message",
	#             "description": "ignored, used by ALMemory"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_onPreferencesSynchronized", [key, value, message])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "_reportError",
	#     "parametersSignature": "(sss)",
	#     "description": "called by behaviors when an error occured",
	#     "parameters": [
	#         {
	#             "name": "fmid",
	#             "description": "the unique identifier of the behavior that failed (the URI of the root box)"
	#         },
	#         {
	#             "name": "boxid",
	#             "description": "the identifier of the box that failed (the URI of the box)."
	#         },
	#         {
	#             "name": "error",
	#             "description": "the error message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFrameManager", "_reportError", [fmid, boxid, error])

@overload
def callBoxInput(box:str, method:str, arg:Any, /) -> Any:
	"""
	call an input on a box
	
	Parameters
	----------
	box:str
		name of the box (the URI of the box).
	method:str
		name of the method
	arg:Any
		input argument
	
	Bridge notes
	------------
	callBoxInput has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "m",
	#     "name": "callBoxInput",
	#     "parametersSignature": "(ssm)",
	#     "description": "call an input on a box",
	#     "parameters": [
	#         {
	#             "name": "box",
	#             "description": "name of the box (the URI of the box)."
	#         },
	#         {
	#             "name": "method",
	#             "description": "name of the method"
	#         },
	#         {
	#             "name": "arg",
	#             "description": "input argument"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def callBoxInput(box:str, method:str, arg1:Any, arg2:Any, /) -> Any:
	"""
	call an input on a box
	
	Parameters
	----------
	box:str
		name of the box (the URI of the box). A box URI is of the format 'behavior_name:/diagram_1/box_2'
	method:str
		name of the method
	arg1:Any
		input argument
	arg2:Any
		input argument
	
	Bridge notes
	------------
	callBoxInput has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "m",
	#     "name": "callBoxInput",
	#     "parametersSignature": "(ssmm)",
	#     "description": "call an input on a box",
	#     "parameters": [
	#         {
	#             "name": "box",
	#             "description": "name of the box (the URI of the box). A box URI is of the format 'behavior_name:/diagram_1/box_2'"
	#         },
	#         {
	#             "name": "method",
	#             "description": "name of the method"
	#         },
	#         {
	#             "name": "arg1",
	#             "description": "input argument"
	#         },
	#         {
	#             "name": "arg2",
	#             "description": "input argument"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def callBoxInput(*args, **kwargs):
	"""
	Bridge notes
	------------
	callBoxInput has 2 variants on the robot:
	- callBoxInput(box:str, method:str, arg:Any)
	- callBoxInput(box:str, method:str, arg1:Any, arg2:Any)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALFrameManager.callBoxInput has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALFrameManager", "callBoxInput", list(args))

class _Signals:
	behaviorCreated: Signal[[str]] = Signal("ALFrameManager", "behaviorCreated")
	"""
	Bridge notes
	------------
	A signal sent by ALFrameManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorPlayed: Signal[[str]] = Signal("ALFrameManager", "behaviorPlayed")
	"""
	Bridge notes
	------------
	A signal sent by ALFrameManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorStopped: Signal[[str]] = Signal("ALFrameManager", "behaviorStopped")
	"""
	Bridge notes
	------------
	A signal sent by ALFrameManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorDestroyed: Signal[[str]] = Signal("ALFrameManager", "behaviorDestroyed")
	"""
	Bridge notes
	------------
	A signal sent by ALFrameManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorFailed: Signal[[str, str, str]] = Signal("ALFrameManager", "behaviorFailed")
	"""
	Bridge notes
	------------
	A signal sent by ALFrameManager on the robot.
	
	subscribe(callback) calls callback(str, str, str) each time the robot sends it.
	"""
signals = _Signals()

