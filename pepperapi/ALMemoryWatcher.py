from .gentypes import *
from .robot_client import send_mfc
import json
"""
This is a module design to buffer and log values from ALMemory
"""
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
	return send_mfc("ALMemoryWatcher", "version", [])

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
	return send_mfc("ALMemoryWatcher", "ping", [])

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
	return send_mfc("ALMemoryWatcher", "getMethodList", [])

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
	return send_mfc("ALMemoryWatcher", "getMethodHelp", [methodName])

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
	return send_mfc("ALMemoryWatcher", "getModuleHelp", [])

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
	return send_mfc("ALMemoryWatcher", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALMemoryWatcher", "wait", [id])

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
	return send_mfc("ALMemoryWatcher", "isRunning", [id])

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
	return send_mfc("ALMemoryWatcher", "stop", [id])

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
	return send_mfc("ALMemoryWatcher", "getBrokerName", [])

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
	return send_mfc("ALMemoryWatcher", "getUsage", [name])

def listeners() -> List[str]:
	"""
	get the list of listened ALMemory keys
	
	Returns
	----------
	a list of ALMemory keys
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "[s]",
	    "name": "listeners",
	    "parametersSignature": "()",
	    "description": "get the list of listened ALMemory keys",
	    "parameters": [],
	    "returnDescription": "a list of ALMemory keys"
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "listeners", [])

def addListener_1(name:str, interval:int) -> None:
	"""
	Note: This is one of the overloads of the original method (addListener)
	
	add an ALMemory key to the list of keys to listen to
	
	Parameters
	----------
	name:str
		the complete name of the ALMemory key
	interval:int
		interval of time the system should wait before retrieving this key value again
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "addListener",
	    "parametersSignature": "(si)",
	    "description": "add an ALMemory key to the list of keys to listen to",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "the complete name of the ALMemory key"
	        },
	        {
	            "name": "interval",
	            "description": "interval of time the system should wait before retrieving this key value again"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "addListener", [name, interval])

def addListener_2(name:str) -> None:
	"""
	Note: This is one of the overloads of the original method (addListener)
	
	add an ALMemory key to the list of keys to listen to
	
	Parameters
	----------
	name:str
		the complete name of the ALMemory key
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "addListener",
	    "parametersSignature": "(s)",
	    "description": "add an ALMemory key to the list of keys to listen to",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "the complete name of the ALMemory key"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "addListener", [name])

def addListeners_1(listNames:List[str], interval:int) -> None:
	"""
	Note: This is one of the overloads of the original method (addListeners)
	
	add a list of ALMemory keys to the list of keys to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of complete names of ALMemory keys
	interval:int
		interval of time the system should wait before retrieving this key value again
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "addListeners",
	    "parametersSignature": "([s]i)",
	    "description": "add a list of ALMemory keys to the list of keys to listen",
	    "parameters": [
	        {
	            "name": "listNames",
	            "description": "the vector of complete names of ALMemory keys"
	        },
	        {
	            "name": "interval",
	            "description": "interval of time the system should wait before retrieving this key value again"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "addListeners", [listNames, interval])

def addListeners_2(listNames:List[str]) -> None:
	"""
	Note: This is one of the overloads of the original method (addListeners)
	
	add a list of ALMemory keys to the list of keys to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of complete names of ALMemory keys
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "addListeners",
	    "parametersSignature": "([s])",
	    "description": "add a list of ALMemory keys to the list of keys to listen",
	    "parameters": [
	        {
	            "name": "listNames",
	            "description": "the vector of complete names of ALMemory keys"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "addListeners", [listNames])

def removeAllListeners() -> None:
	"""
	remove all keys listened to
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "removeAllListeners",
	    "parametersSignature": "()",
	    "description": "remove all keys listened to",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "removeAllListeners", [])

def removeListener(name:str) -> None:
	"""
	remove a key from the list to listen to
	
	Parameters
	----------
	name:str
		the name of the key to stop to listen
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "removeListener",
	    "parametersSignature": "(s)",
	    "description": "remove a key from the list to listen to",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "the name of the key to stop to listen"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "removeListener", [name])

def removeListeners(listNames:List[str]) -> None:
	"""
	remove a list of key from the list to listen
	
	Parameters
	----------
	listNames:List[str]
		the vector of names of key to stop to listen
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "removeListeners",
	    "parametersSignature": "([s])",
	    "description": "remove a list of key from the list to listen",
	    "parameters": [
	        {
	            "name": "listNames",
	            "description": "the vector of names of key to stop to listen"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "removeListeners", [listNames])

def getData() -> object:
	"""
	return an ALValue containing all buffered data                                       since the last call of getData().
	
	Returns
	----------
	The complete array of all buffered data
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "getData",
	    "parametersSignature": "()",
	    "description": "return an ALValue containing all buffered data                                       since the last call of getData().",
	    "parameters": [],
	    "returnDescription": "The complete array of all buffered data"
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "getData", [])

def clearBuffer() -> None:
	"""
	remove all buffered data.                                           The list of keys listened to keeps unchanged.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "clearBuffer",
	    "parametersSignature": "()",
	    "description": "remove all buffered data.                                           The list of keys listened to keeps unchanged.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "clearBuffer", [])

def isWatching() -> bool:
	"""
	tells whether keys are watched and data being gathered.
	
	Returns
	----------
	true if keys are being watched.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "b",
	    "name": "isWatching",
	    "parametersSignature": "()",
	    "description": "tells whether keys are watched and data being gathered.",
	    "parameters": [],
	    "returnDescription": "true if keys are being watched."
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "isWatching", [])

def startWatching(period:int) -> None:
	"""
	start listening to selected keys from ALMemory
	
	Parameters
	----------
	period:int
		the time between two listen of ALMemory keys, in milliseconds.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "startWatching",
	    "parametersSignature": "(i)",
	    "description": "start listening to selected keys from ALMemory",
	    "parameters": [
	        {
	            "name": "period",
	            "description": "the time between two listen of ALMemory keys, in milliseconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "startWatching", [period])

def stopWatching() -> None:
	"""
	stop listening selected keys from ALMemory.                                    List of listened keys and associated buffers keep unchanged.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "stopWatching",
	    "parametersSignature": "()",
	    "description": "stop listening selected keys from ALMemory.                                    List of listened keys and associated buffers keep unchanged.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "stopWatching", [])

def _mainThread() -> None:
	"""
	simple loop calling buffer update every "period" milliseconds
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_mainThread",
	    "parametersSignature": "()",
	    "description": "simple loop calling buffer update every \"period\" milliseconds",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "_mainThread", [])

def setPeriodMs(period:int) -> None:
	"""
	edit "period" value between two buffering.
	
	Parameters
	----------
	period:int
		the new period (in ms) to apply.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "setPeriodMs",
	    "parametersSignature": "(i)",
	    "description": "edit \"period\" value between two buffering.",
	    "parameters": [
	        {
	            "name": "period",
	            "description": "the new period (in ms) to apply."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "setPeriodMs", [period])

def _onEventNotify(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when an event we have subscribe to has changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_onEventNotify",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when an event we have subscribe to has changed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "_onEventNotify", [dataName, dataValue, message])

def _onKeyAdded(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "_onKeyAdded",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when a key is removed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "_onKeyAdded", [dataName, dataValue, message])

def _onKeyRemoved(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when a key is removed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "_onKeyRemoved",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when a key is removed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "_onKeyRemoved", [dataName, dataValue, message])

def _onKeyTypeChanged(dataName:str, dataValue:object, message:object) -> None:
	"""
	Be notified when the type of a key is changed in ALMemory
	
	Parameters
	----------
	dataName:str
		name of the data
	dataValue:object
		value of the data
	message:object
		callback message
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_onKeyTypeChanged",
	    "parametersSignature": "(smm)",
	    "description": "Be notified when the type of a key is changed in ALMemory",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "name of the data"
	        },
	        {
	            "name": "dataValue",
	            "description": "value of the data"
	        },
	        {
	            "name": "message",
	            "description": "callback message"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemoryWatcher", "_onKeyTypeChanged", [dataName, dataValue, message])

