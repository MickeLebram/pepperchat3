from .gentypes import *
from .robot_client import send_mfc
import json
"""
The Animated Speech module makes NAO interpret a text annotated with behaviors.
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
	return send_mfc("ALAnimatedSpeech", "version", [])

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
	return send_mfc("ALAnimatedSpeech", "ping", [])

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
	return send_mfc("ALAnimatedSpeech", "getMethodList", [])

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
	return send_mfc("ALAnimatedSpeech", "getMethodHelp", [methodName])

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
	return send_mfc("ALAnimatedSpeech", "getModuleHelp", [])

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
	return send_mfc("ALAnimatedSpeech", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALAnimatedSpeech", "wait", [id])

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
	return send_mfc("ALAnimatedSpeech", "isRunning", [id])

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
	return send_mfc("ALAnimatedSpeech", "stop", [id])

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
	return send_mfc("ALAnimatedSpeech", "getBrokerName", [])

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
	return send_mfc("ALAnimatedSpeech", "getUsage", [name])

def say_1(text:str) -> None:
	"""
	Note: This is one of the overloads of the original method (say)
	
	Say the annotated text given in parameter and animate it with animations inserted in the text.
	
	Parameters
	----------
	text:str
		An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "say",
	    "parametersSignature": "(s)",
	    "description": "Say the annotated text given in parameter and animate it with animations inserted in the text.",
	    "parameters": [
	        {
	            "name": "text",
	            "description": "An annotated text (for example: \"Hello. ^start(Hey_1) My name is NAO\")."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "say", [text])

def say_2(text:str, configuration:object) -> None:
	"""
	Note: This is one of the overloads of the original method (say)
	
	Say the annotated text given in parameter and animate it with animations inserted in the text.
	
	Parameters
	----------
	text:str
		An annotated text (for example: "Hello. ^start(Hey_1) My name is NAO").
	configuration:object
		The animated speech configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "say",
	    "parametersSignature": "(sm)",
	    "description": "Say the annotated text given in parameter and animate it with animations inserted in the text.",
	    "parameters": [
	        {
	            "name": "text",
	            "description": "An annotated text (for example: \"Hello. ^start(Hey_1) My name is NAO\")."
	        },
	        {
	            "name": "configuration",
	            "description": "The animated speech configuration."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "say", [text, configuration])

def _reset() -> None:
	"""
	Reset the Animated Speech configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_reset",
	    "parametersSignature": "()",
	    "description": "Reset the Animated Speech configuration.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_reset", [])

def _stopAll(blocking:bool) -> None:
	"""
	Stop all the speeches.
	
	Parameters
	----------
	blocking:bool
		If this method wait for the end of the speeches.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_stopAll",
	    "parametersSignature": "(b)",
	    "description": "Stop all the speeches.",
	    "parameters": [
	        {
	            "name": "blocking",
	            "description": "If this method wait for the end of the speeches."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_stopAll", [blocking])

def _isRunning() -> bool:
	"""
	Know if animated speech is running.
	
	Returns
	----------
	True, if animated speech is running, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "_isRunning",
	    "parametersSignature": "()",
	    "description": "Know if animated speech is running.",
	    "parameters": [],
	    "returnDescription": "True, if animated speech is running, False otherwise."
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_isRunning", [])

def setBodyLanguageModeFromStr(stringBodyLanguageMode:str) -> None:
	"""
	Set the current body language mode.
	3 modes exist: "disabled", "random" and "contextual"
	(see BodyLanguageMode enum for more details)
	
	Parameters
	----------
	stringBodyLanguageMode:str
		The choosen body language mode.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "setBodyLanguageModeFromStr",
	    "parametersSignature": "(s)",
	    "description": "Set the current body language mode.\n3 modes exist: \"disabled\", \"random\" and \"contextual\"\n(see BodyLanguageMode enum for more details)",
	    "parameters": [
	        {
	            "name": "stringBodyLanguageMode",
	            "description": "The choosen body language mode."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "setBodyLanguageModeFromStr", [stringBodyLanguageMode])

def setBodyLanguageMode(bodyLanguageMode:int) -> None:
	"""
	Set the current body language mode.
	3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL
	(see BodyLanguageMode enum for more details)
	
	Parameters
	----------
	bodyLanguageMode:int
		The choosen body language mode.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "setBodyLanguageMode",
	    "parametersSignature": "(I)",
	    "description": "Set the current body language mode.\n3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL\n(see BodyLanguageMode enum for more details)",
	    "parameters": [
	        {
	            "name": "bodyLanguageMode",
	            "description": "The choosen body language mode."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "setBodyLanguageMode", [bodyLanguageMode])

def getBodyLanguageModeToStr() -> str:
	"""
	Set the current body language mode.
	3 modes exist: "disabled", "random" and "contextual"
	(see BodyLanguageMode enum for more details)
	
	Returns
	----------
	The current body language mode.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "s",
	    "name": "getBodyLanguageModeToStr",
	    "parametersSignature": "()",
	    "description": "Set the current body language mode.\n3 modes exist: \"disabled\", \"random\" and \"contextual\"\n(see BodyLanguageMode enum for more details)",
	    "parameters": [],
	    "returnDescription": "The current body language mode."
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "getBodyLanguageModeToStr", [])

def getBodyLanguageMode() -> int:
	"""
	Set the current body language mode.
	3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL
	(see BodyLanguageMode enum for more details)
	
	Returns
	----------
	The current body language mode.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "I",
	    "name": "getBodyLanguageMode",
	    "parametersSignature": "()",
	    "description": "Set the current body language mode.\n3 modes exist: SPEAKINGMOVEMENT_MODE_DISABLED,SPEAKINGMOVEMENT_MODE_RANDOM and SPEAKINGMOVEMENT_MODE_CONTEXTUAL\n(see BodyLanguageMode enum for more details)",
	    "parameters": [],
	    "returnDescription": "The current body language mode."
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "getBodyLanguageMode", [])

def _setMSPauseBeforeSpeech(pause:int) -> None:
	"""
	Change the pause's time before the speech.
	
	Parameters
	----------
	pause:int
		The pause's time in milliseconds before the speech.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "_setMSPauseBeforeSpeech",
	    "parametersSignature": "(i)",
	    "description": "Change the pause's time before the speech.",
	    "parameters": [
	        {
	            "name": "pause",
	            "description": "The pause's time in milliseconds before the speech."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_setMSPauseBeforeSpeech", [pause])

def _getMSPauseBeforeSpeech() -> int:
	"""
	Get the pause's time before the speech.
	
	Returns
	----------
	The pause's time in milliseconds before the speech.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "I",
	    "name": "_getMSPauseBeforeSpeech",
	    "parametersSignature": "()",
	    "description": "Get the pause's time before the speech.",
	    "parameters": [],
	    "returnDescription": "The pause's time in milliseconds before the speech."
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_getMSPauseBeforeSpeech", [])

def _isCheckExecutionTimesEnabled() -> bool:
	"""
	If we need to check the execution times.
	
	Returns
	----------
	True, if we need to check the execution times, False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "b",
	    "name": "_isCheckExecutionTimesEnabled",
	    "parametersSignature": "()",
	    "description": "If we need to check the execution times.",
	    "parameters": [],
	    "returnDescription": "True, if we need to check the execution times, False otherwise."
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_isCheckExecutionTimesEnabled", [])

def _setCheckExecutionTimes(pause:bool) -> None:
	"""
	Set if we need to check the execution times.
	
	Parameters
	----------
	pause:bool
		If we need to check the execution times.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_setCheckExecutionTimes",
	    "parametersSignature": "(b)",
	    "description": "Set if we need to check the execution times.",
	    "parameters": [
	        {
	            "name": "pause",
	            "description": "If we need to check the execution times."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_setCheckExecutionTimes", [pause])

def addTagsToWords(tagsToWords:object) -> None:
	"""
	Add some new links between tags and words.
	
	Parameters
	----------
	tagsToWords:object
		Map of tags to words.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "addTagsToWords",
	    "parametersSignature": "(m)",
	    "description": "Add some new links between tags and words.",
	    "parameters": [
	        {
	            "name": "tagsToWords",
	            "description": "Map of tags to words."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "addTagsToWords", [tagsToWords])

def _diagnosis() -> None:
	"""
	Print many debug informations about the current state of animated speech.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_diagnosis",
	    "parametersSignature": "()",
	    "description": "Print many debug informations about the current state of animated speech.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_diagnosis", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_speechBookMarkCallback",
	    "parametersSignature": "(sms)",
	    "description": "Callback for ALMemory subscription for speech bookmark tracking.",
	    "parameters": [
	        {
	            "name": "memoryKey",
	            "description": "The subscribed memory key which changed."
	        },
	        {
	            "name": "value",
	            "description": "The new value of the memory key."
	        },
	        {
	            "name": "message",
	            "description": "The message that comes with the callback."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_speechBookMarkCallback", [memoryKey, value, message])

def _mrkpauseCallback(pBookmark:int) -> None:
	"""
	Method called by the tts when "mrkpause" bookmark is reached.This method is blocking until the action is finish.
	
	Parameters
	----------
	pBookmark:int
		Id of the bookmark.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_mrkpauseCallback",
	    "parametersSignature": "(I)",
	    "description": "Method called by the tts when \"mrkpause\" bookmark is reached.This method is blocking until the action is finish.",
	    "parameters": [
	        {
	            "name": "pBookmark",
	            "description": "Id of the bookmark."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_mrkpauseCallback", [pBookmark])

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
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_speechStatusCallback",
	    "parametersSignature": "(sms)",
	    "description": "Callback for ALMemory subscription for speech status tracking.",
	    "parameters": [
	        {
	            "name": "memoryKey",
	            "description": "The subscribed memory key which changed."
	        },
	        {
	            "name": "value",
	            "description": "The new value of the memory key."
	        },
	        {
	            "name": "message",
	            "description": "The message that comes with the callback."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_speechStatusCallback", [memoryKey, value, message])

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
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "_postureFamilyChangedCallback",
	    "parametersSignature": "(sms)",
	    "description": "Callback for ALMemory subscription to postureFamilyChanged.",
	    "parameters": [
	        {
	            "name": "memoryKey",
	            "description": "The subscribed memory key which changed."
	        },
	        {
	            "name": "value",
	            "description": "The new value of the memory key."
	        },
	        {
	            "name": "message",
	            "description": "The message that comes with the callback."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimatedSpeech", "_postureFamilyChangedCallback", [memoryKey, value, message])

