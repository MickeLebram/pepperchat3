from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALVideoDevice, formerly called Video Input systemis architectured in order to provide every client related to vision, a direct access to raw images from video source, or an access to images transformed in the requested format.
  Extension name of the methods providing images depends on wether clients are local (dynamic library) or remote (executable).
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
	return send_mfc("ALVideoDevice", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALVideoDevice", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALVideoDevice", "metaObject", [p0])

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
	return send_mfc("ALVideoDevice", "terminate", [p0])

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
	return send_mfc("ALVideoDevice", "property", [p0])

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
	return send_mfc("ALVideoDevice", "setProperty", [p0, p1])

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
	return send_mfc("ALVideoDevice", "properties", [])

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
	return send_mfc("ALVideoDevice", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALVideoDevice", "isStatsEnabled", [])

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
	return send_mfc("ALVideoDevice", "enableStats", [p0])

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
	return send_mfc("ALVideoDevice", "stats", [])

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
	return send_mfc("ALVideoDevice", "clearStats", [])

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
	return send_mfc("ALVideoDevice", "isTraceEnabled", [])

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
	return send_mfc("ALVideoDevice", "enableTrace", [p0])

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
	return send_mfc("ALVideoDevice", "version", [])

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
	return send_mfc("ALVideoDevice", "ping", [])

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
	return send_mfc("ALVideoDevice", "getMethodList", [])

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
	return send_mfc("ALVideoDevice", "getMethodHelp", [methodName])

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
	return send_mfc("ALVideoDevice", "getModuleHelp", [])

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
	return send_mfc("ALVideoDevice", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALVideoDevice", "wait", [id])

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
	return send_mfc("ALVideoDevice", "isRunning", [id])

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
	return send_mfc("ALVideoDevice", "stop", [id])

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
	return send_mfc("ALVideoDevice", "getBrokerName", [])

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
	return send_mfc("ALVideoDevice", "getUsage", [name])

def subscribeCamera(name:str, cameraIndex:int, resolution:int, colorSpace:int, fps:int) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndex:int
		Camera requested.
	resolution:int
		Resolution requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
	colorSpace:int
		Colorspace requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
	fps:int
		Fps (frames per second) requested.{5, 10, 15, 30}
	
	Returns
	----------
	Name under which the vision module is known from ALVideoDevice
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "s",
	    "name": "subscribeCamera",
	    "parametersSignature": "(siiii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "resolution",
	            "description": "Resolution requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}"
	        },
	        {
	            "name": "colorSpace",
	            "description": "Colorspace requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}"
	        },
	        {
	            "name": "fps",
	            "description": "Fps (frames per second) requested.{5, 10, 15, 30}"
	        }
	    ],
	    "returnDescription": "Name under which the vision module is known from ALVideoDevice"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "subscribeCamera", [name, cameraIndex, resolution, colorSpace, fps])

def subscribeCameras(name:str, cameraIndexes:object, resolutions:object, colorSpaces:object, fps:int) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndexes:object
		Cameras requested.
	resolutions:object
		Resolutions requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
	colorSpaces:object
		Colorspaces requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
	fps:int
		Fps (frames per second) requested.{5, 10, 15, 30}
	
	Returns
	----------
	Name under which the vision module is known from ALVideoDevice
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "s",
	    "name": "subscribeCameras",
	    "parametersSignature": "(smmmi)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "cameraIndexes",
	            "description": "Cameras requested."
	        },
	        {
	            "name": "resolutions",
	            "description": "Resolutions requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}"
	        },
	        {
	            "name": "colorSpaces",
	            "description": "Colorspaces requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}"
	        },
	        {
	            "name": "fps",
	            "description": "Fps (frames per second) requested.{5, 10, 15, 30}"
	        }
	    ],
	    "returnDescription": "Name under which the vision module is known from ALVideoDevice"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "subscribeCameras", [name, cameraIndexes, resolutions, colorSpaces, fps])

def unsubscribe(nameId:str) -> bool:
	"""
	
	
	Parameters
	----------
	nameId:str
		Name under which the vision module is known from ALVideoDevice.
	
	Returns
	----------
	True if success, false otherwise
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "unsubscribe",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "nameId",
	            "description": "Name under which the vision module is known from ALVideoDevice."
	        }
	    ],
	    "returnDescription": "True if success, false otherwise"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "unsubscribe", [nameId])

def getSubscribers() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "m",
	    "name": "getSubscribers",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getSubscribers", [])

def getCameraIndexes() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "getCameraIndexes",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraIndexes", [])

def getActiveCamera_1() -> int:
	"""
	Note: This is one of the overloads of the original method (getActiveCamera)
	
	Tells which camera is the default one
	
	Returns
	----------
	 0: top camera - 1: bottom camera
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "i",
	    "name": "getActiveCamera",
	    "parametersSignature": "()",
	    "description": "Tells which camera is the default one",
	    "parameters": [],
	    "returnDescription": " 0: top camera - 1: bottom camera"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getActiveCamera", [])

def setActiveCamera_1(activeCamera:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (setActiveCamera)
	
	Set the active camera
	
	Parameters
	----------
	activeCamera:int
		 0: top camera - 1: bottom camera
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "b",
	    "name": "setActiveCamera",
	    "parametersSignature": "(i)",
	    "description": "Set the active camera",
	    "parameters": [
	        {
	            "name": "activeCamera",
	            "description": " 0: top camera - 1: bottom camera"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setActiveCamera", [activeCamera])

def getCameraModel(cameraIndex:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	 1(kOV7670): VGA camera - 2(kMT9M114): HD camera
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "getCameraModel",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": " 1(kOV7670): VGA camera - 2(kMT9M114): HD camera"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraModel", [cameraIndex])

def isCameraSimulated(cameraIndex:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	 True: Camera is simulated - False: Camera is real
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "isCameraSimulated",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": " True: Camera is simulated - False: Camera is real"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "isCameraSimulated", [cameraIndex])

def getCameraName(cameraIndex:int) -> str:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	CameraTop - CameraBottom - CameraDepth
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "s",
	    "name": "getCameraName",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": "CameraTop - CameraBottom - CameraDepth"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraName", [cameraIndex])

def getFrameRate_1(cameraIndex:int) -> int:
	"""
	Note: This is one of the overloads of the original method (getFrameRate)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "i",
	    "name": "getFrameRate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getFrameRate", [cameraIndex])

def getResolution_1(cameraIndex:int) -> int:
	"""
	Note: This is one of the overloads of the original method (getResolution)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "i",
	    "name": "getResolution",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getResolution", [cameraIndex])

def getColorSpace_1(cameraIndex:int) -> int:
	"""
	Note: This is one of the overloads of the original method (getColorSpace)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "i",
	    "name": "getColorSpace",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getColorSpace", [cameraIndex])

def getHorizontalFOV(cameraIndex:int) -> float:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "f",
	    "name": "getHorizontalFOV",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getHorizontalFOV", [cameraIndex])

def getVerticalFOV(cameraIndex:int) -> float:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "f",
	    "name": "getVerticalFOV",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getVerticalFOV", [cameraIndex])

def getParameterList(cameraIndex:int) -> List[int]:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "[i]",
	    "name": "getParameterList",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getParameterList", [cameraIndex])

def getParameter(cameraIndex:int, parameterId:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "i",
	    "name": "getParameter",
	    "parametersSignature": "(ii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getParameter", [cameraIndex, parameterId])

def getParameterRange(cameraIndex:int, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "m",
	    "name": "getParameterRange",
	    "parametersSignature": "(ii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getParameterRange", [cameraIndex, parameterId])

def getParameterInfo(cameraIndex:int, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "m",
	    "name": "getParameterInfo",
	    "parametersSignature": "(ii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getParameterInfo", [cameraIndex, parameterId])

def setParameter(cameraIndex:int, parameterId:int, value:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	value:int
		value requested.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "b",
	    "name": "setParameter",
	    "parametersSignature": "(iii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        },
	        {
	            "name": "value",
	            "description": "value requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setParameter", [cameraIndex, parameterId, value])

def setParameterToDefault(cameraIndex:int, parameterId:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "b",
	    "name": "setParameterToDefault",
	    "parametersSignature": "(ii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setParameterToDefault", [cameraIndex, parameterId])

def setCameraCalibration(cameraIndex:int, filenames:List[str]) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	filenames:List[str]
		Vector of files to retrieve in /media/internal/share/naoqi/vision or ~/.local/share/naoqi/vision
	
	Returns
	----------
	true if succeeded, false otherwise
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "setCameraCalibration",
	    "parametersSignature": "(i[s])",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "filenames",
	            "description": "Vector of files to retrieve in /media/internal/share/naoqi/vision or ~/.local/share/naoqi/vision"
	        }
	    ],
	    "returnDescription": "true if succeeded, false otherwise"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setCameraCalibration", [cameraIndex, filenames])

def setAllParametersToDefault(cameraIndex:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "setAllParametersToDefault",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setAllParametersToDefault", [cameraIndex])

def openCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "b",
	    "name": "openCamera",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "openCamera", [p0])

def closeCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "b",
	    "name": "closeCamera",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "closeCamera", [p0])

def isCameraOpen(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "b",
	    "name": "isCameraOpen",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "isCameraOpen", [p0])

def startCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "b",
	    "name": "startCamera",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "startCamera", [p0])

def stopCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "b",
	    "name": "stopCamera",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "stopCamera", [p0])

def isCameraStarted(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "b",
	    "name": "isCameraStarted",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "isCameraStarted", [p0])

def resetCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "b",
	    "name": "resetCamera",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "resetCamera", [p0])

def startFrameGrabber_1(cameraIndex:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (startFrameGrabber)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "b",
	    "name": "startFrameGrabber",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "startFrameGrabber", [cameraIndex])

def stopFrameGrabber_1(cameraIndex:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (stopFrameGrabber)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "b",
	    "name": "stopFrameGrabber",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "stopFrameGrabber", [cameraIndex])

def isFrameGrabberOff_1(cameraIndex:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (isFrameGrabberOff)
	
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "b",
	    "name": "isFrameGrabberOff",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "isFrameGrabberOff", [cameraIndex])

def hasDepthCamera() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "b",
	    "name": "hasDepthCamera",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "hasDepthCamera", [])

def getFrameRate_2(name:str) -> int:
	"""
	Note: This is one of the overloads of the original method (getFrameRate)
	
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "i",
	    "name": "getFrameRate",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getFrameRate", [name])

def setFrameRate(name:str, frameRate:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	frameRate:int
		Frame Rate requested.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "setFrameRate",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "frameRate",
	            "description": "Frame Rate requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setFrameRate", [name, frameRate])

def getActiveCamera_2(name:str) -> int:
	"""
	Note: This is one of the overloads of the original method (getActiveCamera)
	
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "i",
	    "name": "getActiveCamera",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getActiveCamera", [name])

def setActiveCamera_2(name:str, cameraIndex:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (setActiveCamera)
	
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "b",
	    "name": "setActiveCamera",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setActiveCamera", [name, cameraIndex])

def getResolution_2(name:str) -> int:
	"""
	Note: This is one of the overloads of the original method (getResolution)
	
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "i",
	    "name": "getResolution",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getResolution", [name])

def setResolution(name:str, resolution:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	resolution:int
		Resolution requested.
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "setResolution",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "resolution",
	            "description": "Resolution requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setResolution", [name, resolution])

def getColorSpace_2(name:str) -> int:
	"""
	Note: This is one of the overloads of the original method (getColorSpace)
	
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "i",
	    "name": "getColorSpace",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getColorSpace", [name])

def setColorSpace(name:str, colorSpace:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	colorSpace:int
		Color Space requested.
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "b",
	    "name": "setColorSpace",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "colorSpace",
	            "description": "Color Space requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setColorSpace", [name, colorSpace])

def getCameraParameterList(name:str) -> List[int]:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "[i]",
	    "name": "getCameraParameterList",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraParameterList", [name])

def getCameraParameter(name:str, parameterId:int) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "i",
	    "name": "getCameraParameter",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraParameter", [name, parameterId])

def getCameraParameterRange(name:str, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "m",
	    "name": "getCameraParameterRange",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraParameterRange", [name, parameterId])

def getCameraParameterInfo(name:str, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "m",
	    "name": "getCameraParameterInfo",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCameraParameterInfo", [name, parameterId])

def setCameraParameter(name:str, parameterId:int, value:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	value:int
		value requested.
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "b",
	    "name": "setCameraParameter",
	    "parametersSignature": "(sii)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        },
	        {
	            "name": "value",
	            "description": "value requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setCameraParameter", [name, parameterId, value])

def setCameraParameterToDefault(name:str, parameterId:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "b",
	    "name": "setCameraParameterToDefault",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setCameraParameterToDefault", [name, parameterId])

def setAllCameraParametersToDefault(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "b",
	    "name": "setAllCameraParametersToDefault",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setAllCameraParametersToDefault", [name])

def getDirectRawImageLocal(name:str) -> object:
	"""
	Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.
	Warning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.
	Warning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!
	Warning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Pointer to the locked image buffer, NULL if error.
	Warning, image pointer is valid only for C++ dynamic library.
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "X",
	    "name": "getDirectRawImageLocal",
	    "parametersSignature": "(s)",
	    "description": "Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.\nWarning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.\nWarning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!\nWarning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Pointer to the locked image buffer, NULL if error.\nWarning, image pointer is valid only for C++ dynamic library."
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getDirectRawImageLocal", [name])

def getDirectRawImageRemote(name:str) -> object:
	"""
	Fills an ALValue with data coming directly from raw buffer (no format conversion).
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "m",
	    "name": "getDirectRawImageRemote",
	    "parametersSignature": "(s)",
	    "description": "Fills an ALValue with data coming directly from raw buffer (no format conversion).\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getDirectRawImageRemote", [name])

def releaseDirectRawImage(name:str) -> bool:
	"""
	Release image buffer locked by getDirectRawImageLocal().
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "b",
	    "name": "releaseDirectRawImage",
	    "parametersSignature": "(s)",
	    "description": "Release image buffer locked by getDirectRawImageLocal().\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "releaseDirectRawImage", [name])

def getImageLocal(name:str) -> object:
	"""
	Applies transformations to the last image from video source and returns a pointer to a locked ALImage.
	When image is not necessary anymore, a call to releaseImage() is requested.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library.
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "X",
	    "name": "getImageLocal",
	    "parametersSignature": "(s)",
	    "description": "Applies transformations to the last image from video source and returns a pointer to a locked ALImage.\nWhen image is not necessary anymore, a call to releaseImage() is requested.\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library."
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImageLocal", [name])

def getImageRemote(name:str) -> object:
	"""
	Applies transformations to the last image from video source and fills pFrameOut.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	
	*Reference struct*
	'''
	{
	    "uid": 167,
	    "returnSignature": "m",
	    "name": "getImageRemote",
	    "parametersSignature": "(s)",
	    "description": "Applies transformations to the last image from video source and fills pFrameOut.\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImageRemote", [name])

def releaseImage(name:str) -> bool:
	"""
	Release image buffer locked by getImageLocal().
	If G.V.M. had no locked image buffer, does nothing.
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "b",
	    "name": "releaseImage",
	    "parametersSignature": "(s)",
	    "description": "Release image buffer locked by getImageLocal().\nIf G.V.M. had no locked image buffer, does nothing.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "releaseImage", [name])

def getActiveCameras(name:str) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "m",
	    "name": "getActiveCameras",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getActiveCameras", [name])

def setActiveCameras(name:str, cameraIndexes:object) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndexes:object
		Cameras requested.
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "m",
	    "name": "setActiveCameras",
	    "parametersSignature": "(sm)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "cameraIndexes",
	            "description": "Cameras requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setActiveCameras", [name, cameraIndexes])

def getResolutions(name:str) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "m",
	    "name": "getResolutions",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getResolutions", [name])

def setResolutions(name:str, resolutions:object) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	resolutions:object
		Resolutions requested.
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "m",
	    "name": "setResolutions",
	    "parametersSignature": "(sm)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "resolutions",
	            "description": "Resolutions requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setResolutions", [name, resolutions])

def getColorSpaces(name:str) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "m",
	    "name": "getColorSpaces",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getColorSpaces", [name])

def setColorSpaces(name:str, colorSpaces:object) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	colorSpaces:object
		Color Spaces requested.
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "m",
	    "name": "setColorSpaces",
	    "parametersSignature": "(sm)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "colorSpaces",
	            "description": "Color Spaces requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setColorSpaces", [name, colorSpaces])

def getCamerasParameter(name:str, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 175,
	    "returnSignature": "m",
	    "name": "getCamerasParameter",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getCamerasParameter", [name, parameterId])

def setCamerasParameter(name:str, parameterId:int, values:object) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	values:object
		values requested.
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "m",
	    "name": "setCamerasParameter",
	    "parametersSignature": "(sim)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        },
	        {
	            "name": "values",
	            "description": "values requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setCamerasParameter", [name, parameterId, values])

def setCamerasParameterToDefault(name:str, parameterId:int) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	
	*Reference struct*
	'''
	{
	    "uid": 177,
	    "returnSignature": "m",
	    "name": "setCamerasParameterToDefault",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        },
	        {
	            "name": "parameterId",
	            "description": "Camera parameter requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setCamerasParameterToDefault", [name, parameterId])

def getDirectRawImagesLocal(name:str) -> object:
	"""
	Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.
	Warning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.
	Warning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!
	Warning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array of pointer to the locked image buffer, NULL if error.
	Warning, image pointer is valid only for C++ dynamic library.
	
	*Reference struct*
	'''
	{
	    "uid": 178,
	    "returnSignature": "m",
	    "name": "getDirectRawImagesLocal",
	    "parametersSignature": "(s)",
	    "description": "Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.\nWarning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.\nWarning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!\nWarning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array of pointer to the locked image buffer, NULL if error.\nWarning, image pointer is valid only for C++ dynamic library."
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getDirectRawImagesLocal", [name])

def getDirectRawImagesRemote(name:str) -> object:
	"""
	Fills an ALValue with data coming directly from raw buffer (no format conversion).
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	
	*Reference struct*
	'''
	{
	    "uid": 179,
	    "returnSignature": "m",
	    "name": "getDirectRawImagesRemote",
	    "parametersSignature": "(s)",
	    "description": "Fills an ALValue with data coming directly from raw buffer (no format conversion).\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getDirectRawImagesRemote", [name])

def releaseDirectRawImages(name:str) -> object:
	"""
	Release image buffer locked by getDirectRawImagesLocal().
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 180,
	    "returnSignature": "m",
	    "name": "releaseDirectRawImages",
	    "parametersSignature": "(s)",
	    "description": "Release image buffer locked by getDirectRawImagesLocal().\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "releaseDirectRawImages", [name])

def getImagesLocal(name:str) -> object:
	"""
	Applies transformations to the last image from video source and returns a pointer to a locked ALImage.
	When image is not necessary anymore, a call to releaseImage() is requested.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array of pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library.
	
	*Reference struct*
	'''
	{
	    "uid": 181,
	    "returnSignature": "m",
	    "name": "getImagesLocal",
	    "parametersSignature": "(s)",
	    "description": "Applies transformations to the last image from video source and returns a pointer to a locked ALImage.\nWhen image is not necessary anymore, a call to releaseImage() is requested.\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array of pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library."
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImagesLocal", [name])

def getImagesRemote(name:str) -> object:
	"""
	Applies transformations to the last image from video source and fills pFrameOut.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	
	*Reference struct*
	'''
	{
	    "uid": 182,
	    "returnSignature": "m",
	    "name": "getImagesRemote",
	    "parametersSignature": "(s)",
	    "description": "Applies transformations to the last image from video source and fills pFrameOut.\n",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImagesRemote", [name])

def releaseImages(name:str) -> object:
	"""
	Release image buffer locked by getImageLocal().
	If G.V.M. had no locked image buffer, does nothing.
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 183,
	    "returnSignature": "m",
	    "name": "releaseImages",
	    "parametersSignature": "(s)",
	    "description": "Release image buffer locked by getImageLocal().\nIf G.V.M. had no locked image buffer, does nothing.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the subscribing vision module"
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "releaseImages", [name])

def recordVideo(id:str, path:str, totalNumber:int, period:int) -> bool:
	"""
	Background record of an .arv raw format video from the images processed by a vision module
	Actualy it take picture each time the vision module call getDirectRawImageRemote().
	
	Parameters
	----------
	id:str
		Name under which the G.V.M. is known from the V.I.M.
	path:str
		path/name of the video to be recorded
	totalNumber:int
		number of images to be recorded. 0xFFFFFFFF for "unlimited"
	period:int
		one image recorded every pPeriod images
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 184,
	    "returnSignature": "b",
	    "name": "recordVideo",
	    "parametersSignature": "(ssii)",
	    "description": "Background record of an .arv raw format video from the images processed by a vision module\nActualy it take picture each time the vision module call getDirectRawImageRemote().",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Name under which the G.V.M. is known from the V.I.M."
	        },
	        {
	            "name": "path",
	            "description": "path/name of the video to be recorded"
	        },
	        {
	            "name": "totalNumber",
	            "description": "number of images to be recorded. 0xFFFFFFFF for \"unlimited\""
	        },
	        {
	            "name": "period",
	            "description": "one image recorded every pPeriod images"
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "recordVideo", [id, path, totalNumber, period])

def stopVideo(id:str) -> bool:
	"""
	Stop writing the video sequence
	
	Parameters
	----------
	id:str
		Name under which the G.V.M. is known from ALVideoDevice.
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 185,
	    "returnSignature": "b",
	    "name": "stopVideo",
	    "parametersSignature": "(s)",
	    "description": "Stop writing the video sequence",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Name under which the G.V.M. is known from ALVideoDevice."
	        }
	    ],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "stopVideo", [id])

def getAngularPositionFromImagePosition(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 186,
	    "returnSignature": "[f]",
	    "name": "getAngularPositionFromImagePosition",
	    "parametersSignature": "(i[f])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getAngularPositionFromImagePosition", [p0, p1])

def getImagePositionFromAngularPosition(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 187,
	    "returnSignature": "[f]",
	    "name": "getImagePositionFromAngularPosition",
	    "parametersSignature": "(i[f])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImagePositionFromAngularPosition", [p0, p1])

def getAngularSizeFromImageSize(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 188,
	    "returnSignature": "[f]",
	    "name": "getAngularSizeFromImageSize",
	    "parametersSignature": "(i[f])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getAngularSizeFromImageSize", [p0, p1])

def getImageSizeFromAngularSize(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 189,
	    "returnSignature": "[f]",
	    "name": "getImageSizeFromAngularSize",
	    "parametersSignature": "(i[f])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImageSizeFromAngularSize", [p0, p1])

def getImageInfoFromAngularInfo(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	
	*Reference struct*
	'''
	{
	    "uid": 190,
	    "returnSignature": "[f]",
	    "name": "getImageInfoFromAngularInfo",
	    "parametersSignature": "(i[f])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImageInfoFromAngularInfo", [p0, p1])

def getImageInfoFromAngularInfoWithResolution(p0:int, p1:List[float], p2:int) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 191,
	    "returnSignature": "[f]",
	    "name": "getImageInfoFromAngularInfoWithResolution",
	    "parametersSignature": "(i[f]i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getImageInfoFromAngularInfoWithResolution", [p0, p1, p2])

def putImage_1(cameraIndex:int, timeStamp:object, width:int, height:int, colorSpace:int, imageBuffer:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (putImage)
	
	Allow image buffer pushing
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	timeStamp:object
		time stamp of the image. If empty, use current time.
	width:int
		int width of image among 1280*960, 640*480, 320*240, 240*160
	height:int
		int height of image
	colorSpace:int
		colorSpace of image.
	imageBuffer:object
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	*Reference struct*
	'''
	{
	    "uid": 192,
	    "returnSignature": "b",
	    "name": "putImage",
	    "parametersSignature": "(imiiim)",
	    "description": "Allow image buffer pushing",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "timeStamp",
	            "description": "time stamp of the image. If empty, use current time."
	        },
	        {
	            "name": "width",
	            "description": "int width of image among 1280*960, 640*480, 320*240, 240*160"
	        },
	        {
	            "name": "height",
	            "description": "int height of image"
	        },
	        {
	            "name": "colorSpace",
	            "description": "colorSpace of image."
	        },
	        {
	            "name": "imageBuffer",
	            "description": "Image buffer in bitmap form"
	        }
	    ],
	    "returnDescription": "true if the put succeeded"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "putImage", [cameraIndex, timeStamp, width, height, colorSpace, imageBuffer])

def getExpectedImageParameters_1(cameraIndex:int) -> object:
	"""
	Note: This is one of the overloads of the original method (getExpectedImageParameters)
	
	called by the simulator to know expected image parameters
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	ALValue of expected parameters, [int resolution, int framerate]
	
	*Reference struct*
	'''
	{
	    "uid": 193,
	    "returnSignature": "m",
	    "name": "getExpectedImageParameters",
	    "parametersSignature": "(i)",
	    "description": "called by the simulator to know expected image parameters",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": "ALValue of expected parameters, [int resolution, int framerate]"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getExpectedImageParameters", [cameraIndex])

def _getExternalBrightness(cameraIndex:int) -> int:
	"""
	Get average environment luminance.
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	The average brightness luminance == (15680-Texposure)*256+AverageLuminance
	
	*Reference struct*
	'''
	{
	    "uid": 194,
	    "returnSignature": "i",
	    "name": "_getExternalBrightness",
	    "parametersSignature": "(i)",
	    "description": "Get average environment luminance.",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": "The average brightness luminance == (15680-Texposure)*256+AverageLuminance"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "_getExternalBrightness", [cameraIndex])

def onClientDisconnected(eventName:str, eventContents:object, message:str) -> None:
	"""
	Callback when client is disconnected
	
	Parameters
	----------
	eventName:str
		The echoed event name
	eventContents:object
		The name of the client that has disconnected
	message:str
		The message give when subscribing.
	
	*Reference struct*
	'''
	{
	    "uid": 195,
	    "returnSignature": "v",
	    "name": "onClientDisconnected",
	    "parametersSignature": "(sms)",
	    "description": "Callback when client is disconnected",
	    "parameters": [
	        {
	            "name": "eventName",
	            "description": "The echoed event name"
	        },
	        {
	            "name": "eventContents",
	            "description": "The name of the client that has disconnected"
	        },
	        {
	            "name": "message",
	            "description": "The message give when subscribing."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "onClientDisconnected", [eventName, eventContents, message])

def subscribe(gvmName:str, resolution:int, colorSpace:int, fps:int) -> str:
	"""
	Register to ALVideoDevice (formerly Video Input Module/V.I.M.). When a General Video Module(G.V.M.) registers to ALVideoDevice, a buffer of the requested image format is added to the buffers list.
	Returns the name under which the G.V.M. is registered to ALVideoDevice (useful when two G.V.M. try to register using the same name
	
	Parameters
	----------
	gvmName:str
		Name of the subscribing G.V.M.
	resolution:int
		Resolution requested. {0: kQQVGA, 1: kQVGA, 2: kVGA}
	colorSpace:int
		Colorspace requested. {0: kYuv, 9: kYUV422, 10: kYUV, 11: kRGB, 12: kHSY, 13: kBGR}
	fps:int
		Fps (frames per second) requested. {5, 10, 15, 30}
	
	Returns
	----------
	Name under which the G.V.M. is known from ALVideoDevice, 0 if failed.
	
	*Reference struct*
	'''
	{
	    "uid": 196,
	    "returnSignature": "s",
	    "name": "subscribe",
	    "parametersSignature": "(siii)",
	    "description": "Register to ALVideoDevice (formerly Video Input Module/V.I.M.). When a General Video Module(G.V.M.) registers to ALVideoDevice, a buffer of the requested image format is added to the buffers list.\nReturns the name under which the G.V.M. is registered to ALVideoDevice (useful when two G.V.M. try to register using the same name",
	    "parameters": [
	        {
	            "name": "gvmName",
	            "description": "Name of the subscribing G.V.M."
	        },
	        {
	            "name": "resolution",
	            "description": "Resolution requested. {0: kQQVGA, 1: kQVGA, 2: kVGA}"
	        },
	        {
	            "name": "colorSpace",
	            "description": "Colorspace requested. {0: kYuv, 9: kYUV422, 10: kYUV, 11: kRGB, 12: kHSY, 13: kBGR}"
	        },
	        {
	            "name": "fps",
	            "description": "Fps (frames per second) requested. {5, 10, 15, 30}"
	        }
	    ],
	    "returnDescription": "Name under which the G.V.M. is known from ALVideoDevice, 0 if failed."
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "subscribe", [gvmName, resolution, colorSpace, fps])

def unsubscribeAllInstances(id:str) -> None:
	"""
	Used to unsubscribe all instances for a given G.V.M. (e.g. VisionModule and VisionModule_5) from ALVideoDevice.
	
	Parameters
	----------
	id:str
		Root name of the G.V.M. (e.g. with the example above this will be VisionModule).
	
	*Reference struct*
	'''
	{
	    "uid": 197,
	    "returnSignature": "v",
	    "name": "unsubscribeAllInstances",
	    "parametersSignature": "(s)",
	    "description": "Used to unsubscribe all instances for a given G.V.M. (e.g. VisionModule and VisionModule_5) from ALVideoDevice.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Root name of the G.V.M. (e.g. with the example above this will be VisionModule)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "unsubscribeAllInstances", [id])

def setParam_1(param:int, newValue:int) -> None:
	"""
	Note: This is one of the overloads of the original method (setParam)
	
	Sets the value of a specific parameter for the video source.
	
	Parameters
	----------
	param:int
		Camera parameter requested.
	newValue:int
		value requested.
	
	*Reference struct*
	'''
	{
	    "uid": 205,
	    "returnSignature": "v",
	    "name": "setParam",
	    "parametersSignature": "(ii)",
	    "description": "Sets the value of a specific parameter for the video source.",
	    "parameters": [
	        {
	            "name": "param",
	            "description": "Camera parameter requested."
	        },
	        {
	            "name": "newValue",
	            "description": "value requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setParam", [param, newValue])

def setParam_2(param:int, newValue:int, cameraIndex:int) -> None:
	"""
	Note: This is one of the overloads of the original method (setParam)
	
	Sets the value of a specific parameter for the video source.
	
	Parameters
	----------
	param:int
		Camera parameter requested.
	newValue:int
		value requested.
	cameraIndex:int
		Camera requested.
	
	*Reference struct*
	'''
	{
	    "uid": 206,
	    "returnSignature": "v",
	    "name": "setParam",
	    "parametersSignature": "(iii)",
	    "description": "Sets the value of a specific parameter for the video source.",
	    "parameters": [
	        {
	            "name": "param",
	            "description": "Camera parameter requested."
	        },
	        {
	            "name": "newValue",
	            "description": "value requested."
	        },
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setParam", [param, newValue, cameraIndex])

def getExpectedImageParameters_2() -> object:
	"""
	Note: This is one of the overloads of the original method (getExpectedImageParameters)
	
	called by the simulator to know expected image parameters
	
	Returns
	----------
	ALValue of expected parameters, [int resolution, int framerate]
	
	*Reference struct*
	'''
	{
	    "uid": 218,
	    "returnSignature": "m",
	    "name": "getExpectedImageParameters",
	    "parametersSignature": "()",
	    "description": "called by the simulator to know expected image parameters",
	    "parameters": [],
	    "returnDescription": "ALValue of expected parameters, [int resolution, int framerate]"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "getExpectedImageParameters", [])

def setSimCamInputSize(width:int, height:int) -> bool:
	"""
	called by the simulator to know expected image parameters
	
	Parameters
	----------
	width:int
		int width of image among 1280, 640, 320, 240, 120, 60
	height:int
		int height of image among 960, 480, 240, 160, 80, 40
	
	Returns
	----------
	true if setSize worked
	
	*Reference struct*
	'''
	{
	    "uid": 219,
	    "returnSignature": "b",
	    "name": "setSimCamInputSize",
	    "parametersSignature": "(ii)",
	    "description": "called by the simulator to know expected image parameters",
	    "parameters": [
	        {
	            "name": "width",
	            "description": "int width of image among 1280, 640, 320, 240, 120, 60"
	        },
	        {
	            "name": "height",
	            "description": "int height of image among 960, 480, 240, 160, 80, 40"
	        }
	    ],
	    "returnDescription": "true if setSize worked"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "setSimCamInputSize", [width, height])

def putImage_2(imageBuffer:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (putImage)
	
	Allow image buffer pushing
	
	Parameters
	----------
	imageBuffer:object
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	*Reference struct*
	'''
	{
	    "uid": 220,
	    "returnSignature": "b",
	    "name": "putImage",
	    "parametersSignature": "(m)",
	    "description": "Allow image buffer pushing",
	    "parameters": [
	        {
	            "name": "imageBuffer",
	            "description": "Image buffer in bitmap form"
	        }
	    ],
	    "returnDescription": "true if the put succeeded"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "putImage", [imageBuffer])

def putImage_3(cameraIndex:int, width:int, height:int, imageBuffer:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (putImage)
	
	Allow image buffer pushing
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	width:int
		int width of image among 1280*960, 640*480, 320*240, 240*160
	height:int
		int height of image
	imageBuffer:object
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	*Reference struct*
	'''
	{
	    "uid": 221,
	    "returnSignature": "b",
	    "name": "putImage",
	    "parametersSignature": "(iiim)",
	    "description": "Allow image buffer pushing",
	    "parameters": [
	        {
	            "name": "cameraIndex",
	            "description": "Camera requested."
	        },
	        {
	            "name": "width",
	            "description": "int width of image among 1280*960, 640*480, 320*240, 240*160"
	        },
	        {
	            "name": "height",
	            "description": "int height of image"
	        },
	        {
	            "name": "imageBuffer",
	            "description": "Image buffer in bitmap form"
	        }
	    ],
	    "returnDescription": "true if the put succeeded"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "putImage", [cameraIndex, width, height, imageBuffer])

def startFrameGrabber_2() -> bool:
	"""
	Note: This is one of the overloads of the original method (startFrameGrabber)
	
	Advanced method that opens and initialize video source device if it was not before.
	Note that the first client subscribing to ALVideoDevice will launch it automatically.
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 222,
	    "returnSignature": "b",
	    "name": "startFrameGrabber",
	    "parametersSignature": "()",
	    "description": "Advanced method that opens and initialize video source device if it was not before.\nNote that the first client subscribing to ALVideoDevice will launch it automatically.",
	    "parameters": [],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "startFrameGrabber", [])

def stopFrameGrabber_2() -> bool:
	"""
	Note: This is one of the overloads of the original method (stopFrameGrabber)
	
	Advanced method that close video source device.
	Note that the last client unsubscribing to ALVideoDevice will launch it automatically.
	
	Returns
	----------
	true if success
	
	*Reference struct*
	'''
	{
	    "uid": 223,
	    "returnSignature": "b",
	    "name": "stopFrameGrabber",
	    "parametersSignature": "()",
	    "description": "Advanced method that close video source device.\nNote that the last client unsubscribing to ALVideoDevice will launch it automatically.",
	    "parameters": [],
	    "returnDescription": "true if success"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "stopFrameGrabber", [])

def isFrameGrabberOff_2() -> int:
	"""
	Note: This is one of the overloads of the original method (isFrameGrabberOff)
	
	Advanced method that asks if the framegrabber is off.
	
	Returns
	----------
	true if off
	
	*Reference struct*
	'''
	{
	    "uid": 224,
	    "returnSignature": "i",
	    "name": "isFrameGrabberOff",
	    "parametersSignature": "()",
	    "description": "Advanced method that asks if the framegrabber is off.",
	    "parameters": [],
	    "returnDescription": "true if off"
	}
	'''
	"""
	return send_mfc("ALVideoDevice", "isFrameGrabberOff", [])

