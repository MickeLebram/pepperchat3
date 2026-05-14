from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALMemory provides a centralized memory that can be used to store and retrieve named values. It also acts as a hub for the distribution of event notifications.
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
	return send_mfc("ALMemory", "version", [])

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
	return send_mfc("ALMemory", "ping", [])

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
	return send_mfc("ALMemory", "getMethodList", [])

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
	return send_mfc("ALMemory", "getMethodHelp", [methodName])

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
	return send_mfc("ALMemory", "getModuleHelp", [])

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
	return send_mfc("ALMemory", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALMemory", "wait", [id])

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
	return send_mfc("ALMemory", "isRunning", [id])

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
	return send_mfc("ALMemory", "stop", [id])

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
	return send_mfc("ALMemory", "getBrokerName", [])

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
	return send_mfc("ALMemory", "getUsage", [name])

def declareEvent_1(eventName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (declareEvent)
	
	Declares an event to allow future subscriptions to the event
	
	Parameters
	----------
	eventName:str
		The name of the event
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "declareEvent",
	    "parametersSignature": "(s)",
	    "description": "Declares an event to allow future subscriptions to the event",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "The name of the event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "declareEvent", [eventName])

def declareEvent_2(eventName:str, extractorName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (declareEvent)
	
	Declares an event to allow future subscriptions to the event
	
	Parameters
	----------
	eventName:str
		The name of the event
	extractorName:str
		The name of the extractor capable of creating the event
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "declareEvent",
	    "parametersSignature": "(ss)",
	    "description": "Declares an event to allow future subscriptions to the event",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "The name of the event"
	        },
	        {
	            "name": "extractorName",
	            "description": "The name of the extractor capable of creating the event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "declareEvent", [eventName, extractorName])

def getData(key:str) -> object:
	"""
	Gets the value of a key-value pair stored in memory
	
	Parameters
	----------
	key:str
		Name of the value.
	
	Returns
	----------
	The data as an ALValue. This can often be cast transparently into the original type.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "getData",
	    "parametersSignature": "(s)",
	    "description": "Gets the value of a key-value pair stored in memory",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the value."
	        }
	    ],
	    "returnDescription": "The data as an ALValue. This can often be cast transparently into the original type."
	}
	'''
	"""
	return send_mfc("ALMemory", "getData", [key])

def subscriber(eventName:str) -> object:
	"""
	Get an object wrapping a signal bound to the given ALMemory event. Creates the event if it does not exist.
	
	Parameters
	----------
	eventName:str
		Name of the ALMemory event
	
	Returns
	----------
	An AnyObject with a signal named "signal"
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "o",
	    "name": "subscriber",
	    "parametersSignature": "(s)",
	    "description": "Get an object wrapping a signal bound to the given ALMemory event. Creates the event if it does not exist.",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "Name of the ALMemory event"
	        }
	    ],
	    "returnDescription": "An AnyObject with a signal named \"signal\""
	}
	'''
	"""
	return send_mfc("ALMemory", "subscriber", [eventName])

def getTimestamp(key:str) -> object:
	"""
	Get data value and timestamp
	
	Parameters
	----------
	key:str
		Name of the variable
	
	Returns
	----------
	A list of all the data key names that contain the given string.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getTimestamp",
	    "parametersSignature": "(s)",
	    "description": "Get data value and timestamp",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the variable"
	        }
	    ],
	    "returnDescription": "A list of all the data key names that contain the given string."
	}
	'''
	"""
	return send_mfc("ALMemory", "getTimestamp", [key])

def getEventHistory(key:str) -> object:
	"""
	Get data value and timestamp
	
	Parameters
	----------
	key:str
		Name of the variable
	
	Returns
	----------
	A list of all the data key names that contain the given string.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "getEventHistory",
	    "parametersSignature": "(s)",
	    "description": "Get data value and timestamp",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the variable"
	        }
	    ],
	    "returnDescription": "A list of all the data key names that contain the given string."
	}
	'''
	"""
	return send_mfc("ALMemory", "getEventHistory", [key])

def getDataList(filter:str) -> List[str]:
	"""
	Gets a list of all key names that contain a given string
	
	Parameters
	----------
	filter:str
		A string used as the search term
	
	Returns
	----------
	A list of all the data key names that contain the given string.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[s]",
	    "name": "getDataList",
	    "parametersSignature": "(s)",
	    "description": "Gets a list of all key names that contain a given string",
	    "parameters": [
	        {
	            "name": "filter",
	            "description": "A string used as the search term"
	        }
	    ],
	    "returnDescription": "A list of all the data key names that contain the given string."
	}
	'''
	"""
	return send_mfc("ALMemory", "getDataList", [filter])

def getDataListName() -> List[str]:
	"""
	Gets the key names for all the key-value pairs in memory
	
	Returns
	----------
	A list containing the keys in memory
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "[s]",
	    "name": "getDataListName",
	    "parametersSignature": "()",
	    "description": "Gets the key names for all the key-value pairs in memory",
	    "parameters": [],
	    "returnDescription": "A list containing the keys in memory"
	}
	'''
	"""
	return send_mfc("ALMemory", "getDataListName", [])

def getDataPtr(key:str) -> object:
	"""
	Gets a pointer to 32 a bit data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.
	
	Parameters
	----------
	key:str
		Name of the data.
	
	Returns
	----------
	A pointer converted to int
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "X",
	    "name": "getDataPtr",
	    "parametersSignature": "(s)",
	    "description": "Gets a pointer to 32 a bit data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the data."
	        }
	    ],
	    "returnDescription": "A pointer converted to int"
	}
	'''
	"""
	return send_mfc("ALMemory", "getDataPtr", [key])

def getIntPtr(key:str) -> object:
	"""
	Gets a pointer to a int data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.
	
	Parameters
	----------
	key:str
		Name of the data.
	
	Returns
	----------
	A pointer to int
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "X",
	    "name": "getIntPtr",
	    "parametersSignature": "(s)",
	    "description": "Gets a pointer to a int data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the data."
	        }
	    ],
	    "returnDescription": "A pointer to int"
	}
	'''
	"""
	return send_mfc("ALMemory", "getIntPtr", [key])

def getFloatPtr(key:str) -> object:
	"""
	Gets a pointer to a float data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.
	
	Parameters
	----------
	key:str
		Name of the data.
	
	Returns
	----------
	A pointer to float
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "X",
	    "name": "getFloatPtr",
	    "parametersSignature": "(s)",
	    "description": "Gets a pointer to a float data item. Beware, the pointer will only be valid during the lifetime of the ALMemory object. Use with care, at initialization, not every loop. Insert a data item if needed. Throw if the data item has not the expected type. Only meaningful when called from code running in the same process as ALMemory.",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the data."
	        }
	    ],
	    "returnDescription": "A pointer to float"
	}
	'''
	"""
	return send_mfc("ALMemory", "getFloatPtr", [key])

def getEventList() -> List[str]:
	"""
	Gets a list containing the names of all the declared events
	
	Returns
	----------
	A list containing the names of all events
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "[s]",
	    "name": "getEventList",
	    "parametersSignature": "()",
	    "description": "Gets a list containing the names of all the declared events",
	    "parameters": [],
	    "returnDescription": "A list containing the names of all events"
	}
	'''
	"""
	return send_mfc("ALMemory", "getEventList", [])

def getExtractorEvent(extractorName:str) -> List[str]:
	"""
	Gets the list of all events generated by a given extractor
	
	Parameters
	----------
	extractorName:str
		The name of the extractor
	
	Returns
	----------
	A list containing the names of the events associated with the given extractor
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "[s]",
	    "name": "getExtractorEvent",
	    "parametersSignature": "(s)",
	    "description": "Gets the list of all events generated by a given extractor",
	    "parameters": [
	        {
	            "name": "extractorName",
	            "description": "The name of the extractor"
	        }
	    ],
	    "returnDescription": "A list containing the names of the events associated with the given extractor"
	}
	'''
	"""
	return send_mfc("ALMemory", "getExtractorEvent", [extractorName])

def getListData(keyList:object) -> object:
	"""
	Gets the values associated with the given list of keys. This is more efficient than calling getData many times, especially over the network.
	
	Parameters
	----------
	keyList:object
		An array containing the key names.
	
	Returns
	----------
	An array containing all the values corresponding to the given keys.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "m",
	    "name": "getListData",
	    "parametersSignature": "(m)",
	    "description": "Gets the values associated with the given list of keys. This is more efficient than calling getData many times, especially over the network.",
	    "parameters": [
	        {
	            "name": "keyList",
	            "description": "An array containing the key names."
	        }
	    ],
	    "returnDescription": "An array containing all the values corresponding to the given keys."
	}
	'''
	"""
	return send_mfc("ALMemory", "getListData", [keyList])

def getMicroEventList() -> List[str]:
	"""
	Gets a list containing the names of all the declared micro events
	
	Returns
	----------
	A list containing the names of all the microEvents
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[s]",
	    "name": "getMicroEventList",
	    "parametersSignature": "()",
	    "description": "Gets a list containing the names of all the declared micro events",
	    "parameters": [],
	    "returnDescription": "A list containing the names of all the microEvents"
	}
	'''
	"""
	return send_mfc("ALMemory", "getMicroEventList", [])

def getSubscribers(name:str) -> List[str]:
	"""
	Gets a list containing the names of subscribers to an event.
	
	Parameters
	----------
	name:str
		Name of the event or micro-event
	
	Returns
	----------
	List of subscriber names
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "[s]",
	    "name": "getSubscribers",
	    "parametersSignature": "(s)",
	    "description": "Gets a list containing the names of subscribers to an event.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event or micro-event"
	        }
	    ],
	    "returnDescription": "List of subscriber names"
	}
	'''
	"""
	return send_mfc("ALMemory", "getSubscribers", [name])

def getType(key:str) -> str:
	"""
	Gets the storage class of the stored data. This is not the underlying POD type.
	
	Parameters
	----------
	key:str
		Name of the variable
	
	Returns
	----------
	String type: Data, Event, MicroEvent
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "s",
	    "name": "getType",
	    "parametersSignature": "(s)",
	    "description": "Gets the storage class of the stored data. This is not the underlying POD type.",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the variable"
	        }
	    ],
	    "returnDescription": "String type: Data, Event, MicroEvent"
	}
	'''
	"""
	return send_mfc("ALMemory", "getType", [key])

def insertData_1(key:str, value:int) -> None:
	"""
	Note: This is one of the overloads of the original method (insertData)
	
	Inserts a key-value pair into memory, where value is an int
	
	Parameters
	----------
	key:str
		Name of the value to be inserted.
	value:int
		The int to be inserted
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "insertData",
	    "parametersSignature": "(si)",
	    "description": "Inserts a key-value pair into memory, where value is an int",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the value to be inserted."
	        },
	        {
	            "name": "value",
	            "description": "The int to be inserted"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "insertData", [key, value])

def insertData_2(key:str, value:float) -> None:
	"""
	Note: This is one of the overloads of the original method (insertData)
	
	Inserts a key-value pair into memory, where value is a float
	
	Parameters
	----------
	key:str
		Name of the value to be inserted.
	value:float
		The float to be inserted
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "insertData",
	    "parametersSignature": "(sf)",
	    "description": "Inserts a key-value pair into memory, where value is a float",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the value to be inserted."
	        },
	        {
	            "name": "value",
	            "description": "The float to be inserted"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "insertData", [key, value])

def insertData_3(key:str, value:str) -> None:
	"""
	Note: This is one of the overloads of the original method (insertData)
	
	Inserts a key-value pair into memory, where value is a string
	
	Parameters
	----------
	key:str
		Name of the value to be inserted.
	value:str
		The string to be inserted
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "insertData",
	    "parametersSignature": "(ss)",
	    "description": "Inserts a key-value pair into memory, where value is a string",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the value to be inserted."
	        },
	        {
	            "name": "value",
	            "description": "The string to be inserted"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "insertData", [key, value])

def insertData_4(key:str, data:object) -> None:
	"""
	Note: This is one of the overloads of the original method (insertData)
	
	Inserts a key-value pair into memory, where value is an ALValue
	
	Parameters
	----------
	key:str
		Name of the value to be inserted.
	data:object
		The ALValue to be inserted. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "insertData",
	    "parametersSignature": "(sm)",
	    "description": "Inserts a key-value pair into memory, where value is an ALValue",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the value to be inserted."
	        },
	        {
	            "name": "data",
	            "description": "The ALValue to be inserted. This could contain a basic type, or a more complex array. See the ALValue documentation for more information."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "insertData", [key, data])

def insertListData(list:object) -> None:
	"""
	Inserts a list of key-value pairs into memory.
	
	Parameters
	----------
	list:object
		An ALValue list of the form [[Key, Value],...]. Each item will be inserted.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "insertListData",
	    "parametersSignature": "(m)",
	    "description": "Inserts a list of key-value pairs into memory.",
	    "parameters": [
	        {
	            "name": "list",
	            "description": "An ALValue list of the form [[Key, Value],...]. Each item will be inserted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "insertListData", [list])

def raiseEvent(name:str, value:object) -> None:
	"""
	Publishes the given data to all subscribers.
	
	Parameters
	----------
	name:str
		Name of the event to raise.
	value:object
		The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "raiseEvent",
	    "parametersSignature": "(sm)",
	    "description": "Publishes the given data to all subscribers.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event to raise."
	        },
	        {
	            "name": "value",
	            "description": "The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "raiseEvent", [name, value])

def raiseMicroEvent(name:str, value:object) -> None:
	"""
	Publishes the given data to all subscribers.
	
	Parameters
	----------
	name:str
		Name of the event to raise.
	value:object
		The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "raiseMicroEvent",
	    "parametersSignature": "(sm)",
	    "description": "Publishes the given data to all subscribers.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event to raise."
	        },
	        {
	            "name": "value",
	            "description": "The data associated with the event. This could contain a basic type, or a more complex array. See the ALValue documentation for more information."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "raiseMicroEvent", [name, value])

def removeData(key:str) -> None:
	"""
	Removes a key-value pair from memory
	
	Parameters
	----------
	key:str
		Name of the data to be removed.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "removeData",
	    "parametersSignature": "(s)",
	    "description": "Removes a key-value pair from memory",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "Name of the data to be removed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "removeData", [key])

def removeEvent(name:str) -> None:
	"""
	Removes a event from memory and unsubscribes any exiting subscribers.
	
	Parameters
	----------
	name:str
		Name of the event to remove.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "removeEvent",
	    "parametersSignature": "(s)",
	    "description": "Removes a event from memory and unsubscribes any exiting subscribers.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event to remove."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "removeEvent", [name])

def removeMicroEvent(name:str) -> None:
	"""
	Removes a micro event from memory and unsubscribes any exiting subscribers.
	
	Parameters
	----------
	name:str
		Name of the event to remove.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "removeMicroEvent",
	    "parametersSignature": "(s)",
	    "description": "Removes a micro event from memory and unsubscribes any exiting subscribers.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event to remove."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "removeMicroEvent", [name])

def subscribeToEvent(name:str, callbackModule:str, callbackMethod:str) -> None:
	"""
	Subscribes to an event and automaticaly launches the module that declared itself as the generator of the event if required.
	
	Parameters
	----------
	name:str
		The name of the event to subscribe to
	callbackModule:str
		Name of the module to call with notifications
	callbackMethod:str
		Name of the module's method to call when a data is changed
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "subscribeToEvent",
	    "parametersSignature": "(sss)",
	    "description": "Subscribes to an event and automaticaly launches the module that declared itself as the generator of the event if required.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the event to subscribe to"
	        },
	        {
	            "name": "callbackModule",
	            "description": "Name of the module to call with notifications"
	        },
	        {
	            "name": "callbackMethod",
	            "description": "Name of the module's method to call when a data is changed"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "subscribeToEvent", [name, callbackModule, callbackMethod])

def subscribeToMicroEvent(name:str, callbackModule:str, callbackMessage:str, callbackMethod:str) -> None:
	"""
	Subscribes to a microEvent. Subscribed modules are notified on theircallback method whenever the data is updated, even if the new value is the same as the old value.
	
	Parameters
	----------
	name:str
		Name of the data.
	callbackModule:str
		Name of the module to call with notifications
	callbackMessage:str
		Message included in the notification. This can be used to disambiguate multiple subscriptions.
	callbackMethod:str
		Name of the module's method to call when a data is changed
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "subscribeToMicroEvent",
	    "parametersSignature": "(ssss)",
	    "description": "Subscribes to a microEvent. Subscribed modules are notified on theircallback method whenever the data is updated, even if the new value is the same as the old value.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the data."
	        },
	        {
	            "name": "callbackModule",
	            "description": "Name of the module to call with notifications"
	        },
	        {
	            "name": "callbackMessage",
	            "description": "Message included in the notification. This can be used to disambiguate multiple subscriptions."
	        },
	        {
	            "name": "callbackMethod",
	            "description": "Name of the module's method to call when a data is changed"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "subscribeToMicroEvent", [name, callbackModule, callbackMessage, callbackMethod])

def unregisterModuleReference(moduleName:str) -> None:
	"""
	Informs ALMemory that a module doesn't exist anymore.
	
	Parameters
	----------
	moduleName:str
		Name of the departing module.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "unregisterModuleReference",
	    "parametersSignature": "(s)",
	    "description": "Informs ALMemory that a module doesn't exist anymore.",
	    "parameters": [
	        {
	            "name": "moduleName",
	            "description": "Name of the departing module."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "unregisterModuleReference", [moduleName])

def _perf() -> None:
	"""
	ALMemory performance
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_perf",
	    "parametersSignature": "()",
	    "description": "ALMemory performance",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "_perf", [])

def unsubscribeToEvent(name:str, callbackModule:str) -> None:
	"""
	Unsubscribes a module from the given event. No further notifications will be received.
	
	Parameters
	----------
	name:str
		The name of the event
	callbackModule:str
		The name of the module that was given when subscribing.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "unsubscribeToEvent",
	    "parametersSignature": "(ss)",
	    "description": "Unsubscribes a module from the given event. No further notifications will be received.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the event"
	        },
	        {
	            "name": "callbackModule",
	            "description": "The name of the module that was given when subscribing."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "unsubscribeToEvent", [name, callbackModule])

def unsubscribeToMicroEvent(name:str, callbackModule:str) -> None:
	"""
	Unsubscribes from the given event. No further notifications will be received.
	
	Parameters
	----------
	name:str
		Name of the event.
	callbackModule:str
		The name of the module that was given when subscribing.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "unsubscribeToMicroEvent",
	    "parametersSignature": "(ss)",
	    "description": "Unsubscribes from the given event. No further notifications will be received.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the event."
	        },
	        {
	            "name": "callbackModule",
	            "description": "The name of the module that was given when subscribing."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "unsubscribeToMicroEvent", [name, callbackModule])

def _insertObject(name:str, buffer:object, bufferSize:int) -> None:
	"""
	Insert object in ALMemory. Please use ALMemoryFastAccess
	
	Parameters
	----------
	name:str
		ALMemory data name
	buffer:object
		buffer in ALValue
	bufferSize:int
		buffer size
	
	Returns
	----------
	return an array of data's string name.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "_insertObject",
	    "parametersSignature": "(smi)",
	    "description": "Insert object in ALMemory. Please use ALMemoryFastAccess",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "ALMemory data name"
	        },
	        {
	            "name": "buffer",
	            "description": "buffer in ALValue"
	        },
	        {
	            "name": "bufferSize",
	            "description": "buffer size"
	        }
	    ],
	    "returnDescription": "return an array of data's string name."
	}
	'''
	"""
	return send_mfc("ALMemory", "_insertObject", [name, buffer, bufferSize])

def _subscribeOnDataSetTimePolicy(name:str, callbackModule:str, nTimePolicy:int) -> None:
	"""
	Allows modules to change time policy of already subscribed data.
	
	Parameters
	----------
	name:str
		Name of the data.
	callbackModule:str
		Name of the module.
	nTimePolicy:int
		time of new policy in ms. Default is 0: no time policy: called at every change/insert. If timepolicy > 0, we will not notifiy under timepolicy even if data change under timepolicy frequency
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_subscribeOnDataSetTimePolicy",
	    "parametersSignature": "(ssi)",
	    "description": "Allows modules to change time policy of already subscribed data.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the data."
	        },
	        {
	            "name": "callbackModule",
	            "description": "Name of the module."
	        },
	        {
	            "name": "nTimePolicy",
	            "description": "time of new policy in ms. Default is 0: no time policy: called at every change/insert. If timepolicy > 0, we will not notifiy under timepolicy even if data change under timepolicy frequency"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "_subscribeOnDataSetTimePolicy", [name, callbackModule, nTimePolicy])

def _subscribeOnDataSetSynchronizeResponse(name:str, callbackModule:str, synchronizedResponse:bool) -> None:
	"""
	Receives notifications in the same order that the event were sent. This is slower than
	
	Parameters
	----------
	name:str
		Name of the data.
	callbackModule:str
		Name of the module.
	synchronizedResponse:bool
		True to receive notifications in the same order as events are sent
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "_subscribeOnDataSetSynchronizeResponse",
	    "parametersSignature": "(ssb)",
	    "description": "Receives notifications in the same order that the event were sent. This is slower than",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the data."
	        },
	        {
	            "name": "callbackModule",
	            "description": "Name of the module."
	        },
	        {
	            "name": "synchronizedResponse",
	            "description": "True to receive notifications in the same order as events are sent"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "_subscribeOnDataSetSynchronizeResponse", [name, callbackModule, synchronizedResponse])

def setDescription(name:str, description:str) -> None:
	"""
	Describe a key
	
	Parameters
	----------
	name:str
		Name of the key.
	description:str
		The description of the event (text format).
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "v",
	    "name": "setDescription",
	    "parametersSignature": "(ss)",
	    "description": "Describe a key",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the key."
	        },
	        {
	            "name": "description",
	            "description": "The description of the event (text format)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "setDescription", [name, description])

def getDescriptionList(keylist:List[str]) -> object:
	"""
	Descriptions of all given keys
	
	Parameters
	----------
	keylist:List[str]
		List of keys. (empty to get all descriptions)
	
	Returns
	----------
	an array of tuple (name, type, description) describing all keys.
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "m",
	    "name": "getDescriptionList",
	    "parametersSignature": "([s])",
	    "description": "Descriptions of all given keys",
	    "parameters": [
	        {
	            "name": "keylist",
	            "description": "List of keys. (empty to get all descriptions)"
	        }
	    ],
	    "returnDescription": "an array of tuple (name, type, description) describing all keys."
	}
	'''
	"""
	return send_mfc("ALMemory", "getDescriptionList", [keylist])

def addMapping_1(service:str, signal:str, event:str) -> None:
	"""
	Note: This is one of the overloads of the original method (addMapping)
	
	Add a mapping between signal and event
	
	Parameters
	----------
	service:str
		Name of the service
	signal:str
		Name of the signal
	event:str
		Name of the event
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "addMapping",
	    "parametersSignature": "(sss)",
	    "description": "Add a mapping between signal and event",
	    "parameters": [
	        {
	            "name": "service",
	            "description": "Name of the service"
	        },
	        {
	            "name": "signal",
	            "description": "Name of the signal"
	        },
	        {
	            "name": "event",
	            "description": "Name of the event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "addMapping", [service, signal, event])

def addMapping_2(service:str, signalEvent:Dict[str,str]) -> None:
	"""
	Note: This is one of the overloads of the original method (addMapping)
	
	Add a mapping between signal and event
	
	Parameters
	----------
	service:str
		Name of the service
	signalEvent:Dict[str,str]
		A map of signal corresponding to event
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "addMapping",
	    "parametersSignature": "(s{ss})",
	    "description": "Add a mapping between signal and event",
	    "parameters": [
	        {
	            "name": "service",
	            "description": "Name of the service"
	        },
	        {
	            "name": "signalEvent",
	            "description": "A map of signal corresponding to event"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMemory", "addMapping", [service, signalEvent])

