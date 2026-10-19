"""
This module provides methods to take pictures and store them on disk.
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
	return call_method("ALPhotoCapture", "version", [])

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
	return call_method("ALPhotoCapture", "ping", [])

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
	return call_method("ALPhotoCapture", "getMethodList", [])

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
	return call_method("ALPhotoCapture", "getMethodHelp", [methodName])

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
	return call_method("ALPhotoCapture", "getModuleHelp", [])

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
	return call_method("ALPhotoCapture", "getBrokerName", [])

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
	return call_method("ALPhotoCapture", "getUsage", [name])

def setHalfPressEnabled(enable:bool) -> None:
	"""
	Enables or disables the half-press mode.
	
	Parameters
	----------
	enable:bool
		True to enable, false to disable.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "setHalfPressEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Enables or disables the half-press mode.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "True to enable, false to disable."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setHalfPressEnabled", [enable])

def halfPress() -> bool:
	"""
	Manually (un)subscribes to ALVideoDevice.
	
	Returns
	----------
	True if eveything went well, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "halfPress",
	#     "parametersSignature": "()",
	#     "description": "Manually (un)subscribes to ALVideoDevice.",
	#     "parameters": [],
	#     "returnDescription": "True if eveything went well, False otherwise."
	# }
	return call_method("ALPhotoCapture", "halfPress", [])

@overload
def takePicture(folderPath:str, fileName:str, /) -> Any:
	"""
	Takes one picture.
	
	Parameters
	----------
	folderPath:str
		Folder where the picture is saved.
	fileName:str
		Filename used to save the picture.
	
	Returns
	----------
	Full file name of the picture saved on the disk: [filename]
	
	Bridge notes
	------------
	takePicture has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "takePicture",
	#     "parametersSignature": "(ss)",
	#     "description": "Takes one picture.",
	#     "parameters": [
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the picture is saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the picture."
	#         }
	#     ],
	#     "returnDescription": "Full file name of the picture saved on the disk: [filename]"
	# }
	...

@overload
def takePicture(folderPath:str, fileName:str, overwrite:bool, /) -> Any:
	"""
	Takes one picture.
	
	Parameters
	----------
	folderPath:str
		Folder where the picture is saved.
	fileName:str
		Filename used to save the picture.
	overwrite:bool
		If false and the filename already exists, an error is thrown.
	
	Returns
	----------
	Full file name of the picture saved on the disk: [filename]
	
	Bridge notes
	------------
	takePicture has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "takePicture",
	#     "parametersSignature": "(ssb)",
	#     "description": "Takes one picture.",
	#     "parameters": [
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the picture is saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the picture."
	#         },
	#         {
	#             "name": "overwrite",
	#             "description": "If false and the filename already exists, an error is thrown."
	#         }
	#     ],
	#     "returnDescription": "Full file name of the picture saved on the disk: [filename]"
	# }
	...

def takePicture(*args, **kwargs):
	"""
	Bridge notes
	------------
	takePicture has 2 variants on the robot:
	- takePicture(folderPath:str, fileName:str)
	- takePicture(folderPath:str, fileName:str, overwrite:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPhotoCapture.takePicture has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPhotoCapture", "takePicture", list(args))

@overload
def takePictures(numberOfPictures:int, folderPath:str, fileName:str, /) -> Any:
	"""
	Takes several pictures as quickly as possible
	
	Parameters
	----------
	numberOfPictures:int
		Number of pictures to take
	folderPath:str
		Folder where the pictures are saved.
	fileName:str
		Filename used to save the pictures.
	
	Returns
	----------
	List of all saved files: [[filename1, filename2...]]
	
	Bridge notes
	------------
	takePictures has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "takePictures",
	#     "parametersSignature": "(iss)",
	#     "description": "Takes several pictures as quickly as possible",
	#     "parameters": [
	#         {
	#             "name": "numberOfPictures",
	#             "description": "Number of pictures to take"
	#         },
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the pictures are saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the pictures."
	#         }
	#     ],
	#     "returnDescription": "List of all saved files: [[filename1, filename2...]]"
	# }
	...

@overload
def takePictures(numberOfPictures:int, folderPath:str, fileName:str, overwrite:bool, /) -> Any:
	"""
	Takes several pictures as quickly as possible
	
	Parameters
	----------
	numberOfPictures:int
		Number of pictures to take
	folderPath:str
		Folder where the pictures are saved.
	fileName:str
		Filename used to save the pictures.
	overwrite:bool
		If false and the filename already exists, an error is thrown.
	
	Returns
	----------
	List of all saved files: [[filename1, filename2...]]
	
	Bridge notes
	------------
	takePictures has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "takePictures",
	#     "parametersSignature": "(issb)",
	#     "description": "Takes several pictures as quickly as possible",
	#     "parameters": [
	#         {
	#             "name": "numberOfPictures",
	#             "description": "Number of pictures to take"
	#         },
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the pictures are saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the pictures."
	#         },
	#         {
	#             "name": "overwrite",
	#             "description": "If false and the filename already exists, an error is thrown."
	#         }
	#     ],
	#     "returnDescription": "List of all saved files: [[filename1, filename2...]]"
	# }
	...

def takePictures(*args, **kwargs):
	"""
	Bridge notes
	------------
	takePictures has 2 variants on the robot:
	- takePictures(numberOfPictures:int, folderPath:str, fileName:str)
	- takePictures(numberOfPictures:int, folderPath:str, fileName:str, overwrite:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPhotoCapture.takePictures has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPhotoCapture", "takePictures", list(args))

def setCameraID(cameraID:int) -> None:
	"""
	Sets camera ID.
	
	Parameters
	----------
	cameraID:int
		ID of the camera to use.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setCameraID",
	#     "parametersSignature": "(i)",
	#     "description": "Sets camera ID.",
	#     "parameters": [
	#         {
	#             "name": "cameraID",
	#             "description": "ID of the camera to use."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setCameraID", [cameraID])

def setResolution(resolution:int) -> None:
	"""
	Sets resolution.
	
	Parameters
	----------
	resolution:int
		New frame resolution.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "setResolution",
	#     "parametersSignature": "(i)",
	#     "description": "Sets resolution.",
	#     "parameters": [
	#         {
	#             "name": "resolution",
	#             "description": "New frame resolution."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setResolution", [resolution])

def setColorSpace(colorSpace:int) -> None:
	"""
	Sets color space.
	
	Parameters
	----------
	colorSpace:int
		New color space.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setColorSpace",
	#     "parametersSignature": "(i)",
	#     "description": "Sets color space.",
	#     "parameters": [
	#         {
	#             "name": "colorSpace",
	#             "description": "New color space."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setColorSpace", [colorSpace])

def setCaptureInterval(captureInterval:int) -> None:
	"""
	Sets delay between two captures.
	
	Parameters
	----------
	captureInterval:int
		New delay (in ms) between two pictures.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "setCaptureInterval",
	#     "parametersSignature": "(i)",
	#     "description": "Sets delay between two captures.",
	#     "parameters": [
	#         {
	#             "name": "captureInterval",
	#             "description": "New delay (in ms) between two pictures."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setCaptureInterval", [captureInterval])

def setPictureFormat(pictureFormat:str) -> None:
	"""
	Sets picture extension.
	
	Parameters
	----------
	pictureFormat:str
		New extension used to save pictures.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "setPictureFormat",
	#     "parametersSignature": "(s)",
	#     "description": "Sets picture extension.",
	#     "parameters": [
	#         {
	#             "name": "pictureFormat",
	#             "description": "New extension used to save pictures."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPhotoCapture", "setPictureFormat", [pictureFormat])

def getCameraID() -> int:
	"""
	Returns current camera ID.
	
	Returns
	----------
	Current camera ID.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "getCameraID",
	#     "parametersSignature": "()",
	#     "description": "Returns current camera ID.",
	#     "parameters": [],
	#     "returnDescription": "Current camera ID."
	# }
	return call_method("ALPhotoCapture", "getCameraID", [])

def getResolution() -> int:
	"""
	Returns current resolution.
	
	Returns
	----------
	Current frame resolution.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "()",
	#     "description": "Returns current resolution.",
	#     "parameters": [],
	#     "returnDescription": "Current frame resolution."
	# }
	return call_method("ALPhotoCapture", "getResolution", [])

def getColorSpace() -> int:
	"""
	Returns current color space.
	
	Returns
	----------
	Current color space.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "()",
	#     "description": "Returns current color space.",
	#     "parameters": [],
	#     "returnDescription": "Current color space."
	# }
	return call_method("ALPhotoCapture", "getColorSpace", [])

def getCaptureInterval() -> int:
	"""
	Returns current delay between captures.
	
	Returns
	----------
	Current delay (in ms) between two pictures.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "i",
	#     "name": "getCaptureInterval",
	#     "parametersSignature": "()",
	#     "description": "Returns current delay between captures.",
	#     "parameters": [],
	#     "returnDescription": "Current delay (in ms) between two pictures."
	# }
	return call_method("ALPhotoCapture", "getCaptureInterval", [])

def getPictureFormat() -> str:
	"""
	Returns current picture format.
	
	Returns
	----------
	Current picture format.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "s",
	#     "name": "getPictureFormat",
	#     "parametersSignature": "()",
	#     "description": "Returns current picture format.",
	#     "parameters": [],
	#     "returnDescription": "Current picture format."
	# }
	return call_method("ALPhotoCapture", "getPictureFormat", [])

def isHalfPressEnabled() -> bool:
	"""
	Returns True if the "half press" mode is on.
	
	Returns
	----------
	True or False.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "isHalfPressEnabled",
	#     "parametersSignature": "()",
	#     "description": "Returns True if the \"half press\" mode is on.",
	#     "parameters": [],
	#     "returnDescription": "True or False."
	# }
	return call_method("ALPhotoCapture", "isHalfPressEnabled", [])

def isHalfPressed() -> bool:
	"""
	Returns True if the "half press" mode is on.
	
	Returns
	----------
	True or False.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "isHalfPressed",
	#     "parametersSignature": "()",
	#     "description": "Returns True if the \"half press\" mode is on.",
	#     "parameters": [],
	#     "returnDescription": "True or False."
	# }
	return call_method("ALPhotoCapture", "isHalfPressed", [])

