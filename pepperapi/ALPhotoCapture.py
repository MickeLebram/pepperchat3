from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module provides methods to take pictures and store them on disk.
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
	return send_mfc("ALPhotoCapture", "version", [])

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
	return send_mfc("ALPhotoCapture", "ping", [])

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
	return send_mfc("ALPhotoCapture", "getMethodList", [])

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
	return send_mfc("ALPhotoCapture", "getMethodHelp", [methodName])

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
	return send_mfc("ALPhotoCapture", "getModuleHelp", [])

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
	return send_mfc("ALPhotoCapture", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALPhotoCapture", "wait", [id])

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
	return send_mfc("ALPhotoCapture", "isRunning", [id])

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
	return send_mfc("ALPhotoCapture", "stop", [id])

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
	return send_mfc("ALPhotoCapture", "getBrokerName", [])

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
	return send_mfc("ALPhotoCapture", "getUsage", [name])

def setHalfPressEnabled(enable:bool) -> None:
	"""
	Enables or disables the half-press mode.
	
	Parameters
	----------
	enable:bool
		True to enable, false to disable.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "setHalfPressEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enables or disables the half-press mode.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True to enable, false to disable."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "setHalfPressEnabled", [enable])

def halfPress() -> bool:
	"""
	Manually (un)subscribes to ALVideoDevice.
	
	Returns
	----------
	True if eveything went well, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "halfPress",
	    "parametersSignature": "()",
	    "description": "Manually (un)subscribes to ALVideoDevice.",
	    "parameters": [],
	    "returnDescription": "True if eveything went well, False otherwise."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "halfPress", [])

def takePicture_1(folderPath:str, fileName:str) -> object:
	"""
	Note: This is one of the overloads of the original method (takePicture)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "takePicture",
	    "parametersSignature": "(ss)",
	    "description": "Takes one picture.",
	    "parameters": [
	        {
	            "name": "folderPath",
	            "description": "Folder where the picture is saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the picture."
	        }
	    ],
	    "returnDescription": "Full file name of the picture saved on the disk: [filename]"
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "takePicture", [folderPath, fileName])

def takePicture_2(folderPath:str, fileName:str, overwrite:bool) -> object:
	"""
	Note: This is one of the overloads of the original method (takePicture)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "m",
	    "name": "takePicture",
	    "parametersSignature": "(ssb)",
	    "description": "Takes one picture.",
	    "parameters": [
	        {
	            "name": "folderPath",
	            "description": "Folder where the picture is saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the picture."
	        },
	        {
	            "name": "overwrite",
	            "description": "If false and the filename already exists, an error is thrown."
	        }
	    ],
	    "returnDescription": "Full file name of the picture saved on the disk: [filename]"
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "takePicture", [folderPath, fileName, overwrite])

def takePictures_1(numberOfPictures:int, folderPath:str, fileName:str) -> object:
	"""
	Note: This is one of the overloads of the original method (takePictures)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "takePictures",
	    "parametersSignature": "(iss)",
	    "description": "Takes several pictures as quickly as possible",
	    "parameters": [
	        {
	            "name": "numberOfPictures",
	            "description": "Number of pictures to take"
	        },
	        {
	            "name": "folderPath",
	            "description": "Folder where the pictures are saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the pictures."
	        }
	    ],
	    "returnDescription": "List of all saved files: [[filename1, filename2...]]"
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "takePictures", [numberOfPictures, folderPath, fileName])

def takePictures_2(numberOfPictures:int, folderPath:str, fileName:str, overwrite:bool) -> object:
	"""
	Note: This is one of the overloads of the original method (takePictures)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "takePictures",
	    "parametersSignature": "(issb)",
	    "description": "Takes several pictures as quickly as possible",
	    "parameters": [
	        {
	            "name": "numberOfPictures",
	            "description": "Number of pictures to take"
	        },
	        {
	            "name": "folderPath",
	            "description": "Folder where the pictures are saved."
	        },
	        {
	            "name": "fileName",
	            "description": "Filename used to save the pictures."
	        },
	        {
	            "name": "overwrite",
	            "description": "If false and the filename already exists, an error is thrown."
	        }
	    ],
	    "returnDescription": "List of all saved files: [[filename1, filename2...]]"
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "takePictures", [numberOfPictures, folderPath, fileName, overwrite])

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
	    "uid": 120,
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
	return send_mfc("ALPhotoCapture", "setCameraID", [cameraID])

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
	    "uid": 121,
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
	return send_mfc("ALPhotoCapture", "setResolution", [resolution])

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
	    "uid": 122,
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
	return send_mfc("ALPhotoCapture", "setColorSpace", [colorSpace])

def setCaptureInterval(captureInterval:int) -> None:
	"""
	Sets delay between two captures.
	
	Parameters
	----------
	captureInterval:int
		New delay (in ms) between two pictures.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "setCaptureInterval",
	    "parametersSignature": "(i)",
	    "description": "Sets delay between two captures.",
	    "parameters": [
	        {
	            "name": "captureInterval",
	            "description": "New delay (in ms) between two pictures."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "setCaptureInterval", [captureInterval])

def setPictureFormat(pictureFormat:str) -> None:
	"""
	Sets picture extension.
	
	Parameters
	----------
	pictureFormat:str
		New extension used to save pictures.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "setPictureFormat",
	    "parametersSignature": "(s)",
	    "description": "Sets picture extension.",
	    "parameters": [
	        {
	            "name": "pictureFormat",
	            "description": "New extension used to save pictures."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "setPictureFormat", [pictureFormat])

def getCameraID() -> int:
	"""
	Returns current camera ID.
	
	Returns
	----------
	Current camera ID.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "i",
	    "name": "getCameraID",
	    "parametersSignature": "()",
	    "description": "Returns current camera ID.",
	    "parameters": [],
	    "returnDescription": "Current camera ID."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "getCameraID", [])

def getResolution() -> int:
	"""
	Returns current resolution.
	
	Returns
	----------
	Current frame resolution.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "i",
	    "name": "getResolution",
	    "parametersSignature": "()",
	    "description": "Returns current resolution.",
	    "parameters": [],
	    "returnDescription": "Current frame resolution."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "getResolution", [])

def getColorSpace() -> int:
	"""
	Returns current color space.
	
	Returns
	----------
	Current color space.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "i",
	    "name": "getColorSpace",
	    "parametersSignature": "()",
	    "description": "Returns current color space.",
	    "parameters": [],
	    "returnDescription": "Current color space."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "getColorSpace", [])

def getCaptureInterval() -> int:
	"""
	Returns current delay between captures.
	
	Returns
	----------
	Current delay (in ms) between two pictures.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "i",
	    "name": "getCaptureInterval",
	    "parametersSignature": "()",
	    "description": "Returns current delay between captures.",
	    "parameters": [],
	    "returnDescription": "Current delay (in ms) between two pictures."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "getCaptureInterval", [])

def getPictureFormat() -> str:
	"""
	Returns current picture format.
	
	Returns
	----------
	Current picture format.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "s",
	    "name": "getPictureFormat",
	    "parametersSignature": "()",
	    "description": "Returns current picture format.",
	    "parameters": [],
	    "returnDescription": "Current picture format."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "getPictureFormat", [])

def isHalfPressEnabled() -> bool:
	"""
	Returns True if the "half press" mode is on.
	
	Returns
	----------
	True or False.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "isHalfPressEnabled",
	    "parametersSignature": "()",
	    "description": "Returns True if the \"half press\" mode is on.",
	    "parameters": [],
	    "returnDescription": "True or False."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "isHalfPressEnabled", [])

def isHalfPressed() -> bool:
	"""
	Returns True if the "half press" mode is on.
	
	Returns
	----------
	True or False.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "b",
	    "name": "isHalfPressed",
	    "parametersSignature": "()",
	    "description": "Returns True if the \"half press\" mode is on.",
	    "parameters": [],
	    "returnDescription": "True or False."
	}
	'''
	"""
	return send_mfc("ALPhotoCapture", "isHalfPressed", [])

