from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALMotionRecorder is a very specific module for real-time motion recording in Choregraphe. Users can get a simpler interface for motion recording by using the Animation Mode. ALMotionRecorder also supports recording modes using bumpers or torso button, and selective motion replay.
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
	return send_mfc("ALMotionRecorder", "version", [])

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
	return send_mfc("ALMotionRecorder", "ping", [])

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
	return send_mfc("ALMotionRecorder", "getMethodList", [])

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
	return send_mfc("ALMotionRecorder", "getMethodHelp", [methodName])

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
	return send_mfc("ALMotionRecorder", "getModuleHelp", [])

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
	return send_mfc("ALMotionRecorder", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALMotionRecorder", "wait", [id])

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
	return send_mfc("ALMotionRecorder", "isRunning", [id])

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
	return send_mfc("ALMotionRecorder", "stop", [id])

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
	return send_mfc("ALMotionRecorder", "getBrokerName", [])

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
	return send_mfc("ALMotionRecorder", "getUsage", [name])

def startInteractiveRecording(jointsToRecord:List[str], nbPoses:int, extensionAllowed:bool, mode:int) -> None:
	"""
	Start recording the motion in an interactive mode
	
	Parameters
	----------
	jointsToRecord:List[str]
		Names of joints that must be recorded
	nbPoses:int
		Default number of poses to record
	extensionAllowed:bool
		Set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped
	mode:int
		Indicates which interactive mode must be used. 1 : Use right bumper to enslave and left bumper to store the pose  (deprecated); 2 : Use head tap to store the pose
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "startInteractiveRecording",
	    "parametersSignature": "([s]ibi)",
	    "description": "Start recording the motion in an interactive mode",
	    "parameters": [
	        {
	            "name": "jointsToRecord",
	            "description": "Names of joints that must be recorded"
	        },
	        {
	            "name": "nbPoses",
	            "description": "Default number of poses to record"
	        },
	        {
	            "name": "extensionAllowed",
	            "description": "Set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped"
	        },
	        {
	            "name": "mode",
	            "description": "Indicates which interactive mode must be used. 1 : Use right bumper to enslave and left bumper to store the pose  (deprecated); 2 : Use head tap to store the pose"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotionRecorder", "startInteractiveRecording", [jointsToRecord, nbPoses, extensionAllowed, mode])

def startPeriodicRecording(jointsToRecord:List[str], nbPoses:int, extensionAllowed:bool, timeStep:float, jointsToReplay:List[str], replayData:object) -> None:
	"""
	Start recording the motion in a periodic mode
	
	Parameters
	----------
	jointsToRecord:List[str]
		Names of joints that must be recorded
	nbPoses:int
		Default number of poses to record
	extensionAllowed:bool
		set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped
	timeStep:float
		Time in seconds to wait between two poses
	jointsToReplay:List[str]
		Names of joints that must be replayed
	replayData:object
		An ALValue holding data for replayed joints. It holds two ALValues. The first one is an ALValue where each line corresponds to a joint, and column elements are times of control points The second one is also an ALValue where each line corresponds to a joint, but column elements are arrays containing [float angle, Handle1, Handle2] elements, where Handle is [int InterpolationType, float dAngle, float dTime] describing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceding the point, the second describes the curve following the point.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "startPeriodicRecording",
	    "parametersSignature": "([s]ibf[s]m)",
	    "description": "Start recording the motion in a periodic mode",
	    "parameters": [
	        {
	            "name": "jointsToRecord",
	            "description": "Names of joints that must be recorded"
	        },
	        {
	            "name": "nbPoses",
	            "description": "Default number of poses to record"
	        },
	        {
	            "name": "extensionAllowed",
	            "description": "set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped"
	        },
	        {
	            "name": "timeStep",
	            "description": "Time in seconds to wait between two poses"
	        },
	        {
	            "name": "jointsToReplay",
	            "description": "Names of joints that must be replayed"
	        },
	        {
	            "name": "replayData",
	            "description": "An ALValue holding data for replayed joints. It holds two ALValues. The first one is an ALValue where each line corresponds to a joint, and column elements are times of control points The second one is also an ALValue where each line corresponds to a joint, but column elements are arrays containing [float angle, Handle1, Handle2] elements, where Handle is [int InterpolationType, float dAngle, float dTime] describing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceding the point, the second describes the curve following the point."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotionRecorder", "startPeriodicRecording", [jointsToRecord, nbPoses, extensionAllowed, timeStep, jointsToReplay, replayData])

def stopAndGetRecording() -> object:
	"""
	Stop recording the motion and return data
	
	Returns
	----------
	Returns the recorded data as an ALValue: [[JointName1,[pos1, pos2, ...]], [JointName2,[pos1, pos2, ...]], ...]
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "stopAndGetRecording",
	    "parametersSignature": "()",
	    "description": "Stop recording the motion and return data",
	    "parameters": [],
	    "returnDescription": "Returns the recorded data as an ALValue: [[JointName1,[pos1, pos2, ...]], [JointName2,[pos1, pos2, ...]], ...]"
	}
	'''
	"""
	return send_mfc("ALMotionRecorder", "stopAndGetRecording", [])

def dataChanged(dataName:str, data:object, message:str) -> None:
	"""
	Called by ALMemory when subcription data is updated. INTERNAL
	
	Parameters
	----------
	dataName:str
		Name of the subscribed data.
	data:object
		Value of the the subscribed data
	message:str
		The message give when subscribing.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "dataChanged",
	    "parametersSignature": "(sms)",
	    "description": "Called by ALMemory when subcription data is updated. INTERNAL",
	    "parameters": [
	        {
	            "name": "dataName",
	            "description": "Name of the subscribed data."
	        },
	        {
	            "name": "data",
	            "description": "Value of the the subscribed data"
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
	return send_mfc("ALMotionRecorder", "dataChanged", [dataName, data, message])

