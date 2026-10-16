"""

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
	return call_method("_MotionMove", "version", [])

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
	return call_method("_MotionMove", "ping", [])

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
	return call_method("_MotionMove", "getMethodList", [])

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
	return call_method("_MotionMove", "getMethodHelp", [methodName])

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
	return call_method("_MotionMove", "getModuleHelp", [])

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
	return call_method("_MotionMove", "getBrokerName", [])

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
	return call_method("_MotionMove", "getUsage", [name])

def setParam(p0:object) -> None:
	"""
	Set the parameters.
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "setParam",
	#     "parametersSignature": "(m)",
	#     "description": "Set the parameters.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "setParam", [p0])

def start() -> None:
	"""
	Start to work and subscribe to the specified event.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "()",
	#     "description": "Start to work and subscribe to the specified event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "start", [])

def stopMove() -> None:
	"""
	Stop the moving process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "stopMove",
	#     "parametersSignature": "()",
	#     "description": "Stop the moving process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "stopMove", [])

def stopWithoutStopMove() -> None:
	"""
	Stop the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "stopWithoutStopMove",
	#     "parametersSignature": "()",
	#     "description": "Stop the process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "stopWithoutStopMove", [])

def move(p0:object) -> None:
	"""
	Run the moving process.
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "move",
	#     "parametersSignature": "(m)",
	#     "description": "Run the moving process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "move", [p0])

def moveEvent(p0:str, p1:object) -> None:
	"""
	Run the moving process.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "moveEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Run the moving process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "moveEvent", [p0, p1])

def _stopMoveEvent() -> None:
	"""
	Stop the moving process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "_stopMoveEvent",
	#     "parametersSignature": "()",
	#     "description": "Stop the moving process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_MotionMove", "_stopMoveEvent", [])

