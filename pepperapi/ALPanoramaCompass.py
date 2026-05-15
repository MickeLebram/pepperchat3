from .gentypes import *
from .robot_client import send_mfc
import json
"""

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
	return send_mfc("ALPanoramaCompass", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALPanoramaCompass", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALPanoramaCompass", "metaObject", [p0])

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
	return send_mfc("ALPanoramaCompass", "terminate", [p0])

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
	return send_mfc("ALPanoramaCompass", "property", [p0])

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
	return send_mfc("ALPanoramaCompass", "setProperty", [p0, p1])

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
	return send_mfc("ALPanoramaCompass", "properties", [])

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
	return send_mfc("ALPanoramaCompass", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALPanoramaCompass", "isStatsEnabled", [])

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
	return send_mfc("ALPanoramaCompass", "enableStats", [p0])

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
	return send_mfc("ALPanoramaCompass", "stats", [])

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
	return send_mfc("ALPanoramaCompass", "clearStats", [])

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
	return send_mfc("ALPanoramaCompass", "isTraceEnabled", [])

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
	return send_mfc("ALPanoramaCompass", "enableTrace", [p0])

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
	return send_mfc("ALPanoramaCompass", "version", [])

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
	return send_mfc("ALPanoramaCompass", "ping", [])

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
	return send_mfc("ALPanoramaCompass", "getMethodList", [])

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
	return send_mfc("ALPanoramaCompass", "getMethodHelp", [methodName])

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
	return send_mfc("ALPanoramaCompass", "getModuleHelp", [])

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
	return send_mfc("ALPanoramaCompass", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALPanoramaCompass", "wait", [id])

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
	return send_mfc("ALPanoramaCompass", "isRunning", [id])

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
	return send_mfc("ALPanoramaCompass", "stop", [id])

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
	return send_mfc("ALPanoramaCompass", "getBrokerName", [])

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
	return send_mfc("ALPanoramaCompass", "getUsage", [name])

def setupPanorama() -> int:
	"""
	Shoot a panorama at the current position.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "i",
	    "name": "setupPanorama",
	    "parametersSignature": "()",
	    "description": "Shoot a panorama at the current position.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "setupPanorama", [])

def isDataAvailable() -> bool:
	"""
	Returns true if there is some panorama data
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "isDataAvailable",
	    "parametersSignature": "()",
	    "description": "Returns true if there is some panorama data",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "isDataAvailable", [])

def getCurrentPosition() -> object:
	"""
	Return the current orientation of the robot in the current panorama.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "getCurrentPosition",
	    "parametersSignature": "()",
	    "description": "Return the current orientation of the robot in the current panorama.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "getCurrentPosition", [])

def localizeNoHint() -> List[float]:
	"""
	Localize the robot using the scan,without hint.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "[f]",
	    "name": "localizeNoHint",
	    "parametersSignature": "()",
	    "description": "Localize the robot using the scan,without hint.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "localizeNoHint", [])

def localize_1() -> List[float]:
	"""
	Note: This is one of the overloads of the original method (localize)
	
	*Parsing issues:*
		*Mismatch between 'parameters' and 'parametersSignature'*
		
	Localize the robot using the scan.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "[f]",
	    "name": "localize",
	    "parametersSignature": "()",
	    "description": "Localize the robot using the scan.",
	    "parameters": [
	        {
	            "name": "pMode",
	            "description": "Localization mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "localize", [])

def localize_2(pMode:bool) -> List[float]:
	"""
	Note: This is one of the overloads of the original method (localize)
	
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:bool
		Localization mode
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "[f]",
	    "name": "localize",
	    "parametersSignature": "(b)",
	    "description": "Localize the robot using the scan.",
	    "parameters": [
	        {
	            "name": "pMode",
	            "description": "Localization mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "localize", [pMode])

def localize_3(pMode:int) -> List[float]:
	"""
	Note: This is one of the overloads of the original method (localize)
	
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "[f]",
	    "name": "localize",
	    "parametersSignature": "(i)",
	    "description": "Localize the robot using the scan.",
	    "parameters": [
	        {
	            "name": "pMode",
	            "description": "Localization mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "localize", [pMode])

def localize_4(pMode:int, p1:bool) -> List[float]:
	"""
	Note: This is one of the overloads of the original method (localize)
	
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	p1:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[f]",
	    "name": "localize",
	    "parametersSignature": "(ib)",
	    "description": "Localize the robot using the scan.",
	    "parameters": [
	        {
	            "name": "pMode",
	            "description": "Localization mode"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "localize", [pMode, p1])

def isInPanorama_1() -> int:
	"""
	Note: This is one of the overloads of the original method (isInPanorama)
	
	Check if the robot is in the current Panorama.
	
	Returns
	----------
	Error status.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "isInPanorama",
	    "parametersSignature": "()",
	    "description": "Check if the robot is in the current Panorama.",
	    "parameters": [],
	    "returnDescription": "Error status."
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "isInPanorama", [])

def isRelocalizationRequired() -> bool:
	"""
	Is a relocalization movement required.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "b",
	    "name": "isRelocalizationRequired",
	    "parametersSignature": "()",
	    "description": "Is a relocalization movement required.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "isRelocalizationRequired", [])

def loadPanorama(id:int) -> int:
	"""
	Load the panorama corresponding to the input identity from the hard drive. It has to exist.
	
	Parameters
	----------
	id:int
		Identity of the requested Panorama.
	
	Returns
	----------
	Error status.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "i",
	    "name": "loadPanorama",
	    "parametersSignature": "(i)",
	    "description": "Load the panorama corresponding to the input identity from the hard drive. It has to exist.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Identity of the requested Panorama."
	        }
	    ],
	    "returnDescription": "Error status."
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "loadPanorama", [id])

def getCurrentPanoramaDescriptor() -> object:
	"""
	
	
	Returns
	----------
	Return an ALValue containing Panorama identity and contained Frames identity.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "m",
	    "name": "getCurrentPanoramaDescriptor",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": "Return an ALValue containing Panorama identity and contained Frames identity."
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "getCurrentPanoramaDescriptor", [])

def getFrame(id:int, p1:str) -> object:
	"""
	Return the Frame corresponding to the input identity. It have to be in the current Panorama
	
	Parameters
	----------
	id:int
		Identity of the resquested Frame.
	p1:str
		
	
	Returns
	----------
	ALValue containing the Frame image part.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "m",
	    "name": "getFrame",
	    "parametersSignature": "(is)",
	    "description": "Return the Frame corresponding to the input identity. It have to be in the current Panorama",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Identity of the resquested Frame."
	        }
	    ],
	    "returnDescription": "ALValue containing the Frame image part."
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "getFrame", [id, p1])

def isInPanorama_2(p0:int) -> int:
	"""
	Note: This is one of the overloads of the original method (isInPanorama)
	
	Check if the robot is in the current Panorama.
	
	Parameters
	----------
	p0:int
		
	
	Returns
	----------
	Error status.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "i",
	    "name": "isInPanorama",
	    "parametersSignature": "(i)",
	    "description": "Check if the robot is in the current Panorama.",
	    "parameters": [],
	    "returnDescription": "Error status."
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "isInPanorama", [p0])

def clearAllPanoramas_1() -> int:
	"""
	Note: This is one of the overloads of the original method (clearAllPanoramas)
	
	Delete all panorama files in the current working directory
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "i",
	    "name": "clearAllPanoramas",
	    "parametersSignature": "()",
	    "description": "Delete all panorama files in the current working directory",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "clearAllPanoramas", [])

def clearAllPanoramas_2(p0:bool) -> int:
	"""
	Note: This is one of the overloads of the original method (clearAllPanoramas)
	
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "i",
	    "name": "clearAllPanoramas",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "clearAllPanoramas", [p0])

def clearPanorama(pIdentity:int) -> int:
	"""
	Delete all files related to a given panorama in the current working directory
	
	Parameters
	----------
	pIdentity:int
		Panorama identity
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "i",
	    "name": "clearPanorama",
	    "parametersSignature": "(i)",
	    "description": "Delete all files related to a given panorama in the current working directory",
	    "parameters": [
	        {
	            "name": "pIdentity",
	            "description": "Panorama identity"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "clearPanorama", [pIdentity])

def _launchLocalization() -> List[float]:
	"""
	Forces the robot to localize using the scan.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "[f]",
	    "name": "_launchLocalization",
	    "parametersSignature": "()",
	    "description": "Forces the robot to localize using the scan.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPanoramaCompass", "_launchLocalization", [])

