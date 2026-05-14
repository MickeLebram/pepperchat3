from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALSpeechRecognition gives access to the embedded voice recognition system. It can be dynamically modified. This class allows user to load the current words list that should be recognized. The result of the recognition engine is located in the ALMemory's key: "WordRecognized". The structure of the result is an array :  [ (string) word , (float) confidence ]
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
	return send_mfc("ALSpeechRecognition", "version", [])

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
	return send_mfc("ALSpeechRecognition", "ping", [])

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
	return send_mfc("ALSpeechRecognition", "getMethodList", [])

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
	return send_mfc("ALSpeechRecognition", "getMethodHelp", [methodName])

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
	return send_mfc("ALSpeechRecognition", "getModuleHelp", [])

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
	return send_mfc("ALSpeechRecognition", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALSpeechRecognition", "wait", [id])

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
	return send_mfc("ALSpeechRecognition", "isRunning", [id])

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
	return send_mfc("ALSpeechRecognition", "stop", [id])

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
	return send_mfc("ALSpeechRecognition", "getBrokerName", [])

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
	return send_mfc("ALSpeechRecognition", "getUsage", [name])

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
	return send_mfc("ALSpeechRecognition", "subscribe", [name, period, precision])

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
	return send_mfc("ALSpeechRecognition", "subscribe", [name])

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
	return send_mfc("ALSpeechRecognition", "unsubscribe", [name])

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
	return send_mfc("ALSpeechRecognition", "updatePeriod", [name, period])

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
	return send_mfc("ALSpeechRecognition", "updatePrecision", [name, precision])

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
	return send_mfc("ALSpeechRecognition", "getCurrentPeriod", [])

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
	return send_mfc("ALSpeechRecognition", "getCurrentPrecision", [])

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
	return send_mfc("ALSpeechRecognition", "getMyPeriod", [name])

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
	return send_mfc("ALSpeechRecognition", "getMyPrecision", [name])

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
	return send_mfc("ALSpeechRecognition", "getSubscribersInfo", [])

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
	return send_mfc("ALSpeechRecognition", "getOutputNames", [])

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
	return send_mfc("ALSpeechRecognition", "getEventList", [])

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
	return send_mfc("ALSpeechRecognition", "getMemoryKeyList", [])

def setVisualExpression(setOrNot:bool) -> None:
	"""
	Enable or disable the leds animations showing the state of the recognition engine during the recognition process.
	
	Parameters
	----------
	setOrNot:bool
		Enable (true) or disable it (false).
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "setVisualExpression",
	    "parametersSignature": "(b)",
	    "description": "Enable or disable the leds animations showing the state of the recognition engine during the recognition process.",
	    "parameters": [
	        {
	            "name": "setOrNot",
	            "description": "Enable (true) or disable it (false)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setVisualExpression", [setOrNot])

def setVisualExpressionMode(mode:int) -> None:
	"""
	Sets the LED animation mode
	
	Parameters
	----------
	mode:int
		animation mode: 0: deactivated, 1: eyes, 2: ears, 3: full
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "setVisualExpressionMode",
	    "parametersSignature": "(i)",
	    "description": "Sets the LED animation mode",
	    "parameters": [
	        {
	            "name": "mode",
	            "description": "animation mode: 0: deactivated, 1: eyes, 2: ears, 3: full"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setVisualExpressionMode", [mode])

def setAudioExpression(setOrNot:bool) -> None:
	"""
	Enable or disable the playing of sounds indicating the state of the recognition engine. If this option is enabled, a sound is played at the beginning of the recognition process (after a call to the subscribe method), and a sound is played when the user call the unsubscribe method
	
	Parameters
	----------
	setOrNot:bool
		Enable (true) or disable it (false).
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "setAudioExpression",
	    "parametersSignature": "(b)",
	    "description": "Enable or disable the playing of sounds indicating the state of the recognition engine. If this option is enabled, a sound is played at the beginning of the recognition process (after a call to the subscribe method), and a sound is played when the user call the unsubscribe method",
	    "parameters": [
	        {
	            "name": "setOrNot",
	            "description": "Enable (true) or disable it (false)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setAudioExpression", [setOrNot])

def getAudioExpression() -> bool:
	"""
	To check if audio expression is enabled or disabled.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "getAudioExpression",
	    "parametersSignature": "()",
	    "description": "To check if audio expression is enabled or disabled.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getAudioExpression", [])

def setLanguage(languageName:str) -> None:
	"""
	Set the language used by the speech recognition engine. The list of the available languages can be collected through the getAvailableLanguages method. If you want to set a language as the default language (loading automatically at module launch), please refer to the web page of the robot.
	
	Parameters
	----------
	languageName:str
		Name of the language in English.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "setLanguage",
	    "parametersSignature": "(s)",
	    "description": "Set the language used by the speech recognition engine. The list of the available languages can be collected through the getAvailableLanguages method. If you want to set a language as the default language (loading automatically at module launch), please refer to the web page of the robot.",
	    "parameters": [
	        {
	            "name": "languageName",
	            "description": "Name of the language in English."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setLanguage", [languageName])

def _setDefaultLanguage(pLanguage:str) -> None:
	"""
	Set a language as the default language for the Speech Recognition engine
	
	Parameters
	----------
	pLanguage:str
		The language among those available on your robot as a String
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_setDefaultLanguage",
	    "parametersSignature": "(s)",
	    "description": "Set a language as the default language for the Speech Recognition engine",
	    "parameters": [
	        {
	            "name": "pLanguage",
	            "description": "The language among those available on your robot as a String"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_setDefaultLanguage", [pLanguage])

def getLanguage() -> str:
	"""
	Return the current language used by the speech recognition system.
	
	Returns
	----------
	Current language used by the speech recognition engine.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "s",
	    "name": "getLanguage",
	    "parametersSignature": "()",
	    "description": "Return the current language used by the speech recognition system.",
	    "parameters": [],
	    "returnDescription": "Current language used by the speech recognition engine."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getLanguage", [])

def getAvailableLanguages() -> List[str]:
	"""
	Return the list of the languages installed on the system.
	
	Returns
	----------
	Array of strings that contains the list of the installed languages.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "[s]",
	    "name": "getAvailableLanguages",
	    "parametersSignature": "()",
	    "description": "Return the list of the languages installed on the system.",
	    "parameters": [],
	    "returnDescription": "Array of strings that contains the list of the installed languages."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getAvailableLanguages", [])

def setParameter_1(paramName:str, paramValue:float) -> None:
	"""
	Note: This is one of the overloads of the original method (setParameter)
	
	Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.
	The parameters that can be set and the corresponding values are:
	"Sensitivity" - Values : range is [0.0; 1.0].
	"Timeout" - Values :  default values 3000 ms. Timeout for the remote recognition
	"MinimumTrailingSilence" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.
	
	
	Parameters
	----------
	paramName:str
		Name of the parameter.
	paramValue:float
		Value of the parameter.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "setParameter",
	    "parametersSignature": "(sf)",
	    "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "Name of the parameter."
	        },
	        {
	            "name": "paramValue",
	            "description": "Value of the parameter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setParameter", [paramName, paramValue])

def setParameter_2(paramName:str, paramValue:bool) -> None:
	"""
	Note: This is one of the overloads of the original method (setParameter)
	
	Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.
	The parameters that can be set and the corresponding values are:
	"Sensitivity" - Values : range is [0.0; 1.0].
	"Timeout" - Values :  default values 3000 ms. Timeout for the remote recognition
	"MinimumTrailingSilence" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.
	
	
	Parameters
	----------
	paramName:str
		Name of the parameter.
	paramValue:bool
		Value of the parameter.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "setParameter",
	    "parametersSignature": "(sb)",
	    "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "Name of the parameter."
	        },
	        {
	            "name": "paramValue",
	            "description": "Value of the parameter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setParameter", [paramName, paramValue])

def getParameter(paramName:str) -> float:
	"""
	Get a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be retrieved
	
	Parameters
	----------
	paramName:str
		Name of the parameter.
	
	Returns
	----------
	Value of the parameter.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "f",
	    "name": "getParameter",
	    "parametersSignature": "(s)",
	    "description": "Get a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be retrieved",
	    "parameters": [
	        {
	            "name": "paramName",
	            "description": "Name of the parameter."
	        }
	    ],
	    "returnDescription": "Value of the parameter."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getParameter", [paramName])

def setWordListAsVocabulary(vocabulary:List[str]) -> None:
	"""
	Set the list of words (vocabulary) that should be recognized by the speech recognition engine.
	
	Parameters
	----------
	vocabulary:List[str]
		List of words that should be recognized
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "setWordListAsVocabulary",
	    "parametersSignature": "([s])",
	    "description": "Set the list of words (vocabulary) that should be recognized by the speech recognition engine.",
	    "parameters": [
	        {
	            "name": "vocabulary",
	            "description": "List of words that should be recognized"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setWordListAsVocabulary", [vocabulary])

def setVocabulary(vocabulary:List[str], enabledWordSpotting:bool) -> None:
	"""
	Set the list of words (vocabulary) that should be recognized by the speech recognition engine.
	
	Parameters
	----------
	vocabulary:List[str]
		List of words that should be recognized
	enabledWordSpotting:bool
		If disabled, the engine expects to hear one of the specified words, nothing more, nothing less. If enabled, the specified words can be pronounced in the middle of a whole speech stream, the engine will try to spot them.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "setVocabulary",
	    "parametersSignature": "([s]b)",
	    "description": "Set the list of words (vocabulary) that should be recognized by the speech recognition engine.",
	    "parameters": [
	        {
	            "name": "vocabulary",
	            "description": "List of words that should be recognized"
	        },
	        {
	            "name": "enabledWordSpotting",
	            "description": "If disabled, the engine expects to hear one of the specified words, nothing more, nothing less. If enabled, the specified words can be pronounced in the middle of a whole speech stream, the engine will try to spot them."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setVocabulary", [vocabulary, enabledWordSpotting])

def pause(pause:bool) -> None:
	"""
	Stop and restart the speech recognition engine according to the input parameter This can be used to add contexts, activate or deactivate rules of a contex, add a words to a slot.
	
	Parameters
	----------
	pause:bool
		Boolean to enable or disable pause of the speech recognition engine.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "pause",
	    "parametersSignature": "(b)",
	    "description": "Stop and restart the speech recognition engine according to the input parameter This can be used to add contexts, activate or deactivate rules of a contex, add a words to a slot.",
	    "parameters": [
	        {
	            "name": "pause",
	            "description": "Boolean to enable or disable pause of the speech recognition engine."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "pause", [pause])

def compile(pathToInputBNFFile:str, pathToOutputLCFFile:str, language:str) -> None:
	"""
	Convert a BNF file to a LCF file.
	
	Parameters
	----------
	pathToInputBNFFile:str
		Path to a input BNF file. This BNF file is a set of rules that should be recognized by the speech recognition engine.
	pathToOutputLCFFile:str
		Binary file which contains the same content as the BNF file. Use this file for the method addContext
	language:str
		Name of the language of the BNF file.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "compile",
	    "parametersSignature": "(sss)",
	    "description": "Convert a BNF file to a LCF file.",
	    "parameters": [
	        {
	            "name": "pathToInputBNFFile",
	            "description": "Path to a input BNF file. This BNF file is a set of rules that should be recognized by the speech recognition engine."
	        },
	        {
	            "name": "pathToOutputLCFFile",
	            "description": "Binary file which contains the same content as the BNF file. Use this file for the method addContext"
	        },
	        {
	            "name": "language",
	            "description": "Name of the language of the BNF file."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "compile", [pathToInputBNFFile, pathToOutputLCFFile, language])

def createContext(pathToGrammarFile:str, contextName:str) -> None:
	"""
	Creates a context from an LCF of FCF file.
	
	Parameters
	----------
	pathToGrammarFile:str
		Binary file containing the grammar or SLM
	contextName:str
		Name of the created context
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "createContext",
	    "parametersSignature": "(ss)",
	    "description": "Creates a context from an LCF of FCF file.",
	    "parameters": [
	        {
	            "name": "pathToGrammarFile",
	            "description": "Binary file containing the grammar or SLM"
	        },
	        {
	            "name": "contextName",
	            "description": "Name of the created context"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "createContext", [pathToGrammarFile, contextName])

def deleteContext(contextName:str) -> None:
	"""
	Delete an existing context.
	
	Parameters
	----------
	contextName:str
		Name of the context to delete
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "deleteContext",
	    "parametersSignature": "(s)",
	    "description": "Delete an existing context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to delete"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deleteContext", [contextName])

def deleteAllContexts() -> None:
	"""
	Delete all existing contexts.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "deleteAllContexts",
	    "parametersSignature": "()",
	    "description": "Delete all existing contexts.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deleteAllContexts", [])

def addContext_1(pathToLCFFile:str, contextName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (addContext)
	
	Add a context from a LCF file.
	
	Parameters
	----------
	pathToLCFFile:str
		Path to a LCF file. This LCF file contains the set of rules that should be recognized by the speech recognition engine.
	contextName:str
		Name of the context of your choice.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "addContext",
	    "parametersSignature": "(ss)",
	    "description": "Add a context from a LCF file.",
	    "parameters": [
	        {
	            "name": "pathToLCFFile",
	            "description": "Path to a LCF file. This LCF file contains the set of rules that should be recognized by the speech recognition engine."
	        },
	        {
	            "name": "contextName",
	            "description": "Name of the context of your choice."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "addContext", [pathToLCFFile, contextName])

def addContext_2(contextName:str) -> None:
	"""
	Note: This is one of the overloads of the original method (addContext)
	
	Add an existing context.
	
	Parameters
	----------
	contextName:str
		Name of the context of your choice.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "addContext",
	    "parametersSignature": "(s)",
	    "description": "Add an existing context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context of your choice."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "addContext", [contextName])

def removeContext(contextName:str) -> None:
	"""
	Remove one context from the speech recognition engine.
	
	Parameters
	----------
	contextName:str
		Name of the context to remove from the speech recognition engine.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "removeContext",
	    "parametersSignature": "(s)",
	    "description": "Remove one context from the speech recognition engine.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to remove from the speech recognition engine."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "removeContext", [contextName])

def removeAllContext() -> None:
	"""
	Remove all contexts from the speech recognition engine.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "removeAllContext",
	    "parametersSignature": "()",
	    "description": "Remove all contexts from the speech recognition engine.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "removeAllContext", [])

def pushContexts() -> None:
	"""
	Disable current contexts of the speech recognition engine and save them in a  stack.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "pushContexts",
	    "parametersSignature": "()",
	    "description": "Disable current contexts of the speech recognition engine and save them in a  stack.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "pushContexts", [])

def popContexts() -> None:
	"""
	Disable current contexts and restore saved contexts of the speech recognition engine.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "v",
	    "name": "popContexts",
	    "parametersSignature": "()",
	    "description": "Disable current contexts and restore saved contexts of the speech recognition engine.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "popContexts", [])

def createContextSet(contextList:List[str], name:str) -> bool:
	"""
	Create a context set
	
	Parameters
	----------
	contextList:List[str]
		List of context names to add to the context set
	name:str
		Name of the context set
	
	Returns
	----------
	True if a context set with the same name existed and was overwritten
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "b",
	    "name": "createContextSet",
	    "parametersSignature": "([s]s)",
	    "description": "Create a context set",
	    "parameters": [
	        {
	            "name": "contextList",
	            "description": "List of context names to add to the context set"
	        },
	        {
	            "name": "name",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": "True if a context set with the same name existed and was overwritten"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "createContextSet", [contextList, name])

def deleteContextSet(contextSetName:str) -> None:
	"""
	Erase a context set
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "deleteContextSet",
	    "parametersSignature": "(s)",
	    "description": "Erase a context set",
	    "parameters": [
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deleteContextSet", [contextSetName])

def deleteAllContextSets() -> None:
	"""
	Erase all saved contexts set of the speech recognition engine
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "deleteAllContextSets",
	    "parametersSignature": "()",
	    "description": "Erase all saved contexts set of the speech recognition engine",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deleteAllContextSets", [])

def addContextToSet(contextName:str, contextSetName:str) -> None:
	"""
	Add a context to an existing context set
	
	Parameters
	----------
	contextName:str
		Name of the context to add to the context set
	contextSetName:str
		Name of the context set
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "addContextToSet",
	    "parametersSignature": "(ss)",
	    "description": "Add a context to an existing context set",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to add to the context set"
	        },
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "addContextToSet", [contextName, contextSetName])

def removeContextFromSet(contextName:str, contextSetName:str) -> None:
	"""
	Remove a context from an existing context set
	
	Parameters
	----------
	contextName:str
		Name of the context to remove from the context set
	contextSetName:str
		Name of the context set
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "removeContextFromSet",
	    "parametersSignature": "(ss)",
	    "description": "Remove a context from an existing context set",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to remove from the context set"
	        },
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "removeContextFromSet", [contextName, contextSetName])

def addContextSet(contextSetName:str) -> None:
	"""
	Add a context set to the recognizer
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "v",
	    "name": "addContextSet",
	    "parametersSignature": "(s)",
	    "description": "Add a context set to the recognizer",
	    "parameters": [
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "addContextSet", [contextSetName])

def removeContextSet(contextSetName:str) -> None:
	"""
	Remove a saved context set from the speech recognition engine (without deleting it)
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "v",
	    "name": "removeContextSet",
	    "parametersSignature": "(s)",
	    "description": "Remove a saved context set from the speech recognition engine (without deleting it)",
	    "parameters": [
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "removeContextSet", [contextSetName])

def getContexts_1() -> List[str]:
	"""
	Note: This is one of the overloads of the original method (getContexts)
	
	Get the names of all existing contexts
	
	Returns
	----------
	List of context names
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "[s]",
	    "name": "getContexts",
	    "parametersSignature": "()",
	    "description": "Get the names of all existing contexts",
	    "parameters": [],
	    "returnDescription": "List of context names"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getContexts", [])

def getContexts_2(contextSetName:str) -> List[str]:
	"""
	Note: This is one of the overloads of the original method (getContexts)
	
	Get the names of the contexts belonging to a given context set
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	
	Returns
	----------
	List of context names
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "[s]",
	    "name": "getContexts",
	    "parametersSignature": "(s)",
	    "description": "Get the names of the contexts belonging to a given context set",
	    "parameters": [
	        {
	            "name": "contextSetName",
	            "description": "Name of the context set"
	        }
	    ],
	    "returnDescription": "List of context names"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getContexts", [contextSetName])

def getContextSets() -> List[str]:
	"""
	Get the names of the contexts belonging to a given context set
	
	Returns
	----------
	List of context set names
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "[s]",
	    "name": "getContextSets",
	    "parametersSignature": "()",
	    "description": "Get the names of the contexts belonging to a given context set",
	    "parameters": [],
	    "returnDescription": "List of context set names"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getContextSets", [])

def activateRule(contextName:str, ruleName:str) -> None:
	"""
	Activate a rule contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	ruleName:str
		Name of the rule to activate.
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "v",
	    "name": "activateRule",
	    "parametersSignature": "(ss)",
	    "description": "Activate a rule contained in the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        },
	        {
	            "name": "ruleName",
	            "description": "Name of the rule to activate."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "activateRule", [contextName, ruleName])

def deactivateRule(contextName:str, ruleName:str) -> None:
	"""
	Deactivate a rule contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	ruleName:str
		Name of the rule to deactivate.
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "v",
	    "name": "deactivateRule",
	    "parametersSignature": "(ss)",
	    "description": "Deactivate a rule contained in the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        },
	        {
	            "name": "ruleName",
	            "description": "Name of the rule to deactivate."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deactivateRule", [contextName, ruleName])

def activateAllRules(contextName:str) -> None:
	"""
	Activate all rules contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "v",
	    "name": "activateAllRules",
	    "parametersSignature": "(s)",
	    "description": "Activate all rules contained in the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "activateAllRules", [contextName])

def deactivateAllRules(contextName:str) -> None:
	"""
	Deactivate all rules contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	
	*Reference struct*
	'''
	{
	    "uid": 167,
	    "returnSignature": "v",
	    "name": "deactivateAllRules",
	    "parametersSignature": "(s)",
	    "description": "Deactivate all rules contained in the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "deactivateAllRules", [contextName])

def setContextParam(contextName:str, paramName:str, value:float) -> None:
	"""
	Set the given parameter for the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context
	paramName:str
		Name of the parameter to change
	value:float
		New parameter value
	
	*Reference struct*
	'''
	{
	    "uid": 168,
	    "returnSignature": "v",
	    "name": "setContextParam",
	    "parametersSignature": "(ssf)",
	    "description": "Set the given parameter for the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context"
	        },
	        {
	            "name": "paramName",
	            "description": "Name of the parameter to change"
	        },
	        {
	            "name": "value",
	            "description": "New parameter value"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "setContextParam", [contextName, paramName, value])

def getContextParam(contextName:str, paramName:str) -> float:
	"""
	Get the given parameter for the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context
	paramName:str
		Name of the parameter to get
	
	Returns
	----------
	Value of the fetched parameter
	
	*Reference struct*
	'''
	{
	    "uid": 169,
	    "returnSignature": "f",
	    "name": "getContextParam",
	    "parametersSignature": "(ss)",
	    "description": "Get the given parameter for the specified context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context"
	        },
	        {
	            "name": "paramName",
	            "description": "Name of the parameter to get"
	        }
	    ],
	    "returnDescription": "Value of the fetched parameter"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getContextParam", [contextName, paramName])

def addWordListToSlot(contextName:str, slotName:str, wordList:List[str]) -> None:
	"""
	Add a list of words in a slot. A slot is a part of a context which can be modified. You can add a list of words that should be recognized by the speech recognition engine
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	slotName:str
		Name of the slot to modify.
	wordList:List[str]
		List of words to insert in the slot.
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "v",
	    "name": "addWordListToSlot",
	    "parametersSignature": "(ss[s])",
	    "description": "Add a list of words in a slot. A slot is a part of a context which can be modified. You can add a list of words that should be recognized by the speech recognition engine",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        },
	        {
	            "name": "slotName",
	            "description": "Name of the slot to modify."
	        },
	        {
	            "name": "wordList",
	            "description": "List of words to insert in the slot."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "addWordListToSlot", [contextName, slotName, wordList])

def removeWordListFromSlot(contextName:str, slotName:str) -> None:
	"""
	Remove all words from a slot.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	slotName:str
		Name of the slot to modify.
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "v",
	    "name": "removeWordListFromSlot",
	    "parametersSignature": "(ss)",
	    "description": "Remove all words from a slot.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to modify."
	        },
	        {
	            "name": "slotName",
	            "description": "Name of the slot to modify."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "removeWordListFromSlot", [contextName, slotName])

def getRules(contextName:str, typeName:str) -> List[str]:
	"""
	Get all rules contained for a specific context.
	
	Parameters
	----------
	contextName:str
		Name of the context to analyze.
	typeName:str
		Type of the required rules.
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "[s]",
	    "name": "getRules",
	    "parametersSignature": "(ss)",
	    "description": "Get all rules contained for a specific context.",
	    "parameters": [
	        {
	            "name": "contextName",
	            "description": "Name of the context to analyze."
	        },
	        {
	            "name": "typeName",
	            "description": "Type of the required rules."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "getRules", [contextName, typeName])

def _isFreeSpeechToTextAvailable() -> bool:
	"""
	Enable free speech to text.
	
	Returns
	----------
	Boolean indicating whether free speech to text is available for the current language
	
	*Reference struct*
	'''
	{
	    "uid": 173,
	    "returnSignature": "b",
	    "name": "_isFreeSpeechToTextAvailable",
	    "parametersSignature": "()",
	    "description": "Enable free speech to text.",
	    "parameters": [],
	    "returnDescription": "Boolean indicating whether free speech to text is available for the current language"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_isFreeSpeechToTextAvailable", [])

def _enableFreeSpeechToText() -> None:
	"""
	Enable free speech to text.
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "v",
	    "name": "_enableFreeSpeechToText",
	    "parametersSignature": "()",
	    "description": "Enable free speech to text.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_enableFreeSpeechToText", [])

def _disableFreeSpeechToText() -> None:
	"""
	Disable free speech to text.
	
	*Reference struct*
	'''
	{
	    "uid": 175,
	    "returnSignature": "v",
	    "name": "_disableFreeSpeechToText",
	    "parametersSignature": "()",
	    "description": "Disable free speech to text.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_disableFreeSpeechToText", [])

def _connectRemote() -> None:
	"""
	Connect to remote.
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "v",
	    "name": "_connectRemote",
	    "parametersSignature": "()",
	    "description": "Connect to remote.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_connectRemote", [])

def _disconnectRemote() -> None:
	"""
	Disconnect from remote.
	
	*Reference struct*
	'''
	{
	    "uid": 177,
	    "returnSignature": "v",
	    "name": "_disconnectRemote",
	    "parametersSignature": "()",
	    "description": "Disconnect from remote.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_disconnectRemote", [])

def _setFileAsInput(fileName:str, autoSwitchToMicrophones:bool) -> bool:
	"""
	Load an audio file and set it as the robot audio input, file must be raw format recorded with start/stopAudioInputRecording
	
	Parameters
	----------
	fileName:str
		Location of the file to play.
	autoSwitchToMicrophones:bool
		Boolean, will automatically switch to microphones as audio input at the end of the file if set as True.
	
	Returns
	----------
	Is true if the audio input is set to the file.
	
	*Reference struct*
	'''
	{
	    "uid": 178,
	    "returnSignature": "b",
	    "name": "_setFileAsInput",
	    "parametersSignature": "(sb)",
	    "description": "Load an audio file and set it as the robot audio input, file must be raw format recorded with start/stopAudioInputRecording",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Location of the file to play."
	        },
	        {
	            "name": "autoSwitchToMicrophones",
	            "description": "Boolean, will automatically switch to microphones as audio input at the end of the file if set as True."
	        }
	    ],
	    "returnDescription": "Is true if the audio input is set to the file."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_setFileAsInput", [fileName, autoSwitchToMicrophones])

def _isFileAsInput() -> bool:
	"""
	Return true if the audio input is set to a file.
	
	Returns
	----------
	Is true if the audio input is set to a file.
	
	*Reference struct*
	'''
	{
	    "uid": 179,
	    "returnSignature": "b",
	    "name": "_isFileAsInput",
	    "parametersSignature": "()",
	    "description": "Return true if the audio input is set to a file.",
	    "parameters": [],
	    "returnDescription": "Is true if the audio input is set to a file."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_isFileAsInput", [])

def _isFileRead() -> bool:
	"""
	Return true if the file set as audio input is entirely read.
	
	Returns
	----------
	Is true if the file set as audio input is entirely read.
	
	*Reference struct*
	'''
	{
	    "uid": 180,
	    "returnSignature": "b",
	    "name": "_isFileRead",
	    "parametersSignature": "()",
	    "description": "Return true if the file set as audio input is entirely read.",
	    "parameters": [],
	    "returnDescription": "Is true if the file set as audio input is entirely read."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_isFileRead", [])

def _setMicrophonesAsInput() -> bool:
	"""
	Set microphones as the robot audio input.
	
	Returns
	----------
	Is true if microphones are correctly set as the audio input.
	
	*Reference struct*
	'''
	{
	    "uid": 181,
	    "returnSignature": "b",
	    "name": "_setMicrophonesAsInput",
	    "parametersSignature": "()",
	    "description": "Set microphones as the robot audio input.",
	    "parameters": [],
	    "returnDescription": "Is true if microphones are correctly set as the audio input."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_setMicrophonesAsInput", [])

def _isMicrophonesAsInput() -> bool:
	"""
	Return true if the audio input is set to the microphones.
	
	Returns
	----------
	Is true if microphones are set as the audio input.
	
	*Reference struct*
	'''
	{
	    "uid": 182,
	    "returnSignature": "b",
	    "name": "_isMicrophonesAsInput",
	    "parametersSignature": "()",
	    "description": "Return true if the audio input is set to the microphones.",
	    "parameters": [],
	    "returnDescription": "Is true if microphones are set as the audio input."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_isMicrophonesAsInput", [])

def _startAudioInputRecording(fileName:str) -> bool:
	"""
	Record all samples sent to the speech recognition in a file at wav format (16 bits le, 16Khz, 4 channels).
	
	Parameters
	----------
	fileName:str
		Location of the file to record.
	
	Returns
	----------
	Is true if file is correctly set to record audio input.
	
	*Reference struct*
	'''
	{
	    "uid": 183,
	    "returnSignature": "b",
	    "name": "_startAudioInputRecording",
	    "parametersSignature": "(s)",
	    "description": "Record all samples sent to the speech recognition in a file at wav format (16 bits le, 16Khz, 4 channels).",
	    "parameters": [
	        {
	            "name": "fileName",
	            "description": "Location of the file to record."
	        }
	    ],
	    "returnDescription": "Is true if file is correctly set to record audio input."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_startAudioInputRecording", [fileName])

def _stopAudioInputRecording() -> bool:
	"""
	Stop the recording started with _startAudioInputRecording.
	
	Returns
	----------
	Is true if audio input recording is correctly stopped.
	
	*Reference struct*
	'''
	{
	    "uid": 184,
	    "returnSignature": "b",
	    "name": "_stopAudioInputRecording",
	    "parametersSignature": "()",
	    "description": "Stop the recording started with _startAudioInputRecording.",
	    "parameters": [],
	    "returnDescription": "Is true if audio input recording is correctly stopped."
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_stopAudioInputRecording", [])

def _remoteConsumptionOk() -> int:
	"""
	Get a remote consumption speed change recommendation.
	
	Returns
	----------
	Integer indicating whether to increase, decrease or keep the remote consumption speed
	
	*Reference struct*
	'''
	{
	    "uid": 185,
	    "returnSignature": "i",
	    "name": "_remoteConsumptionOk",
	    "parametersSignature": "()",
	    "description": "Get a remote consumption speed change recommendation.",
	    "parameters": [],
	    "returnDescription": "Integer indicating whether to increase, decrease or keep the remote consumption speed"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_remoteConsumptionOk", [])

def loadVocabulary(vocabularyFile:str) -> None:
	"""
	Load the vocabulary to recognized contained in a .lxd file. This method is not available with the ASR engine language set to Chinese. For more informations see the red documentation
	
	Parameters
	----------
	vocabularyFile:str
		Name of the lxd file containing the vocabulary
	
	*Reference struct*
	'''
	{
	    "uid": 186,
	    "returnSignature": "v",
	    "name": "loadVocabulary",
	    "parametersSignature": "(s)",
	    "description": "Load the vocabulary to recognized contained in a .lxd file. This method is not available with the ASR engine language set to Chinese. For more informations see the red documentation",
	    "parameters": [
	        {
	            "name": "vocabularyFile",
	            "description": "Name of the lxd file containing the vocabulary"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "loadVocabulary", [vocabularyFile])

def _naoStoreApplicationInstalled(p0:str, p1:object, p2:str) -> None:
	"""
	Reload the engine if new application installed is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 187,
	    "returnSignature": "v",
	    "name": "_naoStoreApplicationInstalled",
	    "parametersSignature": "(sms)",
	    "description": "Reload the engine if new application installed is a language",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_naoStoreApplicationInstalled", [p0, p1, p2])

def _naoStoreApplicationUninstalled(p0:str, p1:object, p2:str) -> None:
	"""
	Reload the engine if application uninstalled is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 188,
	    "returnSignature": "v",
	    "name": "_naoStoreApplicationUninstalled",
	    "parametersSignature": "(sms)",
	    "description": "Reload the engine if application uninstalled is a language",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_naoStoreApplicationUninstalled", [p0, p1, p2])

def _enableAudioLogging(path:str) -> None:
	"""
	Enable audio dumps.
	
	Parameters
	----------
	path:str
		Path to write the dump files to. Pass an empty string to deactivate audio logging
	
	*Reference struct*
	'''
	{
	    "uid": 192,
	    "returnSignature": "v",
	    "name": "_enableAudioLogging",
	    "parametersSignature": "(s)",
	    "description": "Enable audio dumps.",
	    "parameters": [
	        {
	            "name": "path",
	            "description": "Path to write the dump files to. Pass an empty string to deactivate audio logging"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_enableAudioLogging", [path])

def _enableBeamformer() -> None:
	"""
	Enable beamformer.
	
	*Reference struct*
	'''
	{
	    "uid": 193,
	    "returnSignature": "v",
	    "name": "_enableBeamformer",
	    "parametersSignature": "()",
	    "description": "Enable beamformer.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_enableBeamformer", [])

def _disableBeamformer() -> None:
	"""
	Disable beamformer.
	
	*Reference struct*
	'''
	{
	    "uid": 194,
	    "returnSignature": "v",
	    "name": "_disableBeamformer",
	    "parametersSignature": "()",
	    "description": "Disable beamformer.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_disableBeamformer", [])

def _beamformerEnabled() -> bool:
	"""
	Get beamformer status.
	
	Returns
	----------
	Whether the beamformer is enabled or not
	
	*Reference struct*
	'''
	{
	    "uid": 195,
	    "returnSignature": "b",
	    "name": "_beamformerEnabled",
	    "parametersSignature": "()",
	    "description": "Get beamformer status.",
	    "parameters": [],
	    "returnDescription": "Whether the beamformer is enabled or not"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_beamformerEnabled", [])

def _getVersion() -> str:
	"""
	get vocon version
	
	Returns
	----------
	Version
	
	*Reference struct*
	'''
	{
	    "uid": 196,
	    "returnSignature": "s",
	    "name": "_getVersion",
	    "parametersSignature": "()",
	    "description": "get vocon version",
	    "parameters": [],
	    "returnDescription": "Version"
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_getVersion", [])

def _startEarsRotation() -> None:
	"""
	Start ears rotation
	
	*Reference struct*
	'''
	{
	    "uid": 197,
	    "returnSignature": "v",
	    "name": "_startEarsRotation",
	    "parametersSignature": "()",
	    "description": "Start ears rotation",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_startEarsRotation", [])

def _startEyesRotation() -> None:
	"""
	Start eyes rotation
	
	*Reference struct*
	'''
	{
	    "uid": 198,
	    "returnSignature": "v",
	    "name": "_startEyesRotation",
	    "parametersSignature": "()",
	    "description": "Start eyes rotation",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_startEyesRotation", [])

def _stopEarsRotation() -> None:
	"""
	Stop ears rotation
	
	*Reference struct*
	'''
	{
	    "uid": 199,
	    "returnSignature": "v",
	    "name": "_stopEarsRotation",
	    "parametersSignature": "()",
	    "description": "Stop ears rotation",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_stopEarsRotation", [])

def _stopEyesRotation() -> None:
	"""
	Stop eyes rotation
	
	*Reference struct*
	'''
	{
	    "uid": 200,
	    "returnSignature": "v",
	    "name": "_stopEyesRotation",
	    "parametersSignature": "()",
	    "description": "Stop eyes rotation",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_stopEyesRotation", [])

def _playBipStart() -> None:
	"""
	Play Bip Start
	
	*Reference struct*
	'''
	{
	    "uid": 201,
	    "returnSignature": "v",
	    "name": "_playBipStart",
	    "parametersSignature": "()",
	    "description": "Play Bip Start",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_playBipStart", [])

def _playBipStop() -> None:
	"""
	Play Bip Stop
	
	*Reference struct*
	'''
	{
	    "uid": 202,
	    "returnSignature": "v",
	    "name": "_playBipStop",
	    "parametersSignature": "()",
	    "description": "Play Bip Stop",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSpeechRecognition", "_playBipStop", [])

