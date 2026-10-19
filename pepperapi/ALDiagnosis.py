"""
This module is dedicated to Aldebaran Robots Diagnosis.
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
	return call_method("ALDiagnosis", "version", [])

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
	return call_method("ALDiagnosis", "ping", [])

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
	return call_method("ALDiagnosis", "getMethodList", [])

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
	return call_method("ALDiagnosis", "getMethodHelp", [methodName])

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
	return call_method("ALDiagnosis", "getModuleHelp", [])

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
	return call_method("ALDiagnosis", "getBrokerName", [])

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
	return call_method("ALDiagnosis", "getUsage", [name])

def getPassiveDiagnosis() -> Any:
	"""
	The actual state of the passive diagnosis.
	
	Returns
	----------
	Return the passive diagnosis last result.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "m",
	#     "name": "getPassiveDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "The actual state of the passive diagnosis.",
	#     "parameters": [],
	#     "returnDescription": "Return the passive diagnosis last result."
	# }
	return call_method("ALDiagnosis", "getPassiveDiagnosis", [])

def getActiveDiagnosis() -> Any:
	"""
	The actual state of the active diagnosis.
	
	Returns
	----------
	Return the active diagnosis last result.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "m",
	#     "name": "getActiveDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "The actual state of the active diagnosis.",
	#     "parameters": [],
	#     "returnDescription": "Return the active diagnosis last result."
	# }
	return call_method("ALDiagnosis", "getActiveDiagnosis", [])

def getDiagnosisStatus() -> Any:
	"""
	The actual state of the active and passive diagnosis.
	
	Returns
	----------
	Return the active and passive last result.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "getDiagnosisStatus",
	#     "parametersSignature": "()",
	#     "description": "The actual state of the active and passive diagnosis.",
	#     "parameters": [],
	#     "returnDescription": "Return the active and passive last result."
	# }
	return call_method("ALDiagnosis", "getDiagnosisStatus", [])

def setEnableNotification(enable:bool) -> None:
	"""
	Enable / Disable diagnosis notification.
	
	Parameters
	----------
	enable:bool
		If True enable diagnosis notification. If False disable diagnosis notification.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "setEnableNotification",
	#     "parametersSignature": "(b)",
	#     "description": "Enable / Disable diagnosis notification.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "If True enable diagnosis notification. If False disable diagnosis notification."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "setEnableNotification", [enable])

def isNotificationEnabled() -> bool:
	"""
	Return true if notification is active.
	
	Returns
	----------
	Return True if notifications is active.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "isNotificationEnabled",
	#     "parametersSignature": "()",
	#     "description": "Return true if notification is active.",
	#     "parameters": [],
	#     "returnDescription": "Return True if notifications is active."
	# }
	return call_method("ALDiagnosis", "isNotificationEnabled", [])

@overload
def _run() -> bool:
	"""
	This function runs the diagnosis.
	
	Bridge notes
	------------
	_run has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "_run",
	#     "parametersSignature": "()",
	#     "description": "This function runs the diagnosis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _run(diagnosisFamily:str, /) -> bool:
	"""
	This function runs the diagnosis.
	
	Parameters
	----------
	diagnosisFamily:str
		The family of tests to be run by the diagnosis.
	
	Bridge notes
	------------
	_run has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "b",
	#     "name": "_run",
	#     "parametersSignature": "(s)",
	#     "description": "This function runs the diagnosis.",
	#     "parameters": [
	#         {
	#             "name": "diagnosisFamily",
	#             "description": "The family of tests to be run by the diagnosis."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def _run(*args, **kwargs):
	"""
	Bridge notes
	------------
	_run has 2 variants on the robot:
	- _run()
	- _run(diagnosisFamily:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALDiagnosis._run has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALDiagnosis", "_run", list(args))

def _getFamilyNames() -> List[str]:
	"""
	Returns a vector of available diagnosis families
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "[s]",
	#     "name": "_getFamilyNames",
	#     "parametersSignature": "()",
	#     "description": "Returns a vector of available diagnosis families",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_getFamilyNames", [])

def _getActiveDiagnosisSummary() -> Any:
	"""
	The summary of the active diagnosis.This Hide API is dedicated for RhM.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "m",
	#     "name": "_getActiveDiagnosisSummary",
	#     "parametersSignature": "()",
	#     "description": "The summary of the active diagnosis.This Hide API is dedicated for RhM.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_getActiveDiagnosisSummary", [])

def _getPassiveDiagnosisSummary(clearBuffers:bool) -> Any:
	"""
	The summary of the passive diagnosis.This Hide API is dedicated for RhM.
	
	Parameters
	----------
	clearBuffers:bool
		If True buffers are cleared.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "_getPassiveDiagnosisSummary",
	#     "parametersSignature": "(b)",
	#     "description": "The summary of the passive diagnosis.This Hide API is dedicated for RhM.",
	#     "parameters": [
	#         {
	#             "name": "clearBuffers",
	#             "description": "If True buffers are cleared."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_getPassiveDiagnosisSummary", [clearBuffers])

def _wakeUpStartedCallBack() -> None:
	"""
	Callback method at wakeUp started.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_wakeUpStartedCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at wakeUp started.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_wakeUpStartedCallBack", [])

def _wakeUpFinishedCallBack() -> None:
	"""
	Callback method at wakeUp finished.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_wakeUpFinishedCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at wakeUp finished.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_wakeUpFinishedCallBack", [])

def _restStartedCallBack() -> None:
	"""
	Callback method at rest started.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_restStartedCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at rest started.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_restStartedCallBack", [])

def _restFinishedCallBack() -> None:
	"""
	Callback method at rest finished.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_restFinishedCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at rest finished.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_restFinishedCallBack", [])

def _naoqiReadyCallBack() -> None:
	"""
	Callback method at naoqi ready.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "_naoqiReadyCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at naoqi ready.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_naoqiReadyCallBack", [])

def _robotIsFallingCallBack() -> None:
	"""
	Callback method at robot is falling.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_robotIsFallingCallBack",
	#     "parametersSignature": "()",
	#     "description": "Callback method at robot is falling.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_robotIsFallingCallBack", [])

def _clearActiveDiagnosis() -> None:
	"""
	Clear all active diagnosis.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_clearActiveDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "Clear all active diagnosis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_clearActiveDiagnosis", [])

def _setLogToFileEnabled(p0:bool) -> None:
	"""
	Enables/Disables file logging active diagnosis.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "_setLogToFileEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Enables/Disables file logging active diagnosis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_setLogToFileEnabled", [p0])

def _runPassiveDiagnosis() -> None:
	"""
	Run the passive diagnosis tests once.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_runPassiveDiagnosis",
	#     "parametersSignature": "()",
	#     "description": "Run the passive diagnosis tests once.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDiagnosis", "_runPassiveDiagnosis", [])

