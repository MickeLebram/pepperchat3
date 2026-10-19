"""
Deals with motor temperature.
A event name HotJointDetected is raised when at least one motor has higher temperature.
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
	return call_method("ALBodyTemperature", "version", [])

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
	return call_method("ALBodyTemperature", "ping", [])

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
	return call_method("ALBodyTemperature", "getMethodList", [])

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
	return call_method("ALBodyTemperature", "getMethodHelp", [methodName])

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
	return call_method("ALBodyTemperature", "getModuleHelp", [])

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
	return call_method("ALBodyTemperature", "getBrokerName", [])

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
	return call_method("ALBodyTemperature", "getUsage", [name])

def getTemperatureDiagnosis() -> Any:
	"""
	The actual state of the temperature diagnosis.
	
	Returns
	----------
	Return the current temperature diagnosis.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "m",
	#     "name": "getTemperatureDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "The actual state of the temperature diagnosis.",
	#     "parameters": [],
	#     "returnDescription": "Return the current temperature diagnosis."
	# }
	return call_method("ALBodyTemperature", "getTemperatureDiagnosis", [])

def setEnableNotifications(enable:bool) -> None:
	"""
	Enables / Disables temperature notifications.
	
	Parameters
	----------
	enable:bool
		If True enable temperature notifications. If False disable temperature notifications.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "setEnableNotifications",
	#     "parametersSignature": "(b)",
	#     "description": "Enables / Disables temperature notifications.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "If True enable temperature notifications. If False disable temperature notifications."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBodyTemperature", "setEnableNotifications", [enable])

def areNotificationsEnabled() -> bool:
	"""
	Return true if notifications are active.
	
	Returns
	----------
	Return True if notifications are active.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "areNotificationsEnabled",
	#     "parametersSignature": "()",
	#     "description": "Return true if notifications are active.",
	#     "parameters": [],
	#     "returnDescription": "Return True if notifications are active."
	# }
	return call_method("ALBodyTemperature", "areNotificationsEnabled", [])

def _getDeviceTemperature(deviceName:str) -> int:
	"""
	Return the current temperature of deviceName.
	
	Parameters
	----------
	deviceName:str
		A joint, actuator or sensor name.
	
	Returns
	----------
	Return the current temperature in degree celsius.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "_getDeviceTemperature",
	#     "parametersSignature": "(s)",
	#     "description": "Return the current temperature of deviceName.",
	#     "parameters": [
	#         {
	#             "name": "deviceName",
	#             "description": "A joint, actuator or sensor name."
	#         }
	#     ],
	#     "returnDescription": "Return the current temperature in degree celsius."
	# }
	return call_method("ALBodyTemperature", "_getDeviceTemperature", [deviceName])

def _getDeviceStatus(deviceName:str) -> int:
	"""
	Return the current temperature status of deviceName.
	
	Parameters
	----------
	deviceName:str
		A joint, actuator or sensor name.
	
	Returns
	----------
	Return the current temperature status.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "i",
	#     "name": "_getDeviceStatus",
	#     "parametersSignature": "(s)",
	#     "description": "Return the current temperature status of deviceName.",
	#     "parameters": [
	#         {
	#             "name": "deviceName",
	#             "description": "A joint, actuator or sensor name."
	#         }
	#     ],
	#     "returnDescription": "Return the current temperature status."
	# }
	return call_method("ALBodyTemperature", "_getDeviceStatus", [deviceName])

def _getTemperatureStatus() -> Any:
	"""
	The actual state of the temperature status.
	
	Returns
	----------
	Return the current temperature status.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "_getTemperatureStatus",
	#     "parametersSignature": "()",
	#     "description": "The actual state of the temperature status.",
	#     "parameters": [],
	#     "returnDescription": "Return the current temperature status."
	# }
	return call_method("ALBodyTemperature", "_getTemperatureStatus", [])

def _setEnableDump(status:bool) -> None:
	"""
	Enabled or disables file dump at temperature error.
	
	Parameters
	----------
	status:bool
		Enables or disables dump.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "_setEnableDump",
	#     "parametersSignature": "(b)",
	#     "description": "Enabled or disables file dump at temperature error.",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "Enables or disables dump."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBodyTemperature", "_setEnableDump", [status])

def _isDumpEnabled() -> bool:
	"""
	Return true if dump to file is active.
	
	Returns
	----------
	Return true if dump is enable.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "_isDumpEnabled",
	#     "parametersSignature": "()",
	#     "description": "Return true if dump to file is active.",
	#     "parameters": [],
	#     "returnDescription": "Return true if dump is enable."
	# }
	return call_method("ALBodyTemperature", "_isDumpEnabled", [])

