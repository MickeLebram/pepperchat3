from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module provides methods to record videos and store them on disk.
"""
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
	return send_mfc("ALVideoRecorder", "version", [])

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
	return send_mfc("ALVideoRecorder", "ping", [])

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
	return send_mfc("ALVideoRecorder", "getMethodList", [])

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
	return send_mfc("ALVideoRecorder", "getMethodHelp", [methodName])

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
	return send_mfc("ALVideoRecorder", "getModuleHelp", [])

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
	return send_mfc("ALVideoRecorder", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALVideoRecorder", "wait", [id])

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
	return send_mfc("ALVideoRecorder", "isRunning", [id])

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
	return send_mfc("ALVideoRecorder", "stop", [id])

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
	return send_mfc("ALVideoRecorder", "getBrokerName", [])

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
	return send_mfc("ALVideoRecorder", "getUsage", [name])

def startRecording_1(folderPath:str, fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (startRecording)
	
	Starts recording a video. Please note that only one record at a time can be made.
	
	Parameters
	----------
	folderPath:str
		Folder where the video is saved.
	fileName:str
		Filename used to save the video.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "startRecording",
	    "parametersSignature": "(ss)",
	    "description": "Starts recording a video. Please note that only one record at a time can be made.",
	    "parameters": [
	        {
	            "name": "folderPath",
	            "description": "Folder where the video is saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the video."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "startRecording", [folderPath, fileName])

def startRecording_2(folderPath:str, fileName:str, overwrite:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (startRecording)
	
	Starts recording a video. Please note that only one record at a time can be made.
	
	Parameters
	----------
	folderPath:str
		Folder where the video is saved.
	fileName:str
		Filename used to save the video.
	overwrite:bool
		If false and the filename already exists, an exception is thrown.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "startRecording",
	    "parametersSignature": "(ssb)",
	    "description": "Starts recording a video. Please note that only one record at a time can be made.",
	    "parameters": [
	        {
	            "name": "folderPath",
	            "description": "Folder where the video is saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the video."
	        },
	        {
	            "name": "overwrite",
	            "description": "If false and the filename already exists, an exception is thrown."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "startRecording", [folderPath, fileName, overwrite])

def stopRecording() -> object:
	"""
	Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.
	
	Returns
	----------
	Array of two elements [numRecordedFrames, recordAbsolutePath]
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "stopRecording",
	    "parametersSignature": "()",
	    "description": "Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.",
	    "parameters": [],
	    "returnDescription": "Array of two elements [numRecordedFrames, recordAbsolutePath]"
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "stopRecording", [])

def isRecording() -> bool:
	"""
	Are we currently recording a video
	
	Returns
	----------
	True/False
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "isRecording",
	    "parametersSignature": "()",
	    "description": "Are we currently recording a video",
	    "parameters": [],
	    "returnDescription": "True/False"
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "isRecording", [])

def _recordVideo(p0:str) -> None:
	"""
	private
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_recordVideo",
	    "parametersSignature": "(s)",
	    "description": "private",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "_recordVideo", [p0])

def setCameraID(cameraID:int) -> None:
	"""
	Sets camera ID.
	
	Parameters
	----------
	cameraID:int
		ID of the camera to use.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "setCameraID",
	    "parametersSignature": "(i)",
	    "description": "Sets camera ID.",
	    "parameters": [
	        {
	            "name": "cameraID",
	            "description": "ID of the camera to use."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "setCameraID", [cameraID])

def setResolution(resolution:int) -> None:
	"""
	Sets resolution.
	
	Parameters
	----------
	resolution:int
		New frame resolution.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "setResolution",
	    "parametersSignature": "(i)",
	    "description": "Sets resolution.",
	    "parameters": [
	        {
	            "name": "resolution",
	            "description": "New frame resolution."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "setResolution", [resolution])

def setColorSpace(colorSpace:int) -> None:
	"""
	Sets color space.
	
	Parameters
	----------
	colorSpace:int
		New color space.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "setColorSpace",
	    "parametersSignature": "(i)",
	    "description": "Sets color space.",
	    "parameters": [
	        {
	            "name": "colorSpace",
	            "description": "New color space."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "setColorSpace", [colorSpace])

def setFrameRate(frameRate:float) -> None:
	"""
	Sets frame rate.
	
	Parameters
	----------
	frameRate:float
		New frame rate.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "setFrameRate",
	    "parametersSignature": "(f)",
	    "description": "Sets frame rate.",
	    "parameters": [
	        {
	            "name": "frameRate",
	            "description": "New frame rate."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "setFrameRate", [frameRate])

def setVideoFormat(videoFormat:str) -> None:
	"""
	Sets video format.
	
	Parameters
	----------
	videoFormat:str
		New video format.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "setVideoFormat",
	    "parametersSignature": "(s)",
	    "description": "Sets video format.",
	    "parameters": [
	        {
	            "name": "videoFormat",
	            "description": "New video format."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "setVideoFormat", [videoFormat])

def getCameraID() -> int:
	"""
	Returns current camera ID.
	
	Returns
	----------
	Current camera ID.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "i",
	    "name": "getCameraID",
	    "parametersSignature": "()",
	    "description": "Returns current camera ID.",
	    "parameters": [],
	    "returnDescription": "Current camera ID."
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "getCameraID", [])

def getResolution() -> int:
	"""
	Returns current resolution.
	
	Returns
	----------
	Current resolution.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "i",
	    "name": "getResolution",
	    "parametersSignature": "()",
	    "description": "Returns current resolution.",
	    "parameters": [],
	    "returnDescription": "Current resolution."
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "getResolution", [])

def getColorSpace() -> int:
	"""
	Returns current color space.
	
	Returns
	----------
	Current color space.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "i",
	    "name": "getColorSpace",
	    "parametersSignature": "()",
	    "description": "Returns current color space.",
	    "parameters": [],
	    "returnDescription": "Current color space."
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "getColorSpace", [])

def getFrameRate() -> int:
	"""
	Returns current frame rate.
	
	Returns
	----------
	Current frame rate.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "i",
	    "name": "getFrameRate",
	    "parametersSignature": "()",
	    "description": "Returns current frame rate.",
	    "parameters": [],
	    "returnDescription": "Current frame rate."
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "getFrameRate", [])

def getVideoFormat() -> str:
	"""
	Returns current video format.
	
	Returns
	----------
	Current video format.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "s",
	    "name": "getVideoFormat",
	    "parametersSignature": "()",
	    "description": "Returns current video format.",
	    "parameters": [],
	    "returnDescription": "Current video format."
	}
	'''
	"""
	return send_mfc("ALVideoRecorder", "getVideoFormat", [])

