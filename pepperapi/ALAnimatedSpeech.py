"""
The Animated Speech module makes NAO interpret a text annotated with behaviors.
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
	return call_method("ALAnimatedSpeech", "version", [])

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
	return call_method("ALAnimatedSpeech", "ping", [])

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
	return call_method("ALAnimatedSpeech", "getMethodList", [])

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
	return call_method("ALAnimatedSpeech", "getMethodHelp", [methodName])

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
	return call_method("ALAnimatedSpeech", "getModuleHelp", [])

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
	return call_method("ALAnimatedSpeech", "getBrokerName", [])

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
	return call_method("ALAnimatedSpeech", "getUsage", [name])

@overload
def say(text:str, /) -> None:
	"""
	Say the annotated text given in parameter and animate it with animations inserted in the text.
	
	Parameters
	----------
	text:str
		An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
	
	Bridge notes
	------------
	say has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "say",
	#     "parametersSignature": "(s)",
	#     "description": "Say the annotated text given in parameter and animate it with animations inserted in the text.",
	#     "parameters": [
	#         {
	#             "name": "text",
	#             "description": "An annotated text (for example: \"Hello. ^start(Hey_1) My name is NAO\")."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def say(text:str, configuration:object, /) -> None:
	"""
	Say the annotated text given in parameter and animate it with animations inserted in the text.
	
	Parameters
	----------
	text:str
		An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
	configuration:object
		The animated speech configuration.
	
	Bridge notes
	------------
	say has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "say",
	#     "parametersSignature": "(sm)",
	#     "description": "Say the annotated text given in parameter and animate it with animations inserted in the text.",
	#     "parameters": [
	#         {
	#             "name": "text",
	#             "description": "An annotated text (for example: \"Hello. ^start(Hey_1) My name is NAO\")."
	#         },
	#         {
	#             "name": "configuration",
	#             "description": "The animated speech configuration."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def say(*args, **kwargs):
	"""
	Bridge notes
	------------
	say has 2 variants on the robot:
	- say(text:str)
	- say(text:str, configuration:object)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAnimatedSpeech.say has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAnimatedSpeech", "say", list(args))

def _reset() -> None:
	"""
	Reset the Animated Speech configuration.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_reset",
	#     "parametersSignature": "()",
	#     "description": "Reset the Animated Speech configuration.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_reset", [])

def _stopAll(blocking:bool) -> None:
	"""
	Stop all the speeches.
	
	Parameters
	----------
	blocking:bool
		If this method wait for the end of the speeches.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_stopAll",
	#     "parametersSignature": "(b)",
	#     "description": "Stop all the speeches.",
	#     "parameters": [
	#         {
	#             "name": "blocking",
	#             "description": "If this method wait for the end of the speeches."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_stopAll", [blocking])

def _isRunning() -> bool:
	"""
	Know if animated speech is running.
	
	Returns
	----------
	True, if animated speech is running, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "_isRunning",
	#     "parametersSignature": "()",
	#     "description": "Know if animated speech is running.",
	#     "parameters": [],
	#     "returnDescription": "True, if animated speech is running, False otherwise."
	# }
	return call_method("ALAnimatedSpeech", "_isRunning", [])

def setBodyLanguageModeFromStr(stringBodyLanguageMode:str) -> None:
	"""
	Set the current body language mode.
	3 modes exist: "disabled", "random" and "contextual"
	(see BodyLanguageMode enum for more details)
	
	Parameters
	----------
	stringBodyLanguageMode:str
		The choosen body language mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "setBodyLanguageModeFromStr",
	#     "parametersSignature": "(s)",
	#     "description": "Set the current body language mode.\n3 modes exist: \"disabled\", \"random\" and \"contextual\"\n(see BodyLanguageMode enum for more details)",
	#     "parameters": [
	#         {
	#             "name": "stringBodyLanguageMode",
	#             "description": "The choosen body language mode."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "setBodyLanguageModeFromStr", [stringBodyLanguageMode])

def setBodyLanguageMode(bodyLanguageMode:int) -> None:
	"""
	Set the current body language mode.
	3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL
	(see BodyLanguageMode enum for more details)
	
	Parameters
	----------
	bodyLanguageMode:int
		The choosen body language mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setBodyLanguageMode",
	#     "parametersSignature": "(I)",
	#     "description": "Set the current body language mode.\n3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL\n(see BodyLanguageMode enum for more details)",
	#     "parameters": [
	#         {
	#             "name": "bodyLanguageMode",
	#             "description": "The choosen body language mode."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "setBodyLanguageMode", [bodyLanguageMode])

def getBodyLanguageModeToStr() -> str:
	"""
	Set the current body language mode.
	3 modes exist: "disabled", "random" and "contextual"
	(see BodyLanguageMode enum for more details)
	
	Returns
	----------
	The current body language mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getBodyLanguageModeToStr",
	#     "parametersSignature": "()",
	#     "description": "Set the current body language mode.\n3 modes exist: \"disabled\", \"random\" and \"contextual\"\n(see BodyLanguageMode enum for more details)",
	#     "parameters": [],
	#     "returnDescription": "The current body language mode."
	# }
	return call_method("ALAnimatedSpeech", "getBodyLanguageModeToStr", [])

def getBodyLanguageMode() -> int:
	"""
	Set the current body language mode.
	3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL
	(see BodyLanguageMode enum for more details)
	
	Returns
	----------
	The current body language mode.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "I",
	#     "name": "getBodyLanguageMode",
	#     "parametersSignature": "()",
	#     "description": "Set the current body language mode.\n3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL\n(see BodyLanguageMode enum for more details)",
	#     "parameters": [],
	#     "returnDescription": "The current body language mode."
	# }
	return call_method("ALAnimatedSpeech", "getBodyLanguageMode", [])

def _setMSPauseBeforeSpeech(pause:int) -> None:
	"""
	Change the pause's time before the speech.
	
	Parameters
	----------
	pause:int
		The pause's time in milliseconds before the speech.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_setMSPauseBeforeSpeech",
	#     "parametersSignature": "(i)",
	#     "description": "Change the pause's time before the speech.",
	#     "parameters": [
	#         {
	#             "name": "pause",
	#             "description": "The pause's time in milliseconds before the speech."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_setMSPauseBeforeSpeech", [pause])

def _getMSPauseBeforeSpeech() -> int:
	"""
	Get the pause's time before the speech.
	
	Returns
	----------
	The pause's time in milliseconds before the speech.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "I",
	#     "name": "_getMSPauseBeforeSpeech",
	#     "parametersSignature": "()",
	#     "description": "Get the pause's time before the speech.",
	#     "parameters": [],
	#     "returnDescription": "The pause's time in milliseconds before the speech."
	# }
	return call_method("ALAnimatedSpeech", "_getMSPauseBeforeSpeech", [])

def _isCheckExecutionTimesEnabled() -> bool:
	"""
	If we need to check the execution times.
	
	Returns
	----------
	True, if we need to check the execution times, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "_isCheckExecutionTimesEnabled",
	#     "parametersSignature": "()",
	#     "description": "If we need to check the execution times.",
	#     "parameters": [],
	#     "returnDescription": "True, if we need to check the execution times, False otherwise."
	# }
	return call_method("ALAnimatedSpeech", "_isCheckExecutionTimesEnabled", [])

def _setCheckExecutionTimes(pause:bool) -> None:
	"""
	Set if we need to check the execution times.
	
	Parameters
	----------
	pause:bool
		If we need to check the execution times.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_setCheckExecutionTimes",
	#     "parametersSignature": "(b)",
	#     "description": "Set if we need to check the execution times.",
	#     "parameters": [
	#         {
	#             "name": "pause",
	#             "description": "If we need to check the execution times."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_setCheckExecutionTimes", [pause])

def addTagsToWords(tagsToWords:object) -> None:
	"""
	Add some new links between tags and words.
	
	Parameters
	----------
	tagsToWords:object
		Map of tags to words.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "addTagsToWords",
	#     "parametersSignature": "(m)",
	#     "description": "Add some new links between tags and words.",
	#     "parameters": [
	#         {
	#             "name": "tagsToWords",
	#             "description": "Map of tags to words."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "addTagsToWords", [tagsToWords])

def _diagnosis() -> None:
	"""
	Print many debug informations about the current state of animated speech.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_diagnosis",
	#     "parametersSignature": "()",
	#     "description": "Print many debug informations about the current state of animated speech.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_diagnosis", [])

def _speechBookMarkCallback(memoryKey:str, value:object, message:str) -> None:
	"""
	Callback for ALMemory subscription for speech bookmark tracking.
	
	Parameters
	----------
	memoryKey:str
		The subscribed memory key which changed.
	value:object
		The new value of the memory key.
	message:str
		The message that comes with the callback.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_speechBookMarkCallback",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback for ALMemory subscription for speech bookmark tracking.",
	#     "parameters": [
	#         {
	#             "name": "memoryKey",
	#             "description": "The subscribed memory key which changed."
	#         },
	#         {
	#             "name": "value",
	#             "description": "The new value of the memory key."
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message that comes with the callback."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_speechBookMarkCallback", [memoryKey, value, message])

def _mrkpauseCallback(pBookmark:int) -> None:
	"""
	Method called by the tts when "mrkpause" bookmark is reached.This method is blocking until the action is finish.
	
	Parameters
	----------
	pBookmark:int
		Id of the bookmark.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "_mrkpauseCallback",
	#     "parametersSignature": "(I)",
	#     "description": "Method called by the tts when \"mrkpause\" bookmark is reached.This method is blocking until the action is finish.",
	#     "parameters": [
	#         {
	#             "name": "pBookmark",
	#             "description": "Id of the bookmark."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_mrkpauseCallback", [pBookmark])

def _speechStatusCallback(memoryKey:str, value:object, message:str) -> None:
	"""
	Callback for ALMemory subscription for speech status tracking.
	
	Parameters
	----------
	memoryKey:str
		The subscribed memory key which changed.
	value:object
		The new value of the memory key.
	message:str
		The message that comes with the callback.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_speechStatusCallback",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback for ALMemory subscription for speech status tracking.",
	#     "parameters": [
	#         {
	#             "name": "memoryKey",
	#             "description": "The subscribed memory key which changed."
	#         },
	#         {
	#             "name": "value",
	#             "description": "The new value of the memory key."
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message that comes with the callback."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_speechStatusCallback", [memoryKey, value, message])

def _postureFamilyChangedCallback(memoryKey:str, value:object, message:str) -> None:
	"""
	Callback for ALMemory subscription to postureFamilyChanged.
	
	Parameters
	----------
	memoryKey:str
		The subscribed memory key which changed.
	value:object
		The new value of the memory key.
	message:str
		The message that comes with the callback.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "_postureFamilyChangedCallback",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback for ALMemory subscription to postureFamilyChanged.",
	#     "parameters": [
	#         {
	#             "name": "memoryKey",
	#             "description": "The subscribed memory key which changed."
	#         },
	#         {
	#             "name": "value",
	#             "description": "The new value of the memory key."
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message that comes with the callback."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimatedSpeech", "_postureFamilyChangedCallback", [memoryKey, value, message])

