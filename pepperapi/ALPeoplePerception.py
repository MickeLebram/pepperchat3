"""
This module controls the People Perception flow and pushes information about detected people in ALMemory.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

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
	return call_method("ALPeoplePerception", "version", [])

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
	return call_method("ALPeoplePerception", "ping", [])

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
	return call_method("ALPeoplePerception", "getMethodList", [])

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
	return call_method("ALPeoplePerception", "getMethodHelp", [methodName])

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
	return call_method("ALPeoplePerception", "getModuleHelp", [])

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
	return call_method("ALPeoplePerception", "getBrokerName", [])

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
	return call_method("ALPeoplePerception", "getUsage", [name])

@overload
def subscribe(name:str, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def subscribe(name:str, period:int, precision:float, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(sif)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds) if relevant."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor if relevant."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def subscribe(*args, **kwargs):
	"""
	Bridge notes
	------------
	subscribe has 2 variants on the robot:
	- subscribe(name:str)
	- subscribe(name:str, period:int, precision:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPeoplePerception.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPeoplePerception", "subscribe", list(args))

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Unsubscribes from the extractor.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which had subscribed."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "updatePeriod",
	#     "parametersSignature": "(si)",
	#     "description": "Updates the period if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "updatePrecision",
	#     "parametersSignature": "(sf)",
	#     "description": "Updates the precision if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "i",
	#     "name": "getCurrentPeriod",
	#     "parametersSignature": "()",
	#     "description": "Gets the current period.",
	#     "parameters": [],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALPeoplePerception", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "f",
	#     "name": "getCurrentPrecision",
	#     "parametersSignature": "()",
	#     "description": "Gets the current precision.",
	#     "parameters": [],
	#     "returnDescription": "Precision of the extractor."
	# }
	return call_method("ALPeoplePerception", "getCurrentPrecision", [])

def getMyPeriod(name:str) -> int:
	"""
	Gets the period for a specific subscription.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "getMyPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the period for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         }
	#     ],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALPeoplePerception", "getMyPeriod", [name])

def getMyPrecision(name:str) -> float:
	"""
	Gets the precision for a specific subscription.
	
	Parameters
	----------
	name:str
		name of the module which has subscribed
	
	Returns
	----------
	precision of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "f",
	#     "name": "getMyPrecision",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the precision for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of the module which has subscribed"
	#         }
	#     ],
	#     "returnDescription": "precision of the extractor"
	# }
	return call_method("ALPeoplePerception", "getMyPrecision", [name])

def getSubscribersInfo() -> object:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getSubscribersInfo",
	#     "parametersSignature": "()",
	#     "description": "Gets the parameters given by the module.",
	#     "parameters": [],
	#     "returnDescription": "Array of names and parameters of all subscribers."
	# }
	return call_method("ALPeoplePerception", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getOutputNames",
	#     "parametersSignature": "()",
	#     "description": "Get the list of values updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of values updated by this extractor in ALMemory"
	# }
	return call_method("ALPeoplePerception", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getEventList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALPeoplePerception", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "getMemoryKeyList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALPeoplePerception", "getMemoryKeyList", [])

def isPaused() -> bool:
	"""
	Gets extractor pause status
	
	Returns
	----------
	True if the extractor is paused, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "isPaused",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor pause status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is paused, False if not"
	# }
	return call_method("ALPeoplePerception", "isPaused", [])

def pause(status:bool) -> None:
	"""
	Changes the pause status of the extractor
	
	Parameters
	----------
	status:bool
		New pause satus
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "pause",
	#     "parametersSignature": "(b)",
	#     "description": "Changes the pause status of the extractor",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "New pause satus"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "pause", [status])

def isProcessing() -> bool:
	"""
	Gets extractor running status
	
	Returns
	----------
	True if the extractor is currently processing images, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "b",
	#     "name": "isProcessing",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor running status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is currently processing images, False if not"
	# }
	return call_method("ALPeoplePerception", "isProcessing", [])

def getMaximumDetectionRange() -> float:
	"""
	Gets the current maximum detection and tracking range.
	
	Returns
	----------
	Maximum range in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "f",
	#     "name": "getMaximumDetectionRange",
	#     "parametersSignature": "()",
	#     "description": "Gets the current maximum detection and tracking range.",
	#     "parameters": [],
	#     "returnDescription": "Maximum range in meters."
	# }
	return call_method("ALPeoplePerception", "getMaximumDetectionRange", [])

def getMinimumBodyHeight() -> float:
	"""
	Gets the current minimum body height used for human detection (3D mode only).
	
	Returns
	----------
	Minimum height in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "f",
	#     "name": "getMinimumBodyHeight",
	#     "parametersSignature": "()",
	#     "description": "Gets the current minimum body height used for human detection (3D mode only).",
	#     "parameters": [],
	#     "returnDescription": "Minimum height in meters."
	# }
	return call_method("ALPeoplePerception", "getMinimumBodyHeight", [])

def getMaximumBodyHeight() -> float:
	"""
	Gets the current maximum body height used for human detection (3D mode only).
	
	Returns
	----------
	Maximum height in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "f",
	#     "name": "getMaximumBodyHeight",
	#     "parametersSignature": "()",
	#     "description": "Gets the current maximum body height used for human detection (3D mode only).",
	#     "parameters": [],
	#     "returnDescription": "Maximum height in meters."
	# }
	return call_method("ALPeoplePerception", "getMaximumBodyHeight", [])

def getTimeBeforePersonDisappears() -> float:
	"""
	Gets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.
	
	Returns
	----------
	Time in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "f",
	#     "name": "getTimeBeforePersonDisappears",
	#     "parametersSignature": "()",
	#     "description": "Gets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.",
	#     "parameters": [],
	#     "returnDescription": "Time in seconds."
	# }
	return call_method("ALPeoplePerception", "getTimeBeforePersonDisappears", [])

def getTimeBeforeVisiblePersonDisappears() -> float:
	"""
	Gets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.
	
	Returns
	----------
	Time in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "f",
	#     "name": "getTimeBeforeVisiblePersonDisappears",
	#     "parametersSignature": "()",
	#     "description": "Gets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.",
	#     "parameters": [],
	#     "returnDescription": "Time in seconds."
	# }
	return call_method("ALPeoplePerception", "getTimeBeforeVisiblePersonDisappears", [])

def isFaceDetectionEnabled() -> bool:
	"""
	Gets the current status of face detection.
	
	Returns
	----------
	True if face detection is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "isFaceDetectionEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of face detection.",
	#     "parameters": [],
	#     "returnDescription": "True if face detection is enabled, False otherwise."
	# }
	return call_method("ALPeoplePerception", "isFaceDetectionEnabled", [])

def isFastModeEnabled() -> bool:
	"""
	Gets the current status of fast mode.
	
	Returns
	----------
	True if fast mode is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "isFastModeEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of fast mode.",
	#     "parameters": [],
	#     "returnDescription": "True if fast mode is enabled, False otherwise."
	# }
	return call_method("ALPeoplePerception", "isFastModeEnabled", [])

def isGraphicalDisplayEnabled() -> bool:
	"""
	Gets the current status of graphical display in Choregraphe.
	
	Returns
	----------
	True if graphical display is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "b",
	#     "name": "isGraphicalDisplayEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of graphical display in Choregraphe.",
	#     "parameters": [],
	#     "returnDescription": "True if graphical display is enabled, False otherwise."
	# }
	return call_method("ALPeoplePerception", "isGraphicalDisplayEnabled", [])

def isMovementDetectionEnabled() -> bool:
	"""
	Gets the current status of movement detection in Choregraphe.
	
	Returns
	----------
	True if movement detection is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "b",
	#     "name": "isMovementDetectionEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of movement detection in Choregraphe.",
	#     "parameters": [],
	#     "returnDescription": "True if movement detection is enabled, False otherwise."
	# }
	return call_method("ALPeoplePerception", "isMovementDetectionEnabled", [])

def resetPopulation() -> None:
	"""
	Empties the tracked population.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "resetPopulation",
	#     "parametersSignature": "()",
	#     "description": "Empties the tracked population.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "resetPopulation", [])

def setFastModeEnabled(enable:bool) -> None:
	"""
	Turns fast mode on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "setFastModeEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turns fast mode on or off.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setFastModeEnabled", [enable])

def setGraphicalDisplayEnabled(enable:bool) -> None:
	"""
	Turns graphical display in Choregraphe on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "setGraphicalDisplayEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turns graphical display in Choregraphe on or off.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setGraphicalDisplayEnabled", [enable])

def setMaximumDetectionRange(range:float) -> None:
	"""
	Sets the maximum range for human detection and tracking.
	
	Parameters
	----------
	range:float
		Maximum range in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "setMaximumDetectionRange",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the maximum range for human detection and tracking.",
	#     "parameters": [
	#         {
	#             "name": "range",
	#             "description": "Maximum range in meters."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setMaximumDetectionRange", [range])

def setMinimumBodyHeight(height:float) -> None:
	"""
	Sets the minimum human body height (3D mode only).
	
	Parameters
	----------
	height:float
		Minimum height in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "setMinimumBodyHeight",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the minimum human body height (3D mode only).",
	#     "parameters": [
	#         {
	#             "name": "height",
	#             "description": "Minimum height in meters."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setMinimumBodyHeight", [height])

def setMaximumBodyHeight(height:float) -> None:
	"""
	Sets the maximum human body height (3D mode only).
	
	Parameters
	----------
	height:float
		Maximum height in meters.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "setMaximumBodyHeight",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the maximum human body height (3D mode only).",
	#     "parameters": [
	#         {
	#             "name": "height",
	#             "description": "Maximum height in meters."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setMaximumBodyHeight", [height])

def setMovementDetectionEnabled(enable:bool) -> None:
	"""
	Turns movement detection on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "setMovementDetectionEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turns movement detection on or off.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setMovementDetectionEnabled", [enable])

def setTimeBeforePersonDisappears(seconds:float) -> None:
	"""
	Sets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.
	
	Parameters
	----------
	seconds:float
		Time in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "setTimeBeforePersonDisappears",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the time after which a person, supposed not to be in the field of view of the camera disappears if it has not been detected.",
	#     "parameters": [
	#         {
	#             "name": "seconds",
	#             "description": "Time in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setTimeBeforePersonDisappears", [seconds])

def setTimeBeforeVisiblePersonDisappears(seconds:float) -> None:
	"""
	Sets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.
	
	Parameters
	----------
	seconds:float
		Time in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "setTimeBeforeVisiblePersonDisappears",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the time after which a person, supposed to be in the field of view of the camera disappears if it has not been detected.",
	#     "parameters": [
	#         {
	#             "name": "seconds",
	#             "description": "Time in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setTimeBeforeVisiblePersonDisappears", [seconds])

def _getDetectionMode() -> str:
	"""
	Gets the mode (2D/3D) used for the people detection.
	
	Returns
	----------
	Current mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "s",
	#     "name": "_getDetectionMode",
	#     "parametersSignature": "()",
	#     "description": "Gets the mode (2D/3D) used for the people detection.",
	#     "parameters": [],
	#     "returnDescription": "Current mode."
	# }
	return call_method("ALPeoplePerception", "_getDetectionMode", [])

def _setDetectionMode(mode:str) -> None:
	"""
	Sets the mode (2D/3D) used for the people detection.
	
	Parameters
	----------
	mode:str
		Mode to use.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "_setDetectionMode",
	#     "parametersSignature": "(s)",
	#     "description": "Sets the mode (2D/3D) used for the people detection.",
	#     "parameters": [
	#         {
	#             "name": "mode",
	#             "description": "Mode to use."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "_setDetectionMode", [mode])

def setFaceDetectionEnabled(enable:bool) -> None:
	"""
	Turns face detection on or off.
	
	Parameters
	----------
	enable:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "setFaceDetectionEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turns face detection on or off.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPeoplePerception", "setFaceDetectionEnabled", [enable])

class _Signals:
	maximumDetectionRangeChanged: Signal[[float]] = Signal("ALPeoplePerception", "maximumDetectionRangeChanged")
	"""
	Bridge notes
	------------
	A signal sent by ALPeoplePerception on the robot.
	
	subscribe(callback) calls callback(float) each time the robot sends it.
	"""
	justArrived: Signal[[int]] = Signal("ALPeoplePerception", "justArrived")
	"""
	Bridge notes
	------------
	A signal sent by ALPeoplePerception on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	justLeft: Signal[[int]] = Signal("ALPeoplePerception", "justLeft")
	"""
	Bridge notes
	------------
	A signal sent by ALPeoplePerception on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	populationReset: Signal[[]] = Signal("ALPeoplePerception", "populationReset")
	"""
	Bridge notes
	------------
	A signal sent by ALPeoplePerception on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
signals = _Signals()

