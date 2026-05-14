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
	return send_mfc("ALVisualCompass", "version", [])

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
	return send_mfc("ALVisualCompass", "ping", [])

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
	return send_mfc("ALVisualCompass", "getMethodList", [])

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
	return send_mfc("ALVisualCompass", "getMethodHelp", [methodName])

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
	return send_mfc("ALVisualCompass", "getModuleHelp", [])

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
	return send_mfc("ALVisualCompass", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALVisualCompass", "wait", [id])

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
	return send_mfc("ALVisualCompass", "isRunning", [id])

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
	return send_mfc("ALVisualCompass", "stop", [id])

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
	return send_mfc("ALVisualCompass", "getBrokerName", [])

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
	return send_mfc("ALVisualCompass", "getUsage", [name])

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
	return send_mfc("ALVisualCompass", "subscribe", [name, period, precision])

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
	return send_mfc("ALVisualCompass", "subscribe", [name])

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
	return send_mfc("ALVisualCompass", "unsubscribe", [name])

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
	return send_mfc("ALVisualCompass", "updatePeriod", [name, period])

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
	return send_mfc("ALVisualCompass", "updatePrecision", [name, precision])

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
	return send_mfc("ALVisualCompass", "getCurrentPeriod", [])

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
	return send_mfc("ALVisualCompass", "getCurrentPrecision", [])

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
	return send_mfc("ALVisualCompass", "getMyPeriod", [name])

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
	return send_mfc("ALVisualCompass", "getMyPrecision", [name])

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
	return send_mfc("ALVisualCompass", "getSubscribersInfo", [])

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
	return send_mfc("ALVisualCompass", "getOutputNames", [])

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
	return send_mfc("ALVisualCompass", "getEventList", [])

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
	return send_mfc("ALVisualCompass", "getMemoryKeyList", [])

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
	return send_mfc("ALVisualCompass", "setFrameRate", [subscriberName, framerate])

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
	return send_mfc("ALVisualCompass", "setFrameRate", [framerate])

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
	return send_mfc("ALVisualCompass", "setResolution", [resolution])

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
	return send_mfc("ALVisualCompass", "setActiveCamera", [cameraId])

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
	return send_mfc("ALVisualCompass", "getFrameRate", [])

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
	return send_mfc("ALVisualCompass", "getResolution", [])

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
	return send_mfc("ALVisualCompass", "getActiveCamera", [])

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
	return send_mfc("ALVisualCompass", "isPaused", [])

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
	return send_mfc("ALVisualCompass", "isProcessing", [])

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
	return send_mfc("ALVisualCompass", "pause", [paused])

def getReferenceImage() -> object:
	"""
	Returns an ALValue containing the image used as a reference.
	
	Returns
	----------
	Reference image (formatted as the ALValue from getImageRemote of ALVideoDevice)
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "m",
	    "name": "getReferenceImage",
	    "parametersSignature": "()",
	    "description": "Returns an ALValue containing the image used as a reference.",
	    "parameters": [],
	    "returnDescription": "Reference image (formatted as the ALValue from getImageRemote of ALVideoDevice)"
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "getReferenceImage", [])

def enableReferenceRefresh(refresh:bool) -> None:
	"""
	
	
	Parameters
	----------
	refresh:bool
		True if the reference is automatically refreshed at extractor startup; false to use the manually set reference image.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "enableReferenceRefresh",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "refresh",
	            "description": "True if the reference is automatically refreshed at extractor startup; false to use the manually set reference image."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "enableReferenceRefresh", [refresh])

def getMatchingQuality() -> object:
	"""
	Returns the reliability of the matching and the compass deviation computations.
	
	Returns
	----------
	[0]: Percentage of the matched keypoints that are used to compute the deviation (significant if over 50%) 
	 [1]: Number of keypoints matching.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "m",
	    "name": "getMatchingQuality",
	    "parametersSignature": "()",
	    "description": "Returns the reliability of the matching and the compass deviation computations.",
	    "parameters": [],
	    "returnDescription": "[0]: Percentage of the matched keypoints that are used to compute the deviation (significant if over 50%) \n [1]: Number of keypoints matching."
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "getMatchingQuality", [])

def setCurrentImageAsReference() -> bool:
	"""
	Sets the reference image for the compass.
	
	Returns
	----------
	True if the reference image has been successfully set
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "b",
	    "name": "setCurrentImageAsReference",
	    "parametersSignature": "()",
	    "description": "Sets the reference image for the compass.",
	    "parameters": [],
	    "returnDescription": "True if the reference image has been successfully set"
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "setCurrentImageAsReference", [])

def moveTo(x:float, y:float, theta:float) -> bool:
	"""
	Go to input pose (in robot referential).
	
	Parameters
	----------
	x:float
		Distance along the X axis in meters.
	y:float
		Distance along the Y axis in meters.
	theta:float
		Rotation around the Z axis in radians [-3.1415 to 3.1415].
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(fff)",
	    "description": "Go to input pose (in robot referential).",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "Distance along the X axis in meters."
	        },
	        {
	            "name": "y",
	            "description": "Distance along the Y axis in meters."
	        },
	        {
	            "name": "theta",
	            "description": "Rotation around the Z axis in radians [-3.1415 to 3.1415]."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "moveTo", [x, y, theta])

def moveStraightTo(x:float) -> bool:
	"""
	Move along the robot X axis.
	
	Parameters
	----------
	x:float
		Algebric distance along the X axis in meters.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "b",
	    "name": "moveStraightTo",
	    "parametersSignature": "(f)",
	    "description": "Move along the robot X axis.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "Algebric distance along the X axis in meters."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "moveStraightTo", [x])

def _stopControllers() -> None:
	"""
	Stops the robot
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_stopControllers",
	    "parametersSignature": "()",
	    "description": "Stops the robot",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "_stopControllers", [])

def _resumeControllers(resumeControllers:bool) -> None:
	"""
	Stops the robot
	
	Parameters
	----------
	resumeControllers:bool
		Resume after stopping
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "_resumeControllers",
	    "parametersSignature": "(b)",
	    "description": "Stops the robot",
	    "parameters": [
	        {
	            "name": "resumeControllers",
	            "description": "Resume after stopping"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "_resumeControllers", [resumeControllers])

def _resume() -> None:
	"""
	Allows the robot to resume after stopping.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "_resume",
	    "parametersSignature": "()",
	    "description": "Allows the robot to resume after stopping.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "_resume", [])

def _setTranslationParameters(pCoefficient:float, thetaThreshold:float, p2:float, p3:float) -> None:
	"""
	Set the rotation controller parameters.
	
	Parameters
	----------
	pCoefficient:float
		Proportional gain of the controller.
	thetaThreshold:float
		Threshold to consider the gap on theta as error.
	p2:float
		
	p3:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "_setTranslationParameters",
	    "parametersSignature": "(ffff)",
	    "description": "Set the rotation controller parameters.",
	    "parameters": [
	        {
	            "name": "pCoefficient",
	            "description": "Proportional gain of the controller."
	        },
	        {
	            "name": "thetaThreshold",
	            "description": "Threshold to consider the gap on theta as error."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "_setTranslationParameters", [pCoefficient, thetaThreshold, p2, p3])

def _setRotationParameters(pCoefficient:object, maxRotationSpeed:float, thetaThreshold:float, p3:float, p4:float, p5:int) -> None:
	"""
	Set the rotation controller parameters.
	
	Parameters
	----------
	pCoefficient:object
		Proportional gain of the controller.
	maxRotationSpeed:float
		Max robot rotation speed.
	thetaThreshold:float
		Threshold to consider the gap on theta as an error.
	p3:float
		
	p4:float
		
	p5:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_setRotationParameters",
	    "parametersSignature": "(mffffi)",
	    "description": "Set the rotation controller parameters.",
	    "parameters": [
	        {
	            "name": "pCoefficient",
	            "description": "Proportional gain of the controller."
	        },
	        {
	            "name": "maxRotationSpeed",
	            "description": "Max robot rotation speed."
	        },
	        {
	            "name": "thetaThreshold",
	            "description": "Threshold to consider the gap on theta as an error."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "_setRotationParameters", [pCoefficient, maxRotationSpeed, thetaThreshold, p3, p4, p5])

def waitUntilTargetReached() -> None:
	"""
	Block the current thread until the target is reached.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "waitUntilTargetReached",
	    "parametersSignature": "()",
	    "description": "Block the current thread until the target is reached.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisualCompass", "waitUntilTargetReached", [])

