"""
Deals with Battery informations.
A event name BatteryChargeCellVoltageMinChanged is raised when the cell voltage Min (int) of the battery changed.
A event name BatteryChargingFlagChanged is raised when the flag battery is charging (bool) changed.
A event name BatteryFullChargedFlagChanged is raised when the flag battery is full charged (bool) changed.
A event name BatteryDisChargingFlagChanged is raised when the flag battery is disCharging (bool) changed.
A event name BatteryChargeChanged is raised when the battery level percentage (int) changed.

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
	return call_method("ALBattery", "version", [])

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
	return call_method("ALBattery", "ping", [])

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
	return call_method("ALBattery", "getMethodList", [])

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
	return call_method("ALBattery", "getMethodHelp", [methodName])

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
	return call_method("ALBattery", "getModuleHelp", [])

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
	return call_method("ALBattery", "getBrokerName", [])

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
	return call_method("ALBattery", "getUsage", [name])

def enablePowerMonitoring(Enable:bool) -> None:
	"""
	Enable power monitoring
	
	Parameters
	----------
	Enable:bool
		True activate power monitoring
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "enablePowerMonitoring",
	#     "parametersSignature": "(b)",
	#     "description": "Enable power monitoring",
	#     "parameters": [
	#         {
	#             "name": "Enable",
	#             "description": "True activate power monitoring"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "enablePowerMonitoring", [Enable])

def getBatteryCharge() -> int:
	"""
	Get the battery charge in percents
	
	Returns
	----------
	the percentage of remaining power
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "i",
	#     "name": "getBatteryCharge",
	#     "parametersSignature": "()",
	#     "description": "Get the battery charge in percents",
	#     "parameters": [],
	#     "returnDescription": "the percentage of remaining power"
	# }
	return call_method("ALBattery", "getBatteryCharge", [])

def _setFirstWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the first warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_setFirstWarningPercent",
	#     "parametersSignature": "(i)",
	#     "description": "Internal set the battery level for the first warning.",
	#     "parameters": [
	#         {
	#             "name": "Percent",
	#             "description": "Percentage of battery."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "_setFirstWarningPercent", [Percent])

def _setWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the second warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_setWarningPercent",
	#     "parametersSignature": "(i)",
	#     "description": "Internal set the battery level for the second warning.",
	#     "parameters": [
	#         {
	#             "name": "Percent",
	#             "description": "Percentage of battery."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "_setWarningPercent", [Percent])

def _setLastWarningPercent(Percent:int) -> None:
	"""
	Internal set the battery level for the last warning.
	
	Parameters
	----------
	Percent:int
		Percentage of battery.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_setLastWarningPercent",
	#     "parametersSignature": "(i)",
	#     "description": "Internal set the battery level for the last warning.",
	#     "parameters": [
	#         {
	#             "name": "Percent",
	#             "description": "Percentage of battery."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "_setLastWarningPercent", [Percent])

def _hasBattery() -> bool:
	"""
	Is battery detected.
	
	Returns
	----------
	Return true if battery is detected.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "_hasBattery",
	#     "parametersSignature": "()",
	#     "description": "Is battery detected.",
	#     "parameters": [],
	#     "returnDescription": "Return true if battery is detected."
	# }
	return call_method("ALBattery", "_hasBattery", [])

def _getBatteryMode() -> int:
	"""
	Get current battery mode.
	
	Returns
	----------
	Return the current battery mode. (Local = 0, robot = 1, simulation = 2)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "_getBatteryMode",
	#     "parametersSignature": "()",
	#     "description": "Get current battery mode.",
	#     "parameters": [],
	#     "returnDescription": "Return the current battery mode. (Local = 0, robot = 1, simulation = 2)"
	# }
	return call_method("ALBattery", "_getBatteryMode", [])

def _getFullyChargedThreshold() -> int:
	"""
	Get current battery fully charged threshold.
	
	Returns
	----------
	the percentage of threshold for fully charged event.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "_getFullyChargedThreshold",
	#     "parametersSignature": "()",
	#     "description": "Get current battery fully charged threshold.",
	#     "parameters": [],
	#     "returnDescription": "the percentage of threshold for fully charged event."
	# }
	return call_method("ALBattery", "_getFullyChargedThreshold", [])

def _setFullyChargedThreshold(threshold:int) -> None:
	"""
	Set battery fully charged threshold.
	
	Parameters
	----------
	threshold:int
		the percentage of threshold for fully charged event.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "_setFullyChargedThreshold",
	#     "parametersSignature": "(i)",
	#     "description": "Set battery fully charged threshold.",
	#     "parameters": [
	#         {
	#             "name": "threshold",
	#             "description": "the percentage of threshold for fully charged event."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "_setFullyChargedThreshold", [threshold])

def _setModeSlave(status:bool) -> None:
	"""
	Set mode slave status.
	
	Parameters
	----------
	status:bool
		Enables or disables mode slave.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_setModeSlave",
	#     "parametersSignature": "(b)",
	#     "description": "Set mode slave status.",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "Enables or disables mode slave."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBattery", "_setModeSlave", [status])

