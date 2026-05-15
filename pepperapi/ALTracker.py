from .gentypes import *
from .robot_client import send_mfc
import json
"""
Use ALTracker module to make the robot track an object or a person with head and arms or not.
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
	return send_mfc("ALTracker", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALTracker", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALTracker", "metaObject", [p0])

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
	return send_mfc("ALTracker", "terminate", [p0])

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
	return send_mfc("ALTracker", "property", [p0])

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
	return send_mfc("ALTracker", "setProperty", [p0, p1])

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
	return send_mfc("ALTracker", "properties", [])

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
	return send_mfc("ALTracker", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALTracker", "isStatsEnabled", [])

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
	return send_mfc("ALTracker", "enableStats", [p0])

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
	return send_mfc("ALTracker", "stats", [])

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
	return send_mfc("ALTracker", "clearStats", [])

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
	return send_mfc("ALTracker", "isTraceEnabled", [])

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
	return send_mfc("ALTracker", "enableTrace", [p0])

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
	return send_mfc("ALTracker", "version", [])

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
	return send_mfc("ALTracker", "ping", [])

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
	return send_mfc("ALTracker", "getMethodList", [])

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
	return send_mfc("ALTracker", "getMethodHelp", [methodName])

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
	return send_mfc("ALTracker", "getModuleHelp", [])

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
	return send_mfc("ALTracker", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALTracker", "wait", [id])

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
	return send_mfc("ALTracker", "isRunning", [id])

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
	return send_mfc("ALTracker", "stop", [id])

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
	return send_mfc("ALTracker", "getBrokerName", [])

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
	return send_mfc("ALTracker", "getUsage", [name])

def getTargetPosition(pFrame:int) -> List[float]:
	"""
	Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.
	
	Parameters
	----------
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	
	Returns
	----------
	Vector of 3 floats corresponding to the target position 3D. 
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "[f]",
	    "name": "getTargetPosition",
	    "parametersSignature": "(i)",
	    "description": "Returns the [x, y, z] position of the target in FRAME_TORSO. This is done assuming an average target size, so it might not be very accurate.",
	    "parameters": [
	        {
	            "name": "pFrame",
	            "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        }
	    ],
	    "returnDescription": "Vector of 3 floats corresponding to the target position 3D. "
	}
	'''
	"""
	return send_mfc("ALTracker", "getTargetPosition", [pFrame])

def getRobotPosition() -> List[float]:
	"""
	Only work with LandMarks target name. Returns the [x, y, z, wx, wy, wz] position of the robot in coordinate system setted with setMap API. This is done assuming an average target size, so it might not be very accurate.
	
	Returns
	----------
	Vector of 6 floats corresponding to the robot position 6D.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "[f]",
	    "name": "getRobotPosition",
	    "parametersSignature": "()",
	    "description": "Only work with LandMarks target name. Returns the [x, y, z, wx, wy, wz] position of the robot in coordinate system setted with setMap API. This is done assuming an average target size, so it might not be very accurate.",
	    "parameters": [],
	    "returnDescription": "Vector of 6 floats corresponding to the robot position 6D."
	}
	'''
	"""
	return send_mfc("ALTracker", "getRobotPosition", [])

def isActive() -> bool:
	"""
	Return true if Tracker is running.
	
	Returns
	----------
	True if Tracker is running.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "isActive",
	    "parametersSignature": "()",
	    "description": "Return true if Tracker is running.",
	    "parameters": [],
	    "returnDescription": "True if Tracker is running."
	}
	'''
	"""
	return send_mfc("ALTracker", "isActive", [])

def isNewTargetDetected() -> bool:
	"""
	Return true if a new target was detected.
	
	Returns
	----------
	True if a new target was detected since the last getTargetPosition().
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "isNewTargetDetected",
	    "parametersSignature": "()",
	    "description": "Return true if a new target was detected.",
	    "parameters": [],
	    "returnDescription": "True if a new target was detected since the last getTargetPosition()."
	}
	'''
	"""
	return send_mfc("ALTracker", "isNewTargetDetected", [])

def setRelativePosition(target:object) -> None:
	"""
	Set the robot position relative to target in Move mode.
	
	Parameters
	----------
	target:object
		Set the final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "setRelativePosition",
	    "parametersSignature": "(m)",
	    "description": "Set the robot position relative to target in Move mode.",
	    "parameters": [
	        {
	            "name": "target",
	            "description": "Set the final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz]."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setRelativePosition", [target])

def getRelativePosition() -> object:
	"""
	Get the robot position relative to target in Move mode.
	
	Returns
	----------
	The final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz].
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getRelativePosition",
	    "parametersSignature": "()",
	    "description": "Get the robot position relative to target in Move mode.",
	    "parameters": [],
	    "returnDescription": "The final goal of the tracking. Could be [distance, thresholdX, thresholdY] or with LandMarks target name [coordX, coordY, coordWz, thresholdX, thresholdY, thresholdWz]."
	}
	'''
	"""
	return send_mfc("ALTracker", "getRelativePosition", [])

def setTargetCoordinates(pCoord:object) -> None:
	"""
	Only work with LandMarks target name. Set objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]
	
	Parameters
	----------
	pCoord:object
		objects coordinates.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "setTargetCoordinates",
	    "parametersSignature": "(m)",
	    "description": "Only work with LandMarks target name. Set objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]",
	    "parameters": [
	        {
	            "name": "pCoord",
	            "description": "objects coordinates."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setTargetCoordinates", [pCoord])

def getTargetCoordinates() -> object:
	"""
	Only work with LandMarks target name. Get objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]
	
	Returns
	----------
	objects coordinates.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "m",
	    "name": "getTargetCoordinates",
	    "parametersSignature": "()",
	    "description": "Only work with LandMarks target name. Get objects coordinates. Could be [[first object coordinate], [second object coordinate]] [[x1, y1, z1], [x2, y2, z2]]",
	    "parameters": [],
	    "returnDescription": "objects coordinates."
	}
	'''
	"""
	return send_mfc("ALTracker", "getTargetCoordinates", [])

def setMode(pMode:str) -> None:
	"""
	Set the tracker in the predefined mode.Could be "Head", "WholeBody" or "Move".
	
	Parameters
	----------
	pMode:str
		a predefined mode.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "setMode",
	    "parametersSignature": "(s)",
	    "description": "Set the tracker in the predefined mode.Could be \"Head\", \"WholeBody\" or \"Move\".",
	    "parameters": [
	        {
	            "name": "pMode",
	            "description": "a predefined mode."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setMode", [pMode])

def getMode() -> str:
	"""
	Get the tracker current mode.
	
	Returns
	----------
	The current tracker mode.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "s",
	    "name": "getMode",
	    "parametersSignature": "()",
	    "description": "Get the tracker current mode.",
	    "parameters": [],
	    "returnDescription": "The current tracker mode."
	}
	'''
	"""
	return send_mfc("ALTracker", "getMode", [])

def getAvailableModes() -> List[str]:
	"""
	Get the list of predefined mode.
	
	Returns
	----------
	List of predefined mode.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "[s]",
	    "name": "getAvailableModes",
	    "parametersSignature": "()",
	    "description": "Get the list of predefined mode.",
	    "parameters": [],
	    "returnDescription": "List of predefined mode."
	}
	'''
	"""
	return send_mfc("ALTracker", "getAvailableModes", [])

def toggleSearch(pSearch:bool) -> None:
	"""
	Enables/disables the target search process. Target search process occurs only when the target is lost.
	
	Parameters
	----------
	pSearch:bool
		If true and if the target is lost, the robot moves the head in order to find the target. If false and if the target is lost the robot does not move.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "toggleSearch",
	    "parametersSignature": "(b)",
	    "description": "Enables/disables the target search process. Target search process occurs only when the target is lost.",
	    "parameters": [
	        {
	            "name": "pSearch",
	            "description": "If true and if the target is lost, the robot moves the head in order to find the target. If false and if the target is lost the robot does not move."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "toggleSearch", [pSearch])

def setSearchFractionMaxSpeed(pFractionMaxSpeed:float) -> None:
	"""
	Set search process fraction max speed.
	
	Parameters
	----------
	pFractionMaxSpeed:float
		a fraction max speed.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "setSearchFractionMaxSpeed",
	    "parametersSignature": "(f)",
	    "description": "Set search process fraction max speed.",
	    "parameters": [
	        {
	            "name": "pFractionMaxSpeed",
	            "description": "a fraction max speed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setSearchFractionMaxSpeed", [pFractionMaxSpeed])

def getSearchFractionMaxSpeed() -> float:
	"""
	Get search process fraction max speed.
	
	Returns
	----------
	a fraction max speed.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "f",
	    "name": "getSearchFractionMaxSpeed",
	    "parametersSignature": "()",
	    "description": "Get search process fraction max speed.",
	    "parameters": [],
	    "returnDescription": "a fraction max speed."
	}
	'''
	"""
	return send_mfc("ALTracker", "getSearchFractionMaxSpeed", [])

def isSearchEnabled() -> bool:
	"""
	Return true if the target search process is enabled.
	
	Returns
	----------
	If true the target search process is enabled.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "isSearchEnabled",
	    "parametersSignature": "()",
	    "description": "Return true if the target search process is enabled.",
	    "parameters": [],
	    "returnDescription": "If true the target search process is enabled."
	}
	'''
	"""
	return send_mfc("ALTracker", "isSearchEnabled", [])

def stopTracker() -> None:
	"""
	Stop the tracker.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "stopTracker",
	    "parametersSignature": "()",
	    "description": "Stop the tracker.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "stopTracker", [])

def isTargetLost() -> bool:
	"""
	Return true if the target was lost.
	
	Returns
	----------
	True if the target was lost.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "isTargetLost",
	    "parametersSignature": "()",
	    "description": "Return true if the target was lost.",
	    "parameters": [],
	    "returnDescription": "True if the target was lost."
	}
	'''
	"""
	return send_mfc("ALTracker", "isTargetLost", [])

def track(pTarget:str) -> None:
	"""
	Set the predefided target to track and start the tracking process if not started.
	
	Parameters
	----------
	pTarget:str
		a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "track",
	    "parametersSignature": "(s)",
	    "description": "Set the predefided target to track and start the tracking process if not started.",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target to track.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "track", [pTarget])

def trackEvent(pEventName:str) -> None:
	"""
	Track event and start the tracking process if not started.
	
	Parameters
	----------
	pEventName:str
		a event name to track.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "trackEvent",
	    "parametersSignature": "(s)",
	    "description": "Track event and start the tracking process if not started.",
	    "parameters": [
	        {
	            "name": "pEventName",
	            "description": "a event name to track."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "trackEvent", [pEventName])

def registerTarget(pTarget:str, pParams:object) -> None:
	"""
	Register a predefined target. Subscribe to corresponding extractor if Tracker is running..
	
	Parameters
	----------
	pTarget:str
		a predefined target to track.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	pParams:object
		a target parameters. (RedBall : set diameter of ball.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "registerTarget",
	    "parametersSignature": "(sm)",
	    "description": "Register a predefined target. Subscribe to corresponding extractor if Tracker is running..",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target to track.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        },
	        {
	            "name": "pParams",
	            "description": "a target parameters. (RedBall : set diameter of ball."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "registerTarget", [pTarget, pParams])

def setExtractorPeriod(pTarget:str, pPeriod:int) -> None:
	"""
	Set a period for the corresponding target name extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	pPeriod:int
		a period in milliseconds
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "setExtractorPeriod",
	    "parametersSignature": "(si)",
	    "description": "Set a period for the corresponding target name extractor.",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target name.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        },
	        {
	            "name": "pPeriod",
	            "description": "a period in milliseconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setExtractorPeriod", [pTarget, pPeriod])

def getExtractorPeriod(pTarget:str) -> int:
	"""
	Get the period of corresponding target name extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target name.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	
	Returns
	----------
	a period in milliseconds
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "i",
	    "name": "getExtractorPeriod",
	    "parametersSignature": "(s)",
	    "description": "Get the period of corresponding target name extractor.",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target name.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        }
	    ],
	    "returnDescription": "a period in milliseconds"
	}
	'''
	"""
	return send_mfc("ALTracker", "getExtractorPeriod", [pTarget])

def unregisterTarget(pTarget:str) -> None:
	"""
	Unregister target name and stop corresponding extractor.
	
	Parameters
	----------
	pTarget:str
		a predefined target to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "unregisterTarget",
	    "parametersSignature": "(s)",
	    "description": "Unregister target name and stop corresponding extractor.",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target to remove.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "unregisterTarget", [pTarget])

def unregisterTargets(pTarget:List[str]) -> None:
	"""
	Unregister a list of target names and stop corresponding extractor.
	
	Parameters
	----------
	pTarget:List[str]
		a predefined target list to remove.Could be "RedBall", "Face", "LandMark", "LandMarks", "People" or "Sound".
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "unregisterTargets",
	    "parametersSignature": "([s])",
	    "description": "Unregister a list of target names and stop corresponding extractor.",
	    "parameters": [
	        {
	            "name": "pTarget",
	            "description": "a predefined target list to remove.Could be \"RedBall\", \"Face\", \"LandMark\", \"LandMarks\", \"People\" or \"Sound\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "unregisterTargets", [pTarget])

def unregisterAllTargets() -> None:
	"""
	Unregister all targets except active target and stop corresponding extractor.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "unregisterAllTargets",
	    "parametersSignature": "()",
	    "description": "Unregister all targets except active target and stop corresponding extractor.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "unregisterAllTargets", [])

def getActiveTarget() -> str:
	"""
	Return active target name.
	
	Returns
	----------
	Tracked target name.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "s",
	    "name": "getActiveTarget",
	    "parametersSignature": "()",
	    "description": "Return active target name.",
	    "parameters": [],
	    "returnDescription": "Tracked target name."
	}
	'''
	"""
	return send_mfc("ALTracker", "getActiveTarget", [])

def getSupportedTargets() -> List[str]:
	"""
	Return a list of supported targets names.
	
	Returns
	----------
	Supported targets names.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "[s]",
	    "name": "getSupportedTargets",
	    "parametersSignature": "()",
	    "description": "Return a list of supported targets names.",
	    "parameters": [],
	    "returnDescription": "Supported targets names."
	}
	'''
	"""
	return send_mfc("ALTracker", "getSupportedTargets", [])

def getRegisteredTargets() -> List[str]:
	"""
	Return a list of registered targets names.
	
	Returns
	----------
	Registered targets names.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "[s]",
	    "name": "getRegisteredTargets",
	    "parametersSignature": "()",
	    "description": "Return a list of registered targets names.",
	    "parameters": [],
	    "returnDescription": "Registered targets names."
	}
	'''
	"""
	return send_mfc("ALTracker", "getRegisteredTargets", [])

def lookAt(pPosition:List[float], pFrame:int, pFractionMaxSpeed:float, pUseWholeBody:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "lookAt",
	    "parametersSignature": "([f]ifb)",
	    "description": "Look at the target position with head.\n",
	    "parameters": [
	        {
	            "name": "pPosition",
	            "description": "position 3D [x, y, z] x position must be striclty positif."
	        },
	        {
	            "name": "pFrame",
	            "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pFractionMaxSpeed",
	            "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	        },
	        {
	            "name": "pUseWholeBody",
	            "description": "If true, use whole body constraints."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "lookAt", [pPosition, pFrame, pFractionMaxSpeed, pUseWholeBody])

def pointAt(pEffector:str, pPosition:List[float], pFrame:int, pFractionMaxSpeed:float) -> None:
	"""
	Point at the target position with arms.
	
	
	Parameters
	----------
	pEffector:str
		effector name. Could be "Arms", "LArm", "RArm".
	pPosition:List[float]
		position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "pointAt",
	    "parametersSignature": "(s[f]if)",
	    "description": "Point at the target position with arms.\n",
	    "parameters": [
	        {
	            "name": "pEffector",
	            "description": "effector name. Could be \"Arms\", \"LArm\", \"RArm\"."
	        },
	        {
	            "name": "pPosition",
	            "description": "position 3D [x, y, z] to point in FRAME_TORSO. x position must be striclty positif."
	        },
	        {
	            "name": "pFrame",
	            "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pFractionMaxSpeed",
	            "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "pointAt", [pEffector, pPosition, pFrame, pFractionMaxSpeed])

def getMoveConfig() -> object:
	"""
	Get the config for move modes.
	
	Returns
	----------
	ALMotion GaitConfig
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "m",
	    "name": "getMoveConfig",
	    "parametersSignature": "()",
	    "description": "Get the config for move modes.",
	    "parameters": [],
	    "returnDescription": "ALMotion GaitConfig"
	}
	'''
	"""
	return send_mfc("ALTracker", "getMoveConfig", [])

def setMoveConfig(config:object) -> None:
	"""
	set a config for move modes.
	
	Parameters
	----------
	config:object
		ALMotion GaitConfig
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "setMoveConfig",
	    "parametersSignature": "(m)",
	    "description": "set a config for move modes.",
	    "parameters": [
	        {
	            "name": "config",
	            "description": "ALMotion GaitConfig"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setMoveConfig", [config])

def getTimeOut() -> int:
	"""
	get the timeout parameter for target lost.
	
	Returns
	----------
	time in milliseconds.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "i",
	    "name": "getTimeOut",
	    "parametersSignature": "()",
	    "description": "get the timeout parameter for target lost.",
	    "parameters": [],
	    "returnDescription": "time in milliseconds."
	}
	'''
	"""
	return send_mfc("ALTracker", "getTimeOut", [])

def setTimeOut(pTimeMs:int) -> None:
	"""
	set the timeout parameter for target lost.
	
	Parameters
	----------
	pTimeMs:int
		time in milliseconds.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "setTimeOut",
	    "parametersSignature": "(i)",
	    "description": "set the timeout parameter for target lost.",
	    "parameters": [
	        {
	            "name": "pTimeMs",
	            "description": "time in milliseconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setTimeOut", [pTimeMs])

def getMaximumDistanceDetection() -> float:
	"""
	get the maximum distance for target detection in meter.
	
	Returns
	----------
	The maximum distance for target detection in meter.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "f",
	    "name": "getMaximumDistanceDetection",
	    "parametersSignature": "()",
	    "description": "get the maximum distance for target detection in meter.",
	    "parameters": [],
	    "returnDescription": "The maximum distance for target detection in meter."
	}
	'''
	"""
	return send_mfc("ALTracker", "getMaximumDistanceDetection", [])

def setMaximumDistanceDetection(pMaxDistance:float) -> None:
	"""
	set the maximum target detection distance in meter.
	
	Parameters
	----------
	pMaxDistance:float
		The maximum distance for target detection in meter.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "setMaximumDistanceDetection",
	    "parametersSignature": "(f)",
	    "description": "set the maximum target detection distance in meter.",
	    "parameters": [
	        {
	            "name": "pMaxDistance",
	            "description": "The maximum distance for target detection in meter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setMaximumDistanceDetection", [pMaxDistance])

def getEffector() -> str:
	"""
	Get active effector.
	
	Returns
	----------
	Active effector name. Could be: "Arms", "LArm", "RArm" or "None". 
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "s",
	    "name": "getEffector",
	    "parametersSignature": "()",
	    "description": "Get active effector.",
	    "parameters": [],
	    "returnDescription": "Active effector name. Could be: \"Arms\", \"LArm\", \"RArm\" or \"None\". "
	}
	'''
	"""
	return send_mfc("ALTracker", "getEffector", [])

def setEffector(pEffector:str) -> None:
	"""
	Set an end-effector to move for tracking.
	
	Parameters
	----------
	pEffector:str
		Name of effector. Could be: "Arms", "LArm", "RArm" or "None". 
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "setEffector",
	    "parametersSignature": "(s)",
	    "description": "Set an end-effector to move for tracking.",
	    "parameters": [
	        {
	            "name": "pEffector",
	            "description": "Name of effector. Could be: \"Arms\", \"LArm\", \"RArm\" or \"None\". "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setEffector", [pEffector])

def initialize() -> None:
	"""
	Initialize tracker parameters with default values.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "initialize",
	    "parametersSignature": "()",
	    "description": "Initialize tracker parameters with default values.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "initialize", [])

def setMaximumVelocity(pVelocity:float) -> None:
	"""
	Set the maximum velocity for tracking.
	
	Parameters
	----------
	pVelocity:float
		The maximum velocity in rad.s-1 .
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "v",
	    "name": "setMaximumVelocity",
	    "parametersSignature": "(f)",
	    "description": "Set the maximum velocity for tracking.",
	    "parameters": [
	        {
	            "name": "pVelocity",
	            "description": "The maximum velocity in rad.s-1 ."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setMaximumVelocity", [pVelocity])

def getMaximumVelocity() -> float:
	"""
	Get the maximum velocity for tracking.
	
	Returns
	----------
	The maximum velocity in rad.s-1 .
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "f",
	    "name": "getMaximumVelocity",
	    "parametersSignature": "()",
	    "description": "Get the maximum velocity for tracking.",
	    "parameters": [],
	    "returnDescription": "The maximum velocity in rad.s-1 ."
	}
	'''
	"""
	return send_mfc("ALTracker", "getMaximumVelocity", [])

def setMaximumAcceleration(pAcceleration:float) -> None:
	"""
	Set the maximum acceleration for tracking.
	
	Parameters
	----------
	pAcceleration:float
		The maximum acceleration in rad.s-2 .
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "setMaximumAcceleration",
	    "parametersSignature": "(f)",
	    "description": "Set the maximum acceleration for tracking.",
	    "parameters": [
	        {
	            "name": "pAcceleration",
	            "description": "The maximum acceleration in rad.s-2 ."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "setMaximumAcceleration", [pAcceleration])

def getMaximumAcceleration() -> float:
	"""
	Get the maximum acceleration for tracking.
	
	Returns
	----------
	The maximum acceleration in rad.s-2 .
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "f",
	    "name": "getMaximumAcceleration",
	    "parametersSignature": "()",
	    "description": "Get the maximum acceleration for tracking.",
	    "parameters": [],
	    "returnDescription": "The maximum acceleration in rad.s-2 ."
	}
	'''
	"""
	return send_mfc("ALTracker", "getMaximumAcceleration", [])

def _pause() -> None:
	"""
	Pause the tracking process.
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "v",
	    "name": "_pause",
	    "parametersSignature": "()",
	    "description": "Pause the tracking process.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_pause", [])

def _restart() -> None:
	"""
	Restart the tracking process.
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "v",
	    "name": "_restart",
	    "parametersSignature": "()",
	    "description": "Restart the tracking process.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_restart", [])

def _setTrackerConfig(config:object) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:object
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "v",
	    "name": "_setTrackerConfig",
	    "parametersSignature": "(m)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "config",
	            "description": "Internal: An array of ALValues [i][0]: name, [i][1]: value"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_setTrackerConfig", [config])

def _getTrackerConfig() -> Dict[str,float]:
	"""
	Get the tracker configuration.
	
	Returns
	----------
	map contraining all the information.
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "{sf}",
	    "name": "_getTrackerConfig",
	    "parametersSignature": "()",
	    "description": "Get the tracker configuration.",
	    "parameters": [],
	    "returnDescription": "map contraining all the information."
	}
	'''
	"""
	return send_mfc("ALTracker", "_getTrackerConfig", [])

def _getTrackerConfigStr() -> str:
	"""
	Get the tracker configuration.
	
	Returns
	----------
	string contraining all the information.
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "s",
	    "name": "_getTrackerConfigStr",
	    "parametersSignature": "()",
	    "description": "Get the tracker configuration.",
	    "parameters": [],
	    "returnDescription": "string contraining all the information."
	}
	'''
	"""
	return send_mfc("ALTracker", "_getTrackerConfigStr", [])

def _lostEvent() -> None:
	"""
	Lost event callback.
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "v",
	    "name": "_lostEvent",
	    "parametersSignature": "()",
	    "description": "Lost event callback.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_lostEvent", [])

def _detectedEvent(p0:str, p1:object) -> None:
	"""
	Detected event callback.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "v",
	    "name": "_detectedEvent",
	    "parametersSignature": "(sm)",
	    "description": "Detected event callback.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_detectedEvent", [p0, p1])

def _setDebugInView3D(p0:bool) -> None:
	"""
	Active debug in choregraphe 3D view.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 175,
	    "returnSignature": "v",
	    "name": "_setDebugInView3D",
	    "parametersSignature": "(b)",
	    "description": "Active debug in choregraphe 3D view.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_setDebugInView3D", [p0])

def _debugCallbackEvent(p0:str, p1:object) -> None:
	"""
	debug event callback.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "v",
	    "name": "_debugCallbackEvent",
	    "parametersSignature": "(sm)",
	    "description": "debug event callback.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_debugCallbackEvent", [p0, p1])

def _lookAtWithMove(pPosition:List[float], pFractionMaxSpeed:float, pUseWholeBody:bool, pUseMove:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] to look in FRAME_TORSO.x position must be striclty positif.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use.Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	pUseMove:bool
		If true, use move to look at target behind.
	
	*Reference struct*
	'''
	{
	    "uid": 177,
	    "returnSignature": "v",
	    "name": "_lookAtWithMove",
	    "parametersSignature": "([f]fbb)",
	    "description": "Look at the target position with head.\n",
	    "parameters": [
	        {
	            "name": "pPosition",
	            "description": "position 3D [x, y, z] to look in FRAME_TORSO.x position must be striclty positif."
	        },
	        {
	            "name": "pFractionMaxSpeed",
	            "description": "The fraction of maximum speed to use.Must be between 0 and 1."
	        },
	        {
	            "name": "pUseWholeBody",
	            "description": "If true, use whole body constraints."
	        },
	        {
	            "name": "pUseMove",
	            "description": "If true, use move to look at target behind."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_lookAtWithMove", [pPosition, pFractionMaxSpeed, pUseWholeBody, pUseMove])

def _lookAtWithEffector(pPosition:List[float], pFrame:int, pEffectorId:int, pFractionMaxSpeed:float, pUseWholeBody:bool) -> None:
	"""
	Look at the target position with head.
	
	
	Parameters
	----------
	pPosition:List[float]
		position 3D [x, y, z] x position must be striclty positif.
	pFrame:int
		target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pEffectorId:int
		effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}.
	pFractionMaxSpeed:float
		The fraction of maximum speed to use. Must be between 0 and 1.
	pUseWholeBody:bool
		If true, use whole body constraints.
	
	*Reference struct*
	'''
	{
	    "uid": 178,
	    "returnSignature": "v",
	    "name": "_lookAtWithEffector",
	    "parametersSignature": "([f]iifb)",
	    "description": "Look at the target position with head.\n",
	    "parameters": [
	        {
	            "name": "pPosition",
	            "description": "position 3D [x, y, z] x position must be striclty positif."
	        },
	        {
	            "name": "pFrame",
	            "description": "target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pEffectorId",
	            "description": "effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}."
	        },
	        {
	            "name": "pFractionMaxSpeed",
	            "description": "The fraction of maximum speed to use. Must be between 0 and 1."
	        },
	        {
	            "name": "pUseWholeBody",
	            "description": "If true, use whole body constraints."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_lookAtWithEffector", [pPosition, pFrame, pEffectorId, pFractionMaxSpeed, pUseWholeBody])

def _stopLookAt() -> None:
	"""
	Stop current look at
	
	
	*Reference struct*
	'''
	{
	    "uid": 179,
	    "returnSignature": "v",
	    "name": "_stopLookAt",
	    "parametersSignature": "()",
	    "description": "Stop current look at\n",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_stopLookAt", [])

def _stopPointAt() -> None:
	"""
	Stop current point at
	
	
	*Reference struct*
	'''
	{
	    "uid": 180,
	    "returnSignature": "v",
	    "name": "_stopPointAt",
	    "parametersSignature": "()",
	    "description": "Stop current point at\n",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_stopPointAt", [])

def _searcherSetUseWholeBodyLookAt(p0:bool) -> None:
	"""
	Enable whole body look at during search
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 181,
	    "returnSignature": "v",
	    "name": "_searcherSetUseWholeBodyLookAt",
	    "parametersSignature": "(b)",
	    "description": "Enable whole body look at during search\n",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_searcherSetUseWholeBodyLookAt", [p0])

def _setMoveEvent(p0:str) -> None:
	"""
	Set a specific event for move.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 182,
	    "returnSignature": "v",
	    "name": "_setMoveEvent",
	    "parametersSignature": "(s)",
	    "description": "Set a specific event for move.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_setMoveEvent", [p0])

def _setMoveHysteresis(p0:List[float]) -> None:
	"""
	Set move hysteresis.
	
	Parameters
	----------
	p0:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 183,
	    "returnSignature": "v",
	    "name": "_setMoveHysteresis",
	    "parametersSignature": "([f])",
	    "description": "Set move hysteresis.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_setMoveHysteresis", [p0])

def _getMoveHysteresis() -> List[float]:
	"""
	Get move hysteresis.
	
	*Reference struct*
	'''
	{
	    "uid": 184,
	    "returnSignature": "[f]",
	    "name": "_getMoveHysteresis",
	    "parametersSignature": "()",
	    "description": "Get move hysteresis.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTracker", "_getMoveHysteresis", [])

