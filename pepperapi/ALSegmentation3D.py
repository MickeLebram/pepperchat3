"""

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
	return call_method("ALSegmentation3D", "version", [])

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
	return call_method("ALSegmentation3D", "ping", [])

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
	return call_method("ALSegmentation3D", "getMethodList", [])

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
	return call_method("ALSegmentation3D", "getMethodHelp", [methodName])

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
	return call_method("ALSegmentation3D", "getModuleHelp", [])

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
	return call_method("ALSegmentation3D", "getBrokerName", [])

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
	return call_method("ALSegmentation3D", "getUsage", [name])

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
		raise TypeError("ALSegmentation3D.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALSegmentation3D", "subscribe", list(args))

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
	return call_method("ALSegmentation3D", "unsubscribe", [name])

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
	return call_method("ALSegmentation3D", "updatePeriod", [name, period])

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
	return call_method("ALSegmentation3D", "updatePrecision", [name, precision])

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
	return call_method("ALSegmentation3D", "getCurrentPeriod", [])

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
	return call_method("ALSegmentation3D", "getCurrentPrecision", [])

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
	return call_method("ALSegmentation3D", "getMyPeriod", [name])

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
	return call_method("ALSegmentation3D", "getMyPrecision", [name])

def getSubscribersInfo() -> Any:
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
	return call_method("ALSegmentation3D", "getSubscribersInfo", [])

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
	return call_method("ALSegmentation3D", "getOutputNames", [])

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
	return call_method("ALSegmentation3D", "getEventList", [])

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
	return call_method("ALSegmentation3D", "getMemoryKeyList", [])

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
	return call_method("ALSegmentation3D", "isPaused", [])

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
	return call_method("ALSegmentation3D", "pause", [status])

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
	return call_method("ALSegmentation3D", "isProcessing", [])

def setFrameRate(value:int) -> bool:
	"""
	Sets extractor framerate
	
	Parameters
	----------
	value:int
		New framerate
	
	Returns
	----------
	True if the update succeeded, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "setFrameRate",
	#     "parametersSignature": "(i)",
	#     "description": "Sets extractor framerate",
	#     "parameters": [
	#         {
	#             "name": "value",
	#             "description": "New framerate"
	#         }
	#     ],
	#     "returnDescription": "True if the update succeeded, False if not"
	# }
	return call_method("ALSegmentation3D", "setFrameRate", [value])

def getFrameRate() -> int:
	"""
	Gets extractor framerate
	
	Returns
	----------
	Current value of the framerate of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor framerate",
	#     "parameters": [],
	#     "returnDescription": "Current value of the framerate of the extractor"
	# }
	return call_method("ALSegmentation3D", "getFrameRate", [])

def setResolution(resolution:int) -> bool:
	"""
	Sets extractor resolution
	
	Parameters
	----------
	resolution:int
		New resolution
	
	Returns
	----------
	True if the update succeeded, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "b",
	#     "name": "setResolution",
	#     "parametersSignature": "(i)",
	#     "description": "Sets extractor resolution",
	#     "parameters": [
	#         {
	#             "name": "resolution",
	#             "description": "New resolution"
	#         }
	#     ],
	#     "returnDescription": "True if the update succeeded, False if not"
	# }
	return call_method("ALSegmentation3D", "setResolution", [resolution])

def getResolution() -> int:
	"""
	Gets extractor resolution
	
	Returns
	----------
	Current value of the resolution of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor resolution",
	#     "parameters": [],
	#     "returnDescription": "Current value of the resolution of the extractor"
	# }
	return call_method("ALSegmentation3D", "getResolution", [])

def setActiveCamera(cameraId:int) -> bool:
	"""
	Sets extractor active camera
	
	Parameters
	----------
	cameraId:int
		Id of the camera that will become the active camera
	
	Returns
	----------
	True if the update succeeded, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "b",
	#     "name": "setActiveCamera",
	#     "parametersSignature": "(i)",
	#     "description": "Sets extractor active camera",
	#     "parameters": [
	#         {
	#             "name": "cameraId",
	#             "description": "Id of the camera that will become the active camera"
	#         }
	#     ],
	#     "returnDescription": "True if the update succeeded, False if not"
	# }
	return call_method("ALSegmentation3D", "setActiveCamera", [cameraId])

def getActiveCamera() -> int:
	"""
	Gets extractor active camera
	
	Returns
	----------
	Id of the current active camera of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "i",
	#     "name": "getActiveCamera",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor active camera",
	#     "parameters": [],
	#     "returnDescription": "Id of the current active camera of the extractor"
	# }
	return call_method("ALSegmentation3D", "getActiveCamera", [])

def getTopOfBlob(distance:float, frame:int, applyVerticalOffset:bool) -> Any:
	"""
	Returns the position of the top of the blob most in the center of the depth image, at the given distance, in the given frame.
	
	Parameters
	----------
	distance:float
		Estimation of the distance (in meters) of the blob or -1 for the nearest blob
	frame:int
		Frame in which to return the position (-1: FRAME_IMAGE, 0: FRAME_TORSO, 1: FRAME_WORLD, 2: FRAME_ROBOT
	applyVerticalOffset:bool
		True to apply the VerticalOffset when computing the position, False otherwise
	
	Returns
	----------
	Position of the top of the corresponding blob (if one is found) in the given frame (Format: [yaw,pitch,distance] in FRAME_IMAGE, [x,y,z] in the other frame).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "m",
	#     "name": "getTopOfBlob",
	#     "parametersSignature": "(fib)",
	#     "description": "Returns the position of the top of the blob most in the center of the depth image, at the given distance, in the given frame.",
	#     "parameters": [
	#         {
	#             "name": "distance",
	#             "description": "Estimation of the distance (in meters) of the blob or -1 for the nearest blob"
	#         },
	#         {
	#             "name": "frame",
	#             "description": "Frame in which to return the position (-1: FRAME_IMAGE, 0: FRAME_TORSO, 1: FRAME_WORLD, 2: FRAME_ROBOT"
	#         },
	#         {
	#             "name": "applyVerticalOffset",
	#             "description": "True to apply the VerticalOffset when computing the position, False otherwise"
	#         }
	#     ],
	#     "returnDescription": "Position of the top of the corresponding blob (if one is found) in the given frame (Format: [yaw,pitch,distance] in FRAME_IMAGE, [x,y,z] in the other frame)."
	# }
	return call_method("ALSegmentation3D", "getTopOfBlob", [distance, frame, applyVerticalOffset])

def setBlobTrackingEnabled(status:bool) -> None:
	"""
	Turn the blob tracker on or off. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.
	
	Parameters
	----------
	status:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "setBlobTrackingEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turn the blob tracker on or off. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSegmentation3D", "setBlobTrackingEnabled", [status])

def isBlobTrackingEnabled() -> bool:
	"""
	Gets the current status of the blob tracker. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.
	
	Returns
	----------
	True if the blob tracker is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "b",
	#     "name": "isBlobTrackingEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of the blob tracker. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.",
	#     "parameters": [],
	#     "returnDescription": "True if the blob tracker is enabled, False otherwise."
	# }
	return call_method("ALSegmentation3D", "isBlobTrackingEnabled", [])

def setBlobTrackingDistance(distance:float) -> None:
	"""
	Sets the distance (in meters) for the blob tracker
	
	Parameters
	----------
	distance:float
		New value (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "setBlobTrackingDistance",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the distance (in meters) for the blob tracker",
	#     "parameters": [
	#         {
	#             "name": "distance",
	#             "description": "New value (in meters)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSegmentation3D", "setBlobTrackingDistance", [distance])

def getBlobTrackingDistance() -> float:
	"""
	Gets the distance (in meters) for the blob tracker
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "f",
	#     "name": "getBlobTrackingDistance",
	#     "parametersSignature": "()",
	#     "description": "Gets the distance (in meters) for the blob tracker",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSegmentation3D", "getBlobTrackingDistance", [])

def setVerticalOffset(value:float) -> None:
	"""
	Sets the value of vertical offset (in meters) for the blob tracker
	
	Parameters
	----------
	value:float
		New vertical offset (in meters), added if positive, substracted if negative
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "setVerticalOffset",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the value of vertical offset (in meters) for the blob tracker",
	#     "parameters": [
	#         {
	#             "name": "value",
	#             "description": "New vertical offset (in meters), added if positive, substracted if negative"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSegmentation3D", "setVerticalOffset", [value])

def getVerticalOffset() -> float:
	"""
	Sets the value of vertical offset (in meters) for the blob tracker
	
	Returns
	----------
	Current vertical offset of the blob tracker
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "f",
	#     "name": "getVerticalOffset",
	#     "parametersSignature": "()",
	#     "description": "Sets the value of vertical offset (in meters) for the blob tracker",
	#     "parameters": [],
	#     "returnDescription": "Current vertical offset of the blob tracker"
	# }
	return call_method("ALSegmentation3D", "getVerticalOffset", [])

def setDeltaDepthThreshold(value:float) -> None:
	"""
	Sets the value of the depth threshold (in meters) used for the segmentation
	
	Parameters
	----------
	value:float
		New depth threshold (in meters) for the segmentation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "setDeltaDepthThreshold",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the value of the depth threshold (in meters) used for the segmentation",
	#     "parameters": [
	#         {
	#             "name": "value",
	#             "description": "New depth threshold (in meters) for the segmentation"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSegmentation3D", "setDeltaDepthThreshold", [value])

def getDeltaDepthThreshold() -> float:
	"""
	Gets the value of the depth threshold (in meters) used for the segmentation
	
	Returns
	----------
	Current depth threshold (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "f",
	#     "name": "getDeltaDepthThreshold",
	#     "parametersSignature": "()",
	#     "description": "Gets the value of the depth threshold (in meters) used for the segmentation",
	#     "parameters": [],
	#     "returnDescription": "Current depth threshold (in meters)"
	# }
	return call_method("ALSegmentation3D", "getDeltaDepthThreshold", [])

