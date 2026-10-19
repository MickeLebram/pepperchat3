"""
Manage link with devices (sensors and actuators). See specific documentation.
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
	return call_method("DCM", "version", [])

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
	return call_method("DCM", "ping", [])

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
	return call_method("DCM", "getMethodList", [])

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
	return call_method("DCM", "getMethodHelp", [methodName])

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
	return call_method("DCM", "getModuleHelp", [])

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
	return call_method("DCM", "getBrokerName", [])

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
	return call_method("DCM", "getUsage", [name])

def set(commands:Any) -> None:
	"""
	Call this function to send a timed-command list to an actuator
	
	Parameters
	----------
	commands:Any
		AL::ALValue with all data
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "set",
	#     "parametersSignature": "(m)",
	#     "description": "Call this function to send a timed-command list to an actuator",
	#     "parameters": [
	#         {
	#             "name": "commands",
	#             "description": "AL::ALValue with all data"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("DCM", "set", [commands])

@overload
def setAlias(commands:Any, /) -> None:
	"""
	Call this function to send timed-command list to an alias (list of actuators)
	
	Parameters
	----------
	commands:Any
		AL::ALValue with all data
	
	Bridge notes
	------------
	setAlias has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "setAlias",
	#     "parametersSignature": "(m)",
	#     "description": "Call this function to send timed-command list to an alias (list of actuators)",
	#     "parameters": [
	#         {
	#             "name": "commands",
	#             "description": "AL::ALValue with all data"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setAlias(name:str, time:int, commands:List[float], /) -> None:
	"""
	Call this function to send timed-command list to an alias (list of actuators) with "ClearAll" merge startegy
	
	Parameters
	----------
	name:str
		alias name
	time:int
		time for the timed command
	commands:List[float]
		std::vector<float> with all commands
	
	Bridge notes
	------------
	setAlias has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "setAlias",
	#     "parametersSignature": "(si[f])",
	#     "description": "Call this function to send timed-command list to an alias (list of actuators) with \"ClearAll\" merge startegy",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "alias name"
	#         },
	#         {
	#             "name": "time",
	#             "description": "time for the timed command"
	#         },
	#         {
	#             "name": "commands",
	#             "description": "std::vector<float> with all commands"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setAlias(*args, **kwargs):
	"""
	Bridge notes
	------------
	setAlias has 2 variants on the robot:
	- setAlias(commands:Any)
	- setAlias(name:str, time:int, commands:List[float])
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("DCM.setAlias has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("DCM", "setAlias", list(args))

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "getTime",
	#     "parametersSignature": "(i)",
	#     "description": "Return the DCM time",
	#     "parameters": [
	#         {
	#             "name": "offset",
	#             "description": "optional time in ms (signed) to add/remove"
	#         }
	#     ],
	#     "returnDescription": "An integer (could be signed) with the DCM time"
	# }
	return call_method("DCM", "getTime", [offset])

def createAlias(alias:Any) -> Any:
	"""
	Create or change an alias (list of actuators)
	
	Parameters
	----------
	alias:Any
		Alias name and description
	
	Returns
	----------
	Same as pParams, but with the name removed if the actuator is not found
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "createAlias",
	#     "parametersSignature": "(m)",
	#     "description": "Create or change an alias (list of actuators)",
	#     "parameters": [
	#         {
	#             "name": "alias",
	#             "description": "Alias name and description"
	#         }
	#     ],
	#     "returnDescription": "Same as pParams, but with the name removed if the actuator is not found"
	# }
	return call_method("DCM", "createAlias", [alias])

def getPrefix() -> Any:
	"""
	Return the STM base name
	
	Returns
	----------
	the STM base name for all device/sensors (1st string in the array) and all devices (2nd string in the array)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "getPrefix",
	#     "parametersSignature": "()",
	#     "description": "Return the STM base name",
	#     "parameters": [],
	#     "returnDescription": "the STM base name for all device/sensors (1st string in the array) and all devices (2nd string in the array)"
	# }
	return call_method("DCM", "getPrefix", [])

def special(result:str) -> None:
	"""
	Special DCM commands
	
	Parameters
	----------
	result:str
		one string and could be Reset, Version, Chain, Diagnostic, Config
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "special",
	#     "parametersSignature": "(s)",
	#     "description": "Special DCM commands",
	#     "parameters": [
	#         {
	#             "name": "result",
	#             "description": "one string and could be Reset, Version, Chain, Diagnostic, Config"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("DCM", "special", [result])

def calibration(calibrationInput:Any) -> None:
	"""
	Calibration of a joint
	
	Parameters
	----------
	calibrationInput:Any
		A complex ALValue. See red documentation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "calibration",
	#     "parametersSignature": "(m)",
	#     "description": "Calibration of a joint",
	#     "parameters": [
	#         {
	#             "name": "calibrationInput",
	#             "description": "A complex ALValue. See red documentation"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("DCM", "calibration", [calibrationInput])

def preferences(action:str, target:str, keyName:str, keyValue:Any) -> int:
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
	keyValue:Any
		The ALVAlue of the key to add
	
	Returns
	----------
	Nothing
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "preferences",
	#     "parametersSignature": "(sssm)",
	#     "description": "Save updated value from DCM in XML pref file",
	#     "parameters": [
	#         {
	#             "name": "action",
	#             "description": "string : 'Save' 'Load' 'Add'"
	#         },
	#         {
	#             "name": "target",
	#             "description": "string : 'Chest' 'Head' 'Main' 'All' "
	#         },
	#         {
	#             "name": "keyName",
	#             "description": "The name of the key if action = 'Add'."
	#         },
	#         {
	#             "name": "keyValue",
	#             "description": "The ALVAlue of the key to add"
	#         }
	#     ],
	#     "returnDescription": "Nothing"
	# }
	return call_method("DCM", "preferences", [action, target, keyName, keyValue])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "b",
	#     "name": "_injectionAdd",
	#     "parametersSignature": "([s][f])",
	#     "description": "Add or update data for injection",
	#     "parameters": [
	#         {
	#             "name": "key",
	#             "description": "List of key name"
	#         },
	#         {
	#             "name": "values",
	#             "description": "list of values (float, could be cast in int)"
	#         }
	#     ],
	#     "returnDescription": "bool : false on error, true if ok"
	# }
	return call_method("DCM", "_injectionAdd", [key, values])

def _injectionStop() -> None:
	"""
	Stop datas injection
	
	Returns
	----------
	Nothing
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_injectionStop",
	#     "parametersSignature": "()",
	#     "description": "Stop datas injection",
	#     "parameters": [],
	#     "returnDescription": "Nothing"
	# }
	return call_method("DCM", "_injectionStop", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_injectionRemove",
	#     "parametersSignature": "([s])",
	#     "description": "Remove datas for injection",
	#     "parameters": [
	#         {
	#             "name": "key",
	#             "description": "List of key name"
	#         }
	#     ],
	#     "returnDescription": "Nothing"
	# }
	return call_method("DCM", "_injectionRemove", [key])

