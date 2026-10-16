"""
This module allows you log errors, warnings, and info stdout or a file. The verbosity level allow you to  customize the output.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
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
	return call_method("ALLogger", "version", [])

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
	return call_method("ALLogger", "ping", [])

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
	return call_method("ALLogger", "getMethodList", [])

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
	return call_method("ALLogger", "getMethodHelp", [methodName])

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
	return call_method("ALLogger", "getModuleHelp", [])

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
	return call_method("ALLogger", "getBrokerName", [])

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
	return call_method("ALLogger", "getUsage", [name])

def setVerbosity(p0:str) -> None:
	"""
	Removed: not implemented anymore.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "setVerbosity",
	#     "parametersSignature": "(s)",
	#     "description": "Removed: not implemented anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLogger", "setVerbosity", [p0])

def verbosity() -> int:
	"""
	Removed: not implemented anymore.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "verbosity",
	#     "parametersSignature": "()",
	#     "description": "Removed: not implemented anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLogger", "verbosity", [])

def logInFile(p0:str) -> None:
	"""
	Removed: not implemented anymore.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "logInFile",
	#     "parametersSignature": "(s)",
	#     "description": "Removed: not implemented anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLogger", "logInFile", [p0])

def logInForwarder(p0:str) -> None:
	"""
	Removed: not implemented anymore.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "logInForwarder",
	#     "parametersSignature": "(s)",
	#     "description": "Removed: not implemented anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLogger", "logInForwarder", [p0])

def removeHandler(p0:str) -> None:
	"""
	Removed: not implemented anymore.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "removeHandler",
	#     "parametersSignature": "(s)",
	#     "description": "Removed: not implemented anymore.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLogger", "removeHandler", [p0])

