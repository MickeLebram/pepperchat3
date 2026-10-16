"""
This module is intended to manage behaviors. With this module, you can load, start, stop behaviors, add default behaviors or remove them. 

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
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
	return call_method("ALBehaviorManager", "version", [])

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
	return call_method("ALBehaviorManager", "ping", [])

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
	return call_method("ALBehaviorManager", "getMethodList", [])

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
	return call_method("ALBehaviorManager", "getMethodHelp", [methodName])

def getModuleHelp() -> object:
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
	return call_method("ALBehaviorManager", "getModuleHelp", [])

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
	return call_method("ALBehaviorManager", "getBrokerName", [])

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
	return call_method("ALBehaviorManager", "getUsage", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "preloadBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Load a behavior",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": "Returns true if it was successfully loaded."
	# }
	return call_method("ALBehaviorManager", "preloadBehavior", [behavior])

def startBehavior(behavior:str) -> None:
	"""
	Starts a behavior, returns when started.
	
	Parameters
	----------
	behavior:str
		Behavior name 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "startBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Starts a behavior, returns when started.",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "startBehavior", [behavior])

def runBehavior(behavior:str) -> None:
	"""
	Runs a behavior, returns when finished
	
	Parameters
	----------
	behavior:str
		Behavior name 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "runBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Runs a behavior, returns when finished",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "runBehavior", [behavior])

def stopBehavior(behavior:str) -> None:
	"""
	Stop a behavior
	
	Parameters
	----------
	behavior:str
		Behavior name 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "stopBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Stop a behavior",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "stopBehavior", [behavior])

def stopAllBehaviors() -> None:
	"""
	Stop all behaviors
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "stopAllBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Stop all behaviors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "stopAllBehaviors", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "isBehaviorInstalled",
	#     "parametersSignature": "(s)",
	#     "description": "Tell if supplied name corresponds to a behavior that has been installed",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The behavior directory name"
	#         }
	#     ],
	#     "returnDescription": "Returns true if it is a valid behavior"
	# }
	return call_method("ALBehaviorManager", "isBehaviorInstalled", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "b",
	#     "name": "isBehaviorPresent",
	#     "parametersSignature": "(s)",
	#     "description": "Tell if the supplied namecorresponds to an existing behavior.",
	#     "parameters": [
	#         {
	#             "name": "prefixedBehavior",
	#             "description": "Prefixed behavior or just behavior's name (latter usage deprecated, in this case the behavior is searched for amongst user's behaviors, then in system behaviors) DEPRECATED in favor of ALBehaviorManager.isBehaviorInstalled."
	#         }
	#     ],
	#     "returnDescription": "Returns true if it is an existing behavior"
	# }
	return call_method("ALBehaviorManager", "isBehaviorPresent", [prefixedBehavior])

def getBehaviorNames() -> List[str]:
	"""
	Get behaviors
	
	Returns
	----------
	Returns the list of behaviors prefixed by their type (User/ or System/). DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "[s]",
	#     "name": "getBehaviorNames",
	#     "parametersSignature": "()",
	#     "description": "Get behaviors",
	#     "parameters": [],
	#     "returnDescription": "Returns the list of behaviors prefixed by their type (User/ or System/). DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	# }
	return call_method("ALBehaviorManager", "getBehaviorNames", [])

def getUserBehaviorNames() -> List[str]:
	"""
	Get user's behaviors
	
	Returns
	----------
	Returns the list of user's behaviors prefixed by User/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "[s]",
	#     "name": "getUserBehaviorNames",
	#     "parametersSignature": "()",
	#     "description": "Get user's behaviors",
	#     "parameters": [],
	#     "returnDescription": "Returns the list of user's behaviors prefixed by User/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	# }
	return call_method("ALBehaviorManager", "getUserBehaviorNames", [])

def getSystemBehaviorNames() -> List[str]:
	"""
	Get system behaviors
	
	Returns
	----------
	Returns the list of system behaviors prefixed by System/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "[s]",
	#     "name": "getSystemBehaviorNames",
	#     "parametersSignature": "()",
	#     "description": "Get system behaviors",
	#     "parameters": [],
	#     "returnDescription": "Returns the list of system behaviors prefixed by System/. DEPRECATED in favor of ALBehaviorManager.getInstalledBehaviors."
	# }
	return call_method("ALBehaviorManager", "getSystemBehaviorNames", [])

def getInstalledBehaviors() -> List[str]:
	"""
	Get installed behaviors directories names
	
	Returns
	----------
	Returns the behaviors list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getInstalledBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Get installed behaviors directories names",
	#     "parameters": [],
	#     "returnDescription": "Returns the behaviors list"
	# }
	return call_method("ALBehaviorManager", "getInstalledBehaviors", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getBehaviorsByTag",
	#     "parametersSignature": "(s)",
	#     "description": "Get installed behaviors directories names and filter it by tag.",
	#     "parameters": [
	#         {
	#             "name": "tag",
	#             "description": "A tag to filter the list with."
	#         }
	#     ],
	#     "returnDescription": "Returns the behaviors list"
	# }
	return call_method("ALBehaviorManager", "getBehaviorsByTag", [tag])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "isBehaviorRunning",
	#     "parametersSignature": "(s)",
	#     "description": "Tell if supplied name corresponds to a running behavior",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": "Returns true if it is a running behavior"
	# }
	return call_method("ALBehaviorManager", "isBehaviorRunning", [behavior])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "isBehaviorLoaded",
	#     "parametersSignature": "(s)",
	#     "description": "Tell if supplied name corresponds to a loaded behavior",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": "Returns true if it is a loaded behavior"
	# }
	return call_method("ALBehaviorManager", "isBehaviorLoaded", [behavior])

def getRunningBehaviors() -> List[str]:
	"""
	Get running behaviors
	
	Returns
	----------
	Return running behaviors
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "[s]",
	#     "name": "getRunningBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Get running behaviors",
	#     "parameters": [],
	#     "returnDescription": "Return running behaviors"
	# }
	return call_method("ALBehaviorManager", "getRunningBehaviors", [])

def getLoadedBehaviors() -> List[str]:
	"""
	Get loaded behaviors
	
	Returns
	----------
	Return loaded behaviors
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "[s]",
	#     "name": "getLoadedBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Get loaded behaviors",
	#     "parameters": [],
	#     "returnDescription": "Return loaded behaviors"
	# }
	return call_method("ALBehaviorManager", "getLoadedBehaviors", [])

def getTagList() -> List[str]:
	"""
	Get tags found on installed behaviors.
	
	Returns
	----------
	The list of tags found.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "[s]",
	#     "name": "getTagList",
	#     "parametersSignature": "()",
	#     "description": "Get tags found on installed behaviors.",
	#     "parameters": [],
	#     "returnDescription": "The list of tags found."
	# }
	return call_method("ALBehaviorManager", "getTagList", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "[s]",
	#     "name": "getBehaviorTags",
	#     "parametersSignature": "(s)",
	#     "description": "Get tags found on the given behavior.",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "The local path towards a behavior or a directory."
	#         }
	#     ],
	#     "returnDescription": "The list of tags found."
	# }
	return call_method("ALBehaviorManager", "getBehaviorTags", [behavior])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "s",
	#     "name": "getBehaviorNature",
	#     "parametersSignature": "(s)",
	#     "description": "Get the nature of the given behavior.",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "The local path towards a behavior or a directory."
	#         }
	#     ],
	#     "returnDescription": "The nature of the behavior."
	# }
	return call_method("ALBehaviorManager", "getBehaviorNature", [behavior])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "s",
	#     "name": "_getBehaviorRelativePath",
	#     "parametersSignature": "(s)",
	#     "description": "Get the relative path of a running behavior inside its package.",
	#     "parameters": [
	#         {
	#             "name": "behaviorId",
	#             "description": "The ID of the behavior."
	#         }
	#     ],
	#     "returnDescription": "The relative path of the behavior."
	# }
	return call_method("ALBehaviorManager", "_getBehaviorRelativePath", [behaviorId])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "s",
	#     "name": "_getPackageUid",
	#     "parametersSignature": "(s)",
	#     "description": "Get the package UID of a running behavior.",
	#     "parameters": [
	#         {
	#             "name": "behaviorId",
	#             "description": "The ID of the behavior."
	#         }
	#     ],
	#     "returnDescription": "The package UID of the behavior."
	# }
	return call_method("ALBehaviorManager", "_getPackageUid", [behaviorId])

def addDefaultBehavior(behavior:str) -> None:
	"""
	Set the given behavior as default
	
	Parameters
	----------
	behavior:str
		Behavior name 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "addDefaultBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Set the given behavior as default",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "addDefaultBehavior", [behavior])

def removeDefaultBehavior(behavior:str) -> None:
	"""
	Remove the given behavior from the default behaviors
	
	Parameters
	----------
	behavior:str
		Behavior name 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "removeDefaultBehavior",
	#     "parametersSignature": "(s)",
	#     "description": "Remove the given behavior from the default behaviors",
	#     "parameters": [
	#         {
	#             "name": "behavior",
	#             "description": "Behavior name "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "removeDefaultBehavior", [behavior])

def getDefaultBehaviors() -> List[str]:
	"""
	Get default behaviors
	
	Returns
	----------
	Return default behaviors
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "[s]",
	#     "name": "getDefaultBehaviors",
	#     "parametersSignature": "()",
	#     "description": "Get default behaviors",
	#     "parameters": [],
	#     "returnDescription": "Return default behaviors"
	# }
	return call_method("ALBehaviorManager", "getDefaultBehaviors", [])

def playDefaultProject() -> None:
	"""
	Play default behaviors
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "playDefaultProject",
	#     "parametersSignature": "()",
	#     "description": "Play default behaviors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "playDefaultProject", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_onDataChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Be notified when something we have subscribe to has changed in ALMemory",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "name of the data"
	#         },
	#         {
	#             "name": "dataValue",
	#             "description": "value of the data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "callback message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "_onDataChanged", [dataName, dataValue, message])

def _getBehaviorFrameManagerId(name:str) -> str:
	"""
	get the FrameManagerID. INTERNAL
	
	Parameters
	----------
	name:str
		name of choregraphe project
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "s",
	#     "name": "_getBehaviorFrameManagerId",
	#     "parametersSignature": "(s)",
	#     "description": "get the FrameManagerID. INTERNAL",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of choregraphe project"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBehaviorManager", "_getBehaviorFrameManagerId", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "s",
	#     "name": "resolveBehaviorName",
	#     "parametersSignature": "(s)",
	#     "description": "Find out the actual <package>/<behavior> path behind a behavior name.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of a behavior"
	#         }
	#     ],
	#     "returnDescription": "The actual <package>/<behavior> path if found, else an empty string. Throws an ALERROR if two behavior names conflicted."
	# }
	return call_method("ALBehaviorManager", "resolveBehaviorName", [name])

class _Signals:
	behaviorsAdded: Signal[[List[str]]] = Signal("ALBehaviorManager", "behaviorsAdded")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(List[str]) each time the robot sends it.
	"""
	behaviorsRemoved: Signal[[List[str]]] = Signal("ALBehaviorManager", "behaviorsRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(List[str]) each time the robot sends it.
	"""
	behaviorLoaded: Signal[[str]] = Signal("ALBehaviorManager", "behaviorLoaded")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorStarted: Signal[[str]] = Signal("ALBehaviorManager", "behaviorStarted")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorStopped: Signal[[str]] = Signal("ALBehaviorManager", "behaviorStopped")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	behaviorFailed: Signal[[str, str, str]] = Signal("ALBehaviorManager", "behaviorFailed")
	"""
	Bridge notes
	------------
	A signal sent by ALBehaviorManager on the robot.
	
	subscribe(callback) calls callback(str, str, str) each time the robot sends it.
	"""
signals = _Signals()

