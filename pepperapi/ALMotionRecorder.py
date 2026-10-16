"""
ALMotionRecorder is a very specific module for real-time motion recording in Choregraphe. Users can get a simpler interface for motion recording by using the Animation Mode. ALMotionRecorder also supports recording modes using bumpers or torso button, and selective motion replay.
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
	return call_method("ALMotionRecorder", "version", [])

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
	return call_method("ALMotionRecorder", "ping", [])

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
	return call_method("ALMotionRecorder", "getMethodList", [])

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
	return call_method("ALMotionRecorder", "getMethodHelp", [methodName])

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
	return call_method("ALMotionRecorder", "getModuleHelp", [])

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
	return call_method("ALMotionRecorder", "getBrokerName", [])

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
	return call_method("ALMotionRecorder", "getUsage", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startInteractiveRecording",
	#     "parametersSignature": "([s]ibi)",
	#     "description": "Start recording the motion in an interactive mode",
	#     "parameters": [
	#         {
	#             "name": "jointsToRecord",
	#             "description": "Names of joints that must be recorded"
	#         },
	#         {
	#             "name": "nbPoses",
	#             "description": "Default number of poses to record"
	#         },
	#         {
	#             "name": "extensionAllowed",
	#             "description": "Set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped"
	#         },
	#         {
	#             "name": "mode",
	#             "description": "Indicates which interactive mode must be used. 1 : Use right bumper to enslave and left bumper to store the pose  (deprecated); 2 : Use head tap to store the pose"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMotionRecorder", "startInteractiveRecording", [jointsToRecord, nbPoses, extensionAllowed, mode])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "startPeriodicRecording",
	#     "parametersSignature": "([s]ibf[s]m)",
	#     "description": "Start recording the motion in a periodic mode",
	#     "parameters": [
	#         {
	#             "name": "jointsToRecord",
	#             "description": "Names of joints that must be recorded"
	#         },
	#         {
	#             "name": "nbPoses",
	#             "description": "Default number of poses to record"
	#         },
	#         {
	#             "name": "extensionAllowed",
	#             "description": "set to true to ignore nbPoses and keep recording new poses as long as record is not manually stopped"
	#         },
	#         {
	#             "name": "timeStep",
	#             "description": "Time in seconds to wait between two poses"
	#         },
	#         {
	#             "name": "jointsToReplay",
	#             "description": "Names of joints that must be replayed"
	#         },
	#         {
	#             "name": "replayData",
	#             "description": "An ALValue holding data for replayed joints. It holds two ALValues. The first one is an ALValue where each line corresponds to a joint, and column elements are times of control points The second one is also an ALValue where each line corresponds to a joint, but column elements are arrays containing [float angle, Handle1, Handle2] elements, where Handle is [int InterpolationType, float dAngle, float dTime] describing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceding the point, the second describes the curve following the point."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMotionRecorder", "startPeriodicRecording", [jointsToRecord, nbPoses, extensionAllowed, timeStep, jointsToReplay, replayData])

def stopAndGetRecording() -> object:
	"""
	Stop recording the motion and return data
	
	Returns
	----------
	Returns the recorded data as an ALValue: [[JointName1,[pos1, pos2, ...]], [JointName2,[pos1, pos2, ...]], ...]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "stopAndGetRecording",
	#     "parametersSignature": "()",
	#     "description": "Stop recording the motion and return data",
	#     "parameters": [],
	#     "returnDescription": "Returns the recorded data as an ALValue: [[JointName1,[pos1, pos2, ...]], [JointName2,[pos1, pos2, ...]], ...]"
	# }
	return call_method("ALMotionRecorder", "stopAndGetRecording", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "dataChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "Called by ALMemory when subcription data is updated. INTERNAL",
	#     "parameters": [
	#         {
	#             "name": "dataName",
	#             "description": "Name of the subscribed data."
	#         },
	#         {
	#             "name": "data",
	#             "description": "Value of the the subscribed data"
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message give when subscribing."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALMotionRecorder", "dataChanged", [dataName, data, message])

