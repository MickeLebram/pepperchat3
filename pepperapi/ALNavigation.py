from .gentypes import *
from .robot_client import send_mfc
import json
"""
Use ALNavigation module to make the robot go safely to the asked pose2D.
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
	return send_mfc("ALNavigation", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALNavigation", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALNavigation", "metaObject", [p0])

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
	return send_mfc("ALNavigation", "terminate", [p0])

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
	return send_mfc("ALNavigation", "property", [p0])

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
	return send_mfc("ALNavigation", "setProperty", [p0, p1])

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
	return send_mfc("ALNavigation", "properties", [])

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
	return send_mfc("ALNavigation", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALNavigation", "isStatsEnabled", [])

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
	return send_mfc("ALNavigation", "enableStats", [p0])

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
	return send_mfc("ALNavigation", "stats", [])

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
	return send_mfc("ALNavigation", "clearStats", [])

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
	return send_mfc("ALNavigation", "isTraceEnabled", [])

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
	return send_mfc("ALNavigation", "enableTrace", [p0])

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
	return send_mfc("ALNavigation", "version", [])

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
	return send_mfc("ALNavigation", "ping", [])

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
	return send_mfc("ALNavigation", "getMethodList", [])

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
	return send_mfc("ALNavigation", "getMethodHelp", [methodName])

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
	return send_mfc("ALNavigation", "getModuleHelp", [])

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
	return send_mfc("ALNavigation", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALNavigation", "wait", [id])

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
	return send_mfc("ALNavigation", "isRunning", [id])

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
	return send_mfc("ALNavigation", "stop", [id])

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
	return send_mfc("ALNavigation", "getBrokerName", [])

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
	return send_mfc("ALNavigation", "getUsage", [name])

def navigateTo_1(x:float, y:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (navigateTo)
	
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "navigateTo",
	    "parametersSignature": "(ff)",
	    "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "navigateTo", [x, y])

def navigateTo_2(x:float, y:float, config:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (navigateTo)
	
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	config:object
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "navigateTo",
	    "parametersSignature": "(ffm)",
	    "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "config",
	            "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "navigateTo", [x, y, config])

def navigateTo_3(x:float, y:float, theta:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (navigateTo)
	
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "navigateTo",
	    "parametersSignature": "(fff)",
	    "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "Orientation of the robot (rad)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "navigateTo", [x, y, theta])

def navigateTo_4(x:float, y:float, theta:float, config:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (navigateTo)
	
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	config:object
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "navigateTo",
	    "parametersSignature": "(fffm)",
	    "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "Orientation of the robot (rad)."
	        },
	        {
	            "name": "config",
	            "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "navigateTo", [x, y, theta, config])

def _setNavigationConfig(config:object) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:object
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_setNavigationConfig",
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
	return send_mfc("ALNavigation", "_setNavigationConfig", [config])

def stopNavigateTo() -> None:
	"""
	Stops the navigateTo.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "stopNavigateTo",
	    "parametersSignature": "()",
	    "description": "Stops the navigateTo.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "stopNavigateTo", [])

def _stopNavigateToWithoutStopMove() -> None:
	"""
	Stops the navigateTo but no stop move.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "_stopNavigateToWithoutStopMove",
	    "parametersSignature": "()",
	    "description": "Stops the navigateTo but no stop move.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_stopNavigateToWithoutStopMove", [])

def _isNavigateToRunning() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "_isNavigateToRunning",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_isNavigateToRunning", [])

def _getObstacleData() -> object:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are the one used by the secure navigator
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "_getObstacleData",
	    "parametersSignature": "()",
	    "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are the one used by the secure navigator",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getObstacleData", [])

def _getOccupancyGrid(client:str) -> object:
	"""
	Get the requested occupancy grid formatted as a ROS navigation stack message.
	
	Parameters
	----------
	client:str
		Internal: 'Secure' for SecureNavigator or 'Local' for LocalNavigator.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "_getOccupancyGrid",
	    "parametersSignature": "(s)",
	    "description": "Get the requested occupancy grid formatted as a ROS navigation stack message.",
	    "parameters": [
	        {
	            "name": "client",
	            "description": "Internal: 'Secure' for SecureNavigator or 'Local' for LocalNavigator."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getOccupancyGrid", [client])

def _getSensorData_1() -> object:
	"""
	Note: This is one of the overloads of the original method (_getSensorData)
	
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "_getSensorData",
	    "parametersSignature": "()",
	    "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorData", [])

def _getSensorData_2(p0:str) -> object:
	"""
	Note: This is one of the overloads of the original method (_getSensorData)
	
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "m",
	    "name": "_getSensorData",
	    "parametersSignature": "(s)",
	    "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorData", [p0])

def _getSensorData_3(p0:List[str]) -> object:
	"""
	Note: This is one of the overloads of the original method (_getSensorData)
	
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:List[str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "m",
	    "name": "_getSensorData",
	    "parametersSignature": "([s])",
	    "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorData", [p0])

def _subscribeToAll(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "_subscribeToAll",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_subscribeToAll", [p0])

def _subscribe(clientName:str, p1:List[str]) -> bool:
	"""
	Start active sensors.The client needs to specify its name to register.If the client is the only one to register, the sensors are turned on, otherwise they are already started.
	
	Parameters
	----------
	clientName:str
		The client name.
	p1:List[str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "_subscribe",
	    "parametersSignature": "(s[s])",
	    "description": "Start active sensors.The client needs to specify its name to register.If the client is the only one to register, the sensors are turned on, otherwise they are already started.",
	    "parameters": [
	        {
	            "name": "clientName",
	            "description": "The client name."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_subscribe", [clientName, p1])

def _unsubscribeFromAll(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "b",
	    "name": "_unsubscribeFromAll",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_unsubscribeFromAll", [p0])

def _unsubscribe(clientName:str, p1:List[str]) -> bool:
	"""
	Stop active sensors.The client needs to specify its name to unregister.The active sensors are actually stopped if not client is registered anymore.
	
	Parameters
	----------
	clientName:str
		The client name.
	p1:List[str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "_unsubscribe",
	    "parametersSignature": "(s[s])",
	    "description": "Stop active sensors.The client needs to specify its name to unregister.The active sensors are actually stopped if not client is registered anymore.",
	    "parameters": [
	        {
	            "name": "clientName",
	            "description": "The client name."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_unsubscribe", [clientName, p1])

def _addSensor(sensor:str) -> bool:
	"""
	Add a sensor family or a sensor.
	
	Parameters
	----------
	sensor:str
		The sensor family name or name.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "b",
	    "name": "_addSensor",
	    "parametersSignature": "(s)",
	    "description": "Add a sensor family or a sensor.",
	    "parameters": [
	        {
	            "name": "sensor",
	            "description": "The sensor family name or name."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_addSensor", [sensor])

def _removeSensor(sensor:str) -> bool:
	"""
	Remove a sensor family or a sensor.
	
	Parameters
	----------
	sensor:str
		The sensor family name or name.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "b",
	    "name": "_removeSensor",
	    "parametersSignature": "(s)",
	    "description": "Remove a sensor family or a sensor.",
	    "parameters": [
	        {
	            "name": "sensor",
	            "description": "The sensor family name or name."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_removeSensor", [sensor])

def _getTrajectory() -> object:
	"""
	Get trajectory from local navigator.ALArray containing successively x, y and theta coordinates.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "m",
	    "name": "_getTrajectory",
	    "parametersSignature": "()",
	    "description": "Get trajectory from local navigator.ALArray containing successively x, y and theta coordinates.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getTrajectory", [])

def _setSpeedFactor(p0:float) -> None:
	"""
	Set speed factor for local navigator
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "_setSpeedFactor",
	    "parametersSignature": "(f)",
	    "description": "Set speed factor for local navigator",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_setSpeedFactor", [p0])

def _getObstacleMap(p0:str) -> object:
	"""
	Get obstacle Map from localnavigator. ALValue formatted as follow for each sensor :[[SensorName1 [[x1 y1] [x2 y2] [x3 y3] ...]] [SensorName2 [[x1 y1] [x2 y2] [x3 y3] ...]] ... ]
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "m",
	    "name": "_getObstacleMap",
	    "parametersSignature": "(s)",
	    "description": "Get obstacle Map from localnavigator. ALValue formatted as follow for each sensor :[[SensorName1 [[x1 y1] [x2 y2] [x3 y3] ...]] [SensorName2 [[x1 y1] [x2 y2] [x3 y3] ...]] ... ]",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getObstacleMap", [p0])

def _enableSensorDebug(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_enableSensorDebug",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_enableSensorDebug", [p0])

def _useHeadChecking(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_useHeadChecking",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_useHeadChecking", [p0])

def _usePathChecking(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_usePathChecking",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_usePathChecking", [p0])

def _usePathCorrection(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_usePathCorrection",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_usePathCorrection", [p0])

def _useArmsOnBelly(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "_useArmsOnBelly",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_useArmsOnBelly", [p0])

def _useSpeedFactor(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "_useSpeedFactor",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_useSpeedFactor", [p0])

def _clearObstacleMap() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_clearObstacleMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_clearObstacleMap", [])

def _useClearNavigationMap(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "_useClearNavigationMap",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_useClearNavigationMap", [p0])

def _clearNavigationMap() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "_clearNavigationMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_clearNavigationMap", [])

def _getSensorSubscribers() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "m",
	    "name": "_getSensorSubscribers",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorSubscribers", [])

def _getSensorList() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "m",
	    "name": "_getSensorList",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorList", [])

def _getSensorListBySubscriber(p0:str) -> object:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "m",
	    "name": "_getSensorListBySubscriber",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getSensorListBySubscriber", [p0])

def _getActiveSensorList() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "m",
	    "name": "_getActiveSensorList",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getActiveSensorList", [])

def _isSensorEnabled(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "_isSensorEnabled",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_isSensorEnabled", [p0])

def _setController(p0:int, p1:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	p1:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "_setController",
	    "parametersSignature": "(ib)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_setController", [p0, p1])

def _writeTree() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_writeTree",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_writeTree", [])

def moveAlong(trajectory:object) -> bool:
	"""
	.
	
	Parameters
	----------
	trajectory:object
		An ALValue describing a trajectory.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "b",
	    "name": "moveAlong",
	    "parametersSignature": "(m)",
	    "description": ".",
	    "parameters": [
	        {
	            "name": "trajectory",
	            "description": "An ALValue describing a trajectory."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "moveAlong", [trajectory])

def _moveAlong(moveAlongScale:float, allowMove:bool, trajectory:object) -> bool:
	"""
	.
	
	Parameters
	----------
	moveAlongScale:float
		a scale factor
	allowMove:bool
		true if the robot should do any move at all
	trajectory:object
		An ALValue describing a trajectory.
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "_moveAlong",
	    "parametersSignature": "(fbm)",
	    "description": ".",
	    "parameters": [
	        {
	            "name": "moveAlongScale",
	            "description": "a scale factor"
	        },
	        {
	            "name": "allowMove",
	            "description": "true if the robot should do any move at all"
	        },
	        {
	            "name": "trajectory",
	            "description": "An ALValue describing a trajectory."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_moveAlong", [moveAlongScale, allowMove, trajectory])

def _enableSafety(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "v",
	    "name": "_enableSafety",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_enableSafety", [p0])

def _isSafetyEnabled() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "b",
	    "name": "_isSafetyEnabled",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_isSafetyEnabled", [])

def _isSafetyLoopRunning() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "b",
	    "name": "_isSafetyLoopRunning",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_isSafetyLoopRunning", [])

def _wakeUpCallBack() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_wakeUpCallBack",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_wakeUpCallBack", [])

def _restCallBack(p0:str, p1:object, p2:str) -> None:
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
	    "name": "_restCallBack",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_restCallBack", [p0, p1, p2])

def getFreeZone(desiredRadius:float, maximumDisplacement:float) -> object:
	"""
	Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]
	
	Parameters
	----------
	desiredRadius:float
		The radius of the space we want in meters [m].
	maximumDisplacement:float
		The max distance we accept to move toreach the found place [m].
	
	Returns
	----------
	Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "m",
	    "name": "getFreeZone",
	    "parametersSignature": "(ff)",
	    "description": "Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]",
	    "parameters": [
	        {
	            "name": "desiredRadius",
	            "description": "The radius of the space we want in meters [m]."
	        },
	        {
	            "name": "maximumDisplacement",
	            "description": "The max distance we accept to move toreach the found place [m]."
	        }
	    ],
	    "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	}
	'''
	"""
	return send_mfc("ALNavigation", "getFreeZone", [desiredRadius, maximumDisplacement])

def findFreeZone(desiredRadius:float, maximumDisplacement:float) -> object:
	"""
	Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]
	
	Parameters
	----------
	desiredRadius:float
		The radius of the space we want in meters [m].
	maximumDisplacement:float
		The max distance we accept to move toreach the found place [m].
	
	Returns
	----------
	Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "m",
	    "name": "findFreeZone",
	    "parametersSignature": "(ff)",
	    "description": "Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]",
	    "parameters": [
	        {
	            "name": "desiredRadius",
	            "description": "The radius of the space we want in meters [m]."
	        },
	        {
	            "name": "maximumDisplacement",
	            "description": "The max distance we accept to move toreach the found place [m]."
	        }
	    ],
	    "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	}
	'''
	"""
	return send_mfc("ALNavigation", "findFreeZone", [desiredRadius, maximumDisplacement])

def explore(p0:float) -> int:
	"""
	Start exploration.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "i",
	    "name": "explore",
	    "parametersSignature": "(f)",
	    "description": "Start exploration.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "explore", [p0])

def stopExploration() -> None:
	"""
	Stop exploration.
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "v",
	    "name": "stopExploration",
	    "parametersSignature": "()",
	    "description": "Stop exploration.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "stopExploration", [])

def getRobotPositionInMap() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "m",
	    "name": "getRobotPositionInMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "getRobotPositionInMap", [])

def getExplorationPath() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "m",
	    "name": "getExplorationPath",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "getExplorationPath", [])

def _getTopoMap() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "m",
	    "name": "_getTopoMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getTopoMap", [])

def _getExplorationParams() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "m",
	    "name": "_getExplorationParams",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getExplorationParams", [])

def _topoNavigateTo(p0:int) -> int:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 167,
	    "returnSignature": "i",
	    "name": "_topoNavigateTo",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_topoNavigateTo", [p0])

def loadExploration(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "b",
	    "name": "loadExploration",
	    "parametersSignature": "(s)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "loadExploration", [p0])

def navigateToInMap(p0:List[float]) -> int:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "i",
	    "name": "navigateToInMap",
	    "parametersSignature": "([f])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "navigateToInMap", [p0])

def _getScanHoles() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "m",
	    "name": "_getScanHoles",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getScanHoles", [])

def _getTargetScanHoleId() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "i",
	    "name": "_getTargetScanHoleId",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getTargetScanHoleId", [])

def _getTopoNodeOccupancyMap(p0:int) -> object:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "m",
	    "name": "_getTopoNodeOccupancyMap",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getTopoNodeOccupancyMap", [p0])

def _computeAggregatedMap() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "b",
	    "name": "_computeAggregatedMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_computeAggregatedMap", [])

def saveExploration() -> str:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "s",
	    "name": "saveExploration",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "saveExploration", [])

def getMetricalMap() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 175,
	    "returnSignature": "m",
	    "name": "getMetricalMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "getMetricalMap", [])

def _getLocalizationDebug() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "m",
	    "name": "_getLocalizationDebug",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getLocalizationDebug", [])

def relocalizeInMap(p0:List[float]) -> object:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 177,
	    "returnSignature": "m",
	    "name": "relocalizeInMap",
	    "parametersSignature": "([f])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "relocalizeInMap", [p0])

def startLocalization() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 178,
	    "returnSignature": "v",
	    "name": "startLocalization",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "startLocalization", [])

def stopLocalization() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 179,
	    "returnSignature": "v",
	    "name": "stopLocalization",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "stopLocalization", [])

def _startTopoMapper() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 180,
	    "returnSignature": "v",
	    "name": "_startTopoMapper",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_startTopoMapper", [])

def _stopTopoMapper() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 181,
	    "returnSignature": "v",
	    "name": "_stopTopoMapper",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_stopTopoMapper", [])

def _resetTopoMap() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 182,
	    "returnSignature": "v",
	    "name": "_resetTopoMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_resetTopoMap", [])

def _getFreeZoneCenter(p0:float) -> object:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 183,
	    "returnSignature": "m",
	    "name": "_getFreeZoneCenter",
	    "parametersSignature": "(d)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getFreeZoneCenter", [p0])

def _getFreeZoneWithConstraints(p0:float) -> object:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 184,
	    "returnSignature": "m",
	    "name": "_getFreeZoneWithConstraints",
	    "parametersSignature": "(f)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getFreeZoneWithConstraints", [p0])

def startFreeZoneUpdate() -> None:
	"""
	 Starts a loop to update the mapping of the free space around the robot. 
	
	*Reference struct*
	'''
	{
	    "uid": 185,
	    "returnSignature": "v",
	    "name": "startFreeZoneUpdate",
	    "parametersSignature": "()",
	    "description": " Starts a loop to update the mapping of the free space around the robot. ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "startFreeZoneUpdate", [])

def _startFreeZoneUpdateWithTimeout(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 186,
	    "returnSignature": "v",
	    "name": "_startFreeZoneUpdateWithTimeout",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_startFreeZoneUpdateWithTimeout", [p0])

def stopAndComputeFreeZone(desiredRadius:float, maximumDisplacement:float) -> object:
	"""
	Stops and returns free zone.
	
	Parameters
	----------
	desiredRadius:float
		The radius of the space we want in meters [m].
	maximumDisplacement:float
		The max distance we accept to move toreach the found place [m].
	
	Returns
	----------
	Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]
	
	*Reference struct*
	'''
	{
	    "uid": 187,
	    "returnSignature": "m",
	    "name": "stopAndComputeFreeZone",
	    "parametersSignature": "(ff)",
	    "description": "Stops and returns free zone.",
	    "parameters": [
	        {
	            "name": "desiredRadius",
	            "description": "The radius of the space we want in meters [m]."
	        },
	        {
	            "name": "maximumDisplacement",
	            "description": "The max distance we accept to move toreach the found place [m]."
	        }
	    ],
	    "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	}
	'''
	"""
	return send_mfc("ALNavigation", "stopAndComputeFreeZone", [desiredRadius, maximumDisplacement])

def _moveToFreeZoneCenter() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 188,
	    "returnSignature": "v",
	    "name": "_moveToFreeZoneCenter",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_moveToFreeZoneCenter", [])

def _stopFreeZoneTasks() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 189,
	    "returnSignature": "v",
	    "name": "_stopFreeZoneTasks",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_stopFreeZoneTasks", [])

def _writeFreeZone() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 190,
	    "returnSignature": "v",
	    "name": "_writeFreeZone",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_writeFreeZone", [])

def _clearFreeZone() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 191,
	    "returnSignature": "v",
	    "name": "_clearFreeZone",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_clearFreeZone", [])

def _getFreeZoneMap() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 192,
	    "returnSignature": "m",
	    "name": "_getFreeZoneMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getFreeZoneMap", [])

def _writeDilatedMaps() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 193,
	    "returnSignature": "v",
	    "name": "_writeDilatedMaps",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_writeDilatedMaps", [])

def _startDiagnosis(p0:List[str]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 194,
	    "returnSignature": "v",
	    "name": "_startDiagnosis",
	    "parametersSignature": "([s])",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_startDiagnosis", [p0])

def _stopDiagnosis() -> object:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 195,
	    "returnSignature": "m",
	    "name": "_stopDiagnosis",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_stopDiagnosis", [])

def _passiveDiagnosisCallBack(p0:str, p1:object, p2:str) -> None:
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
	    "uid": 196,
	    "returnSignature": "v",
	    "name": "_passiveDiagnosisCallBack",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_passiveDiagnosisCallBack", [p0, p1, p2])

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
	    "uid": 197,
	    "returnSignature": "v",
	    "name": "_activeDiagnosisCallBack",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_activeDiagnosisCallBack", [p0, p1, p2])

def _get3DMap() -> str:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 198,
	    "returnSignature": "s",
	    "name": "_get3DMap",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_get3DMap", [])

def _eventMoveFailedCallback() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 199,
	    "returnSignature": "v",
	    "name": "_eventMoveFailedCallback",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_eventMoveFailedCallback", [])

def _setFreeZoneTimeout(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 200,
	    "returnSignature": "v",
	    "name": "_setFreeZoneTimeout",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_setFreeZoneTimeout", [p0])

def _setObstaclesNumber(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 201,
	    "returnSignature": "v",
	    "name": "_setObstaclesNumber",
	    "parametersSignature": "(I)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_setObstaclesNumber", [p0])

def _getObstaclesNumber() -> int:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 202,
	    "returnSignature": "i",
	    "name": "_getObstaclesNumber",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getObstaclesNumber", [])

def _setDiagnosisLogEnabled(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 203,
	    "returnSignature": "v",
	    "name": "_setDiagnosisLogEnabled",
	    "parametersSignature": "(b)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_setDiagnosisLogEnabled", [p0])

def _isDiagnosisLogEnabled() -> bool:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 204,
	    "returnSignature": "b",
	    "name": "_isDiagnosisLogEnabled",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_isDiagnosisLogEnabled", [])

def _initLogger() -> None:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 205,
	    "returnSignature": "v",
	    "name": "_initLogger",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_initLogger", [])

def _enableTouchType(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 206,
	    "returnSignature": "v",
	    "name": "_enableTouchType",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_enableTouchType", [p0])

def _disableTouchType(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 207,
	    "returnSignature": "v",
	    "name": "_disableTouchType",
	    "parametersSignature": "(i)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_disableTouchType", [p0])

def _getEnabledTouchTypes() -> List[int]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 208,
	    "returnSignature": "[i]",
	    "name": "_getEnabledTouchTypes",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getEnabledTouchTypes", [])

def _onTouchChanged(p0:str, p1:object, p2:str) -> None:
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
	    "uid": 209,
	    "returnSignature": "v",
	    "name": "_onTouchChanged",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_onTouchChanged", [p0, p1, p2])

def _onPeopleDetected(p0:str, p1:object, p2:str) -> None:
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
	    "uid": 210,
	    "returnSignature": "v",
	    "name": "_onPeopleDetected",
	    "parametersSignature": "(sms)",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_onPeopleDetected", [p0, p1, p2])

def _getMapperNames() -> List[str]:
	"""
	.
	
	*Reference struct*
	'''
	{
	    "uid": 211,
	    "returnSignature": "[s]",
	    "name": "_getMapperNames",
	    "parametersSignature": "()",
	    "description": ".",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALNavigation", "_getMapperNames", [])

