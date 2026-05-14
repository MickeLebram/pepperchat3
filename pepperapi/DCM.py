from .gentypes import *
from .robot_client import send_mfc
import json
"""
Manage link with devices (sensors and actuators). See specific documentation.
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
	return send_mfc("DCM", "version", [])

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
	return send_mfc("DCM", "ping", [])

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
	return send_mfc("DCM", "getMethodList", [])

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
	return send_mfc("DCM", "getMethodHelp", [methodName])

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
	return send_mfc("DCM", "getModuleHelp", [])

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
	return send_mfc("DCM", "wait", [id, timeoutPeriod])

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
	return send_mfc("DCM", "wait", [id])

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
	return send_mfc("DCM", "isRunning", [id])

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
	return send_mfc("DCM", "stop", [id])

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
	return send_mfc("DCM", "getBrokerName", [])

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
	return send_mfc("DCM", "getUsage", [name])

def set(commands:object) -> None:
	"""
	Call this function to send a timed-command list to an actuator
	
	Parameters
	----------
	commands:object
		AL::ALValue with all data
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "set",
	    "parametersSignature": "(m)",
	    "description": "Call this function to send a timed-command list to an actuator",
	    "parameters": [
	        {
	            "name": "commands",
	            "description": "AL::ALValue with all data"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("DCM", "set", [commands])

def setAlias_1(commands:object) -> None:
	"""
	Note: This is one of the overloads of the original method (setAlias)
	
	Call this function to send timed-command list to an alias (list of actuators)
	
	Parameters
	----------
	commands:object
		AL::ALValue with all data
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "setAlias",
	    "parametersSignature": "(m)",
	    "description": "Call this function to send timed-command list to an alias (list of actuators)",
	    "parameters": [
	        {
	            "name": "commands",
	            "description": "AL::ALValue with all data"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("DCM", "setAlias", [commands])

def setAlias_2(name:str, time:int, commands:List[float]) -> None:
	"""
	Note: This is one of the overloads of the original method (setAlias)
	
	Call this function to send timed-command list to an alias (list of actuators) with "ClearAll" merge startegy
	
	Parameters
	----------
	name:str
		alias name
	time:int
		time for the timed command
	commands:List[float]
		std::vector<float> with all commands
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "setAlias",
	    "parametersSignature": "(si[f])",
	    "description": "Call this function to send timed-command list to an alias (list of actuators) with \"ClearAll\" merge startegy",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "alias name"
	        },
	        {
	            "name": "time",
	            "description": "time for the timed command"
	        },
	        {
	            "name": "commands",
	            "description": "std::vector<float> with all commands"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("DCM", "setAlias", [name, time, commands])

def getTime(offset:int) -> int:
	"""
	Return the DCM time
	
	Parameters
	----------
	offset:int
		optional time in ms (signed) to add/remove
	
	Returns
	----------
	An integer (could be signed) with the DCM time
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "getTime",
	    "parametersSignature": "(i)",
	    "description": "Return the DCM time",
	    "parameters": [
	        {
	            "name": "offset",
	            "description": "optional time in ms (signed) to add/remove"
	        }
	    ],
	    "returnDescription": "An integer (could be signed) with the DCM time"
	}
	'''
	"""
	return send_mfc("DCM", "getTime", [offset])

def createAlias(alias:object) -> object:
	"""
	Create or change an alias (list of actuators)
	
	Parameters
	----------
	alias:object
		Alias name and description
	
	Returns
	----------
	Same as pParams, but with the name removed if the actuator is not found
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "createAlias",
	    "parametersSignature": "(m)",
	    "description": "Create or change an alias (list of actuators)",
	    "parameters": [
	        {
	            "name": "alias",
	            "description": "Alias name and description"
	        }
	    ],
	    "returnDescription": "Same as pParams, but with the name removed if the actuator is not found"
	}
	'''
	"""
	return send_mfc("DCM", "createAlias", [alias])

def getPrefix() -> object:
	"""
	Return the STM base name
	
	Returns
	----------
	the STM base name for all device/sensors (1st string in the array) and all devices (2nd string in the array)
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getPrefix",
	    "parametersSignature": "()",
	    "description": "Return the STM base name",
	    "parameters": [],
	    "returnDescription": "the STM base name for all device/sensors (1st string in the array) and all devices (2nd string in the array)"
	}
	'''
	"""
	return send_mfc("DCM", "getPrefix", [])

def special(result:str) -> None:
	"""
	Special DCM commands
	
	Parameters
	----------
	result:str
		one string and could be Reset, Version, Chain, Diagnostic, Config
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "special",
	    "parametersSignature": "(s)",
	    "description": "Special DCM commands",
	    "parameters": [
	        {
	            "name": "result",
	            "description": "one string and could be Reset, Version, Chain, Diagnostic, Config"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("DCM", "special", [result])

def calibration(calibrationInput:object) -> None:
	"""
	Calibration of a joint
	
	Parameters
	----------
	calibrationInput:object
		A complex ALValue. See red documentation
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "calibration",
	    "parametersSignature": "(m)",
	    "description": "Calibration of a joint",
	    "parameters": [
	        {
	            "name": "calibrationInput",
	            "description": "A complex ALValue. See red documentation"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("DCM", "calibration", [calibrationInput])

def preferences(action:str, target:str, keyName:str, keyValue:object) -> int:
	"""
	Save updated value from DCM in XML pref file
	
	Parameters
	----------
	action:str
		string : 'Save' 'Load' 'Add'
	target:str
		string : 'Chest' 'Head' 'Main' 'All' 
	keyName:str
		The name of the key if action = 'Add'.
	keyValue:object
		The ALVAlue of the key to add
	
	Returns
	----------
	Nothing
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "preferences",
	    "parametersSignature": "(sssm)",
	    "description": "Save updated value from DCM in XML pref file",
	    "parameters": [
	        {
	            "name": "action",
	            "description": "string : 'Save' 'Load' 'Add'"
	        },
	        {
	            "name": "target",
	            "description": "string : 'Chest' 'Head' 'Main' 'All' "
	        },
	        {
	            "name": "keyName",
	            "description": "The name of the key if action = 'Add'."
	        },
	        {
	            "name": "keyValue",
	            "description": "The ALVAlue of the key to add"
	        }
	    ],
	    "returnDescription": "Nothing"
	}
	'''
	"""
	return send_mfc("DCM", "preferences", [action, target, keyName, keyValue])

def _injectionAdd(key:List[str], values:List[float]) -> bool:
	"""
	Add or update data for injection
	
	Parameters
	----------
	key:List[str]
		List of key name
	values:List[float]
		list of values (float, could be cast in int)
	
	Returns
	----------
	bool : false on error, true if ok
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "b",
	    "name": "_injectionAdd",
	    "parametersSignature": "([s][f])",
	    "description": "Add or update data for injection",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "List of key name"
	        },
	        {
	            "name": "values",
	            "description": "list of values (float, could be cast in int)"
	        }
	    ],
	    "returnDescription": "bool : false on error, true if ok"
	}
	'''
	"""
	return send_mfc("DCM", "_injectionAdd", [key, values])

def _injectionStop() -> None:
	"""
	Stop datas injection
	
	Returns
	----------
	Nothing
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_injectionStop",
	    "parametersSignature": "()",
	    "description": "Stop datas injection",
	    "parameters": [],
	    "returnDescription": "Nothing"
	}
	'''
	"""
	return send_mfc("DCM", "_injectionStop", [])

def _injectionRemove(key:List[str]) -> None:
	"""
	Remove datas for injection
	
	Parameters
	----------
	key:List[str]
		List of key name
	
	Returns
	----------
	Nothing
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_injectionRemove",
	    "parametersSignature": "([s])",
	    "description": "Remove datas for injection",
	    "parameters": [
	        {
	            "name": "key",
	            "description": "List of key name"
	        }
	    ],
	    "returnDescription": "Nothing"
	}
	'''
	"""
	return send_mfc("DCM", "_injectionRemove", [key])

