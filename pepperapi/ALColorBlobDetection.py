"""
ALColorBlobDetection is a module which can detect blobs of a certain color.
  The output value is written in ALMemory has a Tracker microEvent.
 
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
	return call_method("ALColorBlobDetection", "version", [])

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
	return call_method("ALColorBlobDetection", "ping", [])

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
	return call_method("ALColorBlobDetection", "getMethodList", [])

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
	return call_method("ALColorBlobDetection", "getMethodHelp", [methodName])

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
	return call_method("ALColorBlobDetection", "getModuleHelp", [])

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
	return call_method("ALColorBlobDetection", "getBrokerName", [])

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
	return call_method("ALColorBlobDetection", "getUsage", [name])

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
		raise TypeError("ALColorBlobDetection.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALColorBlobDetection", "subscribe", list(args))

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
	return call_method("ALColorBlobDetection", "unsubscribe", [name])

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
	return call_method("ALColorBlobDetection", "updatePeriod", [name, period])

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
	return call_method("ALColorBlobDetection", "updatePrecision", [name, precision])

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
	return call_method("ALColorBlobDetection", "getCurrentPeriod", [])

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
	return call_method("ALColorBlobDetection", "getCurrentPrecision", [])

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
	return call_method("ALColorBlobDetection", "getMyPeriod", [name])

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
	return call_method("ALColorBlobDetection", "getMyPrecision", [name])

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
	return call_method("ALColorBlobDetection", "getSubscribersInfo", [])

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
	return call_method("ALColorBlobDetection", "getOutputNames", [])

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
	return call_method("ALColorBlobDetection", "getEventList", [])

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
	return call_method("ALColorBlobDetection", "getMemoryKeyList", [])

@overload
def setFrameRate(framerate:int, /) -> bool:
	"""
	Sets the extractor framerate for all the subscribers
	
	Parameters
	----------
	framerate:int
		New framerate
	
	Returns
	----------
	True if the update succeeded, False if not
	
	Bridge notes
	------------
	setFrameRate has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "setFrameRate",
	#     "parametersSignature": "(i)",
	#     "description": "Sets the extractor framerate for all the subscribers",
	#     "parameters": [
	#         {
	#             "name": "framerate",
	#             "description": "New framerate"
	#         }
	#     ],
	#     "returnDescription": "True if the update succeeded, False if not"
	# }
	...

@overload
def setFrameRate(subscriberName:str, framerate:int, /) -> bool:
	"""
	Sets the extractor framerate for a chosen subscriber
	
	Parameters
	----------
	subscriberName:str
		Name of the subcriber
	framerate:int
		New framerate
	
	Returns
	----------
	True if the update succeeded, False if not
	
	Bridge notes
	------------
	setFrameRate has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "setFrameRate",
	#     "parametersSignature": "(si)",
	#     "description": "Sets the extractor framerate for a chosen subscriber",
	#     "parameters": [
	#         {
	#             "name": "subscriberName",
	#             "description": "Name of the subcriber"
	#         },
	#         {
	#             "name": "framerate",
	#             "description": "New framerate"
	#         }
	#     ],
	#     "returnDescription": "True if the update succeeded, False if not"
	# }
	...

def setFrameRate(*args, **kwargs):
	"""
	Bridge notes
	------------
	setFrameRate has 2 variants on the robot:
	- setFrameRate(framerate:int)
	- setFrameRate(subscriberName:str, framerate:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALColorBlobDetection.setFrameRate has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALColorBlobDetection", "setFrameRate", list(args))

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
	#     "uid": 129,
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
	return call_method("ALColorBlobDetection", "setResolution", [resolution])

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
	#     "uid": 130,
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
	return call_method("ALColorBlobDetection", "setActiveCamera", [cameraId])

def getFrameRate() -> int:
	"""
	Gets extractor framerate
	
	Returns
	----------
	Current value of the framerate of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor framerate",
	#     "parameters": [],
	#     "returnDescription": "Current value of the framerate of the extractor"
	# }
	return call_method("ALColorBlobDetection", "getFrameRate", [])

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
	return call_method("ALColorBlobDetection", "getResolution", [])

def getActiveCamera() -> int:
	"""
	Gets extractor active camera
	
	Returns
	----------
	Id of the current active camera of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "i",
	#     "name": "getActiveCamera",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor active camera",
	#     "parameters": [],
	#     "returnDescription": "Id of the current active camera of the extractor"
	# }
	return call_method("ALColorBlobDetection", "getActiveCamera", [])

def isPaused() -> bool:
	"""
	Gets extractor pause status
	
	Returns
	----------
	True if the extractor is paused, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "isPaused",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor pause status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is paused, False if not"
	# }
	return call_method("ALColorBlobDetection", "isPaused", [])

def isProcessing() -> bool:
	"""
	Gets extractor running status
	
	Returns
	----------
	True if the extractor is currently processing images, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "isProcessing",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor running status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is currently processing images, False if not"
	# }
	return call_method("ALColorBlobDetection", "isProcessing", [])

def pause(paused:bool) -> None:
	"""
	Changes the pause status of the extractor
	
	Parameters
	----------
	paused:bool
		New pause satus
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "pause",
	#     "parametersSignature": "(b)",
	#     "description": "Changes the pause status of the extractor",
	#     "parameters": [
	#         {
	#             "name": "paused",
	#             "description": "New pause satus"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALColorBlobDetection", "pause", [paused])

def _run() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "_run",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALColorBlobDetection", "_run", [])

def setColor(r:int, g:int, b:int, colorThres:int) -> None:
	"""
	Color parameter setting
	
	Parameters
	----------
	r:int
		The R component in RGB of the color to find
	g:int
		The G component in RGB of the color to find
	b:int
		The B component in RGB of the color to find
	colorThres:int
		The color threshold
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "setColor",
	#     "parametersSignature": "(iiii)",
	#     "description": "Color parameter setting",
	#     "parameters": [
	#         {
	#             "name": "r",
	#             "description": "The R component in RGB of the color to find"
	#         },
	#         {
	#             "name": "g",
	#             "description": "The G component in RGB of the color to find"
	#         },
	#         {
	#             "name": "b",
	#             "description": "The B component in RGB of the color to find"
	#         },
	#         {
	#             "name": "colorThres",
	#             "description": "The color threshold"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALColorBlobDetection", "setColor", [r, g, b, colorThres])

@overload
def setObjectProperties(minSize:int, span:float, /) -> None:
	"""
	Object parameter setting
	
	Parameters
	----------
	minSize:int
		The minimum size of the cluster to find
	span:float
		The span of the object in meters
	
	Bridge notes
	------------
	setObjectProperties has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "setObjectProperties",
	#     "parametersSignature": "(if)",
	#     "description": "Object parameter setting",
	#     "parameters": [
	#         {
	#             "name": "minSize",
	#             "description": "The minimum size of the cluster to find"
	#         },
	#         {
	#             "name": "span",
	#             "description": "The span of the object in meters"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setObjectProperties(minSize:int, span:float, shape:str, /) -> None:
	"""
	Object parameter setting
	
	Parameters
	----------
	minSize:int
		The minimum size of the cluster to find
	span:float
		The span of the object in meters
	shape:str
		The shape of the object
	
	Bridge notes
	------------
	setObjectProperties has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "setObjectProperties",
	#     "parametersSignature": "(ifs)",
	#     "description": "Object parameter setting",
	#     "parameters": [
	#         {
	#             "name": "minSize",
	#             "description": "The minimum size of the cluster to find"
	#         },
	#         {
	#             "name": "span",
	#             "description": "The span of the object in meters"
	#         },
	#         {
	#             "name": "shape",
	#             "description": "The shape of the object"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setObjectProperties(*args, **kwargs):
	"""
	Bridge notes
	------------
	setObjectProperties has 2 variants on the robot:
	- setObjectProperties(minSize:int, span:float)
	- setObjectProperties(minSize:int, span:float, shape:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALColorBlobDetection.setObjectProperties has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALColorBlobDetection", "setObjectProperties", list(args))

def getCircle() -> object:
	"""
	Send back the x,y,radius of the circle if any
	
	Returns
	----------
	The circle as x,y,radius in image relative coordinates (x,radius divided by rows and y by cols)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "m",
	#     "name": "getCircle",
	#     "parametersSignature": "()",
	#     "description": "Send back the x,y,radius of the circle if any",
	#     "parameters": [],
	#     "returnDescription": "The circle as x,y,radius in image relative coordinates (x,radius divided by rows and y by cols)"
	# }
	return call_method("ALColorBlobDetection", "getCircle", [])

def getAutoExposure() -> bool:
	"""
	Get the camera auto exposure mode
	
	Returns
	----------
	A flag saying the exposure is auto or not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "b",
	#     "name": "getAutoExposure",
	#     "parametersSignature": "()",
	#     "description": "Get the camera auto exposure mode",
	#     "parameters": [],
	#     "returnDescription": "A flag saying the exposure is auto or not"
	# }
	return call_method("ALColorBlobDetection", "getAutoExposure", [])

def setAutoExposure(mode:bool) -> None:
	"""
	Set the camera auto exposure to on
	
	Parameters
	----------
	mode:bool
		Whether the exposure is auto or not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "setAutoExposure",
	#     "parametersSignature": "(b)",
	#     "description": "Set the camera auto exposure to on",
	#     "parameters": [
	#         {
	#             "name": "mode",
	#             "description": "Whether the exposure is auto or not"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALColorBlobDetection", "setAutoExposure", [mode])

