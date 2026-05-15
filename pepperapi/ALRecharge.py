from .gentypes import *
from .robot_client import send_mfc
import json
"""

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
	return send_mfc("ALRecharge", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALRecharge", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALRecharge", "metaObject", [p0])

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
	return send_mfc("ALRecharge", "terminate", [p0])

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
	return send_mfc("ALRecharge", "property", [p0])

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
	return send_mfc("ALRecharge", "setProperty", [p0, p1])

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
	return send_mfc("ALRecharge", "properties", [])

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
	return send_mfc("ALRecharge", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALRecharge", "isStatsEnabled", [])

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
	return send_mfc("ALRecharge", "enableStats", [p0])

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
	return send_mfc("ALRecharge", "stats", [])

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
	return send_mfc("ALRecharge", "clearStats", [])

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
	return send_mfc("ALRecharge", "isTraceEnabled", [])

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
	return send_mfc("ALRecharge", "enableTrace", [p0])

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
	return send_mfc("ALRecharge", "version", [])

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
	return send_mfc("ALRecharge", "ping", [])

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
	return send_mfc("ALRecharge", "getMethodList", [])

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
	return send_mfc("ALRecharge", "getMethodHelp", [methodName])

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
	return send_mfc("ALRecharge", "getModuleHelp", [])

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
	return send_mfc("ALRecharge", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALRecharge", "wait", [id])

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
	return send_mfc("ALRecharge", "isRunning", [id])

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
	return send_mfc("ALRecharge", "stop", [id])

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
	return send_mfc("ALRecharge", "getBrokerName", [])

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
	return send_mfc("ALRecharge", "getUsage", [name])

def goToStation() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "i",
	    "name": "goToStation",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "goToStation", [])

def leaveStation() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "i",
	    "name": "leaveStation",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "leaveStation", [])

def getStationPosition() -> List[float]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "[f]",
	    "name": "getStationPosition",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "getStationPosition", [])

def stopAll() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "stopAll",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "stopAll", [])

def subscribe() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "subscribe",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "subscribe", [])

def unsubscribe() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "unsubscribe",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "unsubscribe", [])

def getStatus() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "getStatus",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "getStatus", [])

def lookForStation() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "m",
	    "name": "lookForStation",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "lookForStation", [])

def moveInFrontOfStation() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "moveInFrontOfStation",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "moveInFrontOfStation", [])

def dockOnStation() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "i",
	    "name": "dockOnStation",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "dockOnStation", [])

def setUseTrackerSearcher(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "setUseTrackerSearcher",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "setUseTrackerSearcher", [p0])

def getUseTrackerSearcher() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "b",
	    "name": "getUseTrackerSearcher",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "getUseTrackerSearcher", [])

def setMaxNumberOfTries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "setMaxNumberOfTries",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "setMaxNumberOfTries", [p0])

def getMaxNumberOfTries() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "i",
	    "name": "getMaxNumberOfTries",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "getMaxNumberOfTries", [])

def adjustDockingPosition_1() -> int:
	"""
	Note: This is one of the overloads of the original method (adjustDockingPosition)
	
	.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "i",
	    "name": "adjustDockingPosition",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "adjustDockingPosition", [])

def adjustDockingPosition_2(p0:List[List[float]]) -> int:
	"""
	Note: This is one of the overloads of the original method (adjustDockingPosition)
	
	.
	
	Parameters
	----------
	p0:List[List[float]]
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "i",
	    "name": "adjustDockingPosition",
	    "parametersSignature": "([[f]])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "adjustDockingPosition", [p0])

def _stop() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "_stop",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_stop", [])

def _getConfidenceIndex() -> float:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "f",
	    "name": "_getConfidenceIndex",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getConfidenceIndex", [])

def _allowTrackerNavigateTo(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_allowTrackerNavigateTo",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_allowTrackerNavigateTo", [p0])

def _setFinalApproachDistance(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "_setFinalApproachDistance",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setFinalApproachDistance", [p0])

def _getFinalApproachDistance() -> float:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "f",
	    "name": "_getFinalApproachDistance",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getFinalApproachDistance", [])

def _setFinalApproachYOffset(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "_setFinalApproachYOffset",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setFinalApproachYOffset", [p0])

def _getFinalApproachYOffset() -> float:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "f",
	    "name": "_getFinalApproachYOffset",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getFinalApproachYOffset", [])

def _setFinalApproachThreshold(p0:List[float]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_setFinalApproachThreshold",
	    "parametersSignature": "([f])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setFinalApproachThreshold", [p0])

def _getFinalApproachThreshold() -> List[float]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "[f]",
	    "name": "_getFinalApproachThreshold",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getFinalApproachThreshold", [])

def _setStationDetectionConfidenceThreshold(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_setStationDetectionConfidenceThreshold",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setStationDetectionConfidenceThreshold", [p0])

def _getStationDetectionConfidenceThreshold() -> float:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "f",
	    "name": "_getStationDetectionConfidenceThreshold",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getStationDetectionConfidenceThreshold", [])

def _startLogging() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "_startLogging",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_startLogging", [])

def _stopLogging() -> str:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "s",
	    "name": "_stopLogging",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_stopLogging", [])

def _cancelLogging() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "_cancelLogging",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_cancelLogging", [])

def _getFinalConnectionMoves() -> List[List[float]]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "[[f]]",
	    "name": "_getFinalConnectionMoves",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getFinalConnectionMoves", [])

def _setFinalConnectionMoves(p0:List[List[float]]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[List[float]]
		
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "_setFinalConnectionMoves",
	    "parametersSignature": "([[f]])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setFinalConnectionMoves", [p0])

def _setFinalConnectionMovesDelay(p0:float) -> None:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "_setFinalConnectionMovesDelay",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setFinalConnectionMovesDelay", [p0])

def _getFinalConnectionMovesDelay() -> float:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "f",
	    "name": "_getFinalConnectionMovesDelay",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getFinalConnectionMovesDelay", [])

def _setEnableCheckDisconnectionTask(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "_setEnableCheckDisconnectionTask",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setEnableCheckDisconnectionTask", [p0])

def _getEnableCheckDisconnectionTask() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "_getEnableCheckDisconnectionTask",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getEnableCheckDisconnectionTask", [])

def _getLastHopeMaxRetries() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "I",
	    "name": "_getLastHopeMaxRetries",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getLastHopeMaxRetries", [])

def _setLastHopeMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_setLastHopeMaxRetries",
	    "parametersSignature": "(I)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setLastHopeMaxRetries", [p0])

def _getDockingMaxRetries() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "I",
	    "name": "_getDockingMaxRetries",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getDockingMaxRetries", [])

def _setDockingMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "v",
	    "name": "_setDockingMaxRetries",
	    "parametersSignature": "(I)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setDockingMaxRetries", [p0])

def _getLookMaxRetries() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "I",
	    "name": "_getLookMaxRetries",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_getLookMaxRetries", [])

def _setLookMaxRetries(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "_setLookMaxRetries",
	    "parametersSignature": "(I)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_setLookMaxRetries", [p0])

def _updateStationDetection(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "_updateStationDetection",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_updateStationDetection", [p0, p1, p2])

def _eventTrackerSearcherLoopCallback() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_eventTrackerSearcherLoopCallback",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventTrackerSearcherLoopCallback", [])

def _eventTrackerTargetReachedCallback() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "_eventTrackerTargetReachedCallback",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventTrackerTargetReachedCallback", [])

def _eventTrackerTargetLostCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "v",
	    "name": "_eventTrackerTargetLostCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventTrackerTargetLostCallback", [p0, p1, p2])

def _eventTrackerActiveTargetChangedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "v",
	    "name": "_eventTrackerActiveTargetChangedCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventTrackerActiveTargetChangedCallback", [p0, p1, p2])

def _eventTrackerSearcherScanStartedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "v",
	    "name": "_eventTrackerSearcherScanStartedCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventTrackerSearcherScanStartedCallback", [p0, p1, p2])

def _eventMoveFailedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "v",
	    "name": "_eventMoveFailedCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventMoveFailedCallback", [p0, p1, p2])

def _eventBatteryConnectedToChargingStationCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "v",
	    "name": "_eventBatteryConnectedToChargingStationCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventBatteryConnectedToChargingStationCallback", [p0, p1, p2])

def _eventNavigationStatusChangedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "v",
	    "name": "_eventNavigationStatusChangedCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventNavigationStatusChangedCallback", [p0, p1, p2])

def _eventSlopeDetectedChangedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "v",
	    "name": "_eventSlopeDetectedChangedCallback",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRecharge", "_eventSlopeDetectedChangedCallback", [p0, p1, p2])

