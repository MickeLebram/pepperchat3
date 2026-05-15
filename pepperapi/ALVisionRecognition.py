from .gentypes import *
from .robot_client import send_mfc
import json
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
	return send_mfc("ALVisionRecognition", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALVisionRecognition", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALVisionRecognition", "metaObject", [p0])

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
	return send_mfc("ALVisionRecognition", "terminate", [p0])

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
	return send_mfc("ALVisionRecognition", "property", [p0])

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
	return send_mfc("ALVisionRecognition", "setProperty", [p0, p1])

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
	return send_mfc("ALVisionRecognition", "properties", [])

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
	return send_mfc("ALVisionRecognition", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALVisionRecognition", "isStatsEnabled", [])

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
	return send_mfc("ALVisionRecognition", "enableStats", [p0])

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
	return send_mfc("ALVisionRecognition", "stats", [])

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
	return send_mfc("ALVisionRecognition", "clearStats", [])

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
	return send_mfc("ALVisionRecognition", "isTraceEnabled", [])

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
	return send_mfc("ALVisionRecognition", "enableTrace", [p0])

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
	return send_mfc("ALVisionRecognition", "version", [])

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
	return send_mfc("ALVisionRecognition", "ping", [])

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
	return send_mfc("ALVisionRecognition", "getMethodList", [])

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
	return send_mfc("ALVisionRecognition", "getMethodHelp", [methodName])

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
	return send_mfc("ALVisionRecognition", "getModuleHelp", [])

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
	return send_mfc("ALVisionRecognition", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALVisionRecognition", "wait", [id])

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
	return send_mfc("ALVisionRecognition", "isRunning", [id])

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
	return send_mfc("ALVisionRecognition", "stop", [id])

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
	return send_mfc("ALVisionRecognition", "getBrokerName", [])

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
	return send_mfc("ALVisionRecognition", "getUsage", [name])

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
	return send_mfc("ALVisionRecognition", "subscribe", [name, period, precision])

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
	return send_mfc("ALVisionRecognition", "subscribe", [name])

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
	return send_mfc("ALVisionRecognition", "unsubscribe", [name])

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
	return send_mfc("ALVisionRecognition", "updatePeriod", [name, period])

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
	return send_mfc("ALVisionRecognition", "updatePrecision", [name, precision])

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
	return send_mfc("ALVisionRecognition", "getCurrentPeriod", [])

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
	return send_mfc("ALVisionRecognition", "getCurrentPrecision", [])

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
	return send_mfc("ALVisionRecognition", "getMyPeriod", [name])

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
	return send_mfc("ALVisionRecognition", "getMyPrecision", [name])

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
	return send_mfc("ALVisionRecognition", "getSubscribersInfo", [])

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
	return send_mfc("ALVisionRecognition", "getOutputNames", [])

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
	return send_mfc("ALVisionRecognition", "getEventList", [])

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
	return send_mfc("ALVisionRecognition", "getMemoryKeyList", [])

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
	return send_mfc("ALVisionRecognition", "setFrameRate", [subscriberName, framerate])

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
	return send_mfc("ALVisionRecognition", "setFrameRate", [framerate])

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
	return send_mfc("ALVisionRecognition", "setResolution", [resolution])

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
	return send_mfc("ALVisionRecognition", "setActiveCamera", [cameraId])

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
	return send_mfc("ALVisionRecognition", "getFrameRate", [])

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
	return send_mfc("ALVisionRecognition", "getResolution", [])

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
	return send_mfc("ALVisionRecognition", "getActiveCamera", [])

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
	return send_mfc("ALVisionRecognition", "isPaused", [])

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
	return send_mfc("ALVisionRecognition", "isProcessing", [])

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
	return send_mfc("ALVisionRecognition", "pause", [paused])

def _run() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_run",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "_run", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "b",
	    "name": "changeDatabase",
	    "parametersSignature": "(ss)",
	    "description": "By default the database has the name \"current\" and is on the robot in /home/nao/naoqi/share/naoqi/vision/visionrecognition/ folder. This bound method allows to choose both another name and another folder for the database. \n",
	    "parameters": [
	        {
	            "name": "databasePath",
	            "description": "Absolute path of the database on the robot, or \"\" to set default path."
	        },
	        {
	            "name": "databaseName",
	            "description": "Name of the database folder, or \"\" to set default database folder."
	        }
	    ],
	    "returnDescription": "True if the operation succeded, false otherwise."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "changeDatabase", [databasePath, databaseName])

def clearCurrentDatabase() -> None:
	"""
	Clear the current database, the user has to be warned before calling this function.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "clearCurrentDatabase",
	    "parametersSignature": "()",
	    "description": "Clear the current database, the user has to be warned before calling this function.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "clearCurrentDatabase", [])

def getParam(paramName:str) -> object:
	"""
	Get some vision recognition parameters.
	
	Parameters
	----------
	paramName:str
		The name of the parameter to get. "db_path" and "db_name" can be used.
	
	Returns
	----------
	Value of the parameter as a string for "db_path" and "db_name"
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "m",
	    "name": "getParam",
	    "parametersSignature": "(s)",
	    "description": "Get some vision recognition parameters.",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "The name of the parameter to get. \"db_path\" and \"db_name\" can be used."
	        }
	    ],
	    "returnDescription": "Value of the parameter as a string for \"db_path\" and \"db_name\""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "getParam", [paramName])

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
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "b",
	    "name": "learnFromFile",
	    "parametersSignature": "(ss[s]bb)",
	    "description": "Load an image and interpret it as an object.",
	    "parameters": [
	        {
	            "name": "filename",
	            "description": "The filename of the image that will be interpreted as a planar object."
	        },
	        {
	            "name": "name",
	            "description": "The name of the object (used as a unique identifier)."
	        },
	        {
	            "name": "tags",
	            "description": "A list of tags (as strings) containing any met-data about your object."
	        },
	        {
	            "name": "isWholeImage",
	            "description": "indicates if the object occupies the whole image. If set to false, visionrecognition will try to detect the border of the object automatically. This works with unicolor background where object stands out well from the background. By default, this is set to true."
	        },
	        {
	            "name": "forced",
	            "description": "indicates if learned object will replace existing object (having the same original name) if any."
	        }
	    ],
	    "returnDescription": "True if the operation succeded, false otherwise."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "learnFromFile", [filename, name, tags, isWholeImage, forced])

def setMaxOutObjs(iMaxOutObjs:int) -> None:
	"""
	Set the maximal number (not more than 10) of detected objects for each detection. By default, this is set to 1.
	
	Parameters
	----------
	iMaxOutObjs:int
		number of desired objects to be detected.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "setMaxOutObjs",
	    "parametersSignature": "(i)",
	    "description": "Set the maximal number (not more than 10) of detected objects for each detection. By default, this is set to 1.",
	    "parameters": [
	        {
	            "name": "iMaxOutObjs",
	            "description": "number of desired objects to be detected."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "setMaxOutObjs", [iMaxOutObjs])

def getMaxOutObjs() -> int:
	"""
	Get the maximal number of detected objects for each detection.
	
	Returns
	----------
	number of maximal objects to be detected.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "i",
	    "name": "getMaxOutObjs",
	    "parametersSignature": "()",
	    "description": "Get the maximal number of detected objects for each detection.",
	    "parameters": [],
	    "returnDescription": "number of maximal objects to be detected."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "getMaxOutObjs", [])

def getSize() -> int:
	"""
	Get number of objects in the current database.
	
	Returns
	----------
	number of objects in the current database.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "i",
	    "name": "getSize",
	    "parametersSignature": "()",
	    "description": "Get number of objects in the current database.",
	    "parameters": [],
	    "returnDescription": "number of objects in the current database."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "getSize", [])

def _removeObject(hash:str) -> None:
	"""
	Remove an obbject with a specific hash from the DB (Attention: All files related to this object will be deleted.)
	
	Parameters
	----------
	hash:str
		the hash (as a string) of the object to be deleted.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_removeObject",
	    "parametersSignature": "(s)",
	    "description": "Remove an obbject with a specific hash from the DB (Attention: All files related to this object will be deleted.)",
	    "parameters": [
	        {
	            "name": "hash",
	            "description": "the hash (as a string) of the object to be deleted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "_removeObject", [hash])

def detectFromFile(image:str) -> None:
	"""
	Load an image and search for known objects.
	
	Parameters
	----------
	image:str
		The image that will be searched for known objects.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "detectFromFile",
	    "parametersSignature": "(s)",
	    "description": "Load an image and search for known objects.",
	    "parameters": [
	        {
	            "name": "image",
	            "description": "The image that will be searched for known objects."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "detectFromFile", [image])

def getDefaultDatabaseDirectory() -> str:
	"""
	Return the default directory used for databases storage.
	
	Returns
	----------
	Default directory used for databases storage.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "s",
	    "name": "getDefaultDatabaseDirectory",
	    "parametersSignature": "()",
	    "description": "Return the default directory used for databases storage.",
	    "parameters": [],
	    "returnDescription": "Default directory used for databases storage."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "getDefaultDatabaseDirectory", [])

def getDefaultDatabaseName() -> str:
	"""
	Return the default database name.
	
	Returns
	----------
	Default database name.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "s",
	    "name": "getDefaultDatabaseName",
	    "parametersSignature": "()",
	    "description": "Return the default database name.",
	    "parameters": [],
	    "returnDescription": "Default database name."
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "getDefaultDatabaseName", [])

def sendDatabase(name:str, file:object) -> None:
	"""
	Upload a zipped database to the robot.
	
	Parameters
	----------
	name:str
		Database name.
	file:object
		Archive (ZIP) containing the database file.
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "sendDatabase",
	    "parametersSignature": "(so)",
	    "description": "Upload a zipped database to the robot.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Database name."
	        },
	        {
	            "name": "file",
	            "description": "Archive (ZIP) containing the database file."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVisionRecognition", "sendDatabase", [name, file])

