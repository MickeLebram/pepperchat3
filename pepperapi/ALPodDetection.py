from .gentypes import *
from .robot_client import send_mfc
import json
"""
Estimates the presence and pose of pods
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
	return send_mfc("ALPodDetection", "version", [])

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
	return send_mfc("ALPodDetection", "ping", [])

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
	return send_mfc("ALPodDetection", "getMethodList", [])

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
	return send_mfc("ALPodDetection", "getMethodHelp", [methodName])

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
	return send_mfc("ALPodDetection", "getModuleHelp", [])

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
	return send_mfc("ALPodDetection", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALPodDetection", "wait", [id])

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
	return send_mfc("ALPodDetection", "isRunning", [id])

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
	return send_mfc("ALPodDetection", "stop", [id])

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
	return send_mfc("ALPodDetection", "getBrokerName", [])

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
	return send_mfc("ALPodDetection", "getUsage", [name])

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
	return send_mfc("ALPodDetection", "subscribe", [name, period, precision])

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
	return send_mfc("ALPodDetection", "subscribe", [name])

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
	return send_mfc("ALPodDetection", "unsubscribe", [name])

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
	return send_mfc("ALPodDetection", "updatePeriod", [name, period])

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
	return send_mfc("ALPodDetection", "updatePrecision", [name, precision])

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
	return send_mfc("ALPodDetection", "getCurrentPeriod", [])

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
	return send_mfc("ALPodDetection", "getCurrentPrecision", [])

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
	return send_mfc("ALPodDetection", "getMyPeriod", [name])

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
	return send_mfc("ALPodDetection", "getMyPrecision", [name])

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
	return send_mfc("ALPodDetection", "getSubscribersInfo", [])

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
	return send_mfc("ALPodDetection", "getOutputNames", [])

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
	return send_mfc("ALPodDetection", "getEventList", [])

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
	return send_mfc("ALPodDetection", "getMemoryKeyList", [])

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
	return send_mfc("ALPodDetection", "setFrameRate", [subscriberName, framerate])

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
	return send_mfc("ALPodDetection", "setFrameRate", [framerate])

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
	return send_mfc("ALPodDetection", "setResolution", [resolution])

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
	return send_mfc("ALPodDetection", "setActiveCamera", [cameraId])

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
	return send_mfc("ALPodDetection", "getFrameRate", [])

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
	return send_mfc("ALPodDetection", "getResolution", [])

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
	return send_mfc("ALPodDetection", "getActiveCamera", [])

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
	return send_mfc("ALPodDetection", "isPaused", [])

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
	return send_mfc("ALPodDetection", "isProcessing", [])

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
	return send_mfc("ALPodDetection", "pause", [paused])

def _getTrackerEventName() -> str:
	"""
	Get the ALTracker-compatible ALMemory key that is raised at every detection
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "s",
	    "name": "_getTrackerEventName",
	    "parametersSignature": "()",
	    "description": "Get the ALTracker-compatible ALMemory key that is raised at every detection",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getTrackerEventName", [])

def _setTrackerEventName(new_event_name:str) -> None:
	"""
	Set the ALTracker-compatible ALMemory key that is raised at every detection
	
	Parameters
	----------
	new_event_name:str
		New ALMemory key at which ALTracker-compatible detections should be raised
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "_setTrackerEventName",
	    "parametersSignature": "(s)",
	    "description": "Set the ALTracker-compatible ALMemory key that is raised at every detection",
	    "parameters": [
	        {
	            "name": "new_event_name",
	            "description": "New ALMemory key at which ALTracker-compatible detections should be raised"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setTrackerEventName", [new_event_name])

def _getDetectionEventName() -> str:
	"""
	Get the ALMemory key that is raised at every detection
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "s",
	    "name": "_getDetectionEventName",
	    "parametersSignature": "()",
	    "description": "Get the ALMemory key that is raised at every detection",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getDetectionEventName", [])

def _setDetectionEventName(new_event_name:str) -> None:
	"""
	Set the ALMemory key that is raised at every detection
	
	Parameters
	----------
	new_event_name:str
		New ALMemory key at which detections should be raised
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_setDetectionEventName",
	    "parametersSignature": "(s)",
	    "description": "Set the ALMemory key that is raised at every detection",
	    "parameters": [
	        {
	            "name": "new_event_name",
	            "description": "New ALMemory key at which detections should be raised"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setDetectionEventName", [new_event_name])

def _isImageSavingEnabled() -> bool:
	"""
	Query whether image saving is enabled
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "b",
	    "name": "_isImageSavingEnabled",
	    "parametersSignature": "()",
	    "description": "Query whether image saving is enabled",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_isImageSavingEnabled", [])

def _enableImageSaving(enable:bool) -> None:
	"""
	Enable/Disable the image saving at each process
	
	Parameters
	----------
	enable:bool
		if true, the image will be saved before being processed
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "_enableImageSaving",
	    "parametersSignature": "(b)",
	    "description": "Enable/Disable the image saving at each process",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "if true, the image will be saved before being processed"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_enableImageSaving", [enable])

def _getMaxSavedDetections() -> int:
	"""
	Query the size of the saved detection circular buffer
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "I",
	    "name": "_getMaxSavedDetections",
	    "parametersSignature": "()",
	    "description": "Query the size of the saved detection circular buffer",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getMaxSavedDetections", [])

def _setMaxSavedDetections(new_maximum:int) -> None:
	"""
	Set the size of the saved detection circular buffer
	
	Parameters
	----------
	new_maximum:int
		the new maximum number of detections that will be kept on disk
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "_setMaxSavedDetections",
	    "parametersSignature": "(I)",
	    "description": "Set the size of the saved detection circular buffer",
	    "parameters": [
	        {
	            "name": "new_maximum",
	            "description": "the new maximum number of detections that will be kept on disk"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setMaxSavedDetections", [new_maximum])

def _startLogging() -> None:
	"""
	Initialize the saved detection circular buffer and enable image saving during process().
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_startLogging",
	    "parametersSignature": "()",
	    "description": "Initialize the saved detection circular buffer and enable image saving during process().",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_startLogging", [])

def _stopLogging() -> None:
	"""
	Stop the image saving, and start an async to write circular buffer on disk.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "_stopLogging",
	    "parametersSignature": "()",
	    "description": "Stop the image saving, and start an async to write circular buffer on disk.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_stopLogging", [])

def _pauseLogging() -> None:
	"""
	Stop the image saving without writing to the disk.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "_pauseLogging",
	    "parametersSignature": "()",
	    "description": "Stop the image saving without writing to the disk.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_pauseLogging", [])

def _resumeLogging() -> None:
	"""
	Resume the image saving after a pause.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "_resumeLogging",
	    "parametersSignature": "()",
	    "description": "Resume the image saving after a pause.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_resumeLogging", [])

def _getTargetCameraExposure() -> int:
	"""
	Query the target exposure to which the active camera is set to when detecting
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "I",
	    "name": "_getTargetCameraExposure",
	    "parametersSignature": "()",
	    "description": "Query the target exposure to which the active camera is set to when detecting",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getTargetCameraExposure", [])

def _setTargetCameraExposure(new_target_camera_exposure:int) -> None:
	"""
	Set the target exposure to which the active camera is set to when detecting
	
	Parameters
	----------
	new_target_camera_exposure:int
		the new target exposure to user when detecting
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "_setTargetCameraExposure",
	    "parametersSignature": "(I)",
	    "description": "Set the target exposure to which the active camera is set to when detecting",
	    "parameters": [
	        {
	            "name": "new_target_camera_exposure",
	            "description": "the new target exposure to user when detecting"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setTargetCameraExposure", [new_target_camera_exposure])

def _getBeaconColorRGB() -> List[object]:
	"""
	Query the searched blob color as an RGB triplet
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "[C]",
	    "name": "_getBeaconColorRGB",
	    "parametersSignature": "()",
	    "description": "Query the searched blob color as an RGB triplet",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBeaconColorRGB", [])

def _setBeaconColorRGB(new_R:object, new_G:object, new_B:object) -> None:
	"""
	Set the searched blob color as an RGB triplet; this also sets the searched Lab
	
	Parameters
	----------
	new_R:object
		the red component of the new searched color
	new_G:object
		the green component of the new searched color
	new_B:object
		the blue component of the new searched color
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "v",
	    "name": "_setBeaconColorRGB",
	    "parametersSignature": "(CCC)",
	    "description": "Set the searched blob color as an RGB triplet; this also sets the searched Lab",
	    "parameters": [
	        {
	            "name": "new_R",
	            "description": "the red component of the new searched color"
	        },
	        {
	            "name": "new_G",
	            "description": "the green component of the new searched color"
	        },
	        {
	            "name": "new_B",
	            "description": "the blue component of the new searched color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBeaconColorRGB", [new_R, new_G, new_B])

def _getBeaconColorLab() -> List[float]:
	"""
	Query the searched blob color as an Lab triplet
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "[f]",
	    "name": "_getBeaconColorLab",
	    "parametersSignature": "()",
	    "description": "Query the searched blob color as an Lab triplet",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBeaconColorLab", [])

def _setBeaconColorLab(new_L:float, new_a:float, new_b:float) -> None:
	"""
	Set the searched blob color as an Lab triplet; this also sets the searched RGB
	
	Parameters
	----------
	new_L:float
		the L component of the new searched color
	new_a:float
		the a component of the new searched color
	new_b:float
		the b component of the new searched color
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "_setBeaconColorLab",
	    "parametersSignature": "(fff)",
	    "description": "Set the searched blob color as an Lab triplet; this also sets the searched RGB",
	    "parameters": [
	        {
	            "name": "new_L",
	            "description": "the L component of the new searched color"
	        },
	        {
	            "name": "new_a",
	            "description": "the a component of the new searched color"
	        },
	        {
	            "name": "new_b",
	            "description": "the b component of the new searched color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBeaconColorLab", [new_L, new_a, new_b])

def _getBlackWhiteMarginal() -> float:
	"""
	Query the marginal probability of black and white pixels
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "f",
	    "name": "_getBlackWhiteMarginal",
	    "parametersSignature": "()",
	    "description": "Query the marginal probability of black and white pixels",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBlackWhiteMarginal", [])

def _setBlackWhiteMarginal(new_black_white_marginal:float) -> None:
	"""
	Set the marginal probability of black and white pixels
	
	Parameters
	----------
	new_black_white_marginal:float
		the new marginal probability for black and white pixels
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "_setBlackWhiteMarginal",
	    "parametersSignature": "(f)",
	    "description": "Set the marginal probability of black and white pixels",
	    "parameters": [
	        {
	            "name": "new_black_white_marginal",
	            "description": "the new marginal probability for black and white pixels"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBlackWhiteMarginal", [new_black_white_marginal])

def _getColorNormalMean() -> float:
	"""
	Query the mean of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "f",
	    "name": "_getColorNormalMean",
	    "parametersSignature": "()",
	    "description": "Query the mean of the normal distribution around the target color",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getColorNormalMean", [])

def _setColorNormalMean(new_color_normal_mean:float) -> None:
	"""
	Set the mean of the normal distribution around the target color
	
	Parameters
	----------
	new_color_normal_mean:float
		the new mean of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "v",
	    "name": "_setColorNormalMean",
	    "parametersSignature": "(f)",
	    "description": "Set the mean of the normal distribution around the target color",
	    "parameters": [
	        {
	            "name": "new_color_normal_mean",
	            "description": "the new mean of the normal distribution around the target color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setColorNormalMean", [new_color_normal_mean])

def _getColorNormalComponent1StdDev() -> float:
	"""
	Query the standard deviation of the first component of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "f",
	    "name": "_getColorNormalComponent1StdDev",
	    "parametersSignature": "()",
	    "description": "Query the standard deviation of the first component of the normal distribution around the target color",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getColorNormalComponent1StdDev", [])

def _setColorNormalComponent1StdDev(new_color_normal_stddev:float) -> None:
	"""
	Set the standard deviation of the first component of the normal distribution around the target color
	
	Parameters
	----------
	new_color_normal_stddev:float
		the new standard deviation of the first component of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "v",
	    "name": "_setColorNormalComponent1StdDev",
	    "parametersSignature": "(f)",
	    "description": "Set the standard deviation of the first component of the normal distribution around the target color",
	    "parameters": [
	        {
	            "name": "new_color_normal_stddev",
	            "description": "the new standard deviation of the first component of the normal distribution around the target color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setColorNormalComponent1StdDev", [new_color_normal_stddev])

def _getColorNormalComponent2StdDev() -> float:
	"""
	Query the standard deviation of the second component of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "f",
	    "name": "_getColorNormalComponent2StdDev",
	    "parametersSignature": "()",
	    "description": "Query the standard deviation of the second component of the normal distribution around the target color",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getColorNormalComponent2StdDev", [])

def _setColorNormalComponent2StdDev(new_color_normal_stddev:float) -> None:
	"""
	Set the standard deviation of the second component of the normal distribution around the target color
	
	Parameters
	----------
	new_color_normal_stddev:float
		the new standard deviation of the second component of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "v",
	    "name": "_setColorNormalComponent2StdDev",
	    "parametersSignature": "(f)",
	    "description": "Set the standard deviation of the second component of the normal distribution around the target color",
	    "parameters": [
	        {
	            "name": "new_color_normal_stddev",
	            "description": "the new standard deviation of the second component of the normal distribution around the target color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setColorNormalComponent2StdDev", [new_color_normal_stddev])

def _setColorNormal(new_color_normal_mean:float, new_color_normal_component1_stddev:float, new_color_normal_component2_stddev:float) -> None:
	"""
	Set the normal distribution around the target color
	
	Parameters
	----------
	new_color_normal_mean:float
		the new mean of the normal distribution around the target color
	new_color_normal_component1_stddev:float
		the new standard deviation of the first component of the normal distribution around the target color
	new_color_normal_component2_stddev:float
		the new standard deviation of the second component of the normal distribution around the target color
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "v",
	    "name": "_setColorNormal",
	    "parametersSignature": "(fff)",
	    "description": "Set the normal distribution around the target color",
	    "parameters": [
	        {
	            "name": "new_color_normal_mean",
	            "description": "the new mean of the normal distribution around the target color"
	        },
	        {
	            "name": "new_color_normal_component1_stddev",
	            "description": "the new standard deviation of the first component of the normal distribution around the target color"
	        },
	        {
	            "name": "new_color_normal_component2_stddev",
	            "description": "the new standard deviation of the second component of the normal distribution around the target color"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setColorNormal", [new_color_normal_mean, new_color_normal_component1_stddev, new_color_normal_component2_stddev])

def _getLightnessHalfProbability() -> float:
	"""
	Query the lightness half-probability parameter used to control pixel lightness prior
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "f",
	    "name": "_getLightnessHalfProbability",
	    "parametersSignature": "()",
	    "description": "Query the lightness half-probability parameter used to control pixel lightness prior",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getLightnessHalfProbability", [])

def _setLightnessHalfProbability(new_lightness_half_probability:float) -> None:
	"""
	Set the lightness half-probability parameter used to control pixel lightness prior
	
	Parameters
	----------
	new_lightness_half_probability:float
		the new lightness half-probability parameter
	
	*Reference struct*
	'''
	{
	    "uid": 167,
	    "returnSignature": "v",
	    "name": "_setLightnessHalfProbability",
	    "parametersSignature": "(f)",
	    "description": "Set the lightness half-probability parameter used to control pixel lightness prior",
	    "parameters": [
	        {
	            "name": "new_lightness_half_probability",
	            "description": "the new lightness half-probability parameter"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setLightnessHalfProbability", [new_lightness_half_probability])

def _getMinimumBlobProbability() -> float:
	"""
	Query the minimum blob probability used for pre-pruning blobs
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "f",
	    "name": "_getMinimumBlobProbability",
	    "parametersSignature": "()",
	    "description": "Query the minimum blob probability used for pre-pruning blobs",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getMinimumBlobProbability", [])

def _setMinimumBlobProbability(new_minimum_blob_probability:float) -> None:
	"""
	Set the minimum blob probability used for pre-pruning blobs
	
	Parameters
	----------
	new_minimum_blob_probability:float
		the new minimum blob probabilty used for filtering
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "v",
	    "name": "_setMinimumBlobProbability",
	    "parametersSignature": "(f)",
	    "description": "Set the minimum blob probability used for pre-pruning blobs",
	    "parameters": [
	        {
	            "name": "new_minimum_blob_probability",
	            "description": "the new minimum blob probabilty used for filtering"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setMinimumBlobProbability", [new_minimum_blob_probability])

def _getBlobLikelihoodCutoff() -> float:
	"""
	Query the blob likelihood cutoff used for filtering blobs
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "f",
	    "name": "_getBlobLikelihoodCutoff",
	    "parametersSignature": "()",
	    "description": "Query the blob likelihood cutoff used for filtering blobs",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBlobLikelihoodCutoff", [])

def _setBlobLikelihoodCutoff(new_blob_likelihood_cutoff:float) -> None:
	"""
	Set the blob likelihood cutoff used for filtering blobs
	
	Parameters
	----------
	new_blob_likelihood_cutoff:float
		the new blob likelihood threshold used to prune blobs
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "v",
	    "name": "_setBlobLikelihoodCutoff",
	    "parametersSignature": "(f)",
	    "description": "Set the blob likelihood cutoff used for filtering blobs",
	    "parameters": [
	        {
	            "name": "new_blob_likelihood_cutoff",
	            "description": "the new blob likelihood threshold used to prune blobs"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBlobLikelihoodCutoff", [new_blob_likelihood_cutoff])

def _getBlobClosenessCutoff() -> float:
	"""
	Query the blob closeness threshold used to cluster blobs
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "f",
	    "name": "_getBlobClosenessCutoff",
	    "parametersSignature": "()",
	    "description": "Query the blob closeness threshold used to cluster blobs",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBlobClosenessCutoff", [])

def _setBlobClosenessCutoff(new_blob_closeness_cutoff:float) -> None:
	"""
	Set the blob closeness threshold used to cluster blobs
	
	Parameters
	----------
	new_blob_closeness_cutoff:float
		the new blob closeness threshold used to cluster blobs
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "v",
	    "name": "_setBlobClosenessCutoff",
	    "parametersSignature": "(f)",
	    "description": "Set the blob closeness threshold used to cluster blobs",
	    "parameters": [
	        {
	            "name": "new_blob_closeness_cutoff",
	            "description": "the new blob closeness threshold used to cluster blobs"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBlobClosenessCutoff", [new_blob_closeness_cutoff])

def _getMinimumHypothesisProbability() -> float:
	"""
	Query the minimum hypothesis probability used for qualifying hypotheses
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "f",
	    "name": "_getMinimumHypothesisProbability",
	    "parametersSignature": "()",
	    "description": "Query the minimum hypothesis probability used for qualifying hypotheses",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getMinimumHypothesisProbability", [])

def _setMinimumHypothesisProbability(new_minimum_hypothesis_probability:float) -> None:
	"""
	Set the minimum hypothesis probability used for qualifying hypotheses
	
	Parameters
	----------
	new_minimum_hypothesis_probability:float
		the new minimum hypothesis probabilty
	
	*Reference struct*
	'''
	{
	    "uid": 175,
	    "returnSignature": "v",
	    "name": "_setMinimumHypothesisProbability",
	    "parametersSignature": "(f)",
	    "description": "Set the minimum hypothesis probability used for qualifying hypotheses",
	    "parameters": [
	        {
	            "name": "new_minimum_hypothesis_probability",
	            "description": "the new minimum hypothesis probabilty"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setMinimumHypothesisProbability", [new_minimum_hypothesis_probability])

def _getBlobOvercrowdingLimit() -> float:
	"""
	Query maximum number of most likely blobs to considerer when making hypotheses
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "f",
	    "name": "_getBlobOvercrowdingLimit",
	    "parametersSignature": "()",
	    "description": "Query maximum number of most likely blobs to considerer when making hypotheses",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_getBlobOvercrowdingLimit", [])

def _setBlobOvercrowdingLimit(new_blob_overcrowding_limit:int) -> None:
	"""
	Set maximum number of most likely blobs to considerer when making hypotheses
	
	Parameters
	----------
	new_blob_overcrowding_limit:int
		the new minimum hypothesis probabilty
	
	*Reference struct*
	'''
	{
	    "uid": 177,
	    "returnSignature": "v",
	    "name": "_setBlobOvercrowdingLimit",
	    "parametersSignature": "(I)",
	    "description": "Set maximum number of most likely blobs to considerer when making hypotheses",
	    "parameters": [
	        {
	            "name": "new_blob_overcrowding_limit",
	            "description": "the new minimum hypothesis probabilty"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPodDetection", "_setBlobOvercrowdingLimit", [new_blob_overcrowding_limit])

