"""
This module allows to play wav and mp3 files on NAO
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
	return call_method("ALAudioPlayer", "version", [])

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
	return call_method("ALAudioPlayer", "ping", [])

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
	return call_method("ALAudioPlayer", "getMethodList", [])

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
	return call_method("ALAudioPlayer", "getMethodHelp", [methodName])

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
	return call_method("ALAudioPlayer", "getModuleHelp", [])

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
	return call_method("ALAudioPlayer", "getBrokerName", [])

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
	return call_method("ALAudioPlayer", "getUsage", [name])

@overload
def playFile(fileName:str, /) -> None:
	"""
	Plays a wav or mp3 file
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	
	Bridge notes
	------------
	playFile has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "playFile",
	#     "parametersSignature": "(s)",
	#     "description": "Plays a wav or mp3 file",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Path of the sound file"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playFile(fileName:str, volume:float, pan:float, /) -> None:
	"""
	Plays a wav or mp3 file, with specific volume and audio balance
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)
	
	Bridge notes
	------------
	playFile has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "playFile",
	#     "parametersSignature": "(sff)",
	#     "description": "Plays a wav or mp3 file, with specific volume and audio balance",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Path of the sound file"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def playFile(*args, **kwargs):
	"""
	Bridge notes
	------------
	playFile has 2 variants on the robot:
	- playFile(fileName:str)
	- playFile(fileName:str, volume:float, pan:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.playFile has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "playFile", list(args))

@overload
def _playSoundSetFile(fileName:str, /) -> None:
	"""
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	
	Bridge notes
	------------
	_playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_playSoundSetFile",
	#     "parametersSignature": "(s)",
	#     "description": "Plays a file contained in one of the sound sets loaded",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def _playSoundSetFile(soundSetName:str, fileName:str, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	
	Bridge notes
	------------
	_playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_playSoundSetFile",
	#     "parametersSignature": "(ss)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "soundSetName",
	#             "description": "Name of the soundset"
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def _playSoundSetFile(fileName:str, position:float, volume:float, pan:float, loop:bool, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	position:float
		Position in second where the playing has to begin
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	loop:bool
		specify if the file must be played in loop
	
	Bridge notes
	------------
	_playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_playSoundSetFile",
	#     "parametersSignature": "(sfffb)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         },
	#         {
	#             "name": "loop",
	#             "description": "specify if the file must be played in loop"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def _playSoundSetFile(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	position:float
		Position in second where the playing has to begin
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	loop:bool
		specify if the file must be played in loop
	
	Bridge notes
	------------
	_playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_playSoundSetFile",
	#     "parametersSignature": "(ssfffb)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "soundSetName",
	#             "description": "Name of the soundset"
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         },
	#         {
	#             "name": "loop",
	#             "description": "specify if the file must be played in loop"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def _playSoundSetFile(*args, **kwargs):
	"""
	Bridge notes
	------------
	_playSoundSetFile has 4 variants on the robot:
	- _playSoundSetFile(fileName:str)
	- _playSoundSetFile(soundSetName:str, fileName:str)
	- _playSoundSetFile(fileName:str, position:float, volume:float, pan:float, loop:bool)
	- _playSoundSetFile(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer._playSoundSetFile has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "_playSoundSetFile", list(args))

@overload
def playSoundSetFile(fileName:str, /) -> None:
	"""
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	
	Bridge notes
	------------
	playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "playSoundSetFile",
	#     "parametersSignature": "(s)",
	#     "description": "Plays a file contained in one of the sound sets loaded",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playSoundSetFile(soundSetName:str, fileName:str, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	
	Bridge notes
	------------
	playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "playSoundSetFile",
	#     "parametersSignature": "(ss)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "soundSetName",
	#             "description": "Name of the soundset"
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playSoundSetFile(fileName:str, position:float, volume:float, pan:float, loop:bool, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	position:float
		Position in second where the playing has to begin
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	loop:bool
		specify if the file must be played in loop
	
	Bridge notes
	------------
	playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "playSoundSetFile",
	#     "parametersSignature": "(sfffb)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         },
	#         {
	#             "name": "loop",
	#             "description": "specify if the file must be played in loop"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playSoundSetFile(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool, /) -> None:
	"""
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	position:float
		Position in second where the playing has to begin
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	loop:bool
		specify if the file must be played in loop
	
	Bridge notes
	------------
	playSoundSetFile has 4 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "playSoundSetFile",
	#     "parametersSignature": "(ssfffb)",
	#     "description": "Plays a file contained in a given sound set",
	#     "parameters": [
	#         {
	#             "name": "soundSetName",
	#             "description": "Name of the soundset"
	#         },
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         },
	#         {
	#             "name": "loop",
	#             "description": "specify if the file must be played in loop"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def playSoundSetFile(*args, **kwargs):
	"""
	Bridge notes
	------------
	playSoundSetFile has 4 variants on the robot:
	- playSoundSetFile(fileName:str)
	- playSoundSetFile(soundSetName:str, fileName:str)
	- playSoundSetFile(fileName:str, position:float, volume:float, pan:float, loop:bool)
	- playSoundSetFile(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.playSoundSetFile has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "playSoundSetFile", list(args))

def _playSystemSoundSetFile(fileName:str) -> None:
	"""
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_playSystemSoundSetFile",
	#     "parametersSignature": "(s)",
	#     "description": "Plays a file contained in one of the sound sets loaded",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the file without extension"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_playSystemSoundSetFile", [fileName])

def _loadSoundSet(setName:str) -> None:
	"""
	Load a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_loadSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Load a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_loadSoundSet", [setName])

def loadSoundSet(setName:str) -> None:
	"""
	Load a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "loadSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Load a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "loadSoundSet", [setName])

def _unloadSoundSet(setName:str) -> None:
	"""
	Unload a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_unloadSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Unload a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_unloadSoundSet", [setName])

def unloadSoundSet(setName:str) -> None:
	"""
	Unload a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "unloadSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Unload a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "unloadSoundSet", [setName])

def _loadSystemSoundSet(setName:str) -> None:
	"""
	Load a system sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_loadSystemSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Load a system sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_loadSystemSoundSet", [setName])

def _setDefaultSystemSoundSet(setName:str) -> None:
	"""
	Sets the default soundset used for system sounds
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_setDefaultSystemSoundSet",
	#     "parametersSignature": "(s)",
	#     "description": "Sets the default soundset used for system sounds",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_setDefaultSystemSoundSet", [setName])

def _getSoundSetFileNames(setName:str) -> List[str]:
	"""
	Return the list of files contained in a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "[s]",
	#     "name": "_getSoundSetFileNames",
	#     "parametersSignature": "(s)",
	#     "description": "Return the list of files contained in a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getSoundSetFileNames", [setName])

def getSoundSetFileNames(setName:str) -> List[str]:
	"""
	Return the list of files contained in a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "[s]",
	#     "name": "getSoundSetFileNames",
	#     "parametersSignature": "(s)",
	#     "description": "Return the list of files contained in a sound set",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "getSoundSetFileNames", [setName])

def _getCurrentSystemSoundSet() -> str:
	"""
	Return the current sound set loaded
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "s",
	#     "name": "_getCurrentSystemSoundSet",
	#     "parametersSignature": "()",
	#     "description": "Return the current sound set loaded",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getCurrentSystemSoundSet", [])

def _getLoadedSoundSetsList() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "[s]",
	#     "name": "_getLoadedSoundSetsList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getLoadedSoundSetsList", [])

def getLoadedSoundSetsList() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "[s]",
	#     "name": "getLoadedSoundSetsList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "getLoadedSoundSetsList", [])

def _getInstalledSoundSetsList() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "[s]",
	#     "name": "_getInstalledSoundSetsList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getInstalledSoundSetsList", [])

def getInstalledSoundSetsList() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "[s]",
	#     "name": "getInstalledSoundSetsList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "getInstalledSoundSetsList", [])

def _isSoundSetInstalled(setName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "b",
	#     "name": "_isSoundSetInstalled",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_isSoundSetInstalled", [setName])

def isSoundSetInstalled(setName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "isSoundSetInstalled",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "isSoundSetInstalled", [setName])

def _isSoundSetFileInstalled(setName:str, soundName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	soundName:str
		name of the sound
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "_isSoundSetFileInstalled",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         },
	#         {
	#             "name": "soundName",
	#             "description": "name of the sound"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_isSoundSetFileInstalled", [setName, soundName])

def isSoundSetFileInstalled(setName:str, soundName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	soundName:str
		name of the sound
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "b",
	#     "name": "isSoundSetFileInstalled",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "setName",
	#             "description": "name of the set"
	#         },
	#         {
	#             "name": "soundName",
	#             "description": "name of the sound"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "isSoundSetFileInstalled", [setName, soundName])

def _getSystemSoundSetFileDuration(soundName:str) -> float:
	"""
	
	
	Parameters
	----------
	soundName:str
		name of the sound
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "f",
	#     "name": "_getSystemSoundSetFileDuration",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "soundName",
	#             "description": "name of the sound"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getSystemSoundSetFileDuration", [soundName])

def _getSystemSoundSetFilePath(soundName:str) -> str:
	"""
	
	
	Parameters
	----------
	soundName:str
		name of the sound
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "s",
	#     "name": "_getSystemSoundSetFilePath",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "soundName",
	#             "description": "name of the sound"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_getSystemSoundSetFilePath", [soundName])

@overload
def playFileInLoop(fileName:str, /) -> None:
	"""
	Plays a wav or mp3 file in loop
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	
	Bridge notes
	------------
	playFileInLoop has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "playFileInLoop",
	#     "parametersSignature": "(s)",
	#     "description": "Plays a wav or mp3 file in loop",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Path of the sound file"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playFileInLoop(fileName:str, volume:float, pan:float, /) -> None:
	"""
	Plays a wav or mp3 file in loop, with specific volume and audio balance
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	Bridge notes
	------------
	playFileInLoop has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "playFileInLoop",
	#     "parametersSignature": "(sff)",
	#     "description": "Plays a wav or mp3 file in loop, with specific volume and audio balance",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Path of the sound file"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def playFileInLoop(*args, **kwargs):
	"""
	Bridge notes
	------------
	playFileInLoop has 2 variants on the robot:
	- playFileInLoop(fileName:str)
	- playFileInLoop(fileName:str, volume:float, pan:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.playFileInLoop has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "playFileInLoop", list(args))

@overload
def playFileFromPosition(fileName:str, position:float, /) -> None:
	"""
	Plays a wav or mp3 file from a given position in the file.
	
	Parameters
	----------
	fileName:str
		Name of the sound file
	position:float
		Position in second where the playing has to begin
	
	Bridge notes
	------------
	playFileFromPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "playFileFromPosition",
	#     "parametersSignature": "(sf)",
	#     "description": "Plays a wav or mp3 file from a given position in the file.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the sound file"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playFileFromPosition(fileName:str, position:float, volume:float, pan:float, /) -> None:
	"""
	Plays a wav or mp3 file from a given position in the file, with specific volume and audio balance
	
	Parameters
	----------
	fileName:str
		Name of the sound file
	position:float
		Position in second where the playing has to begin
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	Bridge notes
	------------
	playFileFromPosition has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "playFileFromPosition",
	#     "parametersSignature": "(sfff)",
	#     "description": "Plays a wav or mp3 file from a given position in the file, with specific volume and audio balance",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the sound file"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in second where the playing has to begin"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def playFileFromPosition(*args, **kwargs):
	"""
	Bridge notes
	------------
	playFileFromPosition has 2 variants on the robot:
	- playFileFromPosition(fileName:str, position:float)
	- playFileFromPosition(fileName:str, position:float, volume:float, pan:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.playFileFromPosition has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "playFileFromPosition", list(args))

def goTo(playId:int, position:float) -> None:
	"""
	Goes to a given position in a file which is playing.
	
	Parameters
	----------
	playId:int
		Id of the process which is playing the file
	position:float
		Position in the file (in second)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "goTo",
	#     "parametersSignature": "(if)",
	#     "description": "Goes to a given position in a file which is playing.",
	#     "parameters": [
	#         {
	#             "name": "playId",
	#             "description": "Id of the process which is playing the file"
	#         },
	#         {
	#             "name": "position",
	#             "description": "Position in the file (in second)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "goTo", [playId, position])

def stopAll() -> None:
	"""
	Stops all the files that are currently playing.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "stopAll",
	#     "parametersSignature": "()",
	#     "description": "Stops all the files that are currently playing.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "stopAll", [])

def pause(id:int) -> None:
	"""
	Pause a play back
	
	Parameters
	----------
	id:int
		Id of the process that is playing the file you want to put in pause
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "pause",
	#     "parametersSignature": "(i)",
	#     "description": "Pause a play back",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id of the process that is playing the file you want to put in pause"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "pause", [id])

def setVolume(id:int, volume:float) -> None:
	"""
	Sets the volume of the player
	
	Parameters
	----------
	id:int
		Id of the process that is playing the file you want to put louder or less loud
	volume:float
		Volume - range 0.0 to 1.0
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "setVolume",
	#     "parametersSignature": "(if)",
	#     "description": "Sets the volume of the player",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id of the process that is playing the file you want to put louder or less loud"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "Volume - range 0.0 to 1.0"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "setVolume", [id, volume])

def setMasterVolume(volume:float) -> None:
	"""
	Sets the master volume of the player
	
	Parameters
	----------
	volume:float
		Volume - range 0.0 to 1.0
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "v",
	#     "name": "setMasterVolume",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the master volume of the player",
	#     "parameters": [
	#         {
	#             "name": "volume",
	#             "description": "Volume - range 0.0 to 1.0"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "setMasterVolume", [volume])

def getVolume(playId:int) -> float:
	"""
	Returns the volume of the player
	
	Parameters
	----------
	playId:int
		Id of the process which is playing the file
	
	Returns
	----------
	Volume of the player - range 0.0 to 1.0.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "f",
	#     "name": "getVolume",
	#     "parametersSignature": "(i)",
	#     "description": "Returns the volume of the player",
	#     "parameters": [
	#         {
	#             "name": "playId",
	#             "description": "Id of the process which is playing the file"
	#         }
	#     ],
	#     "returnDescription": "Volume of the player - range 0.0 to 1.0."
	# }
	return call_method("ALAudioPlayer", "getVolume", [playId])

def getMasterVolume() -> float:
	"""
	Returns the master volume of the player
	
	Returns
	----------
	Volume of the master - range 0.0 to 1.0.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "f",
	#     "name": "getMasterVolume",
	#     "parametersSignature": "()",
	#     "description": "Returns the master volume of the player",
	#     "parameters": [],
	#     "returnDescription": "Volume of the master - range 0.0 to 1.0."
	# }
	return call_method("ALAudioPlayer", "getMasterVolume", [])

def setPanorama(p0:float) -> None:
	"""
	sets the audio panorama : -1 for left speaker / 1 for right speaker
	
	Parameters
	----------
	p0:float
		
	
	Returns
	----------
	Volume of the player - range 0.0 to 1.0.
	
	Bridge notes
	------------
	NAOqi's return description above doesn't match the method's signature, which returns nothing. This function follows the signature.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "setPanorama",
	#     "parametersSignature": "(f)",
	#     "description": "sets the audio panorama : -1 for left speaker / 1 for right speaker",
	#     "parameters": [],
	#     "returnDescription": "Volume of the player - range 0.0 to 1.0."
	# }
	return call_method("ALAudioPlayer", "setPanorama", [p0])

def loadFile(fileName:str) -> int:
	"""
	Loads a file for ulterior playback
	
	Parameters
	----------
	fileName:str
		Path of the sound file (either mp3 or wav)
	
	Returns
	----------
	Id of the file which has been loaded. This file can then be played with the play function
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "i",
	#     "name": "loadFile",
	#     "parametersSignature": "(s)",
	#     "description": "Loads a file for ulterior playback",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Path of the sound file (either mp3 or wav)"
	#         }
	#     ],
	#     "returnDescription": "Id of the file which has been loaded. This file can then be played with the play function"
	# }
	return call_method("ALAudioPlayer", "loadFile", [fileName])

def unloadFile(id:int) -> None:
	"""
	unloads a file previously loaded with the loadFile function
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "unloadFile",
	#     "parametersSignature": "(i)",
	#     "description": "unloads a file previously loaded with the loadFile function",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "unloadFile", [id])

def unloadAllFiles() -> None:
	"""
	unloads all the files already loaded.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "unloadAllFiles",
	#     "parametersSignature": "()",
	#     "description": "unloads all the files already loaded.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "unloadAllFiles", [])

def getLoadedFilesNames() -> List[str]:
	"""
	returns an array containing the names of the currently loaded files
	
	Returns
	----------
	Array containing the names of the files which has been loaded
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "[s]",
	#     "name": "getLoadedFilesNames",
	#     "parametersSignature": "()",
	#     "description": "returns an array containing the names of the currently loaded files",
	#     "parameters": [],
	#     "returnDescription": "Array containing the names of the files which has been loaded"
	# }
	return call_method("ALAudioPlayer", "getLoadedFilesNames", [])

def getLoadedFilesIds() -> List[str]:
	"""
	returns an array containing the Ids of the currently loaded files
	
	Returns
	----------
	Array containing the Ids of the files which has been loaded
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "[s]",
	#     "name": "getLoadedFilesIds",
	#     "parametersSignature": "()",
	#     "description": "returns an array containing the Ids of the currently loaded files",
	#     "parameters": [],
	#     "returnDescription": "Array containing the Ids of the files which has been loaded"
	# }
	return call_method("ALAudioPlayer", "getLoadedFilesIds", [])

@overload
def play(id:int, /) -> None:
	"""
	Starts the playback of a file preloaded with the loadFile function.
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	Bridge notes
	------------
	play has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "v",
	#     "name": "play",
	#     "parametersSignature": "(i)",
	#     "description": "Starts the playback of a file preloaded with the loadFile function.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def play(id:int, volume:float, pan:float, /) -> None:
	"""
	Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	Bridge notes
	------------
	play has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "v",
	#     "name": "play",
	#     "parametersSignature": "(iff)",
	#     "description": "Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def play(*args, **kwargs):
	"""
	Bridge notes
	------------
	play has 2 variants on the robot:
	- play(id:int)
	- play(id:int, volume:float, pan:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.play has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "play", list(args))

@overload
def playInLoop(id:int, /) -> None:
	"""
	Starts the playback in loop of a file preloaded with the loadFile function
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	Bridge notes
	------------
	playInLoop has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "v",
	#     "name": "playInLoop",
	#     "parametersSignature": "(i)",
	#     "description": "Starts the playback in loop of a file preloaded with the loadFile function",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def playInLoop(id:int, volume:float, pan:float, /) -> None:
	"""
	Plays a wav or mp3 file in loop, with specific volume and audio balance
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	Bridge notes
	------------
	playInLoop has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "v",
	#     "name": "playInLoop",
	#     "parametersSignature": "(iff)",
	#     "description": "Plays a wav or mp3 file in loop, with specific volume and audio balance",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         },
	#         {
	#             "name": "volume",
	#             "description": "volume of the sound file (must be between 0.0 and 1.0)"
	#         },
	#         {
	#             "name": "pan",
	#             "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def playInLoop(*args, **kwargs):
	"""
	Bridge notes
	------------
	playInLoop has 2 variants on the robot:
	- playInLoop(id:int)
	- playInLoop(id:int, volume:float, pan:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAudioPlayer.playInLoop has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAudioPlayer", "playInLoop", list(args))

def playWebStream(streamName:str, p1:float, p2:float) -> None:
	"""
	Starts the playback of a wab audio stream
	
	Parameters
	----------
	streamName:str
		Path of the web audio stream
	p1:float
		
	p2:float
		
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 3 parameters. The others are called p1, p2 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "v",
	#     "name": "playWebStream",
	#     "parametersSignature": "(sff)",
	#     "description": "Starts the playback of a wab audio stream",
	#     "parameters": [
	#         {
	#             "name": "streamName",
	#             "description": "Path of the web audio stream"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "playWebStream", [streamName, p1, p2])

def getFileLength(playId:int) -> float:
	"""
	Returns the length of the file played
	
	Parameters
	----------
	playId:int
		Id of the process which is playing the file
	
	Returns
	----------
	Length of the file in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "f",
	#     "name": "getFileLength",
	#     "parametersSignature": "(i)",
	#     "description": "Returns the length of the file played",
	#     "parameters": [
	#         {
	#             "name": "playId",
	#             "description": "Id of the process which is playing the file"
	#         }
	#     ],
	#     "returnDescription": "Length of the file in seconds"
	# }
	return call_method("ALAudioPlayer", "getFileLength", [playId])

def getCurrentPosition(playId:int) -> float:
	"""
	Returns the position in the file which is currently played
	
	Parameters
	----------
	playId:int
		Id of the process which is playing the file
	
	Returns
	----------
	Position in the file in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "f",
	#     "name": "getCurrentPosition",
	#     "parametersSignature": "(i)",
	#     "description": "Returns the position in the file which is currently played",
	#     "parameters": [
	#         {
	#             "name": "playId",
	#             "description": "Id of the process which is playing the file"
	#         }
	#     ],
	#     "returnDescription": "Position in the file in seconds"
	# }
	return call_method("ALAudioPlayer", "getCurrentPosition", [playId])

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
	#     "uid": 168,
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
	return call_method("ALAudioPlayer", "playSine", [frequence, gain, pan, duration])

def _launchSinePlaying(p0:int, p1:int, p2:int, p3:float) -> None:
	"""
	launch the thread to play sine
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	p3:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "v",
	#     "name": "_launchSinePlaying",
	#     "parametersSignature": "(iiif)",
	#     "description": "launch the thread to play sine",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_launchSinePlaying", [p0, p1, p2, p3])

def _isPlayingThisFile(fileName:str) -> bool:
	"""
	This function allows to know if the ALAudioPlayer module is currently playing the file you give in argument
	
	Parameters
	----------
	fileName:str
		file name of the file you want to test
	
	Returns
	----------
	1 if the file is currently beeing playing / 0 otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "b",
	#     "name": "_isPlayingThisFile",
	#     "parametersSignature": "(s)",
	#     "description": "This function allows to know if the ALAudioPlayer module is currently playing the file you give in argument",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "file name of the file you want to test"
	#         }
	#     ],
	#     "returnDescription": "1 if the file is currently beeing playing / 0 otherwise"
	# }
	return call_method("ALAudioPlayer", "_isPlayingThisFile", [fileName])

def _saySOSIP() -> None:
	"""
	Say ip if there is no tts or behavior manager enable (internal use).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "v",
	#     "name": "_saySOSIP",
	#     "parametersSignature": "()",
	#     "description": "Say ip if there is no tts or behavior manager enable (internal use).",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "_saySOSIP", [])

def disablePitch(id:int) -> None:
	"""
	Remove pitch on the current file
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "v",
	#     "name": "disablePitch",
	#     "parametersSignature": "(i)",
	#     "description": "Remove pitch on the current file",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "disablePitch", [id])

def setPitch(id:int, level:float) -> None:
	"""
	Set a pith on the current playing file
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	level:float
		Pitch shifting to apply
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "v",
	#     "name": "setPitch",
	#     "parametersSignature": "(if)",
	#     "description": "Set a pith on the current playing file",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Id returned by the loadFile function"
	#         },
	#         {
	#             "name": "level",
	#             "description": "Pitch shifting to apply"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAudioPlayer", "setPitch", [id, level])

