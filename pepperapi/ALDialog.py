"""
ALDialog is the dialog module. It allows loading a dialog file (.top), starts/stops/loads/unloads the dialog
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
	return call_method("ALDialog", "version", [])

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
	return call_method("ALDialog", "ping", [])

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
	return call_method("ALDialog", "getMethodList", [])

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
	return call_method("ALDialog", "getMethodHelp", [methodName])

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
	return call_method("ALDialog", "getModuleHelp", [])

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
	return call_method("ALDialog", "getBrokerName", [])

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
	return call_method("ALDialog", "getUsage", [name])

@overload
def subscribe(name:str, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def subscribe(name:str, period:int, precision:float, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(sif)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds) if relevant."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor if relevant."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def subscribe(*args, **kwargs):
	"""
	Bridge notes
	------------
	subscribe has 2 variants on the robot:
	- subscribe(name:str)
	- subscribe(name:str, period:int, precision:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALDialog.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALDialog", "subscribe", list(args))

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Unsubscribes from the extractor.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which had subscribed."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "updatePeriod",
	#     "parametersSignature": "(si)",
	#     "description": "Updates the period if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "updatePrecision",
	#     "parametersSignature": "(sf)",
	#     "description": "Updates the precision if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "i",
	#     "name": "getCurrentPeriod",
	#     "parametersSignature": "()",
	#     "description": "Gets the current period.",
	#     "parameters": [],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALDialog", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "f",
	#     "name": "getCurrentPrecision",
	#     "parametersSignature": "()",
	#     "description": "Gets the current precision.",
	#     "parameters": [],
	#     "returnDescription": "Precision of the extractor."
	# }
	return call_method("ALDialog", "getCurrentPrecision", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "getMyPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the period for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         }
	#     ],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALDialog", "getMyPeriod", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "f",
	#     "name": "getMyPrecision",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the precision for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of the module which has subscribed"
	#         }
	#     ],
	#     "returnDescription": "precision of the extractor"
	# }
	return call_method("ALDialog", "getMyPrecision", [name])

def getSubscribersInfo() -> Any:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getSubscribersInfo",
	#     "parametersSignature": "()",
	#     "description": "Gets the parameters given by the module.",
	#     "parameters": [],
	#     "returnDescription": "Array of names and parameters of all subscribers."
	# }
	return call_method("ALDialog", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getOutputNames",
	#     "parametersSignature": "()",
	#     "description": "Get the list of values updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of values updated by this extractor in ALMemory"
	# }
	return call_method("ALDialog", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getEventList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALDialog", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "getMemoryKeyList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALDialog", "getMemoryKeyList", [])

def _wordRecognized(unsuned:str, value:Any, message:str) -> None:
	"""
	Callback when speech recognition recognized a word
	
	Parameters
	----------
	unsuned:str
		callback unused parameter
	value:Any
		word recognized value
	message:str
		unused message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_wordRecognized",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback when speech recognition recognized a word",
	#     "parameters": [
	#         {
	#             "name": "unsuned",
	#             "description": "callback unused parameter"
	#         },
	#         {
	#             "name": "value",
	#             "description": "word recognized value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "unused message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_wordRecognized", [unsuned, value, message])

def getStoppable() -> bool:
	"""
	Is engine stoppable
	
	Returns
	----------
	Is engine stoppable
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "getStoppable",
	#     "parametersSignature": "()",
	#     "description": "Is engine stoppable",
	#     "parameters": [],
	#     "returnDescription": "Is engine stoppable"
	# }
	return call_method("ALDialog", "getStoppable", [])

def setStoppable(stoppable:bool) -> None:
	"""
	Is engine stoppable
	
	Parameters
	----------
	stoppable:bool
		set if engine can be stopped by user session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "setStoppable",
	#     "parametersSignature": "(b)",
	#     "description": "Is engine stoppable",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setStoppable", [stoppable])

def runTopics(stoppable:List[str]) -> List[str]:
	"""
	Is engine stoppable
	
	Parameters
	----------
	stoppable:List[str]
		set if engine can be stopped by user session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "[s]",
	#     "name": "runTopics",
	#     "parametersSignature": "([s])",
	#     "description": "Is engine stoppable",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "runTopics", [stoppable])

def stopTopics(stoppable:List[str]) -> None:
	"""
	Is engine stoppable
	
	Parameters
	----------
	stoppable:List[str]
		set if engine can be stopped by user session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "stopTopics",
	#     "parametersSignature": "([s])",
	#     "description": "Is engine stoppable",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "stopTopics", [stoppable])

def _setPhonetic(source1:str, source2:str, p2:str) -> None:
	"""
	Set sentence phonetic
	
	Parameters
	----------
	source1:str
		source sentence
	source2:str
		source sentence
	p2:str
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 2 of 3 parameters. The others are called p2 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_setPhonetic",
	#     "parametersSignature": "(sss)",
	#     "description": "Set sentence phonetic",
	#     "parameters": [
	#         {
	#             "name": "source",
	#             "description": "source sentence"
	#         },
	#         {
	#             "name": "source",
	#             "description": "source sentence"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setPhonetic", [source1, source2, p2])

def _pauseEngine(enable:bool) -> None:
	"""
	Pause/unpause dialog engine and asr
	
	Parameters
	----------
	enable:bool
		true to pause
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_pauseEngine",
	#     "parametersSignature": "(b)",
	#     "description": "Pause/unpause dialog engine and asr",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "true to pause"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_pauseEngine", [enable])

def say(stoppable:str, p1:str) -> None:
	"""
	say a sentence from a topic
	
	Parameters
	----------
	stoppable:str
		set if engine can be stopped by user session
	p1:str
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "say",
	#     "parametersSignature": "(ss)",
	#     "description": "say a sentence from a topic",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "say", [stoppable, p1])

def resetLanguage() -> None:
	"""
	ResetLanguage
	
	Bridge notes
	------------
	NAOqi's documentation lists a parameter (stoppable) that the method's signature doesn't have. This function follows the signature and takes no arguments.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "resetLanguage",
	#     "parametersSignature": "()",
	#     "description": "ResetLanguage",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "resetLanguage", [])

def _getTriggerFromID(stoppable:str, p1:str) -> List[str]:
	"""
	getTriggerFromID
	
	Parameters
	----------
	stoppable:str
		set if engine can be stopped by user session
	p1:str
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "[s]",
	#     "name": "_getTriggerFromID",
	#     "parametersSignature": "(ss)",
	#     "description": "getTriggerFromID",
	#     "parameters": [
	#         {
	#             "name": "stoppable",
	#             "description": "set if engine can be stopped by user session"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_getTriggerFromID", [stoppable, p1])

def addBlockingEvent(eventName:str) -> None:
	"""
	The event will stop current TSS
	
	Parameters
	----------
	eventName:str
		Event name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "addBlockingEvent",
	#     "parametersSignature": "(s)",
	#     "description": "The event will stop current TSS",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "Event name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "addBlockingEvent", [eventName])

def removeBlockingEvent(eventName:str) -> None:
	"""
	The event will removed from the blocking list
	
	Parameters
	----------
	eventName:str
		Event name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "removeBlockingEvent",
	#     "parametersSignature": "(s)",
	#     "description": "The event will removed from the blocking list",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "Event name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "removeBlockingEvent", [eventName])

def wordsRecognizedCallback(grammar:Any, utterance_Size:int) -> None:
	"""
	Asr callback for recognized words
	
	Parameters
	----------
	grammar:Any
		recognized grammar
	utterance_Size:int
		Utterance size
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "wordsRecognizedCallback",
	#     "parametersSignature": "(mi)",
	#     "description": "Asr callback for recognized words",
	#     "parameters": [
	#         {
	#             "name": "grammar",
	#             "description": "recognized grammar"
	#         },
	#         {
	#             "name": "utterance Size",
	#             "description": "Utterance size"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "wordsRecognizedCallback", [grammar, utterance_Size])

def endOfUtteranceCallback() -> bool:
	"""
	End of utterance asr callback
	
	Returns
	----------
	true if reprocess buffer
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "endOfUtteranceCallback",
	#     "parametersSignature": "()",
	#     "description": "End of utterance asr callback",
	#     "parameters": [],
	#     "returnDescription": "true if reprocess buffer"
	# }
	return call_method("ALDialog", "endOfUtteranceCallback", [])

def _releaseEngine() -> None:
	"""
	Experimental: release engine after call of controlEngine
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "_releaseEngine",
	#     "parametersSignature": "()",
	#     "description": "Experimental: release engine after call of controlEngine",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_releaseEngine", [])

def _controlEngine(topicName:str, tagName:str) -> List[str]:
	"""
	Experimental: controlEngine and say a tag
	
	Parameters
	----------
	topicName:str
		topic name
	tagName:str
		tag name
	
	Returns
	----------
	Robot answer list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "[s]",
	#     "name": "_controlEngine",
	#     "parametersSignature": "(ss)",
	#     "description": "Experimental: controlEngine and say a tag",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         },
	#         {
	#             "name": "tagName",
	#             "description": "tag name"
	#         }
	#     ],
	#     "returnDescription": "Robot answer list"
	# }
	return call_method("ALDialog", "_controlEngine", [topicName, tagName])

def _hasPreference() -> bool:
	"""
	hasPreference
	
	Returns
	----------
	true if has preference
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "b",
	#     "name": "_hasPreference",
	#     "parametersSignature": "()",
	#     "description": "hasPreference",
	#     "parameters": [],
	#     "returnDescription": "true if has preference"
	# }
	return call_method("ALDialog", "_hasPreference", [])

def _eventReceived(eventName:str, eventValue:Any, message:str) -> None:
	"""
	Callback when dialog received a event
	
	Parameters
	----------
	eventName:str
		event name received
	eventValue:Any
		event value
	message:str
		unused event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "_eventReceived",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback when dialog received a event",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "event name received"
	#         },
	#         {
	#             "name": "eventValue",
	#             "description": "event value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "unused event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_eventReceived", [eventName, eventValue, message])

def _statusChanged(internalCallBackEvent:str, internalCallbackValue:Any, message:str) -> None:
	"""
	Callback when ASR status changes
	
	Parameters
	----------
	internalCallBackEvent:str
		unused
	internalCallbackValue:Any
		unused
	message:str
		unused
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "_statusChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback when ASR status changes",
	#     "parameters": [
	#         {
	#             "name": "internalCallBackEvent",
	#             "description": "unused"
	#         },
	#         {
	#             "name": "internalCallbackValue",
	#             "description": "unused"
	#         },
	#         {
	#             "name": "message",
	#             "description": "unused"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_statusChanged", [internalCallBackEvent, internalCallbackValue, message])

def gotoTag(topicName:str, tagName:str) -> None:
	"""
	Callback when ASR status changes
	
	Parameters
	----------
	topicName:str
		topic name
	tagName:str
		tag name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "gotoTag",
	#     "parametersSignature": "(ss)",
	#     "description": "Callback when ASR status changes",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         },
	#         {
	#             "name": "tagName",
	#             "description": "tag name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "gotoTag", [topicName, tagName])

def noPick(topicName:str) -> None:
	"""
	noPick
	
	Parameters
	----------
	topicName:str
		Topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "noPick",
	#     "parametersSignature": "(s)",
	#     "description": "noPick",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "noPick", [topicName])

def _connectionChanged(internalCallBackEvent:str, internalCallbackValue:Any, message:str) -> None:
	"""
	Callback when remote connection changes
	
	Parameters
	----------
	internalCallBackEvent:str
		unused
	internalCallbackValue:Any
		unused
	message:str
		unused
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "_connectionChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback when remote connection changes",
	#     "parameters": [
	#         {
	#             "name": "internalCallBackEvent",
	#             "description": "unused"
	#         },
	#         {
	#             "name": "internalCallbackValue",
	#             "description": "unused"
	#         },
	#         {
	#             "name": "message",
	#             "description": "unused"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_connectionChanged", [internalCallBackEvent, internalCallbackValue, message])

def compileAll() -> None:
	"""
	compile all for ASR
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "compileAll",
	#     "parametersSignature": "()",
	#     "description": "compile all for ASR",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "compileAll", [])

def compileBundle(p0:str) -> None:
	"""
	compile all for ASR
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "compileBundle",
	#     "parametersSignature": "(s)",
	#     "description": "compile all for ASR",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "compileBundle", [p0])

def createContext(p0:str, p1:str, p2:str) -> None:
	"""
	Create a context
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "createContext",
	#     "parametersSignature": "(sss)",
	#     "description": "Create a context",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "createContext", [p0, p1, p2])

def loadTopic(topicPath:str) -> str:
	"""
	Load a topic
	
	Parameters
	----------
	topicPath:str
		topic full path and filename
	
	Returns
	----------
	Topic path and filename
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "s",
	#     "name": "loadTopic",
	#     "parametersSignature": "(s)",
	#     "description": "Load a topic",
	#     "parameters": [
	#         {
	#             "name": "topicPath",
	#             "description": "topic full path and filename"
	#         }
	#     ],
	#     "returnDescription": "Topic path and filename"
	# }
	return call_method("ALDialog", "loadTopic", [topicPath])

def loadTopicContent(topicContent:str) -> str:
	"""
	Load a topic
	
	Parameters
	----------
	topicContent:str
		topic content
	
	Returns
	----------
	Topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "s",
	#     "name": "loadTopicContent",
	#     "parametersSignature": "(s)",
	#     "description": "Load a topic",
	#     "parameters": [
	#         {
	#             "name": "topicContent",
	#             "description": "topic content"
	#         }
	#     ],
	#     "returnDescription": "Topic name"
	# }
	return call_method("ALDialog", "loadTopicContent", [topicContent])

def deactivateTopic(topicName:str) -> None:
	"""
	Activate a topic
	
	Parameters
	----------
	topicName:str
		topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "v",
	#     "name": "deactivateTopic",
	#     "parametersSignature": "(s)",
	#     "description": "Activate a topic",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "deactivateTopic", [topicName])

def activateTopic(topicName:str) -> None:
	"""
	Activate a topic
	
	Parameters
	----------
	topicName:str
		topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "activateTopic",
	#     "parametersSignature": "(s)",
	#     "description": "Activate a topic",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "activateTopic", [topicName])

def unloadTopic(topicName:str) -> None:
	"""
	unload a dialog
	
	Parameters
	----------
	topicName:str
		topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "v",
	#     "name": "unloadTopic",
	#     "parametersSignature": "(s)",
	#     "description": "unload a dialog",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "unloadTopic", [topicName])

def forceOutput() -> None:
	"""
	Get a proposal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "forceOutput",
	#     "parametersSignature": "()",
	#     "description": "Get a proposal",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "forceOutput", [])

def _isRunDialogInstalled() -> bool:
	"""
	isRunDialogInstalled
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "b",
	#     "name": "_isRunDialogInstalled",
	#     "parametersSignature": "()",
	#     "description": "isRunDialogInstalled",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_isRunDialogInstalled", [])

def forceInput(input:str) -> None:
	"""
	Give a sentence to the dialog and get the answer
	
	Parameters
	----------
	input:str
		input string that simulate humain sentence
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "v",
	#     "name": "forceInput",
	#     "parametersSignature": "(s)",
	#     "description": "Give a sentence to the dialog and get the answer",
	#     "parameters": [
	#         {
	#             "name": "input",
	#             "description": "input string that simulate humain sentence"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "forceInput", [input])

def tell(input:str) -> None:
	"""
	Give a sentence to the dialog and get the answer
	
	Parameters
	----------
	input:str
		input string that simulate humain sentence
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "v",
	#     "name": "tell",
	#     "parametersSignature": "(s)",
	#     "description": "Give a sentence to the dialog and get the answer",
	#     "parameters": [
	#         {
	#             "name": "input",
	#             "description": "input string that simulate humain sentence"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "tell", [input])

def setASRConfidenceThreshold(threshold:float) -> None:
	"""
	Set the minimum confidence required to recognize words. Better to use confidence by asr model
	
	Parameters
	----------
	threshold:float
		input string that simulate humain sentence
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "v",
	#     "name": "setASRConfidenceThreshold",
	#     "parametersSignature": "(f)",
	#     "description": "Set the minimum confidence required to recognize words. Better to use confidence by asr model",
	#     "parameters": [
	#         {
	#             "name": "threshold",
	#             "description": "input string that simulate humain sentence"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setASRConfidenceThreshold", [threshold])

def getASRConfidenceThreshold() -> float:
	"""
	Get the minimum confidence required to recognize words
	
	Returns
	----------
	current asr confidence
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "f",
	#     "name": "getASRConfidenceThreshold",
	#     "parametersSignature": "()",
	#     "description": "Get the minimum confidence required to recognize words",
	#     "parameters": [],
	#     "returnDescription": "current asr confidence"
	# }
	return call_method("ALDialog", "getASRConfidenceThreshold", [])

@overload
def setConfidenceThreshold(strategy:str, confidence:float, /) -> None:
	"""
	Set the confidence threshold
	
	Parameters
	----------
	strategy:str
		BNF / SLM / REMOTE
	confidence:float
		desired confidence threshold [0, 1]
	
	Bridge notes
	------------
	setConfidenceThreshold has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "v",
	#     "name": "setConfidenceThreshold",
	#     "parametersSignature": "(sf)",
	#     "description": "Set the confidence threshold",
	#     "parameters": [
	#         {
	#             "name": "strategy",
	#             "description": "BNF / SLM / REMOTE"
	#         },
	#         {
	#             "name": "confidence",
	#             "description": "desired confidence threshold [0, 1]"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setConfidenceThreshold(strategy:str, confidence:float, language:str, /) -> None:
	"""
	Set the confidence threshold
	
	Parameters
	----------
	strategy:str
		BNF / SLM / REMOTE
	confidence:float
		desired confidence threshold [0, 1]
	language:str
		language for which we set the threshold
	
	Bridge notes
	------------
	setConfidenceThreshold has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "v",
	#     "name": "setConfidenceThreshold",
	#     "parametersSignature": "(sfs)",
	#     "description": "Set the confidence threshold",
	#     "parameters": [
	#         {
	#             "name": "strategy",
	#             "description": "BNF / SLM / REMOTE"
	#         },
	#         {
	#             "name": "confidence",
	#             "description": "desired confidence threshold [0, 1]"
	#         },
	#         {
	#             "name": "language",
	#             "description": "language for which we set the threshold"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setConfidenceThreshold(*args, **kwargs):
	"""
	Bridge notes
	------------
	setConfidenceThreshold has 2 variants on the robot:
	- setConfidenceThreshold(strategy:str, confidence:float)
	- setConfidenceThreshold(strategy:str, confidence:float, language:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALDialog.setConfidenceThreshold has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALDialog", "setConfidenceThreshold", list(args))

def getAllConfidenceThresholds() -> Dict[str,Dict[str,float]]:
	"""
	Get all the confidence thresholds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "{s{sf}}",
	#     "name": "getAllConfidenceThresholds",
	#     "parametersSignature": "()",
	#     "description": "Get all the confidence thresholds",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "getAllConfidenceThresholds", [])

def getConfidenceThreshold(p0:str, p1:str) -> float:
	"""
	Get all the confidence thresholds
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "f",
	#     "name": "getConfidenceThreshold",
	#     "parametersSignature": "(ss)",
	#     "description": "Get all the confidence thresholds",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "getConfidenceThreshold", [p0, p1])

def removeAllLanguageThresholds() -> None:
	"""
	Remove all language specific confidence thresholds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "v",
	#     "name": "removeAllLanguageThresholds",
	#     "parametersSignature": "()",
	#     "description": "Remove all language specific confidence thresholds",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "removeAllLanguageThresholds", [])

def _setConfidence(strategy:str, threshold:float) -> None:
	"""
	Set the minimum confidence required to recognize words for a strategy
	
	Parameters
	----------
	strategy:str
		BNF or SLM
	threshold:float
		threshold [0,1]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "v",
	#     "name": "_setConfidence",
	#     "parametersSignature": "(sf)",
	#     "description": "Set the minimum confidence required to recognize words for a strategy",
	#     "parameters": [
	#         {
	#             "name": "strategy",
	#             "description": "BNF or SLM"
	#         },
	#         {
	#             "name": "threshold",
	#             "description": "threshold [0,1]"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setConfidence", [strategy, threshold])

def _getConfidence(strategy:str) -> float:
	"""
	Get the minimum confidence required to recognize words of a strategy
	
	Parameters
	----------
	strategy:str
		BNF or SLM
	
	Returns
	----------
	current asr confidence for model
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "f",
	#     "name": "_getConfidence",
	#     "parametersSignature": "(s)",
	#     "description": "Get the minimum confidence required to recognize words of a strategy",
	#     "parameters": [
	#         {
	#             "name": "strategy",
	#             "description": "BNF or SLM"
	#         }
	#     ],
	#     "returnDescription": "current asr confidence for model"
	# }
	return call_method("ALDialog", "_getConfidence", [strategy])

def openSession(id:int) -> None:
	"""
	Open a session
	
	Parameters
	----------
	id:int
		user id
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "v",
	#     "name": "openSession",
	#     "parametersSignature": "(i)",
	#     "description": "Open a session",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "user id"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "openSession", [id])

def _getBackend() -> str:
	"""
	Get backend
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "s",
	#     "name": "_getBackend",
	#     "parametersSignature": "()",
	#     "description": "Get backend",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_getBackend", [])

def _openTestSession(p0:str, p1:str, p2:bool, p3:bool, p4:str, p5:str) -> str:
	"""
	Open a test session
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:bool
		
	p3:bool
		
	p4:str
		
	p5:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "s",
	#     "name": "_openTestSession",
	#     "parametersSignature": "(ssbbss)",
	#     "description": "Open a test session",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_openTestSession", [p0, p1, p2, p3, p4, p5])

def _closeTestSession() -> None:
	"""
	close a test session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "v",
	#     "name": "_closeTestSession",
	#     "parametersSignature": "()",
	#     "description": "close a test session",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_closeTestSession", [])

@overload
def _runTotTest(tot:str, /) -> List[Dict[str,str]]:
	"""
	Open a test session
	
	Parameters
	----------
	tot:str
		tot file to test
	
	Bridge notes
	------------
	_runTotTest has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "[{ss}]",
	#     "name": "_runTotTest",
	#     "parametersSignature": "(s)",
	#     "description": "Open a test session",
	#     "parameters": [
	#         {
	#             "name": "tot",
	#             "description": "tot file to test"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def _runTotTest(tot:str, wavMode:str, /) -> List[Dict[str,str]]:
	"""
	Open a test session
	
	Parameters
	----------
	tot:str
		tot file to test
	wavMode:str
		input wav mode
	
	Bridge notes
	------------
	_runTotTest has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "[{ss}]",
	#     "name": "_runTotTest",
	#     "parametersSignature": "(ss)",
	#     "description": "Open a test session",
	#     "parameters": [
	#         {
	#             "name": "tot",
	#             "description": "tot file to test"
	#         },
	#         {
	#             "name": "wavMode",
	#             "description": "input wav mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def _runTotTest(tot:str, wavMode:str, wavTranscriptionFile:str, /) -> List[Dict[str,str]]:
	"""
	Open a test session
	
	Parameters
	----------
	tot:str
		tot file to test
	wavMode:str
		input wav mode
	wavTranscriptionFile:str
		file containing correspondances between a wav file and his transcription
	
	Bridge notes
	------------
	_runTotTest has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "[{ss}]",
	#     "name": "_runTotTest",
	#     "parametersSignature": "(sss)",
	#     "description": "Open a test session",
	#     "parameters": [
	#         {
	#             "name": "tot",
	#             "description": "tot file to test"
	#         },
	#         {
	#             "name": "wavMode",
	#             "description": "input wav mode"
	#         },
	#         {
	#             "name": "wavTranscriptionFile",
	#             "description": "file containing correspondances between a wav file and his transcription"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def _runTotTest(*args, **kwargs):
	"""
	Bridge notes
	------------
	_runTotTest has 3 variants on the robot:
	- _runTotTest(tot:str)
	- _runTotTest(tot:str, wavMode:str)
	- _runTotTest(tot:str, wavMode:str, wavTranscriptionFile:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALDialog._runTotTest has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALDialog", "_runTotTest", list(args))

def closeSession() -> None:
	"""
	Close the current session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "v",
	#     "name": "closeSession",
	#     "parametersSignature": "()",
	#     "description": "Close the current session",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "closeSession", [])

def closeTestSession() -> None:
	"""
	Close the test session
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "v",
	#     "name": "closeTestSession",
	#     "parametersSignature": "()",
	#     "description": "Close the test session",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "closeTestSession", [])

def _generatePOT(application:str, topics:List[str], language:str, destination:str) -> None:
	"""
	generate a .pot file containing all the sentences of a given application
	
	Parameters
	----------
	application:str
		application name
	topics:List[str]
		the topics in the application whose content is included in the .pot file
	language:str
		the language of the content in the application used to generate the .pot file
	destination:str
		the .pot destination
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "v",
	#     "name": "_generatePOT",
	#     "parametersSignature": "(s[s]ss)",
	#     "description": "generate a .pot file containing all the sentences of a given application",
	#     "parameters": [
	#         {
	#             "name": "application",
	#             "description": "application name"
	#         },
	#         {
	#             "name": "topics",
	#             "description": "the topics in the application whose content is included in the .pot file"
	#         },
	#         {
	#             "name": "language",
	#             "description": "the language of the content in the application used to generate the .pot file"
	#         },
	#         {
	#             "name": "destination",
	#             "description": "the .pot destination"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_generatePOT", [application, topics, language, destination])

def setDelay(eventName:str, Delay:int) -> None:
	"""
	change event's delay
	
	Parameters
	----------
	eventName:str
		Event name
	Delay:int
		Delay in second
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "v",
	#     "name": "setDelay",
	#     "parametersSignature": "(si)",
	#     "description": "change event's delay",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "Event name"
	#         },
	#         {
	#             "name": "Delay",
	#             "description": "Delay in second"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setDelay", [eventName, Delay])

def setNumberOfScopes(numberOfScope:int) -> None:
	"""
	Set how many scopes remains open
	
	Parameters
	----------
	numberOfScope:int
		number of scope
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "v",
	#     "name": "setNumberOfScopes",
	#     "parametersSignature": "(i)",
	#     "description": "Set how many scopes remains open",
	#     "parameters": [
	#         {
	#             "name": "numberOfScope",
	#             "description": "number of scope"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setNumberOfScopes", [numberOfScope])

@overload
def setConcept(conceptName:str, language:str, content:List[str], /) -> None:
	"""
	Set the content of a dynamic concept
	
	Parameters
	----------
	conceptName:str
		Name of the concept
	language:str
		Language of the concept
	content:List[str]
		content of the concept
	
	Bridge notes
	------------
	setConcept has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	
	NAOqi's documentation lists 4 parameters (conceptName, language, content, store), but the signature has 3. The first 3 names are used here and may not match the actual parameters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "v",
	#     "name": "setConcept",
	#     "parametersSignature": "(ss[s])",
	#     "description": "Set the content of a dynamic concept",
	#     "parameters": [
	#         {
	#             "name": "conceptName",
	#             "description": "Name of the concept"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language of the concept"
	#         },
	#         {
	#             "name": "content",
	#             "description": "content of the concept"
	#         },
	#         {
	#             "name": "store",
	#             "description": "Store concept in database if true"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setConcept(conceptName:str, language:str, content:List[str], store:bool, /) -> None:
	"""
	Set the content of a dynamic concept
	
	Parameters
	----------
	conceptName:str
		Name of the concept
	language:str
		Language of the concept
	content:List[str]
		content of the concept
	store:bool
		determine if the concept will be save in the database
	
	Bridge notes
	------------
	setConcept has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "v",
	#     "name": "setConcept",
	#     "parametersSignature": "(ss[s]b)",
	#     "description": "Set the content of a dynamic concept",
	#     "parameters": [
	#         {
	#             "name": "conceptName",
	#             "description": "Name of the concept"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language of the concept"
	#         },
	#         {
	#             "name": "content",
	#             "description": "content of the concept"
	#         },
	#         {
	#             "name": "store",
	#             "description": "determine if the concept will be save in the database"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setConcept(*args, **kwargs):
	"""
	Bridge notes
	------------
	setConcept has 2 variants on the robot:
	- setConcept(conceptName:str, language:str, content:List[str])
	- setConcept(conceptName:str, language:str, content:List[str], store:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALDialog.setConcept has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALDialog", "setConcept", list(args))

def setConceptKeepInCache(conceptName:str, language:str, content:List[str]) -> None:
	"""
	set the content of a dynamic concept
	
	Parameters
	----------
	conceptName:str
		concept name
	language:str
		language
	content:List[str]
		concept content
	"""
	# NAOqi metadata:
	# {
	#     "uid": 185,
	#     "returnSignature": "v",
	#     "name": "setConceptKeepInCache",
	#     "parametersSignature": "(ss[s])",
	#     "description": "set the content of a dynamic concept",
	#     "parameters": [
	#         {
	#             "name": "conceptName",
	#             "description": "concept name"
	#         },
	#         {
	#             "name": "language",
	#             "description": "language"
	#         },
	#         {
	#             "name": "content",
	#             "description": "concept content"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setConceptKeepInCache", [conceptName, language, content])

def addToConcept(conceptName:str, language:str, content:List[str]) -> None:
	"""
	add to the content of a dynamic concept
	
	Parameters
	----------
	conceptName:str
		Name of the concept
	language:str
		Language of the concept
	content:List[str]
		content of the concept
	"""
	# NAOqi metadata:
	# {
	#     "uid": 186,
	#     "returnSignature": "v",
	#     "name": "addToConcept",
	#     "parametersSignature": "(ss[s])",
	#     "description": "add to the content of a dynamic concept",
	#     "parameters": [
	#         {
	#             "name": "conceptName",
	#             "description": "Name of the concept"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language of the concept"
	#         },
	#         {
	#             "name": "content",
	#             "description": "content of the concept"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "addToConcept", [conceptName, language, content])

def getConcept(conceptName:str, language:str) -> List[str]:
	"""
	get the content of a dynamic concept
	
	Parameters
	----------
	conceptName:str
		Name of the concept
	language:str
		Language of the concept
	"""
	# NAOqi metadata:
	# {
	#     "uid": 187,
	#     "returnSignature": "[s]",
	#     "name": "getConcept",
	#     "parametersSignature": "(ss)",
	#     "description": "get the content of a dynamic concept",
	#     "parameters": [
	#         {
	#             "name": "conceptName",
	#             "description": "Name of the concept"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language of the concept"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "getConcept", [conceptName, language])

def _setPushMode(pushMode:int) -> None:
	"""
	Set push mode. Frequence of robot question
	
	Parameters
	----------
	pushMode:int
		Push mode from 0 to 4
	"""
	# NAOqi metadata:
	# {
	#     "uid": 188,
	#     "returnSignature": "v",
	#     "name": "_setPushMode",
	#     "parametersSignature": "(i)",
	#     "description": "Set push mode. Frequence of robot question",
	#     "parameters": [
	#         {
	#             "name": "pushMode",
	#             "description": "Push mode from 0 to 4"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setPushMode", [pushMode])

def enableTriggerSentences(enableTriggerSentences:bool) -> None:
	"""
	enableTriggerSentences
	
	Parameters
	----------
	enableTriggerSentences:bool
		Enable trigger sentences if true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 189,
	#     "returnSignature": "v",
	#     "name": "enableTriggerSentences",
	#     "parametersSignature": "(b)",
	#     "description": "enableTriggerSentences",
	#     "parameters": [
	#         {
	#             "name": "enableTriggerSentences",
	#             "description": "Enable trigger sentences if true"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "enableTriggerSentences", [enableTriggerSentences])

def enableCategory(enableCategory:bool) -> None:
	"""
	enableCategory
	
	Parameters
	----------
	enableCategory:bool
		Enable category if true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 190,
	#     "returnSignature": "v",
	#     "name": "enableCategory",
	#     "parametersSignature": "(b)",
	#     "description": "enableCategory",
	#     "parameters": [
	#         {
	#             "name": "enableCategory",
	#             "description": "Enable category if true"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "enableCategory", [enableCategory])

def startPush() -> None:
	"""
	Start push mode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 191,
	#     "returnSignature": "v",
	#     "name": "startPush",
	#     "parametersSignature": "()",
	#     "description": "Start push mode",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "startPush", [])

def stopPush() -> None:
	"""
	Stop push mode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 192,
	#     "returnSignature": "v",
	#     "name": "stopPush",
	#     "parametersSignature": "()",
	#     "description": "Stop push mode",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "stopPush", [])

def setAnimatedSpeechConfiguration(animatedSpeechConfiguration:Any) -> None:
	"""
	Set the configuration of animated speech for the current dialog.
	
	Parameters
	----------
	animatedSpeechConfiguration:Any
		See animated speech documentation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 193,
	#     "returnSignature": "v",
	#     "name": "setAnimatedSpeechConfiguration",
	#     "parametersSignature": "(m)",
	#     "description": "Set the configuration of animated speech for the current dialog.",
	#     "parameters": [
	#         {
	#             "name": "animatedSpeechConfiguration",
	#             "description": "See animated speech documentation"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setAnimatedSpeechConfiguration", [animatedSpeechConfiguration])

def getAnimatedSpeechConfiguration() -> Any:
	"""
	Get the configuration of animated speech for the current dialog.
	
	Returns
	----------
	See animated speech documentation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 194,
	#     "returnSignature": "m",
	#     "name": "getAnimatedSpeechConfiguration",
	#     "parametersSignature": "()",
	#     "description": "Get the configuration of animated speech for the current dialog.",
	#     "parameters": [],
	#     "returnDescription": "See animated speech documentation"
	# }
	return call_method("ALDialog", "getAnimatedSpeechConfiguration", [])

def applicationBlackList(applicationList:List[str]) -> None:
	"""
	Black list a list of application
	
	Parameters
	----------
	applicationList:List[str]
		List of applications that cannot be launched by dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 195,
	#     "returnSignature": "v",
	#     "name": "applicationBlackList",
	#     "parametersSignature": "([s])",
	#     "description": "Black list a list of application",
	#     "parameters": [
	#         {
	#             "name": "applicationList",
	#             "description": "List of applications that cannot be launched by dialog"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "applicationBlackList", [applicationList])

def isContentNeedsUpdate() -> bool:
	"""
	True if new content was installed
	
	Returns
	----------
	True if content was updated since last compilation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 196,
	#     "returnSignature": "b",
	#     "name": "isContentNeedsUpdate",
	#     "parametersSignature": "()",
	#     "description": "True if new content was installed",
	#     "parameters": [],
	#     "returnDescription": "True if content was updated since last compilation"
	# }
	return call_method("ALDialog", "isContentNeedsUpdate", [])

def _addDialogFromTopicBox(topicPathName:str, includeDirectory:str) -> str:
	"""
	private method to be able to set in specific include dir
	
	Parameters
	----------
	topicPathName:str
		Topic path and filename
	includeDirectory:str
		Root of the behavior
	
	Returns
	----------
	Topic name (not filename)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 197,
	#     "returnSignature": "s",
	#     "name": "_addDialogFromTopicBox",
	#     "parametersSignature": "(ss)",
	#     "description": "private method to be able to set in specific include dir",
	#     "parameters": [
	#         {
	#             "name": "topicPathName",
	#             "description": "Topic path and filename"
	#         },
	#         {
	#             "name": "includeDirectory",
	#             "description": "Root of the behavior"
	#         }
	#     ],
	#     "returnDescription": "Topic name (not filename)"
	# }
	return call_method("ALDialog", "_addDialogFromTopicBox", [topicPathName, includeDirectory])

def _cleanEventStack() -> None:
	"""
	Clean event stack
	"""
	# NAOqi metadata:
	# {
	#     "uid": 198,
	#     "returnSignature": "v",
	#     "name": "_cleanEventStack",
	#     "parametersSignature": "()",
	#     "description": "Clean event stack",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_cleanEventStack", [])

def _updateAIClient(libraryPath:str) -> None:
	"""
	Connect to custom AI client
	
	Parameters
	----------
	libraryPath:str
		library path
	"""
	# NAOqi metadata:
	# {
	#     "uid": 199,
	#     "returnSignature": "v",
	#     "name": "_updateAIClient",
	#     "parametersSignature": "(s)",
	#     "description": "Connect to custom AI client",
	#     "parameters": [
	#         {
	#             "name": "libraryPath",
	#             "description": "library path"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_updateAIClient", [libraryPath])

def _addTopicsInGroup(groupName:str, topicNameList:List[str]) -> None:
	"""
	Create a user group
	
	Parameters
	----------
	groupName:str
		User group name
	topicNameList:List[str]
		Topic to add in group
	"""
	# NAOqi metadata:
	# {
	#     "uid": 200,
	#     "returnSignature": "v",
	#     "name": "_addTopicsInGroup",
	#     "parametersSignature": "(s[s])",
	#     "description": "Create a user group",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "User group name"
	#         },
	#         {
	#             "name": "topicNameList",
	#             "description": "Topic to add in group"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_addTopicsInGroup", [groupName, topicNameList])

def _activateGroup(groupName:str) -> None:
	"""
	Group to activate
	
	Parameters
	----------
	groupName:str
		group name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 201,
	#     "returnSignature": "v",
	#     "name": "_activateGroup",
	#     "parametersSignature": "(s)",
	#     "description": "Group to activate",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "group name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_activateGroup", [groupName])

def _deactivateGroup(groupName:str) -> None:
	"""
	private method to be able to set in specific include dir
	
	Parameters
	----------
	groupName:str
		group name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 202,
	#     "returnSignature": "v",
	#     "name": "_deactivateGroup",
	#     "parametersSignature": "(s)",
	#     "description": "private method to be able to set in specific include dir",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "group name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_deactivateGroup", [groupName])

def _suggestNextTopic(topicName:str, suggestionValidity:int) -> None:
	"""
	suggest next topic
	
	Parameters
	----------
	topicName:str
		group name
	suggestionValidity:int
		Suggestion validity in second
	"""
	# NAOqi metadata:
	# {
	#     "uid": 203,
	#     "returnSignature": "v",
	#     "name": "_suggestNextTopic",
	#     "parametersSignature": "(si)",
	#     "description": "suggest next topic",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "group name"
	#         },
	#         {
	#             "name": "suggestionValidity",
	#             "description": "Suggestion validity in second"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_suggestNextTopic", [topicName, suggestionValidity])

def _suggestUserNextTopic(topicName:str, suggestionValidity:int, userID:int) -> None:
	"""
	suggest next topic
	
	Parameters
	----------
	topicName:str
		group name
	suggestionValidity:int
		Suggestion validity in second
	userID:int
		Suggestion validity for userID
	"""
	# NAOqi metadata:
	# {
	#     "uid": 204,
	#     "returnSignature": "v",
	#     "name": "_suggestUserNextTopic",
	#     "parametersSignature": "(sii)",
	#     "description": "suggest next topic",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "group name"
	#         },
	#         {
	#             "name": "suggestionValidity",
	#             "description": "Suggestion validity in second"
	#         },
	#         {
	#             "name": "userID",
	#             "description": "Suggestion validity for userID"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_suggestUserNextTopic", [topicName, suggestionValidity, userID])

def _preloadMain() -> None:
	"""
	preload main dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 205,
	#     "returnSignature": "v",
	#     "name": "_preloadMain",
	#     "parametersSignature": "()",
	#     "description": "preload main dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_preloadMain", [])

def _mainLanguage(languageName:str) -> None:
	"""
	Define only language to use
	
	Parameters
	----------
	languageName:str
		monoLanguageName
	"""
	# NAOqi metadata:
	# {
	#     "uid": 206,
	#     "returnSignature": "v",
	#     "name": "_mainLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "Define only language to use",
	#     "parameters": [
	#         {
	#             "name": "languageName",
	#             "description": "monoLanguageName"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_mainLanguage", [languageName])

def _runMainNoActivation() -> None:
	"""
	run main dialog without speaking
	"""
	# NAOqi metadata:
	# {
	#     "uid": 207,
	#     "returnSignature": "v",
	#     "name": "_runMainNoActivation",
	#     "parametersSignature": "()",
	#     "description": "run main dialog without speaking",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_runMainNoActivation", [])

def _runMain() -> None:
	"""
	run main dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 208,
	#     "returnSignature": "v",
	#     "name": "_runMain",
	#     "parametersSignature": "()",
	#     "description": "run main dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_runMain", [])

def _startDialog(engagementMode:str) -> None:
	"""
	run main dialog
	
	Parameters
	----------
	engagementMode:str
		engagementMode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 209,
	#     "returnSignature": "v",
	#     "name": "_startDialog",
	#     "parametersSignature": "(s)",
	#     "description": "run main dialog",
	#     "parameters": [
	#         {
	#             "name": "engagementMode",
	#             "description": "engagementMode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_startDialog", [engagementMode])

def _setEngagementMode(engagementMode:str) -> None:
	"""
	change engagement mode
	
	Parameters
	----------
	engagementMode:str
		engagementMode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 210,
	#     "returnSignature": "v",
	#     "name": "_setEngagementMode",
	#     "parametersSignature": "(s)",
	#     "description": "change engagement mode",
	#     "parameters": [
	#         {
	#             "name": "engagementMode",
	#             "description": "engagementMode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setEngagementMode", [engagementMode])

def _pause(p0:bool) -> None:
	"""
	change engagement mode
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 211,
	#     "returnSignature": "v",
	#     "name": "_pause",
	#     "parametersSignature": "(b)",
	#     "description": "change engagement mode",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_pause", [p0])

def _endPause() -> None:
	"""
	change engagement mode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 212,
	#     "returnSignature": "v",
	#     "name": "_endPause",
	#     "parametersSignature": "()",
	#     "description": "change engagement mode",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_endPause", [])

def runDialog() -> None:
	"""
	run main dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 213,
	#     "returnSignature": "v",
	#     "name": "runDialog",
	#     "parametersSignature": "()",
	#     "description": "run main dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "runDialog", [])

def _resetPreload() -> None:
	"""
	reset preload settings
	"""
	# NAOqi metadata:
	# {
	#     "uid": 214,
	#     "returnSignature": "v",
	#     "name": "_resetPreload",
	#     "parametersSignature": "()",
	#     "description": "reset preload settings",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_resetPreload", [])

def _stopMain() -> None:
	"""
	stop main dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 215,
	#     "returnSignature": "v",
	#     "name": "_stopMain",
	#     "parametersSignature": "()",
	#     "description": "stop main dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_stopMain", [])

def stopDialog() -> None:
	"""
	stop main dialog
	"""
	# NAOqi metadata:
	# {
	#     "uid": 216,
	#     "returnSignature": "v",
	#     "name": "stopDialog",
	#     "parametersSignature": "()",
	#     "description": "stop main dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "stopDialog", [])

def _loadStrategyConfiguration(strategyFile:str) -> None:
	"""
	load a strategy configuration
	
	Parameters
	----------
	strategyFile:str
		Strategy path and filename
	"""
	# NAOqi metadata:
	# {
	#     "uid": 217,
	#     "returnSignature": "v",
	#     "name": "_loadStrategyConfiguration",
	#     "parametersSignature": "(s)",
	#     "description": "load a strategy configuration",
	#     "parameters": [
	#         {
	#             "name": "strategyFile",
	#             "description": "Strategy path and filename"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_loadStrategyConfiguration", [strategyFile])

def setVariablePath(topic:str, event:str, path:str) -> None:
	"""
	setVariablePath redifine a variable name on the fly
	
	Parameters
	----------
	topic:str
		Source topic name
	event:str
		Event name
	path:str
		New event name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 218,
	#     "returnSignature": "v",
	#     "name": "setVariablePath",
	#     "parametersSignature": "(sss)",
	#     "description": "setVariablePath redifine a variable name on the fly",
	#     "parameters": [
	#         {
	#             "name": "topic",
	#             "description": "Source topic name"
	#         },
	#         {
	#             "name": "event",
	#             "description": "Event name"
	#         },
	#         {
	#             "name": "path",
	#             "description": "New event name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setVariablePath", [topic, event, path])

def _registerIO(boxName:str, topicName:str, inputList:List[str], outputList:List[str]) -> None:
	"""
	register IO
	
	Parameters
	----------
	boxName:str
		Box name
	topicName:str
		Topic name
	inputList:List[str]
		Input list
	outputList:List[str]
		Output list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 219,
	#     "returnSignature": "v",
	#     "name": "_registerIO",
	#     "parametersSignature": "(ss[s][s])",
	#     "description": "register IO",
	#     "parameters": [
	#         {
	#             "name": "boxName",
	#             "description": "Box name"
	#         },
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         },
	#         {
	#             "name": "inputList",
	#             "description": "Input list"
	#         },
	#         {
	#             "name": "outputList",
	#             "description": "Output list"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_registerIO", [boxName, topicName, inputList, outputList])

def _unregisterIO(boxName:str, topicName:str) -> None:
	"""
	unregister IO
	
	Parameters
	----------
	boxName:str
		Box name
	topicName:str
		Topic name
	
	Bridge notes
	------------
	NAOqi's documentation lists 4 parameters (boxName, topicName, inputList, outputList), but the signature has 2. The first 2 names are used here and may not match the actual parameters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 220,
	#     "returnSignature": "v",
	#     "name": "_unregisterIO",
	#     "parametersSignature": "(ss)",
	#     "description": "unregister IO",
	#     "parameters": [
	#         {
	#             "name": "boxName",
	#             "description": "Box name"
	#         },
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         },
	#         {
	#             "name": "inputList",
	#             "description": "Input list"
	#         },
	#         {
	#             "name": "outputList",
	#             "description": "Output list"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_unregisterIO", [boxName, topicName])

def _messageIn(boxName:str, topicName:str, variableName:str, value:Any) -> None:
	"""
	Send a message input
	
	Parameters
	----------
	boxName:str
		Box name
	topicName:str
		Topic name
	variableName:str
		Variable name
	value:Any
		Value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 221,
	#     "returnSignature": "v",
	#     "name": "_messageIn",
	#     "parametersSignature": "(sssm)",
	#     "description": "Send a message input",
	#     "parameters": [
	#         {
	#             "name": "boxName",
	#             "description": "Box name"
	#         },
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         },
	#         {
	#             "name": "variableName",
	#             "description": "Variable name"
	#         },
	#         {
	#             "name": "value",
	#             "description": "Value"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_messageIn", [boxName, topicName, variableName, value])

def setLanguage(Language:str) -> None:
	"""
	setLanguage
	
	Parameters
	----------
	Language:str
		Set dialog language (frf, enu, jpj...)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 222,
	#     "returnSignature": "v",
	#     "name": "setLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "setLanguage",
	#     "parameters": [
	#         {
	#             "name": "Language",
	#             "description": "Set dialog language (frf, enu, jpj...)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setLanguage", [Language])

def getLanguage() -> str:
	"""
	getLanguage
	
	Returns
	----------
	get the dialog language
	"""
	# NAOqi metadata:
	# {
	#     "uid": 223,
	#     "returnSignature": "s",
	#     "name": "getLanguage",
	#     "parametersSignature": "()",
	#     "description": "getLanguage",
	#     "parameters": [],
	#     "returnDescription": "get the dialog language"
	# }
	return call_method("ALDialog", "getLanguage", [])

def _startUpdate(variableName:str, variableValue:Any, message:str) -> None:
	"""
	startUpdate
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 224,
	#     "returnSignature": "v",
	#     "name": "_startUpdate",
	#     "parametersSignature": "(sms)",
	#     "description": "startUpdate",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_startUpdate", [variableName, variableValue, message])

def _startApp(variableName:str, variableValue:Any, message:str) -> None:
	"""
	startUpdate
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 225,
	#     "returnSignature": "v",
	#     "name": "_startApp",
	#     "parametersSignature": "(sms)",
	#     "description": "startUpdate",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_startApp", [variableName, variableValue, message])

def _packageInstalled(variableName:str, variableValue:Any, message:str) -> None:
	"""
	packageInstalled
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 226,
	#     "returnSignature": "v",
	#     "name": "_packageInstalled",
	#     "parametersSignature": "(sms)",
	#     "description": "packageInstalled",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_packageInstalled", [variableName, variableValue, message])

def _packageRemoved(variableName:str, variableValue:Any, message:str) -> None:
	"""
	_packageRemoved
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 227,
	#     "returnSignature": "v",
	#     "name": "_packageRemoved",
	#     "parametersSignature": "(sms)",
	#     "description": "_packageRemoved",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_packageRemoved", [variableName, variableValue, message])

def dialogAnswered(variableName:str, variableValue:Any, message:str) -> None:
	"""
	dialogAnswered
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 228,
	#     "returnSignature": "v",
	#     "name": "dialogAnswered",
	#     "parametersSignature": "(sms)",
	#     "description": "dialogAnswered",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "dialogAnswered", [variableName, variableValue, message])

def _compilationFinished(variableName:str, variableValue:Any, message:str) -> None:
	"""
	compilationFinished
	
	Parameters
	----------
	variableName:str
		variable name
	variableValue:Any
		variable value
	message:str
		message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 229,
	#     "returnSignature": "v",
	#     "name": "_compilationFinished",
	#     "parametersSignature": "(sms)",
	#     "description": "compilationFinished",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "variable value"
	#         },
	#         {
	#             "name": "message",
	#             "description": "message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_compilationFinished", [variableName, variableValue, message])

def setFocus(topicName:str) -> None:
	"""
	Give focus to a dialog
	
	Parameters
	----------
	topicName:str
		Topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 230,
	#     "returnSignature": "v",
	#     "name": "setFocus",
	#     "parametersSignature": "(s)",
	#     "description": "Give focus to a dialog",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "setFocus", [topicName])

def getFocus() -> str:
	"""
	Give focus to a dialog
	
	Returns
	----------
	Current focus name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 231,
	#     "returnSignature": "s",
	#     "name": "getFocus",
	#     "parametersSignature": "()",
	#     "description": "Give focus to a dialog",
	#     "parameters": [],
	#     "returnDescription": "Current focus name"
	# }
	return call_method("ALDialog", "getFocus", [])

def gotoTopic(topicName:str) -> None:
	"""
	Set the focus to a topic and make a proposal
	
	Parameters
	----------
	topicName:str
		Topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 232,
	#     "returnSignature": "v",
	#     "name": "gotoTopic",
	#     "parametersSignature": "(s)",
	#     "description": "Set the focus to a topic and make a proposal",
	#     "parameters": [
	#         {
	#             "name": "topicName",
	#             "description": "Topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "gotoTopic", [topicName])

def _enableOneBNFActivated(enableFullBNF:bool) -> None:
	"""
	Enable AI System
	
	Parameters
	----------
	enableFullBNF:bool
		Add all possible sentences in speech recognition
	"""
	# NAOqi metadata:
	# {
	#     "uid": 233,
	#     "returnSignature": "v",
	#     "name": "_enableOneBNFActivated",
	#     "parametersSignature": "(b)",
	#     "description": "Enable AI System",
	#     "parameters": [
	#         {
	#             "name": "enableFullBNF",
	#             "description": "Add all possible sentences in speech recognition"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_enableOneBNFActivated", [enableFullBNF])

def _enableAISystem(enableAISystem:bool) -> None:
	"""
	Enable AI System
	
	Parameters
	----------
	enableAISystem:bool
		Enable AI system
	"""
	# NAOqi metadata:
	# {
	#     "uid": 234,
	#     "returnSignature": "v",
	#     "name": "_enableAISystem",
	#     "parametersSignature": "(b)",
	#     "description": "Enable AI System",
	#     "parameters": [
	#         {
	#             "name": "enableAISystem",
	#             "description": "Enable AI system"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_enableAISystem", [enableAISystem])

def addFallback(language:str, name:str) -> None:
	"""
	Add a fallback plugin
	
	Parameters
	----------
	language:str
		The language of the plugin
	name:str
		The name of the plugin
	"""
	# NAOqi metadata:
	# {
	#     "uid": 235,
	#     "returnSignature": "v",
	#     "name": "addFallback",
	#     "parametersSignature": "(ss)",
	#     "description": "Add a fallback plugin",
	#     "parameters": [
	#         {
	#             "name": "language",
	#             "description": "The language of the plugin"
	#         },
	#         {
	#             "name": "name",
	#             "description": "The name of the plugin"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "addFallback", [language, name])

def removeFallback(language:str, name:str) -> None:
	"""
	Remove a fallback plugin
	
	Parameters
	----------
	language:str
		The language of the plugin
	name:str
		The name of the plugin
	"""
	# NAOqi metadata:
	# {
	#     "uid": 236,
	#     "returnSignature": "v",
	#     "name": "removeFallback",
	#     "parametersSignature": "(ss)",
	#     "description": "Remove a fallback plugin",
	#     "parameters": [
	#         {
	#             "name": "language",
	#             "description": "The language of the plugin"
	#         },
	#         {
	#             "name": "name",
	#             "description": "The name of the plugin"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "removeFallback", [language, name])

def _loadPrecompiledFile(filepath:str, bundleName:str, language:str) -> None:
	"""
	Load precompiled file
	
	Parameters
	----------
	filepath:str
		File path and filename
	bundleName:str
		Bundle name
	language:str
		Language name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 237,
	#     "returnSignature": "v",
	#     "name": "_loadPrecompiledFile",
	#     "parametersSignature": "(sss)",
	#     "description": "Load precompiled file",
	#     "parameters": [
	#         {
	#             "name": "filepath",
	#             "description": "File path and filename"
	#         },
	#         {
	#             "name": "bundleName",
	#             "description": "Bundle name"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_loadPrecompiledFile", [filepath, bundleName, language])

def _loadSLM(SLMFile:str, language:str) -> None:
	"""
	Load SLM
	
	Parameters
	----------
	SLMFile:str
		SLM path and filename
	language:str
		Language name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 238,
	#     "returnSignature": "v",
	#     "name": "_loadSLM",
	#     "parametersSignature": "(ss)",
	#     "description": "Load SLM",
	#     "parameters": [
	#         {
	#             "name": "SLMFile",
	#             "description": "SLM path and filename"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Language name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_loadSLM", [SLMFile, language])

def getLoadedTopics(language:str) -> List[str]:
	"""
	List loaded topics
	
	Parameters
	----------
	language:str
		Language name
	
	Returns
	----------
	List of loaded topics
	"""
	# NAOqi metadata:
	# {
	#     "uid": 239,
	#     "returnSignature": "[s]",
	#     "name": "getLoadedTopics",
	#     "parametersSignature": "(s)",
	#     "description": "List loaded topics",
	#     "parameters": [
	#         {
	#             "name": "language",
	#             "description": "Language name"
	#         }
	#     ],
	#     "returnDescription": "List of loaded topics"
	# }
	return call_method("ALDialog", "getLoadedTopics", [language])

def getAllLoadedTopics() -> List[str]:
	"""
	List loaded topics independent of language
	
	Returns
	----------
	List of loaded topics
	"""
	# NAOqi metadata:
	# {
	#     "uid": 240,
	#     "returnSignature": "[s]",
	#     "name": "getAllLoadedTopics",
	#     "parametersSignature": "()",
	#     "description": "List loaded topics independent of language",
	#     "parameters": [],
	#     "returnDescription": "List of loaded topics"
	# }
	return call_method("ALDialog", "getAllLoadedTopics", [])

def getActivatedTopics() -> List[str]:
	"""
	Get activated topics
	
	Returns
	----------
	List of activated topics
	"""
	# NAOqi metadata:
	# {
	#     "uid": 241,
	#     "returnSignature": "[s]",
	#     "name": "getActivatedTopics",
	#     "parametersSignature": "()",
	#     "description": "Get activated topics",
	#     "parameters": [],
	#     "returnDescription": "List of activated topics"
	# }
	return call_method("ALDialog", "getActivatedTopics", [])

def _setBehaviorEvent(Event:str) -> None:
	"""
	fast behavior start
	
	Parameters
	----------
	Event:str
		Event name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 242,
	#     "returnSignature": "v",
	#     "name": "_setBehaviorEvent",
	#     "parametersSignature": "(s)",
	#     "description": "fast behavior start",
	#     "parameters": [
	#         {
	#             "name": "Event",
	#             "description": "Event name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setBehaviorEvent", [Event])

def _fastModelActivation(enable:bool) -> None:
	"""
	triggers and proposal are activated in the model at compilation time
	
	Parameters
	----------
	enable:bool
		Enable fast activation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 243,
	#     "returnSignature": "v",
	#     "name": "_fastModelActivation",
	#     "parametersSignature": "(b)",
	#     "description": "triggers and proposal are activated in the model at compilation time",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "Enable fast activation"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_fastModelActivation", [enable])

def _byPassFastApproximateMatching(fastApproximative:bool) -> None:
	"""
	byPass fast approximative matching
	
	Parameters
	----------
	fastApproximative:bool
		enable fast approximative matching
	"""
	# NAOqi metadata:
	# {
	#     "uid": 244,
	#     "returnSignature": "v",
	#     "name": "_byPassFastApproximateMatching",
	#     "parametersSignature": "(b)",
	#     "description": "byPass fast approximative matching",
	#     "parameters": [
	#         {
	#             "name": "fastApproximative",
	#             "description": "enable fast approximative matching"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_byPassFastApproximateMatching", [fastApproximative])

def activateTag(tagName:str, topicName:str) -> None:
	"""
	activate a tag
	
	Parameters
	----------
	tagName:str
		tag name
	topicName:str
		topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 245,
	#     "returnSignature": "v",
	#     "name": "activateTag",
	#     "parametersSignature": "(ss)",
	#     "description": "activate a tag",
	#     "parameters": [
	#         {
	#             "name": "tagName",
	#             "description": "tag name"
	#         },
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "activateTag", [tagName, topicName])

def deactivateTag(tagName:str, topicName:str) -> None:
	"""
	deactivate a tag
	
	Parameters
	----------
	tagName:str
		tag name
	topicName:str
		topic name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 246,
	#     "returnSignature": "v",
	#     "name": "deactivateTag",
	#     "parametersSignature": "(ss)",
	#     "description": "deactivate a tag",
	#     "parameters": [
	#         {
	#             "name": "tagName",
	#             "description": "tag name"
	#         },
	#         {
	#             "name": "topicName",
	#             "description": "topic name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "deactivateTag", [tagName, topicName])

def _fallback(Question:str, Language:str) -> str:
	"""
	fallback (experimentatl)
	
	Parameters
	----------
	Question:str
		User question
	Language:str
		Language
	"""
	# NAOqi metadata:
	# {
	#     "uid": 247,
	#     "returnSignature": "s",
	#     "name": "_fallback",
	#     "parametersSignature": "(ss)",
	#     "description": "fallback (experimentatl)",
	#     "parameters": [
	#         {
	#             "name": "Question",
	#             "description": "User question"
	#         },
	#         {
	#             "name": "Language",
	#             "description": "Language"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_fallback", [Question, Language])

def resetAll() -> None:
	"""
	Reset all engine
	"""
	# NAOqi metadata:
	# {
	#     "uid": 248,
	#     "returnSignature": "v",
	#     "name": "resetAll",
	#     "parametersSignature": "()",
	#     "description": "Reset all engine",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "resetAll", [])

def _setSynchronicity(p0:bool) -> None:
	"""
	set Synchronicity
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 249,
	#     "returnSignature": "v",
	#     "name": "_setSynchronicity",
	#     "parametersSignature": "(b)",
	#     "description": "set Synchronicity",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setSynchronicity", [p0])

def _getSynchronicity() -> bool:
	"""
	get Synchronicity
	"""
	# NAOqi metadata:
	# {
	#     "uid": 250,
	#     "returnSignature": "b",
	#     "name": "_getSynchronicity",
	#     "parametersSignature": "()",
	#     "description": "get Synchronicity",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_getSynchronicity", [])

def insertUserData(variableName:str, variableValue:str, UserID:int) -> None:
	"""
	insert user data into dialog database
	
	Parameters
	----------
	variableName:str
		Variable name
	variableValue:str
		Variable value
	UserID:int
		User ID
	"""
	# NAOqi metadata:
	# {
	#     "uid": 251,
	#     "returnSignature": "v",
	#     "name": "insertUserData",
	#     "parametersSignature": "(ssi)",
	#     "description": "insert user data into dialog database",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "Variable name"
	#         },
	#         {
	#             "name": "variableValue",
	#             "description": "Variable value"
	#         },
	#         {
	#             "name": "UserID",
	#             "description": "User ID"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "insertUserData", [variableName, variableValue, UserID])

def _magicGet(p0:str) -> List[str]:
	"""
	get user data from dialog database
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 252,
	#     "returnSignature": "[s]",
	#     "name": "_magicGet",
	#     "parametersSignature": "(s)",
	#     "description": "get user data from dialog database",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_magicGet", [p0])

def getUserData(variableName:str, UserID:int) -> str:
	"""
	get user data from dialog database
	
	Parameters
	----------
	variableName:str
		Variable name
	UserID:int
		User ID
	
	Returns
	----------
	Value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 253,
	#     "returnSignature": "s",
	#     "name": "getUserData",
	#     "parametersSignature": "(si)",
	#     "description": "get user data from dialog database",
	#     "parameters": [
	#         {
	#             "name": "variableName",
	#             "description": "Variable name"
	#         },
	#         {
	#             "name": "UserID",
	#             "description": "User ID"
	#         }
	#     ],
	#     "returnDescription": "Value"
	# }
	return call_method("ALDialog", "getUserData", [variableName, UserID])

def getUserDataList(UserID:int) -> List[str]:
	"""
	get user data list from dialog database
	
	Parameters
	----------
	UserID:int
		User ID
	
	Returns
	----------
	Variable list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 254,
	#     "returnSignature": "[s]",
	#     "name": "getUserDataList",
	#     "parametersSignature": "(i)",
	#     "description": "get user data list from dialog database",
	#     "parameters": [
	#         {
	#             "name": "UserID",
	#             "description": "User ID"
	#         }
	#     ],
	#     "returnDescription": "Variable list"
	# }
	return call_method("ALDialog", "getUserDataList", [UserID])

def getUserList() -> List[int]:
	"""
	get user list from dialog database
	
	Returns
	----------
	User list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 255,
	#     "returnSignature": "[i]",
	#     "name": "getUserList",
	#     "parametersSignature": "()",
	#     "description": "get user list from dialog database",
	#     "parameters": [],
	#     "returnDescription": "User list"
	# }
	return call_method("ALDialog", "getUserList", [])

def removeUserData(UserID:int) -> None:
	"""
	remove a user from the database
	
	Parameters
	----------
	UserID:int
		User ID
	"""
	# NAOqi metadata:
	# {
	#     "uid": 256,
	#     "returnSignature": "v",
	#     "name": "removeUserData",
	#     "parametersSignature": "(i)",
	#     "description": "remove a user from the database",
	#     "parameters": [
	#         {
	#             "name": "UserID",
	#             "description": "User ID"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "removeUserData", [UserID])

def clearConcepts() -> None:
	"""
	clear concepts in DB
	"""
	# NAOqi metadata:
	# {
	#     "uid": 257,
	#     "returnSignature": "v",
	#     "name": "clearConcepts",
	#     "parametersSignature": "()",
	#     "description": "clear concepts in DB",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "clearConcepts", [])

def _speechDetected() -> None:
	"""
	callback
	"""
	# NAOqi metadata:
	# {
	#     "uid": 258,
	#     "returnSignature": "v",
	#     "name": "_speechDetected",
	#     "parametersSignature": "()",
	#     "description": "callback",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_speechDetected", [])

def enableSendingLogToCloud(EnableLog:bool) -> None:
	"""
	let the robot send log the cloud
	
	Parameters
	----------
	EnableLog:bool
		Enable log
	"""
	# NAOqi metadata:
	# {
	#     "uid": 259,
	#     "returnSignature": "v",
	#     "name": "enableSendingLogToCloud",
	#     "parametersSignature": "(b)",
	#     "description": "let the robot send log the cloud",
	#     "parameters": [
	#         {
	#             "name": "EnableLog",
	#             "description": "Enable log"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "enableSendingLogToCloud", [EnableLog])

def _encryptLog(EnableLog:bool) -> None:
	"""
	encrypt the logs sent tothe cloud
	
	Parameters
	----------
	EnableLog:bool
		Remove user log
	"""
	# NAOqi metadata:
	# {
	#     "uid": 260,
	#     "returnSignature": "v",
	#     "name": "_encryptLog",
	#     "parametersSignature": "(b)",
	#     "description": "encrypt the logs sent tothe cloud",
	#     "parameters": [
	#         {
	#             "name": "EnableLog",
	#             "description": "Remove user log"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_encryptLog", [EnableLog])

def isSendingLogToCloud() -> bool:
	"""
	check if the robot is sending the log to the cloud
	
	Returns
	----------
	True if currently logging
	"""
	# NAOqi metadata:
	# {
	#     "uid": 261,
	#     "returnSignature": "b",
	#     "name": "isSendingLogToCloud",
	#     "parametersSignature": "()",
	#     "description": "check if the robot is sending the log to the cloud",
	#     "parameters": [],
	#     "returnDescription": "True if currently logging"
	# }
	return call_method("ALDialog", "isSendingLogToCloud", [])

def _isEncryptingLog() -> bool:
	"""
	check if the robot is encrypting the log sent to the cloud
	
	Returns
	----------
	True if currently encrypt logging
	"""
	# NAOqi metadata:
	# {
	#     "uid": 262,
	#     "returnSignature": "b",
	#     "name": "_isEncryptingLog",
	#     "parametersSignature": "()",
	#     "description": "check if the robot is encrypting the log sent to the cloud",
	#     "parameters": [],
	#     "returnDescription": "True if currently encrypt logging"
	# }
	return call_method("ALDialog", "_isEncryptingLog", [])

def enableLogAudio(p0:bool) -> None:
	"""
	enable sending log audio (recorded conversation) to the cloud
	
	Parameters
	----------
	p0:bool
		
	
	Returns
	----------
	Enable audio log
	
	Bridge notes
	------------
	NAOqi's return description above doesn't match the method's signature, which returns nothing. This function follows the signature.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 263,
	#     "returnSignature": "v",
	#     "name": "enableLogAudio",
	#     "parametersSignature": "(b)",
	#     "description": "enable sending log audio (recorded conversation) to the cloud",
	#     "parameters": [],
	#     "returnDescription": "Enable audio log"
	# }
	return call_method("ALDialog", "enableLogAudio", [p0])

def _setDeletionCost(MatchingDeletionCost:float) -> None:
	"""
	The deletion cost (deleting from the sentence to match the model)
	
	Parameters
	----------
	MatchingDeletionCost:float
		Deletion cost
	"""
	# NAOqi metadata:
	# {
	#     "uid": 264,
	#     "returnSignature": "v",
	#     "name": "_setDeletionCost",
	#     "parametersSignature": "(f)",
	#     "description": "The deletion cost (deleting from the sentence to match the model)",
	#     "parameters": [
	#         {
	#             "name": "MatchingDeletionCost",
	#             "description": "Deletion cost"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setDeletionCost", [MatchingDeletionCost])

def _setInsertionCost(MatchingInsertCost:float) -> None:
	"""
	The insertion cost (inserting in the sentence to match the model)
	
	Parameters
	----------
	MatchingInsertCost:float
		Insert cost
	"""
	# NAOqi metadata:
	# {
	#     "uid": 265,
	#     "returnSignature": "v",
	#     "name": "_setInsertionCost",
	#     "parametersSignature": "(f)",
	#     "description": "The insertion cost (inserting in the sentence to match the model)",
	#     "parameters": [
	#         {
	#             "name": "MatchingInsertCost",
	#             "description": "Insert cost"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setInsertionCost", [MatchingInsertCost])

def _setSubstitutionCost(MatchingSubstitutionCost:float) -> None:
	"""
	The substitution cost
	
	Parameters
	----------
	MatchingSubstitutionCost:float
		Substitution cost
	"""
	# NAOqi metadata:
	# {
	#     "uid": 266,
	#     "returnSignature": "v",
	#     "name": "_setSubstitutionCost",
	#     "parametersSignature": "(f)",
	#     "description": "The substitution cost",
	#     "parameters": [
	#         {
	#             "name": "MatchingSubstitutionCost",
	#             "description": "Substitution cost"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setSubstitutionCost", [MatchingSubstitutionCost])

def _setStarCost(MatchingStarCost:float) -> None:
	"""
	The cost of matching an open element (such as _*)
	
	Parameters
	----------
	MatchingStarCost:float
		Wildcard cost
	"""
	# NAOqi metadata:
	# {
	#     "uid": 267,
	#     "returnSignature": "v",
	#     "name": "_setStarCost",
	#     "parametersSignature": "(f)",
	#     "description": "The cost of matching an open element (such as _*)",
	#     "parameters": [
	#         {
	#             "name": "MatchingStarCost",
	#             "description": "Wildcard cost"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setStarCost", [MatchingStarCost])

def _setApproximateMatchingThreshold(MatchingThreshold:float) -> None:
	"""
	The approximate matching threshold
	
	Parameters
	----------
	MatchingThreshold:float
		Matching threshold
	"""
	# NAOqi metadata:
	# {
	#     "uid": 268,
	#     "returnSignature": "v",
	#     "name": "_setApproximateMatchingThreshold",
	#     "parametersSignature": "(f)",
	#     "description": "The approximate matching threshold",
	#     "parameters": [
	#         {
	#             "name": "MatchingThreshold",
	#             "description": "Matching threshold"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setApproximateMatchingThreshold", [MatchingThreshold])

def _useAcrobaticMatching(EnableAccrobatic:bool) -> None:
	"""
	Tell to the model to use acrobatic matching
	
	Parameters
	----------
	EnableAccrobatic:bool
		Enable accrobatic matching
	"""
	# NAOqi metadata:
	# {
	#     "uid": 269,
	#     "returnSignature": "v",
	#     "name": "_useAcrobaticMatching",
	#     "parametersSignature": "(b)",
	#     "description": "Tell to the model to use acrobatic matching",
	#     "parameters": [
	#         {
	#             "name": "EnableAccrobatic",
	#             "description": "Enable accrobatic matching"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_useAcrobaticMatching", [EnableAccrobatic])

def _enableStatisticalMatching(EnableSemantic:bool) -> None:
	"""
	Tell to the model to use statistical matching
	
	Parameters
	----------
	EnableSemantic:bool
		Enable semantic matching
	"""
	# NAOqi metadata:
	# {
	#     "uid": 270,
	#     "returnSignature": "v",
	#     "name": "_enableStatisticalMatching",
	#     "parametersSignature": "(b)",
	#     "description": "Tell to the model to use statistical matching",
	#     "parameters": [
	#         {
	#             "name": "EnableSemantic",
	#             "description": "Enable semantic matching"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_enableStatisticalMatching", [EnableSemantic])

def _enablePhoneticMatching(EnablePhonetic:bool) -> None:
	"""
	Tell to the model to use phonetic matching
	
	Parameters
	----------
	EnablePhonetic:bool
		Enable phonetic matching
	"""
	# NAOqi metadata:
	# {
	#     "uid": 271,
	#     "returnSignature": "v",
	#     "name": "_enablePhoneticMatching",
	#     "parametersSignature": "(b)",
	#     "description": "Tell to the model to use phonetic matching",
	#     "parameters": [
	#         {
	#             "name": "EnablePhonetic",
	#             "description": "Enable phonetic matching"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_enablePhoneticMatching", [EnablePhonetic])

def _setSemanticModel(semanticPath:str, p1:str) -> None:
	"""
	Specify the directory and language of the statistical model
	
	Parameters
	----------
	semanticPath:str
		Semantic matching data path
	p1:str
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 272,
	#     "returnSignature": "v",
	#     "name": "_setSemanticModel",
	#     "parametersSignature": "(ss)",
	#     "description": "Specify the directory and language of the statistical model",
	#     "parameters": [
	#         {
	#             "name": "semanticPath",
	#             "description": "Semantic matching data path"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setSemanticModel", [semanticPath, p1])

def _isOnePassEnabled() -> bool:
	"""
	Is one pass enabled
	
	Returns
	----------
	Enable only one speech recognition
	"""
	# NAOqi metadata:
	# {
	#     "uid": 273,
	#     "returnSignature": "b",
	#     "name": "_isOnePassEnabled",
	#     "parametersSignature": "()",
	#     "description": "Is one pass enabled",
	#     "parameters": [],
	#     "returnDescription": "Enable only one speech recognition"
	# }
	return call_method("ALDialog", "_isOnePassEnabled", [])

def _setSLMUpperThreshold(SLMUpper:float) -> None:
	"""
	set SLM High treshold
	
	Parameters
	----------
	SLMUpper:float
		SLM Upper Threshold
	"""
	# NAOqi metadata:
	# {
	#     "uid": 274,
	#     "returnSignature": "v",
	#     "name": "_setSLMUpperThreshold",
	#     "parametersSignature": "(f)",
	#     "description": "set SLM High treshold",
	#     "parameters": [
	#         {
	#             "name": "SLMUpper",
	#             "description": "SLM Upper Threshold"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setSLMUpperThreshold", [SLMUpper])

def _enableSerialization(enableSerialization:bool) -> None:
	"""
	enable use of serialized models
	
	Parameters
	----------
	enableSerialization:bool
		Enable serialization
	"""
	# NAOqi metadata:
	# {
	#     "uid": 275,
	#     "returnSignature": "v",
	#     "name": "_enableSerialization",
	#     "parametersSignature": "(b)",
	#     "description": "enable use of serialized models",
	#     "parameters": [
	#         {
	#             "name": "enableSerialization",
	#             "description": "Enable serialization"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_enableSerialization", [enableSerialization])

def _deleteSerializationFiles() -> None:
	"""
	delete serializations files .ser .ini .bnf .lcf
	"""
	# NAOqi metadata:
	# {
	#     "uid": 276,
	#     "returnSignature": "v",
	#     "name": "_deleteSerializationFiles",
	#     "parametersSignature": "()",
	#     "description": "delete serializations files .ser .ini .bnf .lcf",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_deleteSerializationFiles", [])

def _cleanPhonetic() -> None:
	"""
	Clean phonetic
	"""
	# NAOqi metadata:
	# {
	#     "uid": 277,
	#     "returnSignature": "v",
	#     "name": "_cleanPhonetic",
	#     "parametersSignature": "()",
	#     "description": "Clean phonetic",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_cleanPhonetic", [])

def mute(p0:bool) -> None:
	"""
	mute dialog
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 278,
	#     "returnSignature": "v",
	#     "name": "mute",
	#     "parametersSignature": "(b)",
	#     "description": "mute dialog",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "mute", [p0])

def _copyInputConcepts(copyInput:bool) -> None:
	"""
	Set if the input concepts are copied
	
	Parameters
	----------
	copyInput:bool
		False to optimize
	"""
	# NAOqi metadata:
	# {
	#     "uid": 279,
	#     "returnSignature": "v",
	#     "name": "_copyInputConcepts",
	#     "parametersSignature": "(b)",
	#     "description": "Set if the input concepts are copied",
	#     "parameters": [
	#         {
	#             "name": "copyInput",
	#             "description": "False to optimize"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_copyInputConcepts", [copyInput])

def _copyOutputConcepts(copyOutput:bool) -> None:
	"""
	Set if the input concepts are copied
	
	Parameters
	----------
	copyOutput:bool
		False to optimize
	"""
	# NAOqi metadata:
	# {
	#     "uid": 280,
	#     "returnSignature": "v",
	#     "name": "_copyOutputConcepts",
	#     "parametersSignature": "(b)",
	#     "description": "Set if the input concepts are copied",
	#     "parameters": [
	#         {
	#             "name": "copyOutput",
	#             "description": "False to optimize"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_copyOutputConcepts", [copyOutput])

def generateSentences(destination:str, topic:str, language:str) -> None:
	"""
	Generate sentences
	
	Parameters
	----------
	destination:str
		file destination
	topic:str
		source topic
	language:str
		source language
	"""
	# NAOqi metadata:
	# {
	#     "uid": 281,
	#     "returnSignature": "v",
	#     "name": "generateSentences",
	#     "parametersSignature": "(sss)",
	#     "description": "Generate sentences",
	#     "parameters": [
	#         {
	#             "name": "destination",
	#             "description": "file destination"
	#         },
	#         {
	#             "name": "topic",
	#             "description": "source topic"
	#         },
	#         {
	#             "name": "language",
	#             "description": "source language"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "generateSentences", [destination, topic, language])

def _setLengthForAfterStarOptimization(length:int) -> None:
	"""
	Set the sentence length to apply -after star optimization- in matching
	
	Parameters
	----------
	length:int
		set length
	"""
	# NAOqi metadata:
	# {
	#     "uid": 282,
	#     "returnSignature": "v",
	#     "name": "_setLengthForAfterStarOptimization",
	#     "parametersSignature": "(i)",
	#     "description": "Set the sentence length to apply -after star optimization- in matching",
	#     "parameters": [
	#         {
	#             "name": "length",
	#             "description": "set length"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setLengthForAfterStarOptimization", [length])

def _setLengthForBeforeStarOptimization(length:int) -> None:
	"""
	Set the sentence length to apply -before star optimization- in matching
	
	Parameters
	----------
	length:int
		set length
	"""
	# NAOqi metadata:
	# {
	#     "uid": 283,
	#     "returnSignature": "v",
	#     "name": "_setLengthForBeforeStarOptimization",
	#     "parametersSignature": "(i)",
	#     "description": "Set the sentence length to apply -before star optimization- in matching",
	#     "parameters": [
	#         {
	#             "name": "length",
	#             "description": "set length"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setLengthForBeforeStarOptimization", [length])

def _onUserSessionFocused(p1:str, p2:Any, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:Any
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 284,
	#     "returnSignature": "v",
	#     "name": "_onUserSessionFocused",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_onUserSessionFocused", [p1, p2, p3])

def _onUserDeleted(p1:str, p2:Any, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:Any
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 285,
	#     "returnSignature": "v",
	#     "name": "_onUserDeleted",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_onUserDeleted", [p1, p2, p3])

def _us_getUserData(p1:str, p2:str, p3:str) -> Any:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 286,
	#     "returnSignature": "m",
	#     "name": "_us_getUserData",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_us_getUserData", [p1, p2, p3])

def _setUserSessionObeyed(is_obeyed:bool) -> None:
	"""
	Query if dialog sessions are controlled by ALUserSession
	
	Parameters
	----------
	is_obeyed:bool
		Bool. True if dialog should open/close sessions according to ALUserSession
	"""
	# NAOqi metadata:
	# {
	#     "uid": 287,
	#     "returnSignature": "v",
	#     "name": "_setUserSessionObeyed",
	#     "parametersSignature": "(b)",
	#     "description": "Query if dialog sessions are controlled by ALUserSession",
	#     "parameters": [
	#         {
	#             "name": "is_obeyed",
	#             "description": "Bool. True if dialog should open/close sessions according to ALUserSession"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setUserSessionObeyed", [is_obeyed])

def _isUserSessionObeyed() -> bool:
	"""
	Query if dialog sessions are controlled by ALUserSession
	
	Returns
	----------
	Bool. True if dialog will open/close sessions according to ALUserSession
	"""
	# NAOqi metadata:
	# {
	#     "uid": 288,
	#     "returnSignature": "b",
	#     "name": "_isUserSessionObeyed",
	#     "parametersSignature": "()",
	#     "description": "Query if dialog sessions are controlled by ALUserSession",
	#     "parameters": [],
	#     "returnDescription": "Bool. True if dialog will open/close sessions according to ALUserSession"
	# }
	return call_method("ALDialog", "_isUserSessionObeyed", [])

def getLanguageListISOToNU() -> Dict[str,str]:
	"""
	get language map ISO to NU format
	
	Returns
	----------
	get language map ISO to NU format
	"""
	# NAOqi metadata:
	# {
	#     "uid": 289,
	#     "returnSignature": "{ss}",
	#     "name": "getLanguageListISOToNU",
	#     "parametersSignature": "()",
	#     "description": "get language map ISO to NU format",
	#     "parameters": [],
	#     "returnDescription": "get language map ISO to NU format"
	# }
	return call_method("ALDialog", "getLanguageListISOToNU", [])

def getLanguageListNUToISO() -> Dict[str,str]:
	"""
	get language map NU to ISO format
	
	Returns
	----------
	get language map NU to ISO format
	"""
	# NAOqi metadata:
	# {
	#     "uid": 290,
	#     "returnSignature": "{ss}",
	#     "name": "getLanguageListNUToISO",
	#     "parametersSignature": "()",
	#     "description": "get language map NU to ISO format",
	#     "parameters": [],
	#     "returnDescription": "get language map NU to ISO format"
	# }
	return call_method("ALDialog", "getLanguageListNUToISO", [])

def getLanguageListLongToNU() -> Dict[str,str]:
	"""
	get language map Long to NU format
	
	Returns
	----------
	get language map Long to NU format
	"""
	# NAOqi metadata:
	# {
	#     "uid": 291,
	#     "returnSignature": "{ss}",
	#     "name": "getLanguageListLongToNU",
	#     "parametersSignature": "()",
	#     "description": "get language map Long to NU format",
	#     "parameters": [],
	#     "returnDescription": "get language map Long to NU format"
	# }
	return call_method("ALDialog", "getLanguageListLongToNU", [])

def getLanguageListNUToLong() -> Dict[str,str]:
	"""
	get language map NU to Long format
	
	Returns
	----------
	get language map NU to Long format
	"""
	# NAOqi metadata:
	# {
	#     "uid": 292,
	#     "returnSignature": "{ss}",
	#     "name": "getLanguageListNUToLong",
	#     "parametersSignature": "()",
	#     "description": "get language map NU to Long format",
	#     "parameters": [],
	#     "returnDescription": "get language map NU to Long format"
	# }
	return call_method("ALDialog", "getLanguageListNUToLong", [])

def convertNUToLong(Language:str) -> str:
	"""
	convert language from NU format to Long format
	
	Parameters
	----------
	Language:str
		language in NU format
	
	Returns
	----------
	language in Long format 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 293,
	#     "returnSignature": "s",
	#     "name": "convertNUToLong",
	#     "parametersSignature": "(s)",
	#     "description": "convert language from NU format to Long format",
	#     "parameters": [
	#         {
	#             "name": "Language",
	#             "description": "language in NU format"
	#         }
	#     ],
	#     "returnDescription": "language in Long format "
	# }
	return call_method("ALDialog", "convertNUToLong", [Language])

def convertLongToNU(Language:str) -> str:
	"""
	convert language from Long format to NU format
	
	Parameters
	----------
	Language:str
		language in Long format
	
	Returns
	----------
	language in NU format 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 294,
	#     "returnSignature": "s",
	#     "name": "convertLongToNU",
	#     "parametersSignature": "(s)",
	#     "description": "convert language from Long format to NU format",
	#     "parameters": [
	#         {
	#             "name": "Language",
	#             "description": "language in Long format"
	#         }
	#     ],
	#     "returnDescription": "language in NU format "
	# }
	return call_method("ALDialog", "convertLongToNU", [Language])

def convertISOToNU(Language:str) -> str:
	"""
	convert language from ISO format to NU format
	
	Parameters
	----------
	Language:str
		language in ISO format
	
	Returns
	----------
	language in NU format 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 295,
	#     "returnSignature": "s",
	#     "name": "convertISOToNU",
	#     "parametersSignature": "(s)",
	#     "description": "convert language from ISO format to NU format",
	#     "parameters": [
	#         {
	#             "name": "Language",
	#             "description": "language in ISO format"
	#         }
	#     ],
	#     "returnDescription": "language in NU format "
	# }
	return call_method("ALDialog", "convertISOToNU", [Language])

def convertNUToISO(Language:str) -> str:
	"""
	convert language from NU format to ISO format
	
	Parameters
	----------
	Language:str
		language in NU format
	
	Returns
	----------
	language in ISO format 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 296,
	#     "returnSignature": "s",
	#     "name": "convertNUToISO",
	#     "parametersSignature": "(s)",
	#     "description": "convert language from NU format to ISO format",
	#     "parameters": [
	#         {
	#             "name": "Language",
	#             "description": "language in NU format"
	#         }
	#     ],
	#     "returnDescription": "language in ISO format "
	# }
	return call_method("ALDialog", "convertNUToISO", [Language])

def enableSimulatedApps(simulateApps:bool) -> None:
	"""
	Define if applications will be launched or not
	
	Parameters
	----------
	simulateApps:bool
		set simulated apps
	"""
	# NAOqi metadata:
	# {
	#     "uid": 297,
	#     "returnSignature": "v",
	#     "name": "enableSimulatedApps",
	#     "parametersSignature": "(b)",
	#     "description": "Define if applications will be launched or not",
	#     "parameters": [
	#         {
	#             "name": "simulateApps",
	#             "description": "set simulated apps"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "enableSimulatedApps", [simulateApps])

def _setMachineLearningEnable(Enable:bool) -> None:
	"""
	Set whether to use machine learning techniques or not
	
	Parameters
	----------
	Enable:bool
		whether to enable it or not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 298,
	#     "returnSignature": "v",
	#     "name": "_setMachineLearningEnable",
	#     "parametersSignature": "(b)",
	#     "description": "Set whether to use machine learning techniques or not",
	#     "parameters": [
	#         {
	#             "name": "Enable",
	#             "description": "whether to enable it or not"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setMachineLearningEnable", [Enable])

def _isMachineLearningEnabled() -> bool:
	"""
	Get whether machine learning techniques are used or not
	
	Returns
	----------
	true if machine learning is enabled 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 299,
	#     "returnSignature": "b",
	#     "name": "_isMachineLearningEnabled",
	#     "parametersSignature": "()",
	#     "description": "Get whether machine learning techniques are used or not",
	#     "parameters": [],
	#     "returnDescription": "true if machine learning is enabled "
	# }
	return call_method("ALDialog", "_isMachineLearningEnabled", [])

def _clearLastMisunderstood() -> None:
	"""
	Remove the last misunderstood results
	"""
	# NAOqi metadata:
	# {
	#     "uid": 300,
	#     "returnSignature": "v",
	#     "name": "_clearLastMisunderstood",
	#     "parametersSignature": "()",
	#     "description": "Remove the last misunderstood results",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_clearLastMisunderstood", [])

def _isLastMisunderstoodEnabled() -> bool:
	"""
	Get whether the last misunderstood result is stored and used to improve confidences
	"""
	# NAOqi metadata:
	# {
	#     "uid": 301,
	#     "returnSignature": "b",
	#     "name": "_isLastMisunderstoodEnabled",
	#     "parametersSignature": "()",
	#     "description": "Get whether the last misunderstood result is stored and used to improve confidences",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_isLastMisunderstoodEnabled", [])

def _setLastMisunderstoodEnable(p0:bool) -> None:
	"""
	Set whether the last misunderstood result is stored and used to improve confidences
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 302,
	#     "returnSignature": "v",
	#     "name": "_setLastMisunderstoodEnable",
	#     "parametersSignature": "(b)",
	#     "description": "Set whether the last misunderstood result is stored and used to improve confidences",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDialog", "_setLastMisunderstoodEnable", [p0])

class _Signals:
	_activityRequestedByUser: Signal[[str]] = Signal("ALDialog", "_activityRequestedByUser")
	"""
	Bridge notes
	------------
	A signal sent by ALDialog on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
signals = _Signals()

