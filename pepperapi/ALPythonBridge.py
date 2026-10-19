"""
This module evaluates python commands on the fly.
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
	return call_method("ALPythonBridge", "version", [])

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
	return call_method("ALPythonBridge", "ping", [])

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
	return call_method("ALPythonBridge", "getMethodList", [])

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
	return call_method("ALPythonBridge", "getMethodHelp", [methodName])

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
	return call_method("ALPythonBridge", "getModuleHelp", [])

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
	return call_method("ALPythonBridge", "getBrokerName", [])

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
	return call_method("ALPythonBridge", "getUsage", [name])

def eval(stringToEvaluate:str) -> str:
	"""
	eval script
	
	Parameters
	----------
	stringToEvaluate:str
		string to eval
	
	Returns
	----------
	if the evaluation has gone wrong
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "s",
	#     "name": "eval",
	#     "parametersSignature": "(s)",
	#     "description": "eval script",
	#     "parameters": [
	#         {
	#             "name": "stringToEvaluate",
	#             "description": "string to eval"
	#         }
	#     ],
	#     "returnDescription": "if the evaluation has gone wrong"
	# }
	return call_method("ALPythonBridge", "eval", [stringToEvaluate])

def evalReturn(stringToEvaluate:str) -> Any:
	"""
	eval script and return result. evalReturn(2+2) will return 4
	
	Parameters
	----------
	stringToEvaluate:str
		string to eval
	
	Returns
	----------
	the result of the evaluation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "m",
	#     "name": "evalReturn",
	#     "parametersSignature": "(s)",
	#     "description": "eval script and return result. evalReturn(2+2) will return 4",
	#     "parameters": [
	#         {
	#             "name": "stringToEvaluate",
	#             "description": "string to eval"
	#         }
	#     ],
	#     "returnDescription": "the result of the evaluation"
	# }
	return call_method("ALPythonBridge", "evalReturn", [stringToEvaluate])

def evalFull(stringToEvaluate:str) -> Any:
	"""
	evaluates script and returns an informative array.
	
	Parameters
	----------
	stringToEvaluate:str
		string to eval
	
	Returns
	----------
	an array containing [return value, exceptions, stdout, stderr]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "evalFull",
	#     "parametersSignature": "(s)",
	#     "description": "evaluates script and returns an informative array.",
	#     "parameters": [
	#         {
	#             "name": "stringToEvaluate",
	#             "description": "string to eval"
	#         }
	#     ],
	#     "returnDescription": "an array containing [return value, exceptions, stdout, stderr]"
	# }
	return call_method("ALPythonBridge", "evalFull", [stringToEvaluate])

