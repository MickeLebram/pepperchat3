"""
Use ALNavigation module to make the robot go safely to the asked pose2D.
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
	return call_method("ALNavigation", "version", [])

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
	return call_method("ALNavigation", "ping", [])

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
	return call_method("ALNavigation", "getMethodList", [])

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
	return call_method("ALNavigation", "getMethodHelp", [methodName])

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
	return call_method("ALNavigation", "getModuleHelp", [])

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
	return call_method("ALNavigation", "getBrokerName", [])

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
	return call_method("ALNavigation", "getUsage", [name])

@overload
def navigateTo(x:float, y:float, /) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	
	Bridge notes
	------------
	navigateTo has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- navigateTo_1(float, float)
	- navigateTo_2(float, float, float)
	- navigateTo_3(float, float, Any)
	- navigateTo_4(float, float, float, Any)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(ff)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def navigateTo(x:float, y:float, theta:float, /) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	
	Bridge notes
	------------
	navigateTo has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- navigateTo_1(float, float)
	- navigateTo_2(float, float, float)
	- navigateTo_3(float, float, Any)
	- navigateTo_4(float, float, float, Any)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(fff)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "theta",
	#             "description": "Orientation of the robot (rad)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def navigateTo(x:float, y:float, config:Any, /) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	config:Any
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	Bridge notes
	------------
	navigateTo has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- navigateTo_1(float, float)
	- navigateTo_2(float, float, float)
	- navigateTo_3(float, float, Any)
	- navigateTo_4(float, float, float, Any)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(ffm)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "config",
	#             "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def navigateTo(x:float, y:float, theta:float, config:Any, /) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	config:Any
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	Bridge notes
	------------
	navigateTo has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- navigateTo_1(float, float)
	- navigateTo_2(float, float, float)
	- navigateTo_3(float, float, Any)
	- navigateTo_4(float, float, float, Any)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(fffm)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "theta",
	#             "description": "Orientation of the robot (rad)."
	#         },
	#         {
	#             "name": "config",
	#             "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def navigateTo(*args, **kwargs):
	"""
	Bridge notes
	------------
	navigateTo has 4 variants on the robot:
	- navigateTo(x:float, y:float), explicitly navigateTo_1
	- navigateTo(x:float, y:float, theta:float), explicitly navigateTo_2
	- navigateTo(x:float, y:float, config:Any), explicitly navigateTo_3
	- navigateTo(x:float, y:float, theta:float, config:Any), explicitly navigateTo_4
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALNavigation.navigateTo has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALNavigation", "navigateTo", list(args))

def navigateTo_1(x:float, y:float) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	
	Bridge notes
	------------
	Explicit variant of navigateTo(float, float). Calling navigateTo instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(ff)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "navigateTo", [x, y])

def navigateTo_2(x:float, y:float, theta:float) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	
	Bridge notes
	------------
	Explicit variant of navigateTo(float, float, float). Calling navigateTo instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(fff)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "theta",
	#             "description": "Orientation of the robot (rad)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "navigateTo", [x, y, theta])

def navigateTo_3(x:float, y:float, config:Any) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	config:Any
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	Bridge notes
	------------
	Explicit variant of navigateTo(float, float, Any). Calling navigateTo instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(ffm)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "config",
	#             "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "navigateTo", [x, y, config])

def navigateTo_4(x:float, y:float, theta:float, config:Any) -> bool:
	"""
	Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		Orientation of the robot (rad).
	config:Any
		Configuration ALValue. For example, [["SpeedFactor", 0.5]] sets speedFactor to 0.5
	
	Bridge notes
	------------
	Explicit variant of navigateTo(float, float, float, Any). Calling navigateTo instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "navigateTo",
	#     "parametersSignature": "(fffm)",
	#     "description": "Makes the robot navigate to a relative metrical target pose2D expressed in FRAME_ROBOT. The robot computes a path to avoid obstacles.",
	#     "parameters": [
	#         {
	#             "name": "x",
	#             "description": "The position along x axis [m]."
	#         },
	#         {
	#             "name": "y",
	#             "description": "The position along y axis [m]."
	#         },
	#         {
	#             "name": "theta",
	#             "description": "Orientation of the robot (rad)."
	#         },
	#         {
	#             "name": "config",
	#             "description": "Configuration ALValue. For example, [[\"SpeedFactor\", 0.5]] sets speedFactor to 0.5"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "navigateTo", [x, y, theta, config])

def _setNavigationConfig(config:Any) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:Any
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_setNavigationConfig",
	#     "parametersSignature": "(m)",
	#     "description": "Internal Use.",
	#     "parameters": [
	#         {
	#             "name": "config",
	#             "description": "Internal: An array of ALValues [i][0]: name, [i][1]: value"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setNavigationConfig", [config])

def stopNavigateTo() -> None:
	"""
	Stops the navigateTo.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "stopNavigateTo",
	#     "parametersSignature": "()",
	#     "description": "Stops the navigateTo.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "stopNavigateTo", [])

def _stopNavigateToWithoutStopMove() -> None:
	"""
	Stops the navigateTo but no stop move.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "_stopNavigateToWithoutStopMove",
	#     "parametersSignature": "()",
	#     "description": "Stops the navigateTo but no stop move.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_stopNavigateToWithoutStopMove", [])

def _isNavigateToRunning() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "_isNavigateToRunning",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_isNavigateToRunning", [])

def _getObstacleData() -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are the one used by the secure navigator
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "m",
	#     "name": "_getObstacleData",
	#     "parametersSignature": "()",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are the one used by the secure navigator",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getObstacleData", [])

def _getOccupancyGrid(client:str) -> Any:
	"""
	Get the requested occupancy grid formatted as a ROS navigation stack message.
	
	Parameters
	----------
	client:str
		Internal: 'Secure' for SecureNavigator or 'Local' for LocalNavigator.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "_getOccupancyGrid",
	#     "parametersSignature": "(s)",
	#     "description": "Get the requested occupancy grid formatted as a ROS navigation stack message.",
	#     "parameters": [
	#         {
	#             "name": "client",
	#             "description": "Internal: 'Secure' for SecureNavigator or 'Local' for LocalNavigator."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getOccupancyGrid", [client])

@overload
def _getSensorData() -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Bridge notes
	------------
	_getSensorData has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- _getSensorData_1()
	- _getSensorData_2(List[str])
	- _getSensorData_3(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "()",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _getSensorData(p0:str, /) -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	_getSensorData has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- _getSensorData_1()
	- _getSensorData_2(List[str])
	- _getSensorData_3(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "(s)",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _getSensorData(p0:List[str], /) -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:List[str]
		
	
	Bridge notes
	------------
	_getSensorData has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- _getSensorData_1()
	- _getSensorData_2(List[str])
	- _getSensorData_3(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "([s])",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _getSensorData(*args, **kwargs):
	"""
	Bridge notes
	------------
	_getSensorData has 3 variants on the robot:
	- _getSensorData(), explicitly _getSensorData_1
	- _getSensorData(p0:str), explicitly _getSensorData_3
	- _getSensorData(p0:List[str]), explicitly _getSensorData_2
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALNavigation._getSensorData has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALNavigation", "_getSensorData", list(args))

def _getSensorData_1() -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Bridge notes
	------------
	Explicit variant of _getSensorData(). Calling _getSensorData instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "()",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorData", [])

def _getSensorData_2(p0:List[str]) -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:List[str]
		
	
	Bridge notes
	------------
	Explicit variant of _getSensorData(List[str]). Calling _getSensorData instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "([s])",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorData", [p0])

def _getSensorData_3(p0:str) -> Any:
	"""
	Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	Explicit variant of _getSensorData(str). Calling _getSensorData instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "m",
	#     "name": "_getSensorData",
	#     "parametersSignature": "(s)",
	#     "description": "Obstacles data.ALArray formatted as follow for each ALValue : [0]:familyName[1]:name[2]:Array containing [x, y] arrays of points in robot frame.Those obstacles are taken from sensors",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorData", [p0])

def _subscribeToAll(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "_subscribeToAll",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_subscribeToAll", [p0])

def _subscribe(clientName:str, p1:List[str]) -> bool:
	"""
	Start active sensors.The client needs to specify its name to register.If the client is the only one to register, the sensors are turned on, otherwise they are already started.
	
	Parameters
	----------
	clientName:str
		The client name.
	p1:List[str]
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "_subscribe",
	#     "parametersSignature": "(s[s])",
	#     "description": "Start active sensors.The client needs to specify its name to register.If the client is the only one to register, the sensors are turned on, otherwise they are already started.",
	#     "parameters": [
	#         {
	#             "name": "clientName",
	#             "description": "The client name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_subscribe", [clientName, p1])

def _unsubscribeFromAll(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "b",
	#     "name": "_unsubscribeFromAll",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_unsubscribeFromAll", [p0])

def _unsubscribe(clientName:str, p1:List[str]) -> bool:
	"""
	Stop active sensors.The client needs to specify its name to unregister.The active sensors are actually stopped if not client is registered anymore.
	
	Parameters
	----------
	clientName:str
		The client name.
	p1:List[str]
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "_unsubscribe",
	#     "parametersSignature": "(s[s])",
	#     "description": "Stop active sensors.The client needs to specify its name to unregister.The active sensors are actually stopped if not client is registered anymore.",
	#     "parameters": [
	#         {
	#             "name": "clientName",
	#             "description": "The client name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_unsubscribe", [clientName, p1])

def _addSensor(sensor:str) -> bool:
	"""
	Add a sensor family or a sensor.
	
	Parameters
	----------
	sensor:str
		The sensor family name or name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "_addSensor",
	#     "parametersSignature": "(s)",
	#     "description": "Add a sensor family or a sensor.",
	#     "parameters": [
	#         {
	#             "name": "sensor",
	#             "description": "The sensor family name or name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_addSensor", [sensor])

def _removeSensor(sensor:str) -> bool:
	"""
	Remove a sensor family or a sensor.
	
	Parameters
	----------
	sensor:str
		The sensor family name or name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "b",
	#     "name": "_removeSensor",
	#     "parametersSignature": "(s)",
	#     "description": "Remove a sensor family or a sensor.",
	#     "parameters": [
	#         {
	#             "name": "sensor",
	#             "description": "The sensor family name or name."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_removeSensor", [sensor])

def _getTrajectory() -> Any:
	"""
	Get trajectory from local navigator.ALArray containing successively x, y and theta coordinates.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "m",
	#     "name": "_getTrajectory",
	#     "parametersSignature": "()",
	#     "description": "Get trajectory from local navigator.ALArray containing successively x, y and theta coordinates.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getTrajectory", [])

def _setSpeedFactor(p0:float) -> None:
	"""
	Set speed factor for local navigator
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "_setSpeedFactor",
	#     "parametersSignature": "(f)",
	#     "description": "Set speed factor for local navigator",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setSpeedFactor", [p0])

def _getObstacleMap(p0:str) -> Any:
	"""
	Get obstacle Map from localnavigator. ALValue formatted as follow for each sensor :[[SensorName1 [[x1 y1] [x2 y2] [x3 y3] ...]] [SensorName2 [[x1 y1] [x2 y2] [x3 y3] ...]] ... ]
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "m",
	#     "name": "_getObstacleMap",
	#     "parametersSignature": "(s)",
	#     "description": "Get obstacle Map from localnavigator. ALValue formatted as follow for each sensor :[[SensorName1 [[x1 y1] [x2 y2] [x3 y3] ...]] [SensorName2 [[x1 y1] [x2 y2] [x3 y3] ...]] ... ]",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getObstacleMap", [p0])

def _enableSensorDebug(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "_enableSensorDebug",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_enableSensorDebug", [p0])

def _useHeadChecking(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_useHeadChecking",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_useHeadChecking", [p0])

def _usePathChecking(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "_usePathChecking",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_usePathChecking", [p0])

def _usePathCorrection(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_usePathCorrection",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_usePathCorrection", [p0])

def _useArmsOnBelly(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "_useArmsOnBelly",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_useArmsOnBelly", [p0])

def _useSpeedFactor(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "_useSpeedFactor",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_useSpeedFactor", [p0])

def _clearObstacleMap() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "_clearObstacleMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_clearObstacleMap", [])

def _useClearNavigationMap(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "_useClearNavigationMap",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_useClearNavigationMap", [p0])

def _clearNavigationMap() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "_clearNavigationMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_clearNavigationMap", [])

def _getSensorSubscribers() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "m",
	#     "name": "_getSensorSubscribers",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorSubscribers", [])

def _getSensorList() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "m",
	#     "name": "_getSensorList",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorList", [])

def _getSensorListBySubscriber(p0:str) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "m",
	#     "name": "_getSensorListBySubscriber",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getSensorListBySubscriber", [p0])

def _getActiveSensorList() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "m",
	#     "name": "_getActiveSensorList",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getActiveSensorList", [])

def _isSensorEnabled(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "b",
	#     "name": "_isSensorEnabled",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_isSensorEnabled", [p0])

def _setController(p0:int, p1:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	p1:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "_setController",
	#     "parametersSignature": "(ib)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setController", [p0, p1])

def _writeTree() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "_writeTree",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_writeTree", [])

def moveAlong(trajectory:Any) -> bool:
	"""
	.
	
	Parameters
	----------
	trajectory:Any
		An ALValue describing a trajectory.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "b",
	#     "name": "moveAlong",
	#     "parametersSignature": "(m)",
	#     "description": ".",
	#     "parameters": [
	#         {
	#             "name": "trajectory",
	#             "description": "An ALValue describing a trajectory."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "moveAlong", [trajectory])

def _moveAlong(moveAlongScale:float, allowMove:bool, trajectory:Any) -> bool:
	"""
	.
	
	Parameters
	----------
	moveAlongScale:float
		a scale factor
	allowMove:bool
		true if the robot should do any move at all
	trajectory:Any
		An ALValue describing a trajectory.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "b",
	#     "name": "_moveAlong",
	#     "parametersSignature": "(fbm)",
	#     "description": ".",
	#     "parameters": [
	#         {
	#             "name": "moveAlongScale",
	#             "description": "a scale factor"
	#         },
	#         {
	#             "name": "allowMove",
	#             "description": "true if the robot should do any move at all"
	#         },
	#         {
	#             "name": "trajectory",
	#             "description": "An ALValue describing a trajectory."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_moveAlong", [moveAlongScale, allowMove, trajectory])

def _enableSafety(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "v",
	#     "name": "_enableSafety",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_enableSafety", [p0])

def _isSafetyEnabled() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "b",
	#     "name": "_isSafetyEnabled",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_isSafetyEnabled", [])

def _isSafetyLoopRunning() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "b",
	#     "name": "_isSafetyLoopRunning",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_isSafetyLoopRunning", [])

def _wakeUpCallBack() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "_wakeUpCallBack",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_wakeUpCallBack", [])

def _restCallBack(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "_restCallBack",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_restCallBack", [p0, p1, p2])

def getFreeZone(desiredRadius:float, maximumDisplacement:float) -> Any:
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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "m",
	#     "name": "getFreeZone",
	#     "parametersSignature": "(ff)",
	#     "description": "Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]",
	#     "parameters": [
	#         {
	#             "name": "desiredRadius",
	#             "description": "The radius of the space we want in meters [m]."
	#         },
	#         {
	#             "name": "maximumDisplacement",
	#             "description": "The max distance we accept to move toreach the found place [m]."
	#         }
	#     ],
	#     "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	# }
	return call_method("ALNavigation", "getFreeZone", [desiredRadius, maximumDisplacement])

def findFreeZone(desiredRadius:float, maximumDisplacement:float) -> Any:
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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "m",
	#     "name": "findFreeZone",
	#     "parametersSignature": "(ff)",
	#     "description": "Returns [errorCode, result radius[centerWorldMotionX, centerWorldMotionY]]",
	#     "parameters": [
	#         {
	#             "name": "desiredRadius",
	#             "description": "The radius of the space we want in meters [m]."
	#         },
	#         {
	#             "name": "maximumDisplacement",
	#             "description": "The max distance we accept to move toreach the found place [m]."
	#         }
	#     ],
	#     "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	# }
	return call_method("ALNavigation", "findFreeZone", [desiredRadius, maximumDisplacement])

def explore(p0:float) -> int:
	"""
	Start exploration.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "i",
	#     "name": "explore",
	#     "parametersSignature": "(f)",
	#     "description": "Start exploration.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "explore", [p0])

def stopExploration() -> None:
	"""
	Stop exploration.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "v",
	#     "name": "stopExploration",
	#     "parametersSignature": "()",
	#     "description": "Stop exploration.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "stopExploration", [])

def getRobotPositionInMap() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "m",
	#     "name": "getRobotPositionInMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "getRobotPositionInMap", [])

def getExplorationPath() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "m",
	#     "name": "getExplorationPath",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "getExplorationPath", [])

def _getTopoMap() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "m",
	#     "name": "_getTopoMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getTopoMap", [])

def _getExplorationParams() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "m",
	#     "name": "_getExplorationParams",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getExplorationParams", [])

def _topoNavigateTo(p0:int) -> int:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "i",
	#     "name": "_topoNavigateTo",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_topoNavigateTo", [p0])

def loadExploration(p0:str) -> bool:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "b",
	#     "name": "loadExploration",
	#     "parametersSignature": "(s)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "loadExploration", [p0])

def navigateToInMap(p0:List[float]) -> int:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "i",
	#     "name": "navigateToInMap",
	#     "parametersSignature": "([f])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "navigateToInMap", [p0])

def _getScanHoles() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "m",
	#     "name": "_getScanHoles",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getScanHoles", [])

def _getTargetScanHoleId() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "i",
	#     "name": "_getTargetScanHoleId",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getTargetScanHoleId", [])

def _getTopoNodeOccupancyMap(p0:int) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "m",
	#     "name": "_getTopoNodeOccupancyMap",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getTopoNodeOccupancyMap", [p0])

def _computeAggregatedMap() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "b",
	#     "name": "_computeAggregatedMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_computeAggregatedMap", [])

def saveExploration() -> str:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "s",
	#     "name": "saveExploration",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "saveExploration", [])

def getMetricalMap() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "m",
	#     "name": "getMetricalMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "getMetricalMap", [])

def _getLocalizationDebug() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "m",
	#     "name": "_getLocalizationDebug",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getLocalizationDebug", [])

def relocalizeInMap(p0:List[float]) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "m",
	#     "name": "relocalizeInMap",
	#     "parametersSignature": "([f])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "relocalizeInMap", [p0])

def startLocalization() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "v",
	#     "name": "startLocalization",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "startLocalization", [])

def stopLocalization() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 179,
	#     "returnSignature": "v",
	#     "name": "stopLocalization",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "stopLocalization", [])

def _startTopoMapper() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "v",
	#     "name": "_startTopoMapper",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_startTopoMapper", [])

def _stopTopoMapper() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "v",
	#     "name": "_stopTopoMapper",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_stopTopoMapper", [])

def _resetTopoMap() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "v",
	#     "name": "_resetTopoMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_resetTopoMap", [])

def _getFreeZoneCenter(p0:float) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "m",
	#     "name": "_getFreeZoneCenter",
	#     "parametersSignature": "(d)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getFreeZoneCenter", [p0])

def _getFreeZoneWithConstraints(p0:float) -> Any:
	"""
	.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "m",
	#     "name": "_getFreeZoneWithConstraints",
	#     "parametersSignature": "(f)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getFreeZoneWithConstraints", [p0])

def startFreeZoneUpdate() -> None:
	"""
	 Starts a loop to update the mapping of the free space around the robot. 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 185,
	#     "returnSignature": "v",
	#     "name": "startFreeZoneUpdate",
	#     "parametersSignature": "()",
	#     "description": " Starts a loop to update the mapping of the free space around the robot. ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "startFreeZoneUpdate", [])

def _startFreeZoneUpdateWithTimeout(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 186,
	#     "returnSignature": "v",
	#     "name": "_startFreeZoneUpdateWithTimeout",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_startFreeZoneUpdateWithTimeout", [p0])

def stopAndComputeFreeZone(desiredRadius:float, maximumDisplacement:float) -> Any:
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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 187,
	#     "returnSignature": "m",
	#     "name": "stopAndComputeFreeZone",
	#     "parametersSignature": "(ff)",
	#     "description": "Stops and returns free zone.",
	#     "parameters": [
	#         {
	#             "name": "desiredRadius",
	#             "description": "The radius of the space we want in meters [m]."
	#         },
	#         {
	#             "name": "maximumDisplacement",
	#             "description": "The max distance we accept to move toreach the found place [m]."
	#         }
	#     ],
	#     "returnDescription": "Returns [errorCode, result radius (m), [worldMotionToRobotCenterX (m), worldMotionToRobotCenterY (m)]]"
	# }
	return call_method("ALNavigation", "stopAndComputeFreeZone", [desiredRadius, maximumDisplacement])

def _moveToFreeZoneCenter() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 188,
	#     "returnSignature": "v",
	#     "name": "_moveToFreeZoneCenter",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_moveToFreeZoneCenter", [])

def _stopFreeZoneTasks() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 189,
	#     "returnSignature": "v",
	#     "name": "_stopFreeZoneTasks",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_stopFreeZoneTasks", [])

def _writeFreeZone() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 190,
	#     "returnSignature": "v",
	#     "name": "_writeFreeZone",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_writeFreeZone", [])

def _clearFreeZone() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 191,
	#     "returnSignature": "v",
	#     "name": "_clearFreeZone",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_clearFreeZone", [])

def _getFreeZoneMap() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 192,
	#     "returnSignature": "m",
	#     "name": "_getFreeZoneMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getFreeZoneMap", [])

def _writeDilatedMaps() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 193,
	#     "returnSignature": "v",
	#     "name": "_writeDilatedMaps",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_writeDilatedMaps", [])

def _startDiagnosis(p0:List[str]) -> None:
	"""
	.
	
	Parameters
	----------
	p0:List[str]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 194,
	#     "returnSignature": "v",
	#     "name": "_startDiagnosis",
	#     "parametersSignature": "([s])",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_startDiagnosis", [p0])

def _stopDiagnosis() -> Any:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 195,
	#     "returnSignature": "m",
	#     "name": "_stopDiagnosis",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_stopDiagnosis", [])

def _passiveDiagnosisCallBack(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 196,
	#     "returnSignature": "v",
	#     "name": "_passiveDiagnosisCallBack",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_passiveDiagnosisCallBack", [p0, p1, p2])

def _activeDiagnosisCallBack(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 197,
	#     "returnSignature": "v",
	#     "name": "_activeDiagnosisCallBack",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_activeDiagnosisCallBack", [p0, p1, p2])

def _get3DMap() -> str:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 198,
	#     "returnSignature": "s",
	#     "name": "_get3DMap",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_get3DMap", [])

def _eventMoveFailedCallback() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 199,
	#     "returnSignature": "v",
	#     "name": "_eventMoveFailedCallback",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_eventMoveFailedCallback", [])

def _setFreeZoneTimeout(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 200,
	#     "returnSignature": "v",
	#     "name": "_setFreeZoneTimeout",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setFreeZoneTimeout", [p0])

def _setObstaclesNumber(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 201,
	#     "returnSignature": "v",
	#     "name": "_setObstaclesNumber",
	#     "parametersSignature": "(I)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setObstaclesNumber", [p0])

def _getObstaclesNumber() -> int:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 202,
	#     "returnSignature": "i",
	#     "name": "_getObstaclesNumber",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getObstaclesNumber", [])

def _setDiagnosisLogEnabled(p0:bool) -> None:
	"""
	.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 203,
	#     "returnSignature": "v",
	#     "name": "_setDiagnosisLogEnabled",
	#     "parametersSignature": "(b)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_setDiagnosisLogEnabled", [p0])

def _isDiagnosisLogEnabled() -> bool:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 204,
	#     "returnSignature": "b",
	#     "name": "_isDiagnosisLogEnabled",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_isDiagnosisLogEnabled", [])

def _initLogger() -> None:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 205,
	#     "returnSignature": "v",
	#     "name": "_initLogger",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_initLogger", [])

def _enableTouchType(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 206,
	#     "returnSignature": "v",
	#     "name": "_enableTouchType",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_enableTouchType", [p0])

def _disableTouchType(p0:int) -> None:
	"""
	.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 207,
	#     "returnSignature": "v",
	#     "name": "_disableTouchType",
	#     "parametersSignature": "(i)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_disableTouchType", [p0])

def _getEnabledTouchTypes() -> List[int]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 208,
	#     "returnSignature": "[i]",
	#     "name": "_getEnabledTouchTypes",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getEnabledTouchTypes", [])

def _onTouchChanged(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 209,
	#     "returnSignature": "v",
	#     "name": "_onTouchChanged",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_onTouchChanged", [p0, p1, p2])

def _onPeopleDetected(p0:str, p1:Any, p2:str) -> None:
	"""
	.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 210,
	#     "returnSignature": "v",
	#     "name": "_onPeopleDetected",
	#     "parametersSignature": "(sms)",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_onPeopleDetected", [p0, p1, p2])

def _getMapperNames() -> List[str]:
	"""
	.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 211,
	#     "returnSignature": "[s]",
	#     "name": "_getMapperNames",
	#     "parametersSignature": "()",
	#     "description": ".",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALNavigation", "_getMapperNames", [])

