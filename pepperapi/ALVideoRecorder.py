"""
This module provides methods to record videos and store them on disk.
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
	return call_method("ALVideoRecorder", "version", [])

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
	return call_method("ALVideoRecorder", "ping", [])

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
	return call_method("ALVideoRecorder", "getMethodList", [])

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
	return call_method("ALVideoRecorder", "getMethodHelp", [methodName])

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
	return call_method("ALVideoRecorder", "getModuleHelp", [])

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
	return call_method("ALVideoRecorder", "getBrokerName", [])

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
	return call_method("ALVideoRecorder", "getUsage", [name])

@overload
def startRecording(folderPath:str, fileName:str, /) -> None:
	"""
	Starts recording a video. Please note that only one record at a time can be made.
	
	Parameters
	----------
	folderPath:str
		Folder where the video is saved.
	fileName:str
		Filename used to save the video.
	
	Bridge notes
	------------
	startRecording has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startRecording",
	#     "parametersSignature": "(ss)",
	#     "description": "Starts recording a video. Please note that only one record at a time can be made.",
	#     "parameters": [
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the video is saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the video."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def startRecording(folderPath:str, fileName:str, overwrite:bool, /) -> None:
	"""
	Starts recording a video. Please note that only one record at a time can be made.
	
	Parameters
	----------
	folderPath:str
		Folder where the video is saved.
	fileName:str
		Filename used to save the video.
	overwrite:bool
		If false and the filename already exists, an exception is thrown.
	
	Bridge notes
	------------
	startRecording has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "startRecording",
	#     "parametersSignature": "(ssb)",
	#     "description": "Starts recording a video. Please note that only one record at a time can be made.",
	#     "parameters": [
	#         {
	#             "name": "folderPath",
	#             "description": "Folder where the video is saved."
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Filename used to save the video."
	#         },
	#         {
	#             "name": "overwrite",
	#             "description": "If false and the filename already exists, an exception is thrown."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def startRecording(*args, **kwargs):
	"""
	Bridge notes
	------------
	startRecording has 2 variants on the robot:
	- startRecording(folderPath:str, fileName:str)
	- startRecording(folderPath:str, fileName:str, overwrite:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoRecorder.startRecording has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoRecorder", "startRecording", list(args))

def stopRecording() -> object:
	"""
	Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.
	
	Returns
	----------
	Array of two elements [numRecordedFrames, recordAbsolutePath]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "stopRecording",
	#     "parametersSignature": "()",
	#     "description": "Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.",
	#     "parameters": [],
	#     "returnDescription": "Array of two elements [numRecordedFrames, recordAbsolutePath]"
	# }
	return call_method("ALVideoRecorder", "stopRecording", [])

def isRecording() -> bool:
	"""
	Are we currently recording a video
	
	Returns
	----------
	True/False
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "isRecording",
	#     "parametersSignature": "()",
	#     "description": "Are we currently recording a video",
	#     "parameters": [],
	#     "returnDescription": "True/False"
	# }
	return call_method("ALVideoRecorder", "isRecording", [])

def _recordVideo(p0:str) -> None:
	"""
	private
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_recordVideo",
	#     "parametersSignature": "(s)",
	#     "description": "private",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoRecorder", "_recordVideo", [p0])

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
	#     "uid": 119,
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
	return call_method("ALVideoRecorder", "setCameraID", [cameraID])

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
	#     "uid": 120,
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
	return call_method("ALVideoRecorder", "setResolution", [resolution])

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
	#     "uid": 121,
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
	return call_method("ALVideoRecorder", "setColorSpace", [colorSpace])

def setFrameRate(frameRate:float) -> None:
	"""
	Sets frame rate.
	
	Parameters
	----------
	frameRate:float
		New frame rate.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setFrameRate",
	#     "parametersSignature": "(f)",
	#     "description": "Sets frame rate.",
	#     "parameters": [
	#         {
	#             "name": "frameRate",
	#             "description": "New frame rate."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoRecorder", "setFrameRate", [frameRate])

def setVideoFormat(videoFormat:str) -> None:
	"""
	Sets video format.
	
	Parameters
	----------
	videoFormat:str
		New video format.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "setVideoFormat",
	#     "parametersSignature": "(s)",
	#     "description": "Sets video format.",
	#     "parameters": [
	#         {
	#             "name": "videoFormat",
	#             "description": "New video format."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoRecorder", "setVideoFormat", [videoFormat])

def getCameraID() -> int:
	"""
	Returns current camera ID.
	
	Returns
	----------
	Current camera ID.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "getCameraID",
	#     "parametersSignature": "()",
	#     "description": "Returns current camera ID.",
	#     "parameters": [],
	#     "returnDescription": "Current camera ID."
	# }
	return call_method("ALVideoRecorder", "getCameraID", [])

def getResolution() -> int:
	"""
	Returns current resolution.
	
	Returns
	----------
	Current resolution.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "()",
	#     "description": "Returns current resolution.",
	#     "parameters": [],
	#     "returnDescription": "Current resolution."
	# }
	return call_method("ALVideoRecorder", "getResolution", [])

def getColorSpace() -> int:
	"""
	Returns current color space.
	
	Returns
	----------
	Current color space.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "()",
	#     "description": "Returns current color space.",
	#     "parameters": [],
	#     "returnDescription": "Current color space."
	# }
	return call_method("ALVideoRecorder", "getColorSpace", [])

def getFrameRate() -> int:
	"""
	Returns current frame rate.
	
	Returns
	----------
	Current frame rate.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "()",
	#     "description": "Returns current frame rate.",
	#     "parameters": [],
	#     "returnDescription": "Current frame rate."
	# }
	return call_method("ALVideoRecorder", "getFrameRate", [])

def getVideoFormat() -> str:
	"""
	Returns current video format.
	
	Returns
	----------
	Current video format.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "s",
	#     "name": "getVideoFormat",
	#     "parametersSignature": "()",
	#     "description": "Returns current video format.",
	#     "parameters": [],
	#     "returnDescription": "Current video format."
	# }
	return call_method("ALVideoRecorder", "getVideoFormat", [])

