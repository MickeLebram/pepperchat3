"""
ALVisionRecognition is a module which detects and recognizes learned pictures, like pages of a comic books, faces of objects or even locations.
The learning stage is done using the Choregraphe interface. Follow the steps in the green doc that will explain how to create your own database.
The output value is written in ALMemory in the PictureDetected variable.
It contains an array of tags, with the following format: 
 
[ [ TimeStampField ] [ Picture_info_0 , Picture _info_1, . . . , Picture_info_N-1 ] ] 
 
with as many Picture_info tags as things currently recognized. 
Picture_info = [[labels_list], matched_keypoints, ratio, [boundary_points]] 
with labels_list = [label_0, label_1, ..., label_N-1] and label_n belongs to label_n+1 
and boundary_points = [[x0,y0], [x1,y1], ..., [xN,yN]] 
 
- Labels are the names given to the picture (e.g. "cover/my book", or "fridge corner/kitchen/my flat"). 
- matched_keypoints corresponds to the number of keypoints retrieved in the current frame. 
- ratio represents the number of keypoints found for the object in the current frame divided by the number of keypoints found during the learning stage. 
- boundary_points is a list of points coordinates in angle values representing the reprojection in the current image of the boundaries selected during the learning stage. 

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
	return call_method("ALVisionRecognition", "version", [])

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
	return call_method("ALVisionRecognition", "ping", [])

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
	return call_method("ALVisionRecognition", "getMethodList", [])

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
	return call_method("ALVisionRecognition", "getMethodHelp", [methodName])

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
	return call_method("ALVisionRecognition", "getModuleHelp", [])

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
	return call_method("ALVisionRecognition", "getBrokerName", [])

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
	return call_method("ALVisionRecognition", "getUsage", [name])

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
		raise TypeError("ALVisionRecognition.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVisionRecognition", "subscribe", list(args))

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
	return call_method("ALVisionRecognition", "unsubscribe", [name])

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
	return call_method("ALVisionRecognition", "updatePeriod", [name, period])

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
	return call_method("ALVisionRecognition", "updatePrecision", [name, precision])

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
	return call_method("ALVisionRecognition", "getCurrentPeriod", [])

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
	return call_method("ALVisionRecognition", "getCurrentPrecision", [])

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
	return call_method("ALVisionRecognition", "getMyPeriod", [name])

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
	return call_method("ALVisionRecognition", "getMyPrecision", [name])

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
	return call_method("ALVisionRecognition", "getSubscribersInfo", [])

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
	return call_method("ALVisionRecognition", "getOutputNames", [])

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
	return call_method("ALVisionRecognition", "getEventList", [])

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
	return call_method("ALVisionRecognition", "getMemoryKeyList", [])

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
		raise TypeError("ALVisionRecognition.setFrameRate has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVisionRecognition", "setFrameRate", list(args))

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
	return call_method("ALVisionRecognition", "setResolution", [resolution])

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
	return call_method("ALVisionRecognition", "setActiveCamera", [cameraId])

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
	return call_method("ALVisionRecognition", "getFrameRate", [])

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
	return call_method("ALVisionRecognition", "getResolution", [])

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
	return call_method("ALVisionRecognition", "getActiveCamera", [])

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
	return call_method("ALVisionRecognition", "isPaused", [])

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
	return call_method("ALVisionRecognition", "isProcessing", [])

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
	return call_method("ALVisionRecognition", "pause", [paused])

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
	return call_method("ALVisionRecognition", "_run", [])

def changeDatabase(databasePath:str, databaseName:str) -> bool:
	"""
	By default the database has the name "current" and is on the robot in /home/nao/naoqi/share/naoqi/vision/visionrecognition/ folder. This bound method allows to choose both another name and another folder for the database. 
	
	
	Parameters
	----------
	databasePath:str
		Absolute path of the database on the robot, or "" to set default path.
	databaseName:str
		Name of the database folder, or "" to set default database folder.
	
	Returns
	----------
	True if the operation succeded, false otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "changeDatabase",
	#     "parametersSignature": "(ss)",
	#     "description": "By default the database has the name \"current\" and is on the robot in /home/nao/naoqi/share/naoqi/vision/visionrecognition/ folder. This bound method allows to choose both another name and another folder for the database. \n",
	#     "parameters": [
	#         {
	#             "name": "databasePath",
	#             "description": "Absolute path of the database on the robot, or \"\" to set default path."
	#         },
	#         {
	#             "name": "databaseName",
	#             "description": "Name of the database folder, or \"\" to set default database folder."
	#         }
	#     ],
	#     "returnDescription": "True if the operation succeded, false otherwise."
	# }
	return call_method("ALVisionRecognition", "changeDatabase", [databasePath, databaseName])

def clearCurrentDatabase() -> None:
	"""
	Clear the current database, the user has to be warned before calling this function.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "clearCurrentDatabase",
	#     "parametersSignature": "()",
	#     "description": "Clear the current database, the user has to be warned before calling this function.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVisionRecognition", "clearCurrentDatabase", [])

def getParam(paramName:str) -> Any:
	"""
	Get some vision recognition parameters.
	
	Parameters
	----------
	paramName:str
		The name of the parameter to get. "db_path" and "db_name" can be used.
	
	Returns
	----------
	Value of the parameter as a string for "db_path" and "db_name"
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "m",
	#     "name": "getParam",
	#     "parametersSignature": "(s)",
	#     "description": "Get some vision recognition parameters.",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "The name of the parameter to get. \"db_path\" and \"db_name\" can be used."
	#         }
	#     ],
	#     "returnDescription": "Value of the parameter as a string for \"db_path\" and \"db_name\""
	# }
	return call_method("ALVisionRecognition", "getParam", [paramName])

def learnFromFile(filename:str, name:str, tags:List[str], isWholeImage:bool, forced:bool) -> bool:
	"""
	Load an image and interpret it as an object.
	
	Parameters
	----------
	filename:str
		The filename of the image that will be interpreted as a planar object.
	name:str
		The name of the object (used as a unique identifier).
	tags:List[str]
		A list of tags (as strings) containing any met-data about your object.
	isWholeImage:bool
		indicates if the object occupies the whole image. If set to false, visionrecognition will try to detect the border of the object automatically. This works with unicolor background where object stands out well from the background. By default, this is set to true.
	forced:bool
		indicates if learned object will replace existing object (having the same original name) if any.
	
	Returns
	----------
	True if the operation succeded, false otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "b",
	#     "name": "learnFromFile",
	#     "parametersSignature": "(ss[s]bb)",
	#     "description": "Load an image and interpret it as an object.",
	#     "parameters": [
	#         {
	#             "name": "filename",
	#             "description": "The filename of the image that will be interpreted as a planar object."
	#         },
	#         {
	#             "name": "name",
	#             "description": "The name of the object (used as a unique identifier)."
	#         },
	#         {
	#             "name": "tags",
	#             "description": "A list of tags (as strings) containing any met-data about your object."
	#         },
	#         {
	#             "name": "isWholeImage",
	#             "description": "indicates if the object occupies the whole image. If set to false, visionrecognition will try to detect the border of the object automatically. This works with unicolor background where object stands out well from the background. By default, this is set to true."
	#         },
	#         {
	#             "name": "forced",
	#             "description": "indicates if learned object will replace existing object (having the same original name) if any."
	#         }
	#     ],
	#     "returnDescription": "True if the operation succeded, false otherwise."
	# }
	return call_method("ALVisionRecognition", "learnFromFile", [filename, name, tags, isWholeImage, forced])

def setMaxOutObjs(iMaxOutObjs:int) -> None:
	"""
	Set the maximal number (not more than 10) of detected objects for each detection. By default, this is set to 1.
	
	Parameters
	----------
	iMaxOutObjs:int
		number of desired objects to be detected.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "setMaxOutObjs",
	#     "parametersSignature": "(i)",
	#     "description": "Set the maximal number (not more than 10) of detected objects for each detection. By default, this is set to 1.",
	#     "parameters": [
	#         {
	#             "name": "iMaxOutObjs",
	#             "description": "number of desired objects to be detected."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVisionRecognition", "setMaxOutObjs", [iMaxOutObjs])

def getMaxOutObjs() -> int:
	"""
	Get the maximal number of detected objects for each detection.
	
	Returns
	----------
	number of maximal objects to be detected.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "i",
	#     "name": "getMaxOutObjs",
	#     "parametersSignature": "()",
	#     "description": "Get the maximal number of detected objects for each detection.",
	#     "parameters": [],
	#     "returnDescription": "number of maximal objects to be detected."
	# }
	return call_method("ALVisionRecognition", "getMaxOutObjs", [])

def getSize() -> int:
	"""
	Get number of objects in the current database.
	
	Returns
	----------
	number of objects in the current database.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "i",
	#     "name": "getSize",
	#     "parametersSignature": "()",
	#     "description": "Get number of objects in the current database.",
	#     "parameters": [],
	#     "returnDescription": "number of objects in the current database."
	# }
	return call_method("ALVisionRecognition", "getSize", [])

def _removeObject(hash:str) -> None:
	"""
	Remove an obbject with a specific hash from the DB (Attention: All files related to this object will be deleted.)
	
	Parameters
	----------
	hash:str
		the hash (as a string) of the object to be deleted.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "_removeObject",
	#     "parametersSignature": "(s)",
	#     "description": "Remove an obbject with a specific hash from the DB (Attention: All files related to this object will be deleted.)",
	#     "parameters": [
	#         {
	#             "name": "hash",
	#             "description": "the hash (as a string) of the object to be deleted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVisionRecognition", "_removeObject", [hash])

def detectFromFile(image:str) -> None:
	"""
	Load an image and search for known objects.
	
	Parameters
	----------
	image:str
		The image that will be searched for known objects.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "detectFromFile",
	#     "parametersSignature": "(s)",
	#     "description": "Load an image and search for known objects.",
	#     "parameters": [
	#         {
	#             "name": "image",
	#             "description": "The image that will be searched for known objects."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVisionRecognition", "detectFromFile", [image])

def getDefaultDatabaseDirectory() -> str:
	"""
	Return the default directory used for databases storage.
	
	Returns
	----------
	Default directory used for databases storage.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "s",
	#     "name": "getDefaultDatabaseDirectory",
	#     "parametersSignature": "()",
	#     "description": "Return the default directory used for databases storage.",
	#     "parameters": [],
	#     "returnDescription": "Default directory used for databases storage."
	# }
	return call_method("ALVisionRecognition", "getDefaultDatabaseDirectory", [])

def getDefaultDatabaseName() -> str:
	"""
	Return the default database name.
	
	Returns
	----------
	Default database name.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "s",
	#     "name": "getDefaultDatabaseName",
	#     "parametersSignature": "()",
	#     "description": "Return the default database name.",
	#     "parameters": [],
	#     "returnDescription": "Default database name."
	# }
	return call_method("ALVisionRecognition", "getDefaultDatabaseName", [])

