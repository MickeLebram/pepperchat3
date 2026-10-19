"""
This is a module design to buffer and log values from ALMemory
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

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
	return call_method("ALMemoryWatcher", "version", [])

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
	return call_method("ALMemoryWatcher", "ping", [])

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
	return call_method("ALMemoryWatcher", "getMethodList", [])

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
	return call_method("ALMemoryWatcher", "getMethodHelp", [methodName])

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
	return call_method("ALMemoryWatcher", "getModuleHelp", [])

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
	return call_method("ALMemoryWatcher", "getBrokerName", [])

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
	return call_method("ALMemoryWatcher", "getUsage", [name])

def listeners() -> List[str]:
	"""
	get the list of listened ALMemory keys
	
	Returns
	----------
	a list of ALMemory keys
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "[s]",
	#     "name": "listeners",
	#     "parametersSignature": "()",
	#     "description": "get the list of listened ALMemory keys",
	#     "parameters": [],
	#     "returnDescription": "a list of ALMemory keys"
	# }
	return call_method("ALMemoryWatcher", "listeners", [])

@overload
def addListener(name:str, /) -> None:
	"""
	add an ALMemory key to the list of keys to listen to
	
	Parameters
	----------
	name:str
		the complete name of the ALMemory key
	
	Bridge notes
	------------
	addListener has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "addListener",
	#     "parametersSignature": "(s)",
	#     "description": "add an ALMemory key to the list of keys to listen to",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "the complete name of the ALMemory key"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def addListener(name:str, interval:int, /) -> None:
	"""
	add an ALMemory key to the list of keys to listen to
	
	Parameters
	----------
	name:str
		the complete name of the ALMemory key
	interval:int
		interval of time the system should wait before retrieving this key value again
	
	Bridge notes
	------------
	addListener has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "addListener",
	#     "parametersSignature": "(si)",
	#     "description": "add an ALMemory key to the list of keys to listen to",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "the complete name of the ALMemory key"
	#         },
	#         {
	#             "name": "interval",
	#             "description": "interval of time the system should wait before retrieving this key value again"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def addListener(*args, **kwargs):
	"""
	Bridge notes
	------------
	addListener has 2 variants on the robot:
	- addListener(name:str)
	- addListener(name:str, interval:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALMemoryWatcher.addListener has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALMemoryWatcher", "addListener", list(args))

@overload
def addListeners(listNames:List[str], /) -> None:
	"""
	add a list of ALMemory keys to the list of keys to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of complete names of ALMemory keys
	
	Bridge notes
	------------
	addListeners has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "addListeners",
	#     "parametersSignature": "([s])",
	#     "description": "add a list of ALMemory keys to the list of keys to listen",
	#     "parameters": [
	#         {
	#             "name": "listNames",
	#             "description": "the vector of complete names of ALMemory keys"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def addListeners(listNames:List[str], interval:int, /) -> None:
	"""
	add a list of ALMemory keys to the list of keys to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of complete names of ALMemory keys
	interval:int
		interval of time the system should wait before retrieving this key value again
	
	Bridge notes
	------------
	addListeners has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "addListeners",
	#     "parametersSignature": "([s]i)",
	#     "description": "add a list of ALMemory keys to the list of keys to listen",
	#     "parameters": [
	#         {
	#             "name": "listNames",
	#             "description": "the vector of complete names of ALMemory keys"
	#         },
	#         {
	#             "name": "interval",
	#             "description": "interval of time the system should wait before retrieving this key value again"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def addListeners(*args, **kwargs):
	"""
	Bridge notes
	------------
	addListeners has 2 variants on the robot:
	- addListeners(listNames:List[str])
	- addListeners(listNames:List[str], interval:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALMemoryWatcher.addListeners has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALMemoryWatcher", "addListeners", list(args))

def removeAllListeners() -> None:
	"""
	remove all keys listened to
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "removeAllListeners",
	#     "parametersSignature": "()",
	#     "description": "remove all keys listened to",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "removeAllListeners", [])

def removeListener(name:str) -> None:
	"""
	remove a key from the list to listen to
	
	Parameters
	----------
	name:str
		the name of the key to stop to listen
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "removeListener",
	#     "parametersSignature": "(s)",
	#     "description": "remove a key from the list to listen to",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "the name of the key to stop to listen"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "removeListener", [name])

def removeListeners(listNames:List[str]) -> None:
	"""
	remove a list of key from the list to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of names of key to stop to listen
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "removeListeners",
	#     "parametersSignature": "([s])",
	#     "description": "remove a list of key from the list to listen",
	#     "parameters": [
	#         {
	#             "name": "listNames",
	#             "description": "the vector of names of key to stop to listen"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "removeListeners", [listNames])

def getData() -> Any:
	"""
	return an ALValue containing all buffered data                                       since the last call of getData().
	
	Returns
	----------
	The complete array of all buffered data
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "m",
	#     "name": "getData",
	#     "parametersSignature": "()",
	#     "description": "return an ALValue containing all buffered data                                       since the last call of getData().",
	#     "parameters": [],
	#     "returnDescription": "The complete array of all buffered data"
	# }
	return call_method("ALMemoryWatcher", "getData", [])

def clearBuffer() -> None:
	"""
	remove all buffered data.                                           The list of keys listened to keeps unchanged.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "clearBuffer",
	#     "parametersSignature": "()",
	#     "description": "remove all buffered data.                                           The list of keys listened to keeps unchanged.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "clearBuffer", [])

def isWatching() -> bool:
	"""
	tells whether keys are watched and data being gathered.
	
	Returns
	----------
	true if keys are being watched.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "b",
	#     "name": "isWatching",
	#     "parametersSignature": "()",
	#     "description": "tells whether keys are watched and data being gathered.",
	#     "parameters": [],
	#     "returnDescription": "true if keys are being watched."
	# }
	return call_method("ALMemoryWatcher", "isWatching", [])

def startWatching(period:int) -> None:
	"""
	start listening to selected keys from ALMemory
	
	Parameters
	----------
	period:int
		the time between two listen of ALMemory keys, in milliseconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "startWatching",
	#     "parametersSignature": "(i)",
	#     "description": "start listening to selected keys from ALMemory",
	#     "parameters": [
	#         {
	#             "name": "period",
	#             "description": "the time between two listen of ALMemory keys, in milliseconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "startWatching", [period])

def stopWatching() -> None:
	"""
	stop listening selected keys from ALMemory.                                    List of listened keys and associated buffers keep unchanged.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "stopWatching",
	#     "parametersSignature": "()",
	#     "description": "stop listening selected keys from ALMemory.                                    List of listened keys and associated buffers keep unchanged.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "stopWatching", [])

def _mainThread() -> None:
	"""
	simple loop calling buffer update every "period" milliseconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_mainThread",
	#     "parametersSignature": "()",
	#     "description": "simple loop calling buffer update every \"period\" milliseconds",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "_mainThread", [])

def setPeriodMs(period:int) -> None:
	"""
	edit "period" value between two buffering.
	
	Parameters
	----------
	period:int
		the new period (in ms) to apply.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "setPeriodMs",
	#     "parametersSignature": "(i)",
	#     "description": "edit \"period\" value between two buffering.",
	#     "parameters": [
	#         {
	#             "name": "period",
	#             "description": "the new period (in ms) to apply."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMemoryWatcher", "setPeriodMs", [period])

def _onEventNotify(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when an event we have subscribe to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_onEventNotify",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when an event we have subscribe to has changed in ALMemory",
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
	return call_method("ALMemoryWatcher", "_onEventNotify", [dataName, dataValue, message])

def _onKeyAdded(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_onKeyAdded",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when a key is removed in ALMemory",
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
	return call_method("ALMemoryWatcher", "_onKeyAdded", [dataName, dataValue, message])

def _onKeyRemoved(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "_onKeyRemoved",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when a key is removed in ALMemory",
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
	return call_method("ALMemoryWatcher", "_onKeyRemoved", [dataName, dataValue, message])

def _onKeyTypeChanged(dataName:str, dataValue:Any, message:Any) -> None:
	"""
	Be notified when the type of a key is changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:Any
		value of the data
	message:Any
		callback message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_onKeyTypeChanged",
	#     "parametersSignature": "(smm)",
	#     "description": "Be notified when the type of a key is changed in ALMemory",
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
	return call_method("ALMemoryWatcher", "_onKeyTypeChanged", [dataName, dataValue, message])

