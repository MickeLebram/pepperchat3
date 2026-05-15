from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module allows to play wav and mp3 files on NAO
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
	return send_mfc("ALAudioPlayer", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALAudioPlayer", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALAudioPlayer", "metaObject", [p0])

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
	return send_mfc("ALAudioPlayer", "terminate", [p0])

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
	return send_mfc("ALAudioPlayer", "property", [p0])

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
	return send_mfc("ALAudioPlayer", "setProperty", [p0, p1])

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
	return send_mfc("ALAudioPlayer", "properties", [])

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
	return send_mfc("ALAudioPlayer", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALAudioPlayer", "isStatsEnabled", [])

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
	return send_mfc("ALAudioPlayer", "enableStats", [p0])

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
	return send_mfc("ALAudioPlayer", "stats", [])

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
	return send_mfc("ALAudioPlayer", "clearStats", [])

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
	return send_mfc("ALAudioPlayer", "isTraceEnabled", [])

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
	return send_mfc("ALAudioPlayer", "enableTrace", [p0])

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
	return send_mfc("ALAudioPlayer", "version", [])

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
	return send_mfc("ALAudioPlayer", "ping", [])

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
	return send_mfc("ALAudioPlayer", "getMethodList", [])

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
	return send_mfc("ALAudioPlayer", "getMethodHelp", [methodName])

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
	return send_mfc("ALAudioPlayer", "getModuleHelp", [])

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
	return send_mfc("ALAudioPlayer", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALAudioPlayer", "wait", [id])

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
	return send_mfc("ALAudioPlayer", "isRunning", [id])

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
	return send_mfc("ALAudioPlayer", "stop", [id])

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
	return send_mfc("ALAudioPlayer", "getBrokerName", [])

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
	return send_mfc("ALAudioPlayer", "getUsage", [name])

def playFile_1(fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (playFile)
	
	Plays a wav or mp3 file
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "playFile",
	    "parametersSignature": "(s)",
	    "description": "Plays a wav or mp3 file",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Path of the sound file"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFile", [fileName])

def playFile_2(fileName:str, volume:float, pan:float) -> None:
	"""
	Note: This is one of the overloads of the original method (playFile)
	
	Plays a wav or mp3 file, with specific volume and audio balance
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "playFile",
	    "parametersSignature": "(sff)",
	    "description": "Plays a wav or mp3 file, with specific volume and audio balance",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Path of the sound file"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFile", [fileName, volume, pan])

def _playSoundSetFile_1(fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (_playSoundSetFile)
	
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_playSoundSetFile",
	    "parametersSignature": "(s)",
	    "description": "Plays a file contained in one of the sound sets loaded",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_playSoundSetFile", [fileName])

def playSoundSetFile_1(fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (playSoundSetFile)
	
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "playSoundSetFile",
	    "parametersSignature": "(s)",
	    "description": "Plays a file contained in one of the sound sets loaded",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playSoundSetFile", [fileName])

def _playSystemSoundSetFile(fileName:str) -> None:
	"""
	Plays a file contained in one of the sound sets loaded
	
	Parameters
	----------
	fileName:str
		Name of the file without extension
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_playSystemSoundSetFile",
	    "parametersSignature": "(s)",
	    "description": "Plays a file contained in one of the sound sets loaded",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_playSystemSoundSetFile", [fileName])

def _playSoundSetFile_2(soundSetName:str, fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (_playSoundSetFile)
	
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "_playSoundSetFile",
	    "parametersSignature": "(ss)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "soundSetName",
	            "description": "Name of the soundset"
	        },
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_playSoundSetFile", [soundSetName, fileName])

def playSoundSetFile_2(soundSetName:str, fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (playSoundSetFile)
	
	Plays a file contained in a given sound set
	
	Parameters
	----------
	soundSetName:str
		Name of the soundset
	fileName:str
		Name of the file without extension
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "playSoundSetFile",
	    "parametersSignature": "(ss)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "soundSetName",
	            "description": "Name of the soundset"
	        },
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playSoundSetFile", [soundSetName, fileName])

def _playSoundSetFile_3(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (_playSoundSetFile)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_playSoundSetFile",
	    "parametersSignature": "(ssfffb)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "soundSetName",
	            "description": "Name of the soundset"
	        },
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        },
	        {
	            "name": "loop",
	            "description": "specify if the file must be played in loop"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_playSoundSetFile", [soundSetName, fileName, position, volume, pan, loop])

def playSoundSetFile_3(soundSetName:str, fileName:str, position:float, volume:float, pan:float, loop:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (playSoundSetFile)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "playSoundSetFile",
	    "parametersSignature": "(ssfffb)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "soundSetName",
	            "description": "Name of the soundset"
	        },
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        },
	        {
	            "name": "loop",
	            "description": "specify if the file must be played in loop"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playSoundSetFile", [soundSetName, fileName, position, volume, pan, loop])

def _playSoundSetFile_4(fileName:str, position:float, volume:float, pan:float, loop:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (_playSoundSetFile)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_playSoundSetFile",
	    "parametersSignature": "(sfffb)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        },
	        {
	            "name": "loop",
	            "description": "specify if the file must be played in loop"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_playSoundSetFile", [fileName, position, volume, pan, loop])

def playSoundSetFile_4(fileName:str, position:float, volume:float, pan:float, loop:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (playSoundSetFile)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "playSoundSetFile",
	    "parametersSignature": "(sfffb)",
	    "description": "Plays a file contained in a given sound set",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the file without extension"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        },
	        {
	            "name": "loop",
	            "description": "specify if the file must be played in loop"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playSoundSetFile", [fileName, position, volume, pan, loop])

def _loadSoundSet(setName:str) -> None:
	"""
	Load a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_loadSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Load a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_loadSoundSet", [setName])

def loadSoundSet(setName:str) -> None:
	"""
	Load a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "loadSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Load a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "loadSoundSet", [setName])

def _unloadSoundSet(setName:str) -> None:
	"""
	Unload a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_unloadSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Unload a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_unloadSoundSet", [setName])

def unloadSoundSet(setName:str) -> None:
	"""
	Unload a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "unloadSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Unload a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "unloadSoundSet", [setName])

def _loadSystemSoundSet(setName:str) -> None:
	"""
	Load a system sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_loadSystemSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Load a system sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_loadSystemSoundSet", [setName])

def _setDefaultSystemSoundSet(setName:str) -> None:
	"""
	Sets the default soundset used for system sounds
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "_setDefaultSystemSoundSet",
	    "parametersSignature": "(s)",
	    "description": "Sets the default soundset used for system sounds",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_setDefaultSystemSoundSet", [setName])

def _getSoundSetFileNames(setName:str) -> List[str]:
	"""
	Return the list of files contained in a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "[s]",
	    "name": "_getSoundSetFileNames",
	    "parametersSignature": "(s)",
	    "description": "Return the list of files contained in a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getSoundSetFileNames", [setName])

def getSoundSetFileNames(setName:str) -> List[str]:
	"""
	Return the list of files contained in a sound set
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "[s]",
	    "name": "getSoundSetFileNames",
	    "parametersSignature": "(s)",
	    "description": "Return the list of files contained in a sound set",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getSoundSetFileNames", [setName])

def _getCurrentSystemSoundSet() -> str:
	"""
	Return the current sound set loaded
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "s",
	    "name": "_getCurrentSystemSoundSet",
	    "parametersSignature": "()",
	    "description": "Return the current sound set loaded",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getCurrentSystemSoundSet", [])

def _getLoadedSoundSetsList() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "[s]",
	    "name": "_getLoadedSoundSetsList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getLoadedSoundSetsList", [])

def getLoadedSoundSetsList() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "[s]",
	    "name": "getLoadedSoundSetsList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getLoadedSoundSetsList", [])

def _getInstalledSoundSetsList() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "[s]",
	    "name": "_getInstalledSoundSetsList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getInstalledSoundSetsList", [])

def getInstalledSoundSetsList() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "[s]",
	    "name": "getInstalledSoundSetsList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getInstalledSoundSetsList", [])

def _isSoundSetInstalled(setName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "b",
	    "name": "_isSoundSetInstalled",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_isSoundSetInstalled", [setName])

def isSoundSetInstalled(setName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "b",
	    "name": "isSoundSetInstalled",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "isSoundSetInstalled", [setName])

def _isSoundSetFileInstalled(setName:str, soundName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	soundName:str
		name of the sound
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "b",
	    "name": "_isSoundSetFileInstalled",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        },
	        {
	            "name": "soundName",
	            "description": "name of the sound"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_isSoundSetFileInstalled", [setName, soundName])

def isSoundSetFileInstalled(setName:str, soundName:str) -> bool:
	"""
	
	
	Parameters
	----------
	setName:str
		name of the set
	soundName:str
		name of the sound
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "b",
	    "name": "isSoundSetFileInstalled",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "setName",
	            "description": "name of the set"
	        },
	        {
	            "name": "soundName",
	            "description": "name of the sound"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "isSoundSetFileInstalled", [setName, soundName])

def _getSystemSoundSetFileDuration(soundName:str) -> float:
	"""
	
	
	Parameters
	----------
	soundName:str
		name of the sound
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "f",
	    "name": "_getSystemSoundSetFileDuration",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "soundName",
	            "description": "name of the sound"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getSystemSoundSetFileDuration", [soundName])

def _getSystemSoundSetFilePath(soundName:str) -> str:
	"""
	
	
	Parameters
	----------
	soundName:str
		name of the sound
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "s",
	    "name": "_getSystemSoundSetFilePath",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "soundName",
	            "description": "name of the sound"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_getSystemSoundSetFilePath", [soundName])

def playFileInLoop_1(fileName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (playFileInLoop)
	
	Plays a wav or mp3 file in loop
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "playFileInLoop",
	    "parametersSignature": "(s)",
	    "description": "Plays a wav or mp3 file in loop",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Path of the sound file"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFileInLoop", [fileName])

def playFileInLoop_2(fileName:str, volume:float, pan:float) -> None:
	"""
	Note: This is one of the overloads of the original method (playFileInLoop)
	
	Plays a wav or mp3 file in loop, with specific volume and audio balance
	
	Parameters
	----------
	fileName:str
		Path of the sound file
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "playFileInLoop",
	    "parametersSignature": "(sff)",
	    "description": "Plays a wav or mp3 file in loop, with specific volume and audio balance",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Path of the sound file"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFileInLoop", [fileName, volume, pan])

def playFileFromPosition_1(fileName:str, position:float) -> None:
	"""
	Note: This is one of the overloads of the original method (playFileFromPosition)
	
	Plays a wav or mp3 file from a given position in the file.
	
	Parameters
	----------
	fileName:str
		Name of the sound file
	position:float
		Position in second where the playing has to begin
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "playFileFromPosition",
	    "parametersSignature": "(sf)",
	    "description": "Plays a wav or mp3 file from a given position in the file.",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the sound file"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFileFromPosition", [fileName, position])

def playFileFromPosition_2(fileName:str, position:float, volume:float, pan:float) -> None:
	"""
	Note: This is one of the overloads of the original method (playFileFromPosition)
	
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
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "playFileFromPosition",
	    "parametersSignature": "(sfff)",
	    "description": "Plays a wav or mp3 file from a given position in the file, with specific volume and audio balance",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Name of the sound file"
	        },
	        {
	            "name": "position",
	            "description": "Position in second where the playing has to begin"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playFileFromPosition", [fileName, position, volume, pan])

def goTo(playId:int, position:float) -> None:
	"""
	Goes to a given position in a file which is playing.
	
	Parameters
	----------
	playId:int
		Id of the process which is playing the file
	position:float
		Position in the file (in second)
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "goTo",
	    "parametersSignature": "(if)",
	    "description": "Goes to a given position in a file which is playing.",
	    "parameters": [
	        {
	            "name": "playId",
	            "description": "Id of the process which is playing the file"
	        },
	        {
	            "name": "position",
	            "description": "Position in the file (in second)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "goTo", [playId, position])

def stopAll() -> None:
	"""
	Stops all the files that are currently playing.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "stopAll",
	    "parametersSignature": "()",
	    "description": "Stops all the files that are currently playing.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "stopAll", [])

def pause(id:int) -> None:
	"""
	Pause a play back
	
	Parameters
	----------
	id:int
		Id of the process that is playing the file you want to put in pause
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "pause",
	    "parametersSignature": "(i)",
	    "description": "Pause a play back",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id of the process that is playing the file you want to put in pause"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "pause", [id])

def setVolume(id:int, volume:float) -> None:
	"""
	Sets the volume of the player
	
	Parameters
	----------
	id:int
		Id of the process that is playing the file you want to put louder or less loud
	volume:float
		Volume - range 0.0 to 1.0
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "setVolume",
	    "parametersSignature": "(if)",
	    "description": "Sets the volume of the player",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id of the process that is playing the file you want to put louder or less loud"
	        },
	        {
	            "name": "volume",
	            "description": "Volume - range 0.0 to 1.0"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "setVolume", [id, volume])

def setMasterVolume(volume:float) -> None:
	"""
	Sets the master volume of the player
	
	Parameters
	----------
	volume:float
		Volume - range 0.0 to 1.0
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "v",
	    "name": "setMasterVolume",
	    "parametersSignature": "(f)",
	    "description": "Sets the master volume of the player",
	    "parameters": [
	        {
	            "name": "volume",
	            "description": "Volume - range 0.0 to 1.0"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "setMasterVolume", [volume])

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
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "f",
	    "name": "getVolume",
	    "parametersSignature": "(i)",
	    "description": "Returns the volume of the player",
	    "parameters": [
	        {
	            "name": "playId",
	            "description": "Id of the process which is playing the file"
	        }
	    ],
	    "returnDescription": "Volume of the player - range 0.0 to 1.0."
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getVolume", [playId])

def getMasterVolume() -> float:
	"""
	Returns the master volume of the player
	
	Returns
	----------
	Volume of the master - range 0.0 to 1.0.
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "f",
	    "name": "getMasterVolume",
	    "parametersSignature": "()",
	    "description": "Returns the master volume of the player",
	    "parameters": [],
	    "returnDescription": "Volume of the master - range 0.0 to 1.0."
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getMasterVolume", [])

def setPanorama(p0:float) -> None:
	"""
	sets the audio panorama : -1 for left speaker / 1 for right speaker
	
	Parameters
	----------
	p0:float
		
	
	Returns
	----------
	Volume of the player - range 0.0 to 1.0.
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "setPanorama",
	    "parametersSignature": "(f)",
	    "description": "sets the audio panorama : -1 for left speaker / 1 for right speaker",
	    "parameters": [],
	    "returnDescription": "Volume of the player - range 0.0 to 1.0."
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "setPanorama", [p0])

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
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "i",
	    "name": "loadFile",
	    "parametersSignature": "(s)",
	    "description": "Loads a file for ulterior playback",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Path of the sound file (either mp3 or wav)"
	        }
	    ],
	    "returnDescription": "Id of the file which has been loaded. This file can then be played with the play function"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "loadFile", [fileName])

def unloadFile(id:int) -> None:
	"""
	unloads a file previously loaded with the loadFile function
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "unloadFile",
	    "parametersSignature": "(i)",
	    "description": "unloads a file previously loaded with the loadFile function",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "unloadFile", [id])

def unloadAllFiles() -> None:
	"""
	unloads all the files already loaded.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "unloadAllFiles",
	    "parametersSignature": "()",
	    "description": "unloads all the files already loaded.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "unloadAllFiles", [])

def getLoadedFilesNames() -> List[str]:
	"""
	returns an array containing the names of the currently loaded files
	
	Returns
	----------
	Array containing the names of the files which has been loaded
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "[s]",
	    "name": "getLoadedFilesNames",
	    "parametersSignature": "()",
	    "description": "returns an array containing the names of the currently loaded files",
	    "parameters": [],
	    "returnDescription": "Array containing the names of the files which has been loaded"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getLoadedFilesNames", [])

def getLoadedFilesIds() -> List[str]:
	"""
	returns an array containing the Ids of the currently loaded files
	
	Returns
	----------
	Array containing the Ids of the files which has been loaded
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "[s]",
	    "name": "getLoadedFilesIds",
	    "parametersSignature": "()",
	    "description": "returns an array containing the Ids of the currently loaded files",
	    "parameters": [],
	    "returnDescription": "Array containing the Ids of the files which has been loaded"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getLoadedFilesIds", [])

def play_1(id:int) -> None:
	"""
	Note: This is one of the overloads of the original method (play)
	
	Starts the playback of a file preloaded with the loadFile function.
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "v",
	    "name": "play",
	    "parametersSignature": "(i)",
	    "description": "Starts the playback of a file preloaded with the loadFile function.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "play", [id])

def play_2(id:int, volume:float, pan:float) -> None:
	"""
	Note: This is one of the overloads of the original method (play)
	
	Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "v",
	    "name": "play",
	    "parametersSignature": "(iff)",
	    "description": "Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "play", [id, volume, pan])

def playInLoop_1(id:int) -> None:
	"""
	Note: This is one of the overloads of the original method (playInLoop)
	
	Starts the playback in loop of a file preloaded with the loadFile function
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "v",
	    "name": "playInLoop",
	    "parametersSignature": "(i)",
	    "description": "Starts the playback in loop of a file preloaded with the loadFile function",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playInLoop", [id])

def playInLoop_2(id:int, volume:float, pan:float) -> None:
	"""
	Note: This is one of the overloads of the original method (playInLoop)
	
	Plays a wav or mp3 file in loop, with specific volume and audio balance
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	volume:float
		volume of the sound file (must be between 0.0 and 1.0)
	pan:float
		audio balance of the sound file (-1.0 : left / 1.0 : right)
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "v",
	    "name": "playInLoop",
	    "parametersSignature": "(iff)",
	    "description": "Plays a wav or mp3 file in loop, with specific volume and audio balance",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        },
	        {
	            "name": "volume",
	            "description": "volume of the sound file (must be between 0.0 and 1.0)"
	        },
	        {
	            "name": "pan",
	            "description": "audio balance of the sound file (-1.0 : left / 1.0 : right)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playInLoop", [id, volume, pan])

def playWebStream(streamName:str, p1:float, p2:float) -> None:
	"""
	Starts the playback of a wab audio stream
	
	Parameters
	----------
	streamName:str
		Path of the web audio stream
	p1:float
		
	p2:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "v",
	    "name": "playWebStream",
	    "parametersSignature": "(sff)",
	    "description": "Starts the playback of a wab audio stream",
	    "parameters": [
	        {
	            "name": "streamName",
	            "description": "Path of the web audio stream"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playWebStream", [streamName, p1, p2])

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
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "f",
	    "name": "getFileLength",
	    "parametersSignature": "(i)",
	    "description": "Returns the length of the file played",
	    "parameters": [
	        {
	            "name": "playId",
	            "description": "Id of the process which is playing the file"
	        }
	    ],
	    "returnDescription": "Length of the file in seconds"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getFileLength", [playId])

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
	
	*Reference struct*
	'''
	{
	    "uid": 167,
	    "returnSignature": "f",
	    "name": "getCurrentPosition",
	    "parametersSignature": "(i)",
	    "description": "Returns the position in the file which is currently played",
	    "parameters": [
	        {
	            "name": "playId",
	            "description": "Id of the process which is playing the file"
	        }
	    ],
	    "returnDescription": "Position in the file in seconds"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "getCurrentPosition", [playId])

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
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "v",
	    "name": "playSine",
	    "parametersSignature": "(iiif)",
	    "description": "Play a sine wave which specified caracteristics.",
	    "parameters": [
	        {
	            "name": "frequence",
	            "description": "Frequence in Hertz"
	        },
	        {
	            "name": "gain",
	            "description": "Volume Gain between 0 and 100"
	        },
	        {
	            "name": "pan",
	            "description": "Stereo Pan set to either {-1,0,+1}"
	        },
	        {
	            "name": "duration",
	            "description": "Duration of the sine wave in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "playSine", [frequence, gain, pan, duration])

def _launchSinePlaying(p0:int, p1:int, p2:int, p3:float) -> None:
	"""
	launch the thread to play sine
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	p3:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "v",
	    "name": "_launchSinePlaying",
	    "parametersSignature": "(iiif)",
	    "description": "launch the thread to play sine",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_launchSinePlaying", [p0, p1, p2, p3])

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
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "b",
	    "name": "_isPlayingThisFile",
	    "parametersSignature": "(s)",
	    "description": "This function allows to know if the ALAudioPlayer module is currently playing the file you give in argument",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "file name of the file you want to test"
	        }
	    ],
	    "returnDescription": "1 if the file is currently beeing playing / 0 otherwise"
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_isPlayingThisFile", [fileName])

def _saySOSIP() -> None:
	"""
	Say ip if there is no tts or behavior manager enable (internal use).
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "v",
	    "name": "_saySOSIP",
	    "parametersSignature": "()",
	    "description": "Say ip if there is no tts or behavior manager enable (internal use).",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "_saySOSIP", [])

def disablePitch(id:int) -> None:
	"""
	Remove pitch on the current file
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "v",
	    "name": "disablePitch",
	    "parametersSignature": "(i)",
	    "description": "Remove pitch on the current file",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "disablePitch", [id])

def setPitch(id:int, level:float) -> None:
	"""
	Set a pith on the current playing file
	
	Parameters
	----------
	id:int
		Id returned by the loadFile function
	level:float
		Pitch shifting to apply
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "v",
	    "name": "setPitch",
	    "parametersSignature": "(if)",
	    "description": "Set a pith on the current playing file",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "Id returned by the loadFile function"
	        },
	        {
	            "name": "level",
	            "description": "Pitch shifting to apply"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAudioPlayer", "setPitch", [id, level])

