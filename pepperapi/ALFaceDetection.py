from .gentypes import *
from .robot_client import send_mfc
import json
"""

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
	return send_mfc("ALFaceDetection", "version", [])

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
	return send_mfc("ALFaceDetection", "ping", [])

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
	return send_mfc("ALFaceDetection", "getMethodList", [])

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
	return send_mfc("ALFaceDetection", "getMethodHelp", [methodName])

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
	return send_mfc("ALFaceDetection", "getModuleHelp", [])

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
	return send_mfc("ALFaceDetection", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALFaceDetection", "wait", [id])

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
	return send_mfc("ALFaceDetection", "isRunning", [id])

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
	return send_mfc("ALFaceDetection", "stop", [id])

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
	return send_mfc("ALFaceDetection", "getBrokerName", [])

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
	return send_mfc("ALFaceDetection", "getUsage", [name])

def subscribe_1(name:str, period:int, precision:float) -> None:
	"""
	Note: This is one of the overloads of the original method (subscribe)
	
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "subscribe",
	    "parametersSignature": "(sif)",
	    "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which subscribes."
	        },
	        {
	            "name": "period",
	            "description": "Refresh period (in milliseconds) if relevant."
	        },
	        {
	            "name": "precision",
	            "description": "Precision of the extractor if relevant."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "subscribe", [name, period, precision])

def subscribe_2(name:str) -> None:
	"""
	Note: This is one of the overloads of the original method (subscribe)
	
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "subscribe",
	    "parametersSignature": "(s)",
	    "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which subscribes."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "subscribe", [name])

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "unsubscribe",
	    "parametersSignature": "(s)",
	    "description": "Unsubscribes from the extractor.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which had subscribed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "updatePeriod",
	    "parametersSignature": "(si)",
	    "description": "Updates the period if relevant.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        },
	        {
	            "name": "period",
	            "description": "Refresh period (in milliseconds)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "updatePrecision",
	    "parametersSignature": "(sf)",
	    "description": "Updates the precision if relevant.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        },
	        {
	            "name": "precision",
	            "description": "Precision of the extractor."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "i",
	    "name": "getCurrentPeriod",
	    "parametersSignature": "()",
	    "description": "Gets the current period.",
	    "parameters": [],
	    "returnDescription": "Refresh period (in milliseconds)."
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "f",
	    "name": "getCurrentPrecision",
	    "parametersSignature": "()",
	    "description": "Gets the current precision.",
	    "parameters": [],
	    "returnDescription": "Precision of the extractor."
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getCurrentPrecision", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "getMyPeriod",
	    "parametersSignature": "(s)",
	    "description": "Gets the period for a specific subscription.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the module which has subscribed."
	        }
	    ],
	    "returnDescription": "Refresh period (in milliseconds)."
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getMyPeriod", [name])

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
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "f",
	    "name": "getMyPrecision",
	    "parametersSignature": "(s)",
	    "description": "Gets the precision for a specific subscription.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "name of the module which has subscribed"
	        }
	    ],
	    "returnDescription": "precision of the extractor"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getMyPrecision", [name])

def getSubscribersInfo() -> object:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "getSubscribersInfo",
	    "parametersSignature": "()",
	    "description": "Gets the parameters given by the module.",
	    "parameters": [],
	    "returnDescription": "Array of names and parameters of all subscribers."
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "[s]",
	    "name": "getOutputNames",
	    "parametersSignature": "()",
	    "description": "Get the list of values updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of values updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "[s]",
	    "name": "getEventList",
	    "parametersSignature": "()",
	    "description": "Get the list of events updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of events updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "[s]",
	    "name": "getMemoryKeyList",
	    "parametersSignature": "()",
	    "description": "Get the list of events updated in ALMemory.",
	    "parameters": [],
	    "returnDescription": "Array of events updated by this extractor in ALMemory"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getMemoryKeyList", [])

def setFrameRate_1(subscriberName:str, framerate:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (setFrameRate)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "setFrameRate",
	    "parametersSignature": "(si)",
	    "description": "Sets the extractor framerate for a chosen subscriber",
	    "parameters": [
	        {
	            "name": "subscriberName",
	            "description": "Name of the subcriber"
	        },
	        {
	            "name": "framerate",
	            "description": "New framerate"
	        }
	    ],
	    "returnDescription": "True if the update succeeded, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setFrameRate", [subscriberName, framerate])

def setFrameRate_2(framerate:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (setFrameRate)
	
	Sets the extractor framerate for all the subscribers
	
	Parameters
	----------
	framerate:int
		New framerate
	
	Returns
	----------
	True if the update succeeded, False if not
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "setFrameRate",
	    "parametersSignature": "(i)",
	    "description": "Sets the extractor framerate for all the subscribers",
	    "parameters": [
	        {
	            "name": "framerate",
	            "description": "New framerate"
	        }
	    ],
	    "returnDescription": "True if the update succeeded, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setFrameRate", [framerate])

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
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "b",
	    "name": "setResolution",
	    "parametersSignature": "(i)",
	    "description": "Sets extractor resolution",
	    "parameters": [
	        {
	            "name": "resolution",
	            "description": "New resolution"
	        }
	    ],
	    "returnDescription": "True if the update succeeded, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setResolution", [resolution])

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
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "setActiveCamera",
	    "parametersSignature": "(i)",
	    "description": "Sets extractor active camera",
	    "parameters": [
	        {
	            "name": "cameraId",
	            "description": "Id of the camera that will become the active camera"
	        }
	    ],
	    "returnDescription": "True if the update succeeded, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setActiveCamera", [cameraId])

def getFrameRate() -> int:
	"""
	Gets extractor framerate
	
	Returns
	----------
	Current value of the framerate of the extractor
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "i",
	    "name": "getFrameRate",
	    "parametersSignature": "()",
	    "description": "Gets extractor framerate",
	    "parameters": [],
	    "returnDescription": "Current value of the framerate of the extractor"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getFrameRate", [])

def getResolution() -> int:
	"""
	Gets extractor resolution
	
	Returns
	----------
	Current value of the resolution of the extractor
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "i",
	    "name": "getResolution",
	    "parametersSignature": "()",
	    "description": "Gets extractor resolution",
	    "parameters": [],
	    "returnDescription": "Current value of the resolution of the extractor"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getResolution", [])

def getActiveCamera() -> int:
	"""
	Gets extractor active camera
	
	Returns
	----------
	Id of the current active camera of the extractor
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "i",
	    "name": "getActiveCamera",
	    "parametersSignature": "()",
	    "description": "Gets extractor active camera",
	    "parameters": [],
	    "returnDescription": "Id of the current active camera of the extractor"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getActiveCamera", [])

def isPaused() -> bool:
	"""
	Gets extractor pause status
	
	Returns
	----------
	True if the extractor is paused, False if not
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "isPaused",
	    "parametersSignature": "()",
	    "description": "Gets extractor pause status",
	    "parameters": [],
	    "returnDescription": "True if the extractor is paused, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "isPaused", [])

def isProcessing() -> bool:
	"""
	Gets extractor running status
	
	Returns
	----------
	True if the extractor is currently processing images, False if not
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "isProcessing",
	    "parametersSignature": "()",
	    "description": "Gets extractor running status",
	    "parameters": [],
	    "returnDescription": "True if the extractor is currently processing images, False if not"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "isProcessing", [])

def pause(paused:bool) -> None:
	"""
	Changes the pause status of the extractor
	
	Parameters
	----------
	paused:bool
		New pause satus
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "pause",
	    "parametersSignature": "(b)",
	    "description": "Changes the pause status of the extractor",
	    "parameters": [
	        {
	            "name": "paused",
	            "description": "New pause satus"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "pause", [paused])

def setRecognitionEnabled(enable:bool) -> None:
	"""
	enable/disable the recognition stageProcess will be faster when disabled when you don't need to recognize people
	
	Parameters
	----------
	enable:bool
		True/False
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "setRecognitionEnabled",
	    "parametersSignature": "(b)",
	    "description": "enable/disable the recognition stageProcess will be faster when disabled when you don't need to recognize people",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True/False"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setRecognitionEnabled", [enable])

def isRecognitionEnabled() -> bool:
	"""
	Returns if recognition is enabled.
	
	Returns
	----------
	True/False
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "b",
	    "name": "isRecognitionEnabled",
	    "parametersSignature": "()",
	    "description": "Returns if recognition is enabled.",
	    "parameters": [],
	    "returnDescription": "True/False"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "isRecognitionEnabled", [])

def getRecognitionConfidenceThreshold() -> float:
	"""
	Get the current confidence threshold for face recognition.
	
	Returns
	----------
	Confidence threshold
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "f",
	    "name": "getRecognitionConfidenceThreshold",
	    "parametersSignature": "()",
	    "description": "Get the current confidence threshold for face recognition.",
	    "parameters": [],
	    "returnDescription": "Confidence threshold"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getRecognitionConfidenceThreshold", [])

def setRecognitionConfidenceThreshold(confThreshold:float) -> None:
	"""
	Set the current confidence threshold for face recognition. Matches with lower confidence value will not be considered.
	
	Parameters
	----------
	confThreshold:float
		New confidence threshold between 0.0 and 1.0 (default 0.4).
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "setRecognitionConfidenceThreshold",
	    "parametersSignature": "(f)",
	    "description": "Set the current confidence threshold for face recognition. Matches with lower confidence value will not be considered.",
	    "parameters": [
	        {
	            "name": "confThreshold",
	            "description": "New confidence threshold between 0.0 and 1.0 (default 0.4)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setRecognitionConfidenceThreshold", [confThreshold])

def setTrackingEnabled(enable:bool) -> None:
	"""
	(BETA) Choose to enable or disable tracking. Enabling tracking usually allows you to follow a face for a longer period of time. However, it can lead to more false detections. 
	
	Parameters
	----------
	enable:bool
		True/False
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "setTrackingEnabled",
	    "parametersSignature": "(b)",
	    "description": "(BETA) Choose to enable or disable tracking. Enabling tracking usually allows you to follow a face for a longer period of time. However, it can lead to more false detections. ",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "True/False"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "setTrackingEnabled", [enable])

def isTrackingEnabled() -> bool:
	"""
	(BETA) Returns if tracking is enabled.
	
	Returns
	----------
	True/False
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "b",
	    "name": "isTrackingEnabled",
	    "parametersSignature": "()",
	    "description": "(BETA) Returns if tracking is enabled.",
	    "parameters": [],
	    "returnDescription": "True/False"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "isTrackingEnabled", [])

def learnFace(id:str) -> bool:
	"""
	Add a new face in the database.
	
	Parameters
	----------
	id:str
		The name of the person to save
	
	Returns
	----------
	true if the operation succeeds
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "b",
	    "name": "learnFace",
	    "parametersSignature": "(s)",
	    "description": "Add a new face in the database.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The name of the person to save"
	        }
	    ],
	    "returnDescription": "true if the operation succeeds"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "learnFace", [id])

def reLearnFace(id:str) -> bool:
	"""
	use in a new learning process the latest images where a face has been wrongly recognized 
	
	Parameters
	----------
	id:str
		The name of the person to save
	
	Returns
	----------
	true if the operation succeeds
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "b",
	    "name": "reLearnFace",
	    "parametersSignature": "(s)",
	    "description": "use in a new learning process the latest images where a face has been wrongly recognized ",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The name of the person to save"
	        }
	    ],
	    "returnDescription": "true if the operation succeeds"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "reLearnFace", [id])

def forgetPerson(id:str) -> bool:
	"""
	Delete from the database all faces instances of a person.
	
	Parameters
	----------
	id:str
		The name of the person to forget
	
	Returns
	----------
	true if the operation succeeds
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "forgetPerson",
	    "parametersSignature": "(s)",
	    "description": "Delete from the database all faces instances of a person.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The name of the person to forget"
	        }
	    ],
	    "returnDescription": "true if the operation succeeds"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "forgetPerson", [id])

def clearDatabase() -> bool:
	"""
	Remove all faces from the database.
	
	Returns
	----------
	true if the operation succeeds
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "b",
	    "name": "clearDatabase",
	    "parametersSignature": "()",
	    "description": "Remove all faces from the database.",
	    "parameters": [],
	    "returnDescription": "true if the operation succeeds"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "clearDatabase", [])

def _setDetectionMode(mode:int) -> bool:
	"""
	Changes the mode of detection
	
	Parameters
	----------
	mode:int
		0 - Still Image,
		Motion mode:
		1 - Whole search mode,
		2 - 3 Partition search mode,
		3 - Gradual progress search mode.
	
	Returns
	----------
	True if success
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "b",
	    "name": "_setDetectionMode",
	    "parametersSignature": "(i)",
	    "description": "Changes the mode of detection",
	    "parameters": [
	        {
	            "name": "mode",
	            "description": "0 - Still Image,\nMotion mode:\n1 - Whole search mode,\n2 - 3 Partition search mode,\n3 - Gradual progress search mode."
	        }
	    ],
	    "returnDescription": "True if success"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "_setDetectionMode", [mode])

def _getDetectionMode() -> int:
	"""
	Returns the current mode of detection
	
	Returns
	----------
	current mode of detection (0, 1, 2 or 3)
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "i",
	    "name": "_getDetectionMode",
	    "parametersSignature": "()",
	    "description": "Returns the current mode of detection",
	    "parameters": [],
	    "returnDescription": "current mode of detection (0, 1, 2 or 3)"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "_getDetectionMode", [])

def _isFaceAnalysisEnabled() -> bool:
	"""
	Returns the current face analysis state
	
	Returns
	----------
	True/False
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "_isFaceAnalysisEnabled",
	    "parametersSignature": "()",
	    "description": "Returns the current face analysis state",
	    "parameters": [],
	    "returnDescription": "True/False"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "_isFaceAnalysisEnabled", [])

def _setFaceAnalysisEnabled(enabled:bool) -> None:
	"""
	Enables or disables the full face analysis
	
	Parameters
	----------
	enabled:bool
		True to enable, False to disable
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "v",
	    "name": "_setFaceAnalysisEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enables or disables the full face analysis",
	    "parameters": [
	        {
	            "name": "enabled",
	            "description": "True to enable, False to disable"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "_setFaceAnalysisEnabled", [enabled])

def importOldDatabase(policy:str) -> bool:
	"""
	Imports the content of an old face reco DB
	
	Parameters
	----------
	policy:str
		Merging policy if an imported entry has the same name as an existing one.
		It can be either:
		"overwrite" to replace the existing entry by the imported one,
		"merge" to merge data from both entries (if they don't relate to the same person, face recognition may fail),
		"keep" to keep the existing entry and skip the imported one.
	
	Returns
	----------
	True if the import succeeded, false otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "b",
	    "name": "importOldDatabase",
	    "parametersSignature": "(s)",
	    "description": "Imports the content of an old face reco DB",
	    "parameters": [
	        {
	            "name": "policy",
	            "description": "Merging policy if an imported entry has the same name as an existing one.\nIt can be either:\n\"overwrite\" to replace the existing entry by the imported one,\n\"merge\" to merge data from both entries (if they don't relate to the same person, face recognition may fail),\n\"keep\" to keep the existing entry and skip the imported one."
	        }
	    ],
	    "returnDescription": "True if the import succeeded, false otherwise."
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "importOldDatabase", [policy])

def getLearnedFacesList() -> object:
	"""
	Returns the list of learned faces.
	
	Returns
	----------
	List of names
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "m",
	    "name": "getLearnedFacesList",
	    "parametersSignature": "()",
	    "description": "Returns the list of learned faces.",
	    "parameters": [],
	    "returnDescription": "List of names"
	}
	'''
	"""
	return send_mfc("ALFaceDetection", "getLearnedFacesList", [])

