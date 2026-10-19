"""
The ALAudioDevice module allows other modules to access to the sound data of the nao's microphones, and to send sound toward its loudspeakers  The way to receive or send the audio data depends whether the modules are local (dynamic library) or remote (executable).
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

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
	return call_method("ALAudioDevice", "version", [])

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
	return call_method("ALAudioDevice", "ping", [])

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
	return call_method("ALAudioDevice", "getMethodList", [])

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
	return call_method("ALAudioDevice", "getMethodHelp", [methodName])

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
	return call_method("ALAudioDevice", "getModuleHelp", [])

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
	return call_method("ALAudioDevice", "getBrokerName", [])

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
	return call_method("ALAudioDevice", "getUsage", [name])

def subscribe(pModule:str) -> None:
	"""
	This function allows a module to subscribe to the ALAudioDevice module.For more informations see the audio part of the red documentation
	
	Parameters
	----------
	pModule:str
		Name of the module
	
	Bridge notes
	------------
	NAOqi calls back the module named in the arguments, so that module must run on the robot. A module on the PC can't be called back, since the bridge only carries calls from the PC to the robot.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(s)",
	#     "description": "This function allows a module to subscribe to the ALAudioDevice module.For more informations see the audio part of the red documentation",
	#     "parameters": [
	#         {
	#             "name": "pModule",
	#             "description": "Name of the module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "subscribe", [pModule])

def unsubscribe(pModule:str) -> None:
	"""
	This function allows a module to subscribe to the ALAudioDevice module.For more informations see the audio part of the red documentation
	
	Parameters
	----------
	pModule:str
		Name of the module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "This function allows a module to subscribe to the ALAudioDevice module.For more informations see the audio part of the red documentation",
	#     "parameters": [
	#         {
	#             "name": "pModule",
	#             "description": "Name of the module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "unsubscribe", [pModule])

def sendLocalBufferToOutput(nbOfFrames:int, pBuffer:int) -> bool:
	"""
	This function allows a local module to send sound onto the nao's loudpseakers
	You must pass to this function a pointer to the stereo buffer to send, and the number of frames per channel. The buffer must contain 16bits stereo interleaved samples, and the number of frames does not exceed 16384
	
	Parameters
	----------
	nbOfFrames:int
		Number of 16 bits samples per channel to send.
	pBuffer:int
		Buffer to send
	
	Returns
	----------
	True if the operation is successfull - False otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "sendLocalBufferToOutput",
	#     "parametersSignature": "(ii)",
	#     "description": "This function allows a local module to send sound onto the nao's loudpseakers\nYou must pass to this function a pointer to the stereo buffer to send, and the number of frames per channel. The buffer must contain 16bits stereo interleaved samples, and the number of frames does not exceed 16384",
	#     "parameters": [
	#         {
	#             "name": "nbOfFrames",
	#             "description": "Number of 16 bits samples per channel to send."
	#         },
	#         {
	#             "name": "pBuffer",
	#             "description": "Buffer to send"
	#         }
	#     ],
	#     "returnDescription": "True if the operation is successfull - False otherwise"
	# }
	return call_method("ALAudioDevice", "sendLocalBufferToOutput", [nbOfFrames, pBuffer])

def sendRemoteBufferToOutput(nbOfFrames:int, pBuffer:Any) -> bool:
	"""
	This function allows a remote module to send sound onto the nao's loudpseakers
	You must pass to this function the stereo buffer you want to send as an ALValue converted to binary, and the number of frames per channel. The number of frames does not exceed 16384. For more information please see the red documentation
	
	Parameters
	----------
	nbOfFrames:int
		Number of 16 bits samples per channel to send.
	pBuffer:Any
		Buffer to send
	
	Returns
	----------
	True if the operation is successfull - False otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "sendRemoteBufferToOutput",
	#     "parametersSignature": "(im)",
	#     "description": "This function allows a remote module to send sound onto the nao's loudpseakers\nYou must pass to this function the stereo buffer you want to send as an ALValue converted to binary, and the number of frames per channel. The number of frames does not exceed 16384. For more information please see the red documentation",
	#     "parameters": [
	#         {
	#             "name": "nbOfFrames",
	#             "description": "Number of 16 bits samples per channel to send."
	#         },
	#         {
	#             "name": "pBuffer",
	#             "description": "Buffer to send"
	#         }
	#     ],
	#     "returnDescription": "True if the operation is successfull - False otherwise"
	# }
	return call_method("ALAudioDevice", "sendRemoteBufferToOutput", [nbOfFrames, pBuffer])

def setFileAsInput(pFileName:str) -> None:
	"""
	This method allows to send sound samples contained in a sound file at the input of ALAudioDevice, instead of the nao's microphones sound data. The sound file must be a .wav file containing 16bits / 4 channels / interleaved samples. Once the file has been read, microphones sound data will again taken as input
	
	Parameters
	----------
	pFileName:str
		Name of the input file.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "setFileAsInput",
	#     "parametersSignature": "(s)",
	#     "description": "This method allows to send sound samples contained in a sound file at the input of ALAudioDevice, instead of the nao's microphones sound data. The sound file must be a .wav file containing 16bits / 4 channels / interleaved samples. Once the file has been read, microphones sound data will again taken as input",
	#     "parameters": [
	#         {
	#             "name": "pFileName",
	#             "description": "Name of the input file."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "setFileAsInput", [pFileName])

def setParameter(pParamName:str, pParamValue:int) -> None:
	"""
	This method sets the specified internal parameter ('outputSampleRate' or 'inputBufferSize')
	inputBufferSize can bet set to 8192 or 16384. Warning: when speech recognition is running, a buffer size of 8192 is used. Don't change it during the recognition process.
	outputSampleRate can bet set to 16000 Hz, 22050 Hz, 44100 Hz or 48000 Hz. Warning: if speech synthesis is running, a sample rate of 16000 Hz or 22050 Hz is used (depending of the language). Don't change it during the synthesis process
	
	Parameters
	----------
	pParamName:str
		Name of the parameter to set ('outputSampleRate' or 'inputBufferSize').
	pParamValue:int
		The value to which the specified parameter should be set.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(si)",
	#     "description": "This method sets the specified internal parameter ('outputSampleRate' or 'inputBufferSize')\ninputBufferSize can bet set to 8192 or 16384. Warning: when speech recognition is running, a buffer size of 8192 is used. Don't change it during the recognition process.\noutputSampleRate can bet set to 16000 Hz, 22050 Hz, 44100 Hz or 48000 Hz. Warning: if speech synthesis is running, a sample rate of 16000 Hz or 22050 Hz is used (depending of the language). Don't change it during the synthesis process",
	#     "parameters": [
	#         {
	#             "name": "pParamName",
	#             "description": "Name of the parameter to set ('outputSampleRate' or 'inputBufferSize')."
	#         },
	#         {
	#             "name": "pParamValue",
	#             "description": "The value to which the specified parameter should be set."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "setParameter", [pParamName, pParamValue])

def getParameter(pParamName:str) -> int:
	"""
	This method returns the specified internal parameter ('outputSampleRate' or 'inputBufferSize'). The value -1 is returned if the specified parameter is not valid.
	
	Parameters
	----------
	pParamName:str
		Name of the parameter to get ('outputSampleRate' or 'inputBufferSize').
	
	Returns
	----------
	value of the specified parameter
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "getParameter",
	#     "parametersSignature": "(s)",
	#     "description": "This method returns the specified internal parameter ('outputSampleRate' or 'inputBufferSize'). The value -1 is returned if the specified parameter is not valid.",
	#     "parameters": [
	#         {
	#             "name": "pParamName",
	#             "description": "Name of the parameter to get ('outputSampleRate' or 'inputBufferSize')."
	#         }
	#     ],
	#     "returnDescription": "value of the specified parameter"
	# }
	return call_method("ALAudioDevice", "getParameter", [pParamName])

def startMicrophonesRecording(pFileName:str) -> None:
	"""
	This method allows to record the signal collected on the nao's microphones. You can choose to record only the front microphone in a ogg file, or the 4 microphones in a wav file. In this last case the format of the file is 4 channels, 16 bits little endian, 48 KHz
	
	Parameters
	----------
	pFileName:str
		Name of the file where to record the sound.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "startMicrophonesRecording",
	#     "parametersSignature": "(s)",
	#     "description": "This method allows to record the signal collected on the nao's microphones. You can choose to record only the front microphone in a ogg file, or the 4 microphones in a wav file. In this last case the format of the file is 4 channels, 16 bits little endian, 48 KHz",
	#     "parameters": [
	#         {
	#             "name": "pFileName",
	#             "description": "Name of the file where to record the sound."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "startMicrophonesRecording", [pFileName])

def stopMicrophonesRecording() -> None:
	"""
	This method stops the recording of the sound collected by the microphones.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "stopMicrophonesRecording",
	#     "parametersSignature": "()",
	#     "description": "This method stops the recording of the sound collected by the microphones.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "stopMicrophonesRecording", [])

def setOutputVolume(volume:int) -> None:
	"""
	Sets the output sound level of the system.
	
	Parameters
	----------
	volume:int
		Volume [0-100].
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "setOutputVolume",
	#     "parametersSignature": "(i)",
	#     "description": "Sets the output sound level of the system.",
	#     "parameters": [
	#         {
	#             "name": "volume",
	#             "description": "Volume [0-100]."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "setOutputVolume", [volume])

def getOutputVolume() -> int:
	"""
	Gets the output sound level of the system.
	
	Returns
	----------
	outputVolume of the system
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "getOutputVolume",
	#     "parametersSignature": "()",
	#     "description": "Gets the output sound level of the system.",
	#     "parameters": [],
	#     "returnDescription": "outputVolume of the system"
	# }
	return call_method("ALAudioDevice", "getOutputVolume", [])

def openAudioInputs() -> None:
	"""
	Opens the audio device for capture. If you closed the audio inputs with the closeAudioInputs method, you must call this method to be able to access to the sound data of the nao's microphones. 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "openAudioInputs",
	#     "parametersSignature": "()",
	#     "description": "Opens the audio device for capture. If you closed the audio inputs with the closeAudioInputs method, you must call this method to be able to access to the sound data of the nao's microphones. ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "openAudioInputs", [])

def openAudioOutputs() -> None:
	"""
	Opens the audio device for playback. If you closed the audio outputs with the closeAudioOutputs method, you must call this method to ear or send sound onto the nao's loudspeakers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "openAudioOutputs",
	#     "parametersSignature": "()",
	#     "description": "Opens the audio device for playback. If you closed the audio outputs with the closeAudioOutputs method, you must call this method to ear or send sound onto the nao's loudspeakers.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "openAudioOutputs", [])

def closeAudioInputs() -> None:
	"""
	Closes the audio device for capture. You can call this method if you want to have access to the alsa input buffers in another program than naoqi while naoqi is running (with arecord for example)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "closeAudioInputs",
	#     "parametersSignature": "()",
	#     "description": "Closes the audio device for capture. You can call this method if you want to have access to the alsa input buffers in another program than naoqi while naoqi is running (with arecord for example)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "closeAudioInputs", [])

def closeAudioOutputs() -> None:
	"""
	Closes the audio device for playback. close the audio device for capture. You can call this method if you want to send sound to alsa in another program than naoqi while naoqi is running (with aplay for example)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "closeAudioOutputs",
	#     "parametersSignature": "()",
	#     "description": "Closes the audio device for playback. close the audio device for capture. You can call this method if you want to send sound to alsa in another program than naoqi while naoqi is running (with aplay for example)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "closeAudioOutputs", [])

def flushAudioOutputs() -> None:
	"""
	Flush the audio device for playback. close the audio device for capture. You can call this method if you want to send sound to alsa in another program than naoqi while naoqi is running (with aplay for example)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "flushAudioOutputs",
	#     "parametersSignature": "()",
	#     "description": "Flush the audio device for playback. close the audio device for capture. You can call this method if you want to send sound to alsa in another program than naoqi while naoqi is running (with aplay for example)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "flushAudioOutputs", [])

def isOutputClosed() -> bool:
	"""
	Allows to know if audio ouputs are closed or not
	
	Returns
	----------
	True if audio outputs are closed / False otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "isOutputClosed",
	#     "parametersSignature": "()",
	#     "description": "Allows to know if audio ouputs are closed or not",
	#     "parameters": [],
	#     "returnDescription": "True if audio outputs are closed / False otherwise"
	# }
	return call_method("ALAudioDevice", "isOutputClosed", [])

def isInputClosed() -> bool:
	"""
	Allows to know if audio inputs are closed or not
	
	Returns
	----------
	True if audio inputs are closed / False otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "isInputClosed",
	#     "parametersSignature": "()",
	#     "description": "Allows to know if audio inputs are closed or not",
	#     "parameters": [],
	#     "returnDescription": "True if audio inputs are closed / False otherwise"
	# }
	return call_method("ALAudioDevice", "isInputClosed", [])

def _listOutputs() -> Any:
	"""
	return the list of available outputs
	
	Returns
	----------
	A list of AudioDeviceInfo
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "m",
	#     "name": "_listOutputs",
	#     "parametersSignature": "()",
	#     "description": "return the list of available outputs",
	#     "parameters": [],
	#     "returnDescription": "A list of AudioDeviceInfo"
	# }
	return call_method("ALAudioDevice", "_listOutputs", [])

def _output(index:int) -> Any:
	"""
	return the output matching the index
	
	Parameters
	----------
	index:int
		The output index
	
	Returns
	----------
	An AudioDeviceInfo
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "m",
	#     "name": "_output",
	#     "parametersSignature": "(I)",
	#     "description": "return the output matching the index",
	#     "parameters": [
	#         {
	#             "name": "index",
	#             "description": "The output index"
	#         }
	#     ],
	#     "returnDescription": "An AudioDeviceInfo"
	# }
	return call_method("ALAudioDevice", "_output", [index])

def _defaultOutput() -> int:
	"""
	return the default output
	
	Returns
	----------
	The default output index
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "I",
	#     "name": "_defaultOutput",
	#     "parametersSignature": "()",
	#     "description": "return the default output",
	#     "parameters": [],
	#     "returnDescription": "The default output index"
	# }
	return call_method("ALAudioDevice", "_defaultOutput", [])

def _setDefaultOutput(index:int) -> None:
	"""
	set the default output
	
	Parameters
	----------
	index:int
		The output index
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "_setDefaultOutput",
	#     "parametersSignature": "(I)",
	#     "description": "set the default output",
	#     "parameters": [
	#         {
	#             "name": "index",
	#             "description": "The output index"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "_setDefaultOutput", [index])

def _listInputs() -> Any:
	"""
	return the list of available inputs
	
	Returns
	----------
	A list of AudioDeviceInfo
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "m",
	#     "name": "_listInputs",
	#     "parametersSignature": "()",
	#     "description": "return the list of available inputs",
	#     "parameters": [],
	#     "returnDescription": "A list of AudioDeviceInfo"
	# }
	return call_method("ALAudioDevice", "_listInputs", [])

def _input(index:int) -> Any:
	"""
	return the input matching the index
	
	Parameters
	----------
	index:int
		The input index
	
	Returns
	----------
	An AudioDeviceInfo
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "m",
	#     "name": "_input",
	#     "parametersSignature": "(I)",
	#     "description": "return the input matching the index",
	#     "parameters": [
	#         {
	#             "name": "index",
	#             "description": "The input index"
	#         }
	#     ],
	#     "returnDescription": "An AudioDeviceInfo"
	# }
	return call_method("ALAudioDevice", "_input", [index])

def _defaultInput() -> int:
	"""
	return the default input
	
	Returns
	----------
	The default input index
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "I",
	#     "name": "_defaultInput",
	#     "parametersSignature": "()",
	#     "description": "return the default input",
	#     "parameters": [],
	#     "returnDescription": "The default input index"
	# }
	return call_method("ALAudioDevice", "_defaultInput", [])

def _setDefaultInput(index:int) -> None:
	"""
	set the default input
	
	Parameters
	----------
	index:int
		The input index
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_setDefaultInput",
	#     "parametersSignature": "(I)",
	#     "description": "set the default input",
	#     "parameters": [
	#         {
	#             "name": "index",
	#             "description": "The input index"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "_setDefaultInput", [index])

def playSine(frequence:int, gain:int, pan:int, duration:float) -> None:
	"""
	Play a sine wave which specified caracteristics.
	
	Parameters
	----------
	frequence:int
		Frequence in Hertz
	gain:int
		Volume Gain between 0 and 100
	pan:int
		Stereo Pan set to either {-1,0,+1}
	duration:float
		Duration of the sine wave in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "playSine",
	#     "parametersSignature": "(iiif)",
	#     "description": "Play a sine wave which specified caracteristics.",
	#     "parameters": [
	#         {
	#             "name": "frequence",
	#             "description": "Frequence in Hertz"
	#         },
	#         {
	#             "name": "gain",
	#             "description": "Volume Gain between 0 and 100"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "Stereo Pan set to either {-1,0,+1}"
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Duration of the sine wave in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "playSine", [frequence, gain, pan, duration])

def enableEnergyComputation() -> None:
	"""
	Enables the computation of the energy of each microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "enableEnergyComputation",
	#     "parametersSignature": "()",
	#     "description": "Enables the computation of the energy of each microphone signal",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "enableEnergyComputation", [])

def disableEnergyComputation() -> None:
	"""
	Disables the computation of the energy of each microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "disableEnergyComputation",
	#     "parametersSignature": "()",
	#     "description": "Disables the computation of the energy of each microphone signal",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "disableEnergyComputation", [])

def getLeftMicEnergy() -> float:
	"""
	Returns the energy of the left microphone signal
	
	Returns
	----------
	energy of the left microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "f",
	#     "name": "getLeftMicEnergy",
	#     "parametersSignature": "()",
	#     "description": "Returns the energy of the left microphone signal",
	#     "parameters": [],
	#     "returnDescription": "energy of the left microphone signal"
	# }
	return call_method("ALAudioDevice", "getLeftMicEnergy", [])

def getRightMicEnergy() -> float:
	"""
	Returns the energy of the right microphone signal
	
	Returns
	----------
	energy of the right microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "f",
	#     "name": "getRightMicEnergy",
	#     "parametersSignature": "()",
	#     "description": "Returns the energy of the right microphone signal",
	#     "parameters": [],
	#     "returnDescription": "energy of the right microphone signal"
	# }
	return call_method("ALAudioDevice", "getRightMicEnergy", [])

def getFrontMicEnergy() -> float:
	"""
	Returns the energy of the front microphone signal
	
	Returns
	----------
	energy of the front microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "f",
	#     "name": "getFrontMicEnergy",
	#     "parametersSignature": "()",
	#     "description": "Returns the energy of the front microphone signal",
	#     "parameters": [],
	#     "returnDescription": "energy of the front microphone signal"
	# }
	return call_method("ALAudioDevice", "getFrontMicEnergy", [])

def getRearMicEnergy() -> float:
	"""
	Returns the energy of the rear microphone signal
	
	Returns
	----------
	energy of the rear microphone signal
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "f",
	#     "name": "getRearMicEnergy",
	#     "parametersSignature": "()",
	#     "description": "Returns the energy of the rear microphone signal",
	#     "parameters": [],
	#     "returnDescription": "energy of the rear microphone signal"
	# }
	return call_method("ALAudioDevice", "getRearMicEnergy", [])

def _setInputVolume(volume:int) -> None:
	"""
	Sets the input level of Nao's microphones.
	
	Parameters
	----------
	volume:int
		Volume [0-100].
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "_setInputVolume",
	#     "parametersSignature": "(i)",
	#     "description": "Sets the input level of Nao's microphones.",
	#     "parameters": [
	#         {
	#             "name": "volume",
	#             "description": "Volume [0-100]."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "_setInputVolume", [volume])

def setClientPreferences(name:str, sampleRate:int, channelsConfiguration:int, deinterleaved:int) -> None:
	"""
	Set AudioDevice Client preferences
	
	Parameters
	----------
	name:str
		name of the client
	sampleRate:int
		sample rate of the microphones data sent to the process function - must be 16000 or 48000
	channelsConfiguration:int
		An int (defined in ALSoundExtractor) indicating which microphones data will be send to the process function. ALLCHANNELS, LEFTCHANNEL, RIGHTCHANNEL, FRONTCHANNEL, REARCHANNEL are the configuration currently supported.
	deinterleaved:int
		indicates if the microphones data sent to the process function are interleaved or not - 0 : interleaved - 1 : deinterleaved 
	
	Bridge notes
	------------
	NAOqi calls back the module named in the arguments, so that module must run on the robot. A module on the PC can't be called back, since the bridge only carries calls from the PC to the robot.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "setClientPreferences",
	#     "parametersSignature": "(siii)",
	#     "description": "Set AudioDevice Client preferences",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of the client"
	#         },
	#         {
	#             "name": "sampleRate",
	#             "description": "sample rate of the microphones data sent to the process function - must be 16000 or 48000"
	#         },
	#         {
	#             "name": "channelsConfiguration",
	#             "description": "An int (defined in ALSoundExtractor) indicating which microphones data will be send to the process function. ALLCHANNELS, LEFTCHANNEL, RIGHTCHANNEL, FRONTCHANNEL, REARCHANNEL are the configuration currently supported."
	#         },
	#         {
	#             "name": "deinterleaved",
	#             "description": "indicates if the microphones data sent to the process function are interleaved or not - 0 : interleaved - 1 : deinterleaved "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "setClientPreferences", [name, sampleRate, channelsConfiguration, deinterleaved])

def muteAudioOut(p0:bool) -> None:
	"""
	mute the loudspeakers
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "muteAudioOut",
	#     "parametersSignature": "(b)",
	#     "description": "mute the loudspeakers",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "muteAudioOut", [p0])

def _muteAudioIn(p0:bool) -> None:
	"""
	mute the microphones
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "_muteAudioIn",
	#     "parametersSignature": "(b)",
	#     "description": "mute the microphones",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "_muteAudioIn", [p0])

def isAudioOutMuted() -> bool:
	"""
	check if loudspeakers are muted
	
	Returns
	----------
	1 if true / 0 otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "b",
	#     "name": "isAudioOutMuted",
	#     "parametersSignature": "()",
	#     "description": "check if loudspeakers are muted",
	#     "parameters": [],
	#     "returnDescription": "1 if true / 0 otherwise"
	# }
	return call_method("ALAudioDevice", "isAudioOutMuted", [])

def _getNbOfMicrophones() -> int:
	"""
	get the number of microphones
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "i",
	#     "name": "_getNbOfMicrophones",
	#     "parametersSignature": "()",
	#     "description": "get the number of microphones",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioDevice", "_getNbOfMicrophones", [])

class _Signals:
	speakersPlaying: Signal[[bool]] = Signal("ALAudioDevice", "speakersPlaying")
	"""
	Bridge notes
	------------
	A signal sent by ALAudioDevice on the robot.
	
	subscribe(callback) calls callback(bool) each time the robot sends it.
	"""
signals = _Signals()

