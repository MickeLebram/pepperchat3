"""
This module records NAO's microphones signals into sound files.
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
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
	return call_method("ALAudioRecorder", "version", [])

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
	return call_method("ALAudioRecorder", "ping", [])

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
	return call_method("ALAudioRecorder", "getMethodList", [])

def getMethodHelp(methodName:str) -> Any:
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
	return call_method("ALAudioRecorder", "getMethodHelp", [methodName])

def getModuleHelp() -> Any:
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
	return call_method("ALAudioRecorder", "getModuleHelp", [])

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
	return call_method("ALAudioRecorder", "getBrokerName", [])

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
	return call_method("ALAudioRecorder", "getUsage", [name])

def startMicrophonesRecording(filename:str, type:str, samplerate:int, channels:Any) -> None:
	"""
	This method allows to record the signal collected on the nao's microphones. You can choose to record only the front microphone in a ogg file, or the 4 microphones in a wav file.
	
	Parameters
	----------
	filename:str
		Name of the file where to record the sound.
	type:str
		wav or ogg.
	samplerate:int
		Required sample rate.
	channels:Any
		vector of booleans.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startMicrophonesRecording",
	#     "parametersSignature": "(ssim)",
	#     "description": "This method allows to record the signal collected on the nao's microphones. You can choose to record only the front microphone in a ogg file, or the 4 microphones in a wav file.",
	#     "parameters": [
	#         {
	#             "name": "filename",
	#             "description": "Name of the file where to record the sound."
	#         },
	#         {
	#             "name": "type",
	#             "description": "wav or ogg."
	#         },
	#         {
	#             "name": "samplerate",
	#             "description": "Required sample rate."
	#         },
	#         {
	#             "name": "channels",
	#             "description": "vector of booleans."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioRecorder", "startMicrophonesRecording", [filename, type, samplerate, channels])

def stopMicrophonesRecording() -> None:
	"""
	This method stops the recording of the sound collected by the microphones.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "stopMicrophonesRecording",
	#     "parametersSignature": "()",
	#     "description": "This method stops the recording of the sound collected by the microphones.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioRecorder", "stopMicrophonesRecording", [])

def _isRecordingThisFile(fileName:str) -> bool:
	"""
	This function allows you to know if ALAudioDevice is currently recording the file you give in argument
	
	Parameters
	----------
	fileName:str
		file name of the file you want to test
	
	Returns
	----------
	1 if the file is currently beeing recording / 0 otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "_isRecordingThisFile",
	#     "parametersSignature": "(s)",
	#     "description": "This function allows you to know if ALAudioDevice is currently recording the file you give in argument",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "file name of the file you want to test"
	#         }
	#     ],
	#     "returnDescription": "1 if the file is currently beeing recording / 0 otherwise"
	# }
	return call_method("ALAudioRecorder", "_isRecordingThisFile", [fileName])

