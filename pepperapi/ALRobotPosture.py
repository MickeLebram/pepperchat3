from .gentypes import *
from .robot_client import send_mfc
import json
"""
Use ALRobotPosture module to make the robot go tothe asked posture.
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
	return send_mfc("ALRobotPosture", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALRobotPosture", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALRobotPosture", "metaObject", [p0])

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
	return send_mfc("ALRobotPosture", "terminate", [p0])

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
	return send_mfc("ALRobotPosture", "property", [p0])

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
	return send_mfc("ALRobotPosture", "setProperty", [p0, p1])

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
	return send_mfc("ALRobotPosture", "properties", [])

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
	return send_mfc("ALRobotPosture", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALRobotPosture", "isStatsEnabled", [])

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
	return send_mfc("ALRobotPosture", "enableStats", [p0])

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
	return send_mfc("ALRobotPosture", "stats", [])

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
	return send_mfc("ALRobotPosture", "clearStats", [])

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
	return send_mfc("ALRobotPosture", "isTraceEnabled", [])

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
	return send_mfc("ALRobotPosture", "enableTrace", [p0])

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
	return send_mfc("ALRobotPosture", "version", [])

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
	return send_mfc("ALRobotPosture", "ping", [])

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
	return send_mfc("ALRobotPosture", "getMethodList", [])

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
	return send_mfc("ALRobotPosture", "getMethodHelp", [methodName])

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
	return send_mfc("ALRobotPosture", "getModuleHelp", [])

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
	return send_mfc("ALRobotPosture", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALRobotPosture", "wait", [id])

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
	return send_mfc("ALRobotPosture", "isRunning", [id])

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
	return send_mfc("ALRobotPosture", "stop", [id])

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
	return send_mfc("ALRobotPosture", "getBrokerName", [])

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
	return send_mfc("ALRobotPosture", "getUsage", [name])

def getPostureFamily() -> str:
	"""
	Returns the posture family for example Standing, LyingBelly,...
	
	Returns
	----------
	Returns the posture family, e.g. Standing.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "s",
	    "name": "getPostureFamily",
	    "parametersSignature": "()",
	    "description": "Returns the posture family for example Standing, LyingBelly,...",
	    "parameters": [],
	    "returnDescription": "Returns the posture family, e.g. Standing."
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "getPostureFamily", [])

def goToPosture(postureName:str, maxSpeedFraction:float) -> bool:
	"""
	Make the robot go to the choosenposture.
	
	Parameters
	----------
	postureName:str
		Name of the desired posture. Use getPostureList to get the list of posture name available.
	maxSpeedFraction:float
		A fraction.
	
	Returns
	----------
	Returns if the posture was reached or not.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "goToPosture",
	    "parametersSignature": "(sf)",
	    "description": "Make the robot go to the choosenposture.",
	    "parameters": [
	        {
	            "name": "postureName",
	            "description": "Name of the desired posture. Use getPostureList to get the list of posture name available."
	        },
	        {
	            "name": "maxSpeedFraction",
	            "description": "A fraction."
	        }
	    ],
	    "returnDescription": "Returns if the posture was reached or not."
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "goToPosture", [postureName, maxSpeedFraction])

def applyPosture(postureName:str, maxSpeedFraction:float) -> bool:
	"""
	Set the angle of the joints of the  robot to the choosen posture.
	
	Parameters
	----------
	postureName:str
		Name of the desired posture. Use getPostureList to get the list of posture name available.
	maxSpeedFraction:float
		A fraction.
	
	Returns
	----------
	Returns if the posture was reached or not.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "applyPosture",
	    "parametersSignature": "(sf)",
	    "description": "Set the angle of the joints of the  robot to the choosen posture.",
	    "parameters": [
	        {
	            "name": "postureName",
	            "description": "Name of the desired posture. Use getPostureList to get the list of posture name available."
	        },
	        {
	            "name": "maxSpeedFraction",
	            "description": "A fraction."
	        }
	    ],
	    "returnDescription": "Returns if the posture was reached or not."
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "applyPosture", [postureName, maxSpeedFraction])

def stopMove() -> None:
	"""
	Stop the posture move.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "stopMove",
	    "parametersSignature": "()",
	    "description": "Stop the posture move.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "stopMove", [])

def getPostureList() -> List[str]:
	"""
	Get the list of posture names available.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "[s]",
	    "name": "getPostureList",
	    "parametersSignature": "()",
	    "description": "Get the list of posture names available.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "getPostureList", [])

def getPostureFamilyList() -> List[str]:
	"""
	Get the list of posture family names available.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "[s]",
	    "name": "getPostureFamilyList",
	    "parametersSignature": "()",
	    "description": "Get the list of posture family names available.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "getPostureFamilyList", [])

def setMaxTryNumber(pMaxTryNumber:int) -> None:
	"""
	Set maximum of tries ongoToPosture fail.
	
	Parameters
	----------
	pMaxTryNumber:int
		Number of retry if goToPosture fail.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "setMaxTryNumber",
	    "parametersSignature": "(i)",
	    "description": "Set maximum of tries ongoToPosture fail.",
	    "parameters": [
	        {
	            "name": "pMaxTryNumber",
	            "description": "Number of retry if goToPosture fail."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "setMaxTryNumber", [pMaxTryNumber])

def getPosture() -> str:
	"""
	Determine posture.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "s",
	    "name": "getPosture",
	    "parametersSignature": "()",
	    "description": "Determine posture.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "getPosture", [])

def _isRobotInPosture(p0:str, p1:float, p2:float) -> object:
	"""
	Articular distance
	
	Parameters
	----------
	p0:str
		
	p1:float
		
	p2:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "_isRobotInPosture",
	    "parametersSignature": "(sff)",
	    "description": "Articular distance",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_isRobotInPosture", [p0, p1, p2])

def _isRobotInPostureId(p0:int, p1:float, p2:float) -> bool:
	"""
	Articular distance
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	p2:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "b",
	    "name": "_isRobotInPostureId",
	    "parametersSignature": "(iff)",
	    "description": "Articular distance",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_isRobotInPostureId", [p0, p1, p2])

def _getPosture() -> object:
	"""
	Determine posture id.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "_getPosture",
	    "parametersSignature": "()",
	    "description": "Determine posture id.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getPosture", [])

def _setPostureId(p0:int, p1:float) -> bool:
	"""
	Set the angle of the joints.
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "b",
	    "name": "_setPostureId",
	    "parametersSignature": "(if)",
	    "description": "Set the angle of the joints.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setPostureId", [p0, p1])

def _goToPostureId(p0:int, p1:float) -> bool:
	"""
	Set the angle of thejoints and of the inertial unit
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "b",
	    "name": "_goToPostureId",
	    "parametersSignature": "(if)",
	    "description": "Set the angle of thejoints and of the inertial unit",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_goToPostureId", [p0, p1])

def _namePosture(p0:int, p1:str) -> bool:
	"""
	Name posture from id.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "_namePosture",
	    "parametersSignature": "(is)",
	    "description": "Name posture from id.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_namePosture", [p0, p1])

def _renamePosture(p0:str, p1:str) -> bool:
	"""
	Rename posture from name.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "_renamePosture",
	    "parametersSignature": "(ss)",
	    "description": "Rename posture from name.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_renamePosture", [p0, p1])

def _resavePosture(p0:int) -> bool:
	"""
	Resave posture joints, inertial, family. Keep neighbours.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "b",
	    "name": "_resavePosture",
	    "parametersSignature": "(i)",
	    "description": "Resave posture joints, inertial, family. Keep neighbours.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_resavePosture", [p0])

def _setSlowFactor(p0:int, p1:int, p2:float) -> bool:
	"""
	Set slow factorbetween two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "_setSlowFactor",
	    "parametersSignature": "(iif)",
	    "description": "Set slow factorbetween two postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setSlowFactor", [p0, p1, p2])

def _setAntiCollision(p0:int, p1:bool) -> bool:
	"""
	Set anti collisionbetween two postures.
	
	Parameters
	----------
	p0:int
		
	p1:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "b",
	    "name": "_setAntiCollision",
	    "parametersSignature": "(ib)",
	    "description": "Set anti collisionbetween two postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setAntiCollision", [p0, p1])

def _setUseAntiCollision(enable:bool) -> None:
	"""
	Enables/Disables anti collision management by RobotPosture.
	
	Parameters
	----------
	enable:bool
		A bool that enable anticollision management.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_setUseAntiCollision",
	    "parametersSignature": "(b)",
	    "description": "Enables/Disables anti collision management by RobotPosture.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "A bool that enable anticollision management."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setUseAntiCollision", [enable])

def _setUseAutoBalance(enable:bool) -> None:
	"""
	Enables/Disables auto balance management by RobotPosture.
	
	Parameters
	----------
	enable:bool
		A bool that enable auto balance management.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "_setUseAutoBalance",
	    "parametersSignature": "(b)",
	    "description": "Enables/Disables auto balance management by RobotPosture.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "A bool that enable auto balance management."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setUseAutoBalance", [enable])

def _setCost(p0:int, p1:float) -> bool:
	"""
	Set cost between two postures.
	
	Parameters
	----------
	p0:int
		
	p1:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "b",
	    "name": "_setCost",
	    "parametersSignature": "(if)",
	    "description": "Set cost between two postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_setCost", [p0, p1])

def _saveCurrentPosture(p0:int) -> bool:
	"""
	Save current posture.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "_saveCurrentPosture",
	    "parametersSignature": "(i)",
	    "description": "Save current posture.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_saveCurrentPosture", [p0])

def _saveCurrentPostureWithName(p0:int, p1:str) -> bool:
	"""
	Save with a namecurrent posture.
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "_saveCurrentPostureWithName",
	    "parametersSignature": "(is)",
	    "description": "Save with a namecurrent posture.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_saveCurrentPostureWithName", [p0, p1])

def _applyPostures(p0:List[int], p1:float, p2:bool, p3:bool) -> bool:
	"""
	Apply postures.
	
	Parameters
	----------
	p0:List[int]
		
	p1:float
		
	p2:bool
		
	p3:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "b",
	    "name": "_applyPostures",
	    "parametersSignature": "([i]fbb)",
	    "description": "Apply postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_applyPostures", [p0, p1, p2, p3])

def _eraseAllPostures() -> bool:
	"""
	Erase all postures.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "b",
	    "name": "_eraseAllPostures",
	    "parametersSignature": "()",
	    "description": "Erase all postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_eraseAllPostures", [])

def _bindPostures(p0:int, p1:int, p2:float, p3:float) -> bool:
	"""
	Bind two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	p3:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "b",
	    "name": "_bindPostures",
	    "parametersSignature": "(iiff)",
	    "description": "Bind two postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_bindPostures", [p0, p1, p2, p3])

def _addNeighbourToPosture(p0:int, p1:int, p2:float) -> bool:
	"""
	Add a neighbour to a postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "b",
	    "name": "_addNeighbourToPosture",
	    "parametersSignature": "(iif)",
	    "description": "Add a neighbour to a postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_addNeighbourToPosture", [p0, p1, p2])

def _removeNeighbourFromPosture(p0:int, p1:int) -> bool:
	"""
	Remove a neighbour from postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "b",
	    "name": "_removeNeighbourFromPosture",
	    "parametersSignature": "(ii)",
	    "description": "Remove a neighbour from postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_removeNeighbourFromPosture", [p0, p1])

def _unBindPostures(p0:int, p1:int) -> bool:
	"""
	Unbind two postures.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "b",
	    "name": "_unBindPostures",
	    "parametersSignature": "(ii)",
	    "description": "Unbind two postures.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_unBindPostures", [p0, p1])

def _erasePosture(p0:int) -> bool:
	"""
	Erase the posture and unBind theneighbours.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "b",
	    "name": "_erasePosture",
	    "parametersSignature": "(i)",
	    "description": "Erase the posture and unBind theneighbours.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_erasePosture", [p0])

def _getLibrarySize() -> int:
	"""
	Get library size.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "i",
	    "name": "_getLibrarySize",
	    "parametersSignature": "()",
	    "description": "Get library size.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getLibrarySize", [])

def _loadPostureLibraryFromName(p0:str) -> bool:
	"""
	Load a new library file.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "b",
	    "name": "_loadPostureLibraryFromName",
	    "parametersSignature": "(s)",
	    "description": "Load a new library file.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_loadPostureLibraryFromName", [p0])

def _getCurrentPath() -> List[float]:
	"""
	Get current graph path.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "[f]",
	    "name": "_getCurrentPath",
	    "parametersSignature": "()",
	    "description": "Get current graph path.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getCurrentPath", [])

def _isStandCallBack(p0:str, p1:object, p2:str) -> None:
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
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_isStandCallBack",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_isStandCallBack", [p0, p1, p2])

def _savePostureLibrary(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "b",
	    "name": "_savePostureLibrary",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_savePostureLibrary", [p0])

def _getArticularDistanceToPosture(p0:int) -> float:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "f",
	    "name": "_getArticularDistanceToPosture",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getArticularDistanceToPosture", [p0])

def _getCartesianDistanceToPosture(p0:int) -> object:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "m",
	    "name": "_getCartesianDistanceToPosture",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getCartesianDistanceToPosture", [p0])

def _getCartesianDistanceVector(p0:int) -> List[float]:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "[f]",
	    "name": "_getCartesianDistanceVector",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getCartesianDistanceVector", [p0])

def _getPostureIdList() -> List[int]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "[i]",
	    "name": "_getPostureIdList",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getPostureIdList", [])

def _isReachable(p0:int) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "_isReachable",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_isReachable", [p0])

def _generateCartesianMap() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "v",
	    "name": "_generateCartesianMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_generateCartesianMap", [])

def _getPostureZ(p0:float) -> object:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "m",
	    "name": "_getPostureZ",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getPostureZ", [p0])

def _getPostureNoZ() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "m",
	    "name": "_getPostureNoZ",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getPostureNoZ", [])

def _getIdFromName(p0:str) -> int:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "i",
	    "name": "_getIdFromName",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_getIdFromName", [p0])

def _activeDiagnosisCallBack(p0:str, p1:object, p2:str) -> None:
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
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "_activeDiagnosisCallBack",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_activeDiagnosisCallBack", [p0, p1, p2])

def _eraseFamily(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "b",
	    "name": "_eraseFamily",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRobotPosture", "_eraseFamily", [p0])

