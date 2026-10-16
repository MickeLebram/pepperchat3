"""
ALSpeechRecognition gives access to the embedded voice recognition system. It can be dynamically modified. This class allows user to load the current words list that should be recognized. The result of the recognition engine is located in the ALMemory's key: "WordRecognized". The structure of the result is an array :  [ (string) word , (float) confidence ]
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
	return call_method("ALSpeechRecognition", "version", [])

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
	return call_method("ALSpeechRecognition", "ping", [])

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
	return call_method("ALSpeechRecognition", "getMethodList", [])

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
	return call_method("ALSpeechRecognition", "getMethodHelp", [methodName])

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
	return call_method("ALSpeechRecognition", "getModuleHelp", [])

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
	return call_method("ALSpeechRecognition", "getBrokerName", [])

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
	return call_method("ALSpeechRecognition", "getUsage", [name])

@overload
def subscribe(name:str, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def subscribe(name:str, period:int, precision:float, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(sif)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds) if relevant."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor if relevant."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def subscribe(*args, **kwargs):
	"""
	Bridge notes
	------------
	subscribe has 2 variants on the robot:
	- subscribe(name:str)
	- subscribe(name:str, period:int, precision:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALSpeechRecognition.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALSpeechRecognition", "subscribe", list(args))

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Unsubscribes from the extractor.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which had subscribed."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "updatePeriod",
	#     "parametersSignature": "(si)",
	#     "description": "Updates the period if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "updatePrecision",
	#     "parametersSignature": "(sf)",
	#     "description": "Updates the precision if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "i",
	#     "name": "getCurrentPeriod",
	#     "parametersSignature": "()",
	#     "description": "Gets the current period.",
	#     "parameters": [],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALSpeechRecognition", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "f",
	#     "name": "getCurrentPrecision",
	#     "parametersSignature": "()",
	#     "description": "Gets the current precision.",
	#     "parameters": [],
	#     "returnDescription": "Precision of the extractor."
	# }
	return call_method("ALSpeechRecognition", "getCurrentPrecision", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "getMyPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the period for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         }
	#     ],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALSpeechRecognition", "getMyPeriod", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "f",
	#     "name": "getMyPrecision",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the precision for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of the module which has subscribed"
	#         }
	#     ],
	#     "returnDescription": "precision of the extractor"
	# }
	return call_method("ALSpeechRecognition", "getMyPrecision", [name])

def getSubscribersInfo() -> object:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getSubscribersInfo",
	#     "parametersSignature": "()",
	#     "description": "Gets the parameters given by the module.",
	#     "parameters": [],
	#     "returnDescription": "Array of names and parameters of all subscribers."
	# }
	return call_method("ALSpeechRecognition", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getOutputNames",
	#     "parametersSignature": "()",
	#     "description": "Get the list of values updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of values updated by this extractor in ALMemory"
	# }
	return call_method("ALSpeechRecognition", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getEventList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALSpeechRecognition", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "getMemoryKeyList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALSpeechRecognition", "getMemoryKeyList", [])

def setVisualExpression(setOrNot:bool) -> None:
	"""
	Enable or disable the leds animations showing the state of the recognition engine during the recognition process.
	
	Parameters
	----------
	setOrNot:bool
		Enable (true) or disable it (false).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "setVisualExpression",
	#     "parametersSignature": "(b)",
	#     "description": "Enable or disable the leds animations showing the state of the recognition engine during the recognition process.",
	#     "parameters": [
	#         {
	#             "name": "setOrNot",
	#             "description": "Enable (true) or disable it (false)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setVisualExpression", [setOrNot])

def setVisualExpressionMode(mode:int) -> None:
	"""
	Sets the LED animation mode
	
	Parameters
	----------
	mode:int
		animation mode: 0: deactivated, 1: eyes, 2: ears, 3: full
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "setVisualExpressionMode",
	#     "parametersSignature": "(i)",
	#     "description": "Sets the LED animation mode",
	#     "parameters": [
	#         {
	#             "name": "mode",
	#             "description": "animation mode: 0: deactivated, 1: eyes, 2: ears, 3: full"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setVisualExpressionMode", [mode])

def setAudioExpression(setOrNot:bool) -> None:
	"""
	Enable or disable the playing of sounds indicating the state of the recognition engine. If this option is enabled, a sound is played at the beginning of the recognition process (after a call to the subscribe method), and a sound is played when the user call the unsubscribe method
	
	Parameters
	----------
	setOrNot:bool
		Enable (true) or disable it (false).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "setAudioExpression",
	#     "parametersSignature": "(b)",
	#     "description": "Enable or disable the playing of sounds indicating the state of the recognition engine. If this option is enabled, a sound is played at the beginning of the recognition process (after a call to the subscribe method), and a sound is played when the user call the unsubscribe method",
	#     "parameters": [
	#         {
	#             "name": "setOrNot",
	#             "description": "Enable (true) or disable it (false)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setAudioExpression", [setOrNot])

def getAudioExpression() -> bool:
	"""
	To check if audio expression is enabled or disabled.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "getAudioExpression",
	#     "parametersSignature": "()",
	#     "description": "To check if audio expression is enabled or disabled.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "getAudioExpression", [])

def setLanguage(languageName:str) -> None:
	"""
	Set the language used by the speech recognition engine. The list of the available languages can be collected through the getAvailableLanguages method. If you want to set a language as the default language (loading automatically at module launch), please refer to the web page of the robot.
	
	Parameters
	----------
	languageName:str
		Name of the language in English.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "setLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "Set the language used by the speech recognition engine. The list of the available languages can be collected through the getAvailableLanguages method. If you want to set a language as the default language (loading automatically at module launch), please refer to the web page of the robot.",
	#     "parameters": [
	#         {
	#             "name": "languageName",
	#             "description": "Name of the language in English."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setLanguage", [languageName])

def _setDefaultLanguage(pLanguage:str) -> None:
	"""
	Set a language as the default language for the Speech Recognition engine
	
	Parameters
	----------
	pLanguage:str
		The language among those available on your robot as a String
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_setDefaultLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "Set a language as the default language for the Speech Recognition engine",
	#     "parameters": [
	#         {
	#             "name": "pLanguage",
	#             "description": "The language among those available on your robot as a String"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_setDefaultLanguage", [pLanguage])

def getLanguage() -> str:
	"""
	Return the current language used by the speech recognition system.
	
	Returns
	----------
	Current language used by the speech recognition engine.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "s",
	#     "name": "getLanguage",
	#     "parametersSignature": "()",
	#     "description": "Return the current language used by the speech recognition system.",
	#     "parameters": [],
	#     "returnDescription": "Current language used by the speech recognition engine."
	# }
	return call_method("ALSpeechRecognition", "getLanguage", [])

def getAvailableLanguages() -> List[str]:
	"""
	Return the list of the languages installed on the system.
	
	Returns
	----------
	Array of strings that contains the list of the installed languages.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "[s]",
	#     "name": "getAvailableLanguages",
	#     "parametersSignature": "()",
	#     "description": "Return the list of the languages installed on the system.",
	#     "parameters": [],
	#     "returnDescription": "Array of strings that contains the list of the installed languages."
	# }
	return call_method("ALSpeechRecognition", "getAvailableLanguages", [])

@overload
def setParameter(paramName:str, paramValue:bool, /) -> None:
	"""
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
	
	Bridge notes
	------------
	setParameter has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- setParameter_bool(str, bool)
	- setParameter_float(str, float)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(sb)",
	#     "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter."
	#         },
	#         {
	#             "name": "paramValue",
	#             "description": "Value of the parameter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setParameter(paramName:str, paramValue:float, /) -> None:
	"""
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
	
	Bridge notes
	------------
	setParameter has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- setParameter_bool(str, bool)
	- setParameter_float(str, float)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(sf)",
	#     "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter."
	#         },
	#         {
	#             "name": "paramValue",
	#             "description": "Value of the parameter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setParameter(*args, **kwargs):
	"""
	Bridge notes
	------------
	setParameter has 2 variants on the robot:
	- setParameter(paramName:str, paramValue:bool), explicitly setParameter_bool
	- setParameter(paramName:str, paramValue:float), explicitly setParameter_float
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALSpeechRecognition.setParameter has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALSpeechRecognition", "setParameter", list(args))

def setParameter_bool(paramName:str, paramValue:bool) -> None:
	"""
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
	
	Bridge notes
	------------
	Explicit variant of setParameter(str, bool). Calling setParameter instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(sb)",
	#     "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter."
	#         },
	#         {
	#             "name": "paramValue",
	#             "description": "Value of the parameter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setParameter", [paramName, paramValue])

def setParameter_float(paramName:str, paramValue:float) -> None:
	"""
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
	
	Bridge notes
	------------
	Explicit variant of setParameter(str, float). Calling setParameter instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(sf)",
	#     "description": "Set a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be set.\nThe parameters that can be set and the corresponding values are:\n\"Sensitivity\" - Values : range is [0.0; 1.0].\n\"Timeout\" - Values :  default values 3000 ms. Timeout for the remote recognition\n\"MinimumTrailingSilence\" : Values : 0 (no) or 1 (yes) - Applies a High-Pass filter on the input signal - default value is 0.\n",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter."
	#         },
	#         {
	#             "name": "paramValue",
	#             "description": "Value of the parameter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setParameter", [paramName, paramValue])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "f",
	#     "name": "getParameter",
	#     "parametersSignature": "(s)",
	#     "description": "Get a parameter of the speech recognition engine. Note that when the ASR engine language is set to Chinese, no parameter can be retrieved",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter."
	#         }
	#     ],
	#     "returnDescription": "Value of the parameter."
	# }
	return call_method("ALSpeechRecognition", "getParameter", [paramName])

def setWordListAsVocabulary(vocabulary:List[str]) -> None:
	"""
	Set the list of words (vocabulary) that should be recognized by the speech recognition engine.
	
	Parameters
	----------
	vocabulary:List[str]
		List of words that should be recognized
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "setWordListAsVocabulary",
	#     "parametersSignature": "([s])",
	#     "description": "Set the list of words (vocabulary) that should be recognized by the speech recognition engine.",
	#     "parameters": [
	#         {
	#             "name": "vocabulary",
	#             "description": "List of words that should be recognized"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setWordListAsVocabulary", [vocabulary])

def setVocabulary(vocabulary:List[str], enabledWordSpotting:bool) -> None:
	"""
	Set the list of words (vocabulary) that should be recognized by the speech recognition engine.
	
	Parameters
	----------
	vocabulary:List[str]
		List of words that should be recognized
	enabledWordSpotting:bool
		If disabled, the engine expects to hear one of the specified words, nothing more, nothing less. If enabled, the specified words can be pronounced in the middle of a whole speech stream, the engine will try to spot them.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "setVocabulary",
	#     "parametersSignature": "([s]b)",
	#     "description": "Set the list of words (vocabulary) that should be recognized by the speech recognition engine.",
	#     "parameters": [
	#         {
	#             "name": "vocabulary",
	#             "description": "List of words that should be recognized"
	#         },
	#         {
	#             "name": "enabledWordSpotting",
	#             "description": "If disabled, the engine expects to hear one of the specified words, nothing more, nothing less. If enabled, the specified words can be pronounced in the middle of a whole speech stream, the engine will try to spot them."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setVocabulary", [vocabulary, enabledWordSpotting])

def pause(pause:bool) -> None:
	"""
	Stop and restart the speech recognition engine according to the input parameter This can be used to add contexts, activate or deactivate rules of a contex, add a words to a slot.
	
	Parameters
	----------
	pause:bool
		Boolean to enable or disable pause of the speech recognition engine.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "pause",
	#     "parametersSignature": "(b)",
	#     "description": "Stop and restart the speech recognition engine according to the input parameter This can be used to add contexts, activate or deactivate rules of a contex, add a words to a slot.",
	#     "parameters": [
	#         {
	#             "name": "pause",
	#             "description": "Boolean to enable or disable pause of the speech recognition engine."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "pause", [pause])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "compile",
	#     "parametersSignature": "(sss)",
	#     "description": "Convert a BNF file to a LCF file.",
	#     "parameters": [
	#         {
	#             "name": "pathToInputBNFFile",
	#             "description": "Path to a input BNF file. This BNF file is a set of rules that should be recognized by the speech recognition engine."
	#         },
	#         {
	#             "name": "pathToOutputLCFFile",
	#             "description": "Binary file which contains the same content as the BNF file. Use this file for the method addContext"
	#         },
	#         {
	#             "name": "language",
	#             "description": "Name of the language of the BNF file."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "compile", [pathToInputBNFFile, pathToOutputLCFFile, language])

def createContext(pathToGrammarFile:str, contextName:str) -> None:
	"""
	Creates a context from an LCF of FCF file.
	
	Parameters
	----------
	pathToGrammarFile:str
		Binary file containing the grammar or SLM
	contextName:str
		Name of the created context
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "createContext",
	#     "parametersSignature": "(ss)",
	#     "description": "Creates a context from an LCF of FCF file.",
	#     "parameters": [
	#         {
	#             "name": "pathToGrammarFile",
	#             "description": "Binary file containing the grammar or SLM"
	#         },
	#         {
	#             "name": "contextName",
	#             "description": "Name of the created context"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "createContext", [pathToGrammarFile, contextName])

def deleteContext(contextName:str) -> None:
	"""
	Delete an existing context.
	
	Parameters
	----------
	contextName:str
		Name of the context to delete
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "deleteContext",
	#     "parametersSignature": "(s)",
	#     "description": "Delete an existing context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to delete"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deleteContext", [contextName])

def deleteAllContexts() -> None:
	"""
	Delete all existing contexts.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "deleteAllContexts",
	#     "parametersSignature": "()",
	#     "description": "Delete all existing contexts.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deleteAllContexts", [])

@overload
def addContext(contextName:str, /) -> None:
	"""
	Add an existing context.
	
	Parameters
	----------
	contextName:str
		Name of the context of your choice.
	
	Bridge notes
	------------
	addContext has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "addContext",
	#     "parametersSignature": "(s)",
	#     "description": "Add an existing context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context of your choice."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def addContext(pathToLCFFile:str, contextName:str, /) -> None:
	"""
	Add a context from a LCF file.
	
	Parameters
	----------
	pathToLCFFile:str
		Path to a LCF file. This LCF file contains the set of rules that should be recognized by the speech recognition engine.
	contextName:str
		Name of the context of your choice.
	
	Bridge notes
	------------
	addContext has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "addContext",
	#     "parametersSignature": "(ss)",
	#     "description": "Add a context from a LCF file.",
	#     "parameters": [
	#         {
	#             "name": "pathToLCFFile",
	#             "description": "Path to a LCF file. This LCF file contains the set of rules that should be recognized by the speech recognition engine."
	#         },
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context of your choice."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def addContext(*args, **kwargs):
	"""
	Bridge notes
	------------
	addContext has 2 variants on the robot:
	- addContext(contextName:str)
	- addContext(pathToLCFFile:str, contextName:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALSpeechRecognition.addContext has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALSpeechRecognition", "addContext", list(args))

def removeContext(contextName:str) -> None:
	"""
	Remove one context from the speech recognition engine.
	
	Parameters
	----------
	contextName:str
		Name of the context to remove from the speech recognition engine.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "removeContext",
	#     "parametersSignature": "(s)",
	#     "description": "Remove one context from the speech recognition engine.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to remove from the speech recognition engine."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "removeContext", [contextName])

def removeAllContext() -> None:
	"""
	Remove all contexts from the speech recognition engine.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "removeAllContext",
	#     "parametersSignature": "()",
	#     "description": "Remove all contexts from the speech recognition engine.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "removeAllContext", [])

def pushContexts() -> None:
	"""
	Disable current contexts of the speech recognition engine and save them in a  stack.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "pushContexts",
	#     "parametersSignature": "()",
	#     "description": "Disable current contexts of the speech recognition engine and save them in a  stack.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "pushContexts", [])

def popContexts() -> None:
	"""
	Disable current contexts and restore saved contexts of the speech recognition engine.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "v",
	#     "name": "popContexts",
	#     "parametersSignature": "()",
	#     "description": "Disable current contexts and restore saved contexts of the speech recognition engine.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "popContexts", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "b",
	#     "name": "createContextSet",
	#     "parametersSignature": "([s]s)",
	#     "description": "Create a context set",
	#     "parameters": [
	#         {
	#             "name": "contextList",
	#             "description": "List of context names to add to the context set"
	#         },
	#         {
	#             "name": "name",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": "True if a context set with the same name existed and was overwritten"
	# }
	return call_method("ALSpeechRecognition", "createContextSet", [contextList, name])

def deleteContextSet(contextSetName:str) -> None:
	"""
	Erase a context set
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "deleteContextSet",
	#     "parametersSignature": "(s)",
	#     "description": "Erase a context set",
	#     "parameters": [
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deleteContextSet", [contextSetName])

def deleteAllContextSets() -> None:
	"""
	Erase all saved contexts set of the speech recognition engine
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "v",
	#     "name": "deleteAllContextSets",
	#     "parametersSignature": "()",
	#     "description": "Erase all saved contexts set of the speech recognition engine",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deleteAllContextSets", [])

def addContextToSet(contextName:str, contextSetName:str) -> None:
	"""
	Add a context to an existing context set
	
	Parameters
	----------
	contextName:str
		Name of the context to add to the context set
	contextSetName:str
		Name of the context set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "addContextToSet",
	#     "parametersSignature": "(ss)",
	#     "description": "Add a context to an existing context set",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to add to the context set"
	#         },
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "addContextToSet", [contextName, contextSetName])

def removeContextFromSet(contextName:str, contextSetName:str) -> None:
	"""
	Remove a context from an existing context set
	
	Parameters
	----------
	contextName:str
		Name of the context to remove from the context set
	contextSetName:str
		Name of the context set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "removeContextFromSet",
	#     "parametersSignature": "(ss)",
	#     "description": "Remove a context from an existing context set",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to remove from the context set"
	#         },
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "removeContextFromSet", [contextName, contextSetName])

def addContextSet(contextSetName:str) -> None:
	"""
	Add a context set to the recognizer
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "v",
	#     "name": "addContextSet",
	#     "parametersSignature": "(s)",
	#     "description": "Add a context set to the recognizer",
	#     "parameters": [
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "addContextSet", [contextSetName])

def removeContextSet(contextSetName:str) -> None:
	"""
	Remove a saved context set from the speech recognition engine (without deleting it)
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "v",
	#     "name": "removeContextSet",
	#     "parametersSignature": "(s)",
	#     "description": "Remove a saved context set from the speech recognition engine (without deleting it)",
	#     "parameters": [
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "removeContextSet", [contextSetName])

@overload
def getContexts() -> List[str]:
	"""
	Get the names of all existing contexts
	
	Returns
	----------
	List of context names
	
	Bridge notes
	------------
	getContexts has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "[s]",
	#     "name": "getContexts",
	#     "parametersSignature": "()",
	#     "description": "Get the names of all existing contexts",
	#     "parameters": [],
	#     "returnDescription": "List of context names"
	# }
	...

@overload
def getContexts(contextSetName:str, /) -> List[str]:
	"""
	Get the names of the contexts belonging to a given context set
	
	Parameters
	----------
	contextSetName:str
		Name of the context set
	
	Returns
	----------
	List of context names
	
	Bridge notes
	------------
	getContexts has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "[s]",
	#     "name": "getContexts",
	#     "parametersSignature": "(s)",
	#     "description": "Get the names of the contexts belonging to a given context set",
	#     "parameters": [
	#         {
	#             "name": "contextSetName",
	#             "description": "Name of the context set"
	#         }
	#     ],
	#     "returnDescription": "List of context names"
	# }
	...

def getContexts(*args, **kwargs):
	"""
	Bridge notes
	------------
	getContexts has 2 variants on the robot:
	- getContexts()
	- getContexts(contextSetName:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALSpeechRecognition.getContexts has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALSpeechRecognition", "getContexts", list(args))

def getContextSets() -> List[str]:
	"""
	Get the names of the contexts belonging to a given context set
	
	Returns
	----------
	List of context set names
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "[s]",
	#     "name": "getContextSets",
	#     "parametersSignature": "()",
	#     "description": "Get the names of the contexts belonging to a given context set",
	#     "parameters": [],
	#     "returnDescription": "List of context set names"
	# }
	return call_method("ALSpeechRecognition", "getContextSets", [])

def activateRule(contextName:str, ruleName:str) -> None:
	"""
	Activate a rule contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	ruleName:str
		Name of the rule to activate.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "v",
	#     "name": "activateRule",
	#     "parametersSignature": "(ss)",
	#     "description": "Activate a rule contained in the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         },
	#         {
	#             "name": "ruleName",
	#             "description": "Name of the rule to activate."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "activateRule", [contextName, ruleName])

def deactivateRule(contextName:str, ruleName:str) -> None:
	"""
	Deactivate a rule contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	ruleName:str
		Name of the rule to deactivate.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "v",
	#     "name": "deactivateRule",
	#     "parametersSignature": "(ss)",
	#     "description": "Deactivate a rule contained in the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         },
	#         {
	#             "name": "ruleName",
	#             "description": "Name of the rule to deactivate."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deactivateRule", [contextName, ruleName])

def activateAllRules(contextName:str) -> None:
	"""
	Activate all rules contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "v",
	#     "name": "activateAllRules",
	#     "parametersSignature": "(s)",
	#     "description": "Activate all rules contained in the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "activateAllRules", [contextName])

def deactivateAllRules(contextName:str) -> None:
	"""
	Deactivate all rules contained in the specified context.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "v",
	#     "name": "deactivateAllRules",
	#     "parametersSignature": "(s)",
	#     "description": "Deactivate all rules contained in the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "deactivateAllRules", [contextName])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "v",
	#     "name": "setContextParam",
	#     "parametersSignature": "(ssf)",
	#     "description": "Set the given parameter for the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context"
	#         },
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter to change"
	#         },
	#         {
	#             "name": "value",
	#             "description": "New parameter value"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "setContextParam", [contextName, paramName, value])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "f",
	#     "name": "getContextParam",
	#     "parametersSignature": "(ss)",
	#     "description": "Get the given parameter for the specified context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context"
	#         },
	#         {
	#             "name": "paramName",
	#             "description": "Name of the parameter to get"
	#         }
	#     ],
	#     "returnDescription": "Value of the fetched parameter"
	# }
	return call_method("ALSpeechRecognition", "getContextParam", [contextName, paramName])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "v",
	#     "name": "addWordListToSlot",
	#     "parametersSignature": "(ss[s])",
	#     "description": "Add a list of words in a slot. A slot is a part of a context which can be modified. You can add a list of words that should be recognized by the speech recognition engine",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         },
	#         {
	#             "name": "slotName",
	#             "description": "Name of the slot to modify."
	#         },
	#         {
	#             "name": "wordList",
	#             "description": "List of words to insert in the slot."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "addWordListToSlot", [contextName, slotName, wordList])

def removeWordListFromSlot(contextName:str, slotName:str) -> None:
	"""
	Remove all words from a slot.
	
	Parameters
	----------
	contextName:str
		Name of the context to modify.
	slotName:str
		Name of the slot to modify.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "v",
	#     "name": "removeWordListFromSlot",
	#     "parametersSignature": "(ss)",
	#     "description": "Remove all words from a slot.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to modify."
	#         },
	#         {
	#             "name": "slotName",
	#             "description": "Name of the slot to modify."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "removeWordListFromSlot", [contextName, slotName])

def getRules(contextName:str, typeName:str) -> List[str]:
	"""
	Get all rules contained for a specific context.
	
	Parameters
	----------
	contextName:str
		Name of the context to analyze.
	typeName:str
		Type of the required rules.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "[s]",
	#     "name": "getRules",
	#     "parametersSignature": "(ss)",
	#     "description": "Get all rules contained for a specific context.",
	#     "parameters": [
	#         {
	#             "name": "contextName",
	#             "description": "Name of the context to analyze."
	#         },
	#         {
	#             "name": "typeName",
	#             "description": "Type of the required rules."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "getRules", [contextName, typeName])

def _isFreeSpeechToTextAvailable() -> bool:
	"""
	Enable free speech to text.
	
	Returns
	----------
	Boolean indicating whether free speech to text is available for the current language
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "b",
	#     "name": "_isFreeSpeechToTextAvailable",
	#     "parametersSignature": "()",
	#     "description": "Enable free speech to text.",
	#     "parameters": [],
	#     "returnDescription": "Boolean indicating whether free speech to text is available for the current language"
	# }
	return call_method("ALSpeechRecognition", "_isFreeSpeechToTextAvailable", [])

def _enableFreeSpeechToText() -> None:
	"""
	Enable free speech to text.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "v",
	#     "name": "_enableFreeSpeechToText",
	#     "parametersSignature": "()",
	#     "description": "Enable free speech to text.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_enableFreeSpeechToText", [])

def _disableFreeSpeechToText() -> None:
	"""
	Disable free speech to text.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "v",
	#     "name": "_disableFreeSpeechToText",
	#     "parametersSignature": "()",
	#     "description": "Disable free speech to text.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_disableFreeSpeechToText", [])

def _connectRemote() -> None:
	"""
	Connect to remote.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "v",
	#     "name": "_connectRemote",
	#     "parametersSignature": "()",
	#     "description": "Connect to remote.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_connectRemote", [])

def _disconnectRemote() -> None:
	"""
	Disconnect from remote.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "v",
	#     "name": "_disconnectRemote",
	#     "parametersSignature": "()",
	#     "description": "Disconnect from remote.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_disconnectRemote", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "b",
	#     "name": "_setFileAsInput",
	#     "parametersSignature": "(sb)",
	#     "description": "Load an audio file and set it as the robot audio input, file must be raw format recorded with start/stopAudioInputRecording",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Location of the file to play."
	#         },
	#         {
	#             "name": "autoSwitchToMicrophones",
	#             "description": "Boolean, will automatically switch to microphones as audio input at the end of the file if set as True."
	#         }
	#     ],
	#     "returnDescription": "Is true if the audio input is set to the file."
	# }
	return call_method("ALSpeechRecognition", "_setFileAsInput", [fileName, autoSwitchToMicrophones])

def _isFileAsInput() -> bool:
	"""
	Return true if the audio input is set to a file.
	
	Returns
	----------
	Is true if the audio input is set to a file.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 179,
	#     "returnSignature": "b",
	#     "name": "_isFileAsInput",
	#     "parametersSignature": "()",
	#     "description": "Return true if the audio input is set to a file.",
	#     "parameters": [],
	#     "returnDescription": "Is true if the audio input is set to a file."
	# }
	return call_method("ALSpeechRecognition", "_isFileAsInput", [])

def _isFileRead() -> bool:
	"""
	Return true if the file set as audio input is entirely read.
	
	Returns
	----------
	Is true if the file set as audio input is entirely read.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "b",
	#     "name": "_isFileRead",
	#     "parametersSignature": "()",
	#     "description": "Return true if the file set as audio input is entirely read.",
	#     "parameters": [],
	#     "returnDescription": "Is true if the file set as audio input is entirely read."
	# }
	return call_method("ALSpeechRecognition", "_isFileRead", [])

def _setMicrophonesAsInput() -> bool:
	"""
	Set microphones as the robot audio input.
	
	Returns
	----------
	Is true if microphones are correctly set as the audio input.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "b",
	#     "name": "_setMicrophonesAsInput",
	#     "parametersSignature": "()",
	#     "description": "Set microphones as the robot audio input.",
	#     "parameters": [],
	#     "returnDescription": "Is true if microphones are correctly set as the audio input."
	# }
	return call_method("ALSpeechRecognition", "_setMicrophonesAsInput", [])

def _isMicrophonesAsInput() -> bool:
	"""
	Return true if the audio input is set to the microphones.
	
	Returns
	----------
	Is true if microphones are set as the audio input.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "b",
	#     "name": "_isMicrophonesAsInput",
	#     "parametersSignature": "()",
	#     "description": "Return true if the audio input is set to the microphones.",
	#     "parameters": [],
	#     "returnDescription": "Is true if microphones are set as the audio input."
	# }
	return call_method("ALSpeechRecognition", "_isMicrophonesAsInput", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "b",
	#     "name": "_startAudioInputRecording",
	#     "parametersSignature": "(s)",
	#     "description": "Record all samples sent to the speech recognition in a file at wav format (16 bits le, 16Khz, 4 channels).",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Location of the file to record."
	#         }
	#     ],
	#     "returnDescription": "Is true if file is correctly set to record audio input."
	# }
	return call_method("ALSpeechRecognition", "_startAudioInputRecording", [fileName])

def _stopAudioInputRecording() -> bool:
	"""
	Stop the recording started with _startAudioInputRecording.
	
	Returns
	----------
	Is true if audio input recording is correctly stopped.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "b",
	#     "name": "_stopAudioInputRecording",
	#     "parametersSignature": "()",
	#     "description": "Stop the recording started with _startAudioInputRecording.",
	#     "parameters": [],
	#     "returnDescription": "Is true if audio input recording is correctly stopped."
	# }
	return call_method("ALSpeechRecognition", "_stopAudioInputRecording", [])

def _remoteConsumptionOk() -> int:
	"""
	Get a remote consumption speed change recommendation.
	
	Returns
	----------
	Integer indicating whether to increase, decrease or keep the remote consumption speed
	"""
	# NAOqi metadata:
	# {
	#     "uid": 185,
	#     "returnSignature": "i",
	#     "name": "_remoteConsumptionOk",
	#     "parametersSignature": "()",
	#     "description": "Get a remote consumption speed change recommendation.",
	#     "parameters": [],
	#     "returnDescription": "Integer indicating whether to increase, decrease or keep the remote consumption speed"
	# }
	return call_method("ALSpeechRecognition", "_remoteConsumptionOk", [])

def loadVocabulary(vocabularyFile:str) -> None:
	"""
	Load the vocabulary to recognized contained in a .lxd file. This method is not available with the ASR engine language set to Chinese. For more informations see the red documentation
	
	Parameters
	----------
	vocabularyFile:str
		Name of the lxd file containing the vocabulary
	"""
	# NAOqi metadata:
	# {
	#     "uid": 186,
	#     "returnSignature": "v",
	#     "name": "loadVocabulary",
	#     "parametersSignature": "(s)",
	#     "description": "Load the vocabulary to recognized contained in a .lxd file. This method is not available with the ASR engine language set to Chinese. For more informations see the red documentation",
	#     "parameters": [
	#         {
	#             "name": "vocabularyFile",
	#             "description": "Name of the lxd file containing the vocabulary"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "loadVocabulary", [vocabularyFile])

def _naoStoreApplicationInstalled(p0:str, p1:object, p2:str) -> None:
	"""
	Reload the engine if new application installed is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 187,
	#     "returnSignature": "v",
	#     "name": "_naoStoreApplicationInstalled",
	#     "parametersSignature": "(sms)",
	#     "description": "Reload the engine if new application installed is a language",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_naoStoreApplicationInstalled", [p0, p1, p2])

def _naoStoreApplicationUninstalled(p0:str, p1:object, p2:str) -> None:
	"""
	Reload the engine if application uninstalled is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 188,
	#     "returnSignature": "v",
	#     "name": "_naoStoreApplicationUninstalled",
	#     "parametersSignature": "(sms)",
	#     "description": "Reload the engine if application uninstalled is a language",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_naoStoreApplicationUninstalled", [p0, p1, p2])

def _systemSoundSetChanged() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 189,
	#     "returnSignature": "v",
	#     "name": "_systemSoundSetChanged",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_systemSoundSetChanged", [])

def _silentNextBipOn() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 190,
	#     "returnSignature": "v",
	#     "name": "_silentNextBipOn",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_silentNextBipOn", [])

def _silentNextBipOff() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 191,
	#     "returnSignature": "v",
	#     "name": "_silentNextBipOff",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_silentNextBipOff", [])

def _enableAudioLogging(path:str) -> None:
	"""
	Enable audio dumps.
	
	Parameters
	----------
	path:str
		Path to write the dump files to. Pass an empty string to deactivate audio logging
	"""
	# NAOqi metadata:
	# {
	#     "uid": 192,
	#     "returnSignature": "v",
	#     "name": "_enableAudioLogging",
	#     "parametersSignature": "(s)",
	#     "description": "Enable audio dumps.",
	#     "parameters": [
	#         {
	#             "name": "path",
	#             "description": "Path to write the dump files to. Pass an empty string to deactivate audio logging"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_enableAudioLogging", [path])

def _enableBeamformer() -> None:
	"""
	Enable beamformer.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 193,
	#     "returnSignature": "v",
	#     "name": "_enableBeamformer",
	#     "parametersSignature": "()",
	#     "description": "Enable beamformer.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_enableBeamformer", [])

def _disableBeamformer() -> None:
	"""
	Disable beamformer.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 194,
	#     "returnSignature": "v",
	#     "name": "_disableBeamformer",
	#     "parametersSignature": "()",
	#     "description": "Disable beamformer.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_disableBeamformer", [])

def _beamformerEnabled() -> bool:
	"""
	Get beamformer status.
	
	Returns
	----------
	Whether the beamformer is enabled or not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 195,
	#     "returnSignature": "b",
	#     "name": "_beamformerEnabled",
	#     "parametersSignature": "()",
	#     "description": "Get beamformer status.",
	#     "parameters": [],
	#     "returnDescription": "Whether the beamformer is enabled or not"
	# }
	return call_method("ALSpeechRecognition", "_beamformerEnabled", [])

def _getVersion() -> str:
	"""
	get vocon version
	
	Returns
	----------
	Version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 196,
	#     "returnSignature": "s",
	#     "name": "_getVersion",
	#     "parametersSignature": "()",
	#     "description": "get vocon version",
	#     "parameters": [],
	#     "returnDescription": "Version"
	# }
	return call_method("ALSpeechRecognition", "_getVersion", [])

def _startEarsRotation() -> None:
	"""
	Start ears rotation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 197,
	#     "returnSignature": "v",
	#     "name": "_startEarsRotation",
	#     "parametersSignature": "()",
	#     "description": "Start ears rotation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_startEarsRotation", [])

def _startEyesRotation() -> None:
	"""
	Start eyes rotation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 198,
	#     "returnSignature": "v",
	#     "name": "_startEyesRotation",
	#     "parametersSignature": "()",
	#     "description": "Start eyes rotation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_startEyesRotation", [])

def _stopEarsRotation() -> None:
	"""
	Stop ears rotation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 199,
	#     "returnSignature": "v",
	#     "name": "_stopEarsRotation",
	#     "parametersSignature": "()",
	#     "description": "Stop ears rotation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_stopEarsRotation", [])

def _stopEyesRotation() -> None:
	"""
	Stop eyes rotation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 200,
	#     "returnSignature": "v",
	#     "name": "_stopEyesRotation",
	#     "parametersSignature": "()",
	#     "description": "Stop eyes rotation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_stopEyesRotation", [])

def _playBipStart() -> None:
	"""
	Play Bip Start
	"""
	# NAOqi metadata:
	# {
	#     "uid": 201,
	#     "returnSignature": "v",
	#     "name": "_playBipStart",
	#     "parametersSignature": "()",
	#     "description": "Play Bip Start",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_playBipStart", [])

def _playBipStop() -> None:
	"""
	Play Bip Stop
	"""
	# NAOqi metadata:
	# {
	#     "uid": 202,
	#     "returnSignature": "v",
	#     "name": "_playBipStop",
	#     "parametersSignature": "()",
	#     "description": "Play Bip Stop",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSpeechRecognition", "_playBipStop", [])

