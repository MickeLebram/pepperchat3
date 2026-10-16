"""
ALExpressiveness: Give some life to the robot.
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
	return call_method("_ALExpressiveness", "version", [])

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
	return call_method("_ALExpressiveness", "ping", [])

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
	return call_method("_ALExpressiveness", "getMethodList", [])

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
	return call_method("_ALExpressiveness", "getMethodHelp", [methodName])

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
	return call_method("_ALExpressiveness", "getModuleHelp", [])

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
	return call_method("_ALExpressiveness", "getBrokerName", [])

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
	return call_method("_ALExpressiveness", "getUsage", [name])

def _naoqiIsReady(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when NAOqi is ready to enable display of notifications.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_naoqiIsReady",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when NAOqi is ready to enable display of notifications.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALExpressiveness", "_naoqiIsReady", [p0, p1, p2])

def _updateNotification(p0:str, p1:object, p2:object) -> None:
	"""
	Callback when new notification just comming.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "_updateNotification",
	#     "parametersSignature": "(smm)",
	#     "description": "Callback when new notification just comming.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALExpressiveness", "_updateNotification", [p0, p1, p2])

def _setNotificationEnabled(enable:bool) -> None:
	"""
	Enable or disable the display of pending notifications.
	
	Parameters
	----------
	enable:bool
		The boolean value: true to enable, false to disable.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_setNotificationEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Enable or disable the display of pending notifications.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "The boolean value: true to enable, false to disable."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_ALExpressiveness", "_setNotificationEnabled", [enable])

