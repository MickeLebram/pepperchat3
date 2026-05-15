from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module is dedicated to Aldebaran Robots Diagnosis.
"""
def registerEvent(p0:int, p1:int, p2:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 0,
	    "returnSignature": "L",
	    "name": "registerEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "registerEvent", [p0, p1, p2])

def unregisterEvent(p0:int, p1:int, p2:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 1,
	    "returnSignature": "v",
	    "name": "unregisterEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "unregisterEvent", [p0, p1, p2])

def metaObject(p0:int) -> MetaObject:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 2,
	    "returnSignature": "({I(Issss[(ss)<MetaMethodParameter,name,description>]s)<MetaMethod,uid,returnSignature,name,parametersSignature,description,parameters,returnDescription>}{I(Iss)<MetaSignal,uid,name,signature>}{I(Iss)<MetaProperty,uid,name,signature>}s)<MetaObject,methods,signals,properties,description>",
	    "name": "metaObject",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "metaObject", [p0])

def terminate(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 3,
	    "returnSignature": "v",
	    "name": "terminate",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "terminate", [p0])

def property(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 5,
	    "returnSignature": "m",
	    "name": "property",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "property", [p0])

def setProperty(p0:object, p1:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 6,
	    "returnSignature": "v",
	    "name": "setProperty",
	    "parametersSignature": "(mm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "setProperty", [p0, p1])

def properties() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 7,
	    "returnSignature": "[s]",
	    "name": "properties",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "properties", [])

def registerEventWithSignature(p0:int, p1:int, p2:int, p3:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 8,
	    "returnSignature": "L",
	    "name": "registerEventWithSignature",
	    "parametersSignature": "(IILs)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "registerEventWithSignature", [p0, p1, p2, p3])

def isStatsEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 80,
	    "returnSignature": "b",
	    "name": "isStatsEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "isStatsEnabled", [])

def enableStats(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 81,
	    "returnSignature": "v",
	    "name": "enableStats",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "enableStats", [p0])

def stats() -> Dict[int,MethodStatistics]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 82,
	    "returnSignature": "{I(I(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>)<MethodStatistics,count,wall,user,system>}",
	    "name": "stats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "stats", [])

def clearStats() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 83,
	    "returnSignature": "v",
	    "name": "clearStats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "clearStats", [])

def isTraceEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 84,
	    "returnSignature": "b",
	    "name": "isTraceEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "isTraceEnabled", [])

def enableTrace(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 85,
	    "returnSignature": "v",
	    "name": "enableTrace",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "enableTrace", [p0])

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
	return send_mfc("ALDiagnosis", "version", [])

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
	return send_mfc("ALDiagnosis", "ping", [])

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
	return send_mfc("ALDiagnosis", "getMethodList", [])

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
	return send_mfc("ALDiagnosis", "getMethodHelp", [methodName])

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
	return send_mfc("ALDiagnosis", "getModuleHelp", [])

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
	return send_mfc("ALDiagnosis", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALDiagnosis", "wait", [id])

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
	return send_mfc("ALDiagnosis", "isRunning", [id])

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
	return send_mfc("ALDiagnosis", "stop", [id])

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
	return send_mfc("ALDiagnosis", "getBrokerName", [])

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
	return send_mfc("ALDiagnosis", "getUsage", [name])

def getPassiveDiagnosis() -> object:
	"""
	The actual state of the passive diagnosis.
	
	Returns
	----------
	Return the passive diagnosis last result.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "m",
	    "name": "getPassiveDiagnosis",
	    "parametersSignature": "()",
	    "description": "The actual state of the passive diagnosis.",
	    "parameters": [],
	    "returnDescription": "Return the passive diagnosis last result."
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "getPassiveDiagnosis", [])

def getActiveDiagnosis() -> object:
	"""
	The actual state of the active diagnosis.
	
	Returns
	----------
	Return the active diagnosis last result.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "m",
	    "name": "getActiveDiagnosis",
	    "parametersSignature": "()",
	    "description": "The actual state of the active diagnosis.",
	    "parameters": [],
	    "returnDescription": "Return the active diagnosis last result."
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "getActiveDiagnosis", [])

def getDiagnosisStatus() -> object:
	"""
	The actual state of the active and passive diagnosis.
	
	Returns
	----------
	Return the active and passive last result.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "getDiagnosisStatus",
	    "parametersSignature": "()",
	    "description": "The actual state of the active and passive diagnosis.",
	    "parameters": [],
	    "returnDescription": "Return the active and passive last result."
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "getDiagnosisStatus", [])

def setEnableNotification(enable:bool) -> None:
	"""
	Enable / Disable diagnosis notification.
	
	Parameters
	----------
	enable:bool
		If True enable diagnosis notification. If False disable diagnosis notification.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "setEnableNotification",
	    "parametersSignature": "(b)",
	    "description": "Enable / Disable diagnosis notification.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "If True enable diagnosis notification. If False disable diagnosis notification."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "setEnableNotification", [enable])

def isNotificationEnabled() -> bool:
	"""
	Return true if notification is active.
	
	Returns
	----------
	Return True if notifications is active.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "isNotificationEnabled",
	    "parametersSignature": "()",
	    "description": "Return true if notification is active.",
	    "parameters": [],
	    "returnDescription": "Return True if notifications is active."
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "isNotificationEnabled", [])

def _run_1() -> bool:
	"""
	Note: This is one of the overloads of the original method (_run)
	
	This function runs the diagnosis.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "_run",
	    "parametersSignature": "()",
	    "description": "This function runs the diagnosis.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_run", [])

def _run_2(diagnosisFamily:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_run)
	
	This function runs the diagnosis.
	
	Parameters
	----------
	diagnosisFamily:str
		The family of tests to be run by the diagnosis.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "b",
	    "name": "_run",
	    "parametersSignature": "(s)",
	    "description": "This function runs the diagnosis.",
	    "parameters": [
	        {
	            "name": "diagnosisFamily",
	            "description": "The family of tests to be run by the diagnosis."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_run", [diagnosisFamily])

def _getFamilyNames() -> List[str]:
	"""
	Returns a vector of available diagnosis families
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[s]",
	    "name": "_getFamilyNames",
	    "parametersSignature": "()",
	    "description": "Returns a vector of available diagnosis families",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_getFamilyNames", [])

def _getActiveDiagnosisSummary() -> object:
	"""
	The summary of the active diagnosis.This Hide API is dedicated for RhM.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "_getActiveDiagnosisSummary",
	    "parametersSignature": "()",
	    "description": "The summary of the active diagnosis.This Hide API is dedicated for RhM.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_getActiveDiagnosisSummary", [])

def _getPassiveDiagnosisSummary(clearBuffers:bool) -> object:
	"""
	The summary of the passive diagnosis.This Hide API is dedicated for RhM.
	
	Parameters
	----------
	clearBuffers:bool
		If True buffers are cleared.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "_getPassiveDiagnosisSummary",
	    "parametersSignature": "(b)",
	    "description": "The summary of the passive diagnosis.This Hide API is dedicated for RhM.",
	    "parameters": [
	        {
	            "name": "clearBuffers",
	            "description": "If True buffers are cleared."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_getPassiveDiagnosisSummary", [clearBuffers])

def _wakeUpStartedCallBack() -> None:
	"""
	Callback method at wakeUp started.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "_wakeUpStartedCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at wakeUp started.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_wakeUpStartedCallBack", [])

def _wakeUpFinishedCallBack() -> None:
	"""
	Callback method at wakeUp finished.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_wakeUpFinishedCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at wakeUp finished.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_wakeUpFinishedCallBack", [])

def _restStartedCallBack() -> None:
	"""
	Callback method at rest started.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "_restStartedCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at rest started.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_restStartedCallBack", [])

def _restFinishedCallBack() -> None:
	"""
	Callback method at rest finished.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_restFinishedCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at rest finished.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_restFinishedCallBack", [])

def _naoqiReadyCallBack() -> None:
	"""
	Callback method at naoqi ready.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "_naoqiReadyCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at naoqi ready.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_naoqiReadyCallBack", [])

def _robotIsFallingCallBack() -> None:
	"""
	Callback method at robot is falling.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_robotIsFallingCallBack",
	    "parametersSignature": "()",
	    "description": "Callback method at robot is falling.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_robotIsFallingCallBack", [])

def _clearActiveDiagnosis() -> None:
	"""
	Clear all active diagnosis.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "_clearActiveDiagnosis",
	    "parametersSignature": "()",
	    "description": "Clear all active diagnosis.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_clearActiveDiagnosis", [])

def _setLogToFileEnabled(p0:bool) -> None:
	"""
	Enables/Disables file logging active diagnosis.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "_setLogToFileEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enables/Disables file logging active diagnosis.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_setLogToFileEnabled", [p0])

def _runPassiveDiagnosis() -> None:
	"""
	Run the passive diagnosis tests once.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_runPassiveDiagnosis",
	    "parametersSignature": "()",
	    "description": "Run the passive diagnosis tests once.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALDiagnosis", "_runPassiveDiagnosis", [])

