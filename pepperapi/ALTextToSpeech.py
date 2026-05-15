from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module embeds a speech synthetizer whose role is to convert text commands into sound waves that are then either sent to Nao's loudspeakers or written into a file. This service supports several languages and some parameters of the synthetizer can be tuned to change each language's synthetic voice.
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
	return send_mfc("ALTextToSpeech", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALTextToSpeech", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALTextToSpeech", "metaObject", [p0])

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
	return send_mfc("ALTextToSpeech", "terminate", [p0])

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
	return send_mfc("ALTextToSpeech", "property", [p0])

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
	return send_mfc("ALTextToSpeech", "setProperty", [p0, p1])

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
	return send_mfc("ALTextToSpeech", "properties", [])

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
	return send_mfc("ALTextToSpeech", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALTextToSpeech", "isStatsEnabled", [])

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
	return send_mfc("ALTextToSpeech", "enableStats", [p0])

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
	return send_mfc("ALTextToSpeech", "stats", [])

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
	return send_mfc("ALTextToSpeech", "clearStats", [])

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
	return send_mfc("ALTextToSpeech", "isTraceEnabled", [])

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
	return send_mfc("ALTextToSpeech", "enableTrace", [p0])

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
	return send_mfc("ALTextToSpeech", "version", [])

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
	return send_mfc("ALTextToSpeech", "ping", [])

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
	return send_mfc("ALTextToSpeech", "getMethodList", [])

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
	return send_mfc("ALTextToSpeech", "getMethodHelp", [methodName])

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
	return send_mfc("ALTextToSpeech", "getModuleHelp", [])

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
	return send_mfc("ALTextToSpeech", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALTextToSpeech", "wait", [id])

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
	return send_mfc("ALTextToSpeech", "isRunning", [id])

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
	return send_mfc("ALTextToSpeech", "stop", [id])

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
	return send_mfc("ALTextToSpeech", "getBrokerName", [])

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
	return send_mfc("ALTextToSpeech", "getUsage", [name])

def say_1(stringToSay:str) -> None:
	"""
	Note: This is one of the overloads of the original method (say)
	
	Performs the text-to-speech operations : it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8.
	
	Parameters
	----------
	stringToSay:str
		Text to say, encoded in UTF-8.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "say",
	    "parametersSignature": "(s)",
	    "description": "Performs the text-to-speech operations : it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8.",
	    "parameters": [
	        {
	            "name": "stringToSay",
	            "description": "Text to say, encoded in UTF-8."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "say", [stringToSay])

def say_2(stringToSay:str, language:str) -> None:
	"""
	Note: This is one of the overloads of the original method (say)
	
	Performs the text-to-speech operations in a specific language: it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8. Once the text is said, the language is set back to its initial value.
	
	Parameters
	----------
	stringToSay:str
		Text to say, encoded in UTF-8.
	language:str
		Language used to say the text.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "say",
	    "parametersSignature": "(ss)",
	    "description": "Performs the text-to-speech operations in a specific language: it takes a std::string as input and outputs a sound in both speakers. String encoding must be UTF8. Once the text is said, the language is set back to its initial value.",
	    "parameters": [
	        {
	            "name": "stringToSay",
	            "description": "Text to say, encoded in UTF-8."
	        },
	        {
	            "name": "language",
	            "description": "Language used to say the text."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "say", [stringToSay, language])

def sayToFile(pStringToSay:str, pFileName:str) -> None:
	"""
	Performs the text-to-speech operations: it takes a std::string as input and outputs the corresponding audio signal in the specified file.
	
	Parameters
	----------
	pStringToSay:str
		Text to say, encoded in UTF-8.
	pFileName:str
		RAW file where to store the generated signal. The signal is encoded with a sample rate of 22050Hz, format S16_LE, 2 channels.
	
	Returns
	----------
	Id of the task. Can be used to interrupt it.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "sayToFile",
	    "parametersSignature": "(ss)",
	    "description": "Performs the text-to-speech operations: it takes a std::string as input and outputs the corresponding audio signal in the specified file.",
	    "parameters": [
	        {
	            "name": "pStringToSay",
	            "description": "Text to say, encoded in UTF-8."
	        },
	        {
	            "name": "pFileName",
	            "description": "RAW file where to store the generated signal. The signal is encoded with a sample rate of 22050Hz, format S16_LE, 2 channels."
	        }
	    ],
	    "returnDescription": "Id of the task. Can be used to interrupt it."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "sayToFile", [pStringToSay, pFileName])

def stopAll() -> None:
	"""
	This method stops the current and all the pending tasks immediately.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "stopAll",
	    "parametersSignature": "()",
	    "description": "This method stops the current and all the pending tasks immediately.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "stopAll", [])

def setLanguage(pLanguage:str) -> None:
	"""
	Changes the language used by the Text-to-Speech engine. It automatically changes the voice used since each of them is related to a unique language. If you want that change to take effect automatically after reboot of your robot, refer to the robot web page (setting page).
	
	Parameters
	----------
	pLanguage:str
		Language name. Must belong to the languages available in TTS (can be obtained with the getAvailableLanguages method).  It should be an identifier std::string.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "setLanguage",
	    "parametersSignature": "(s)",
	    "description": "Changes the language used by the Text-to-Speech engine. It automatically changes the voice used since each of them is related to a unique language. If you want that change to take effect automatically after reboot of your robot, refer to the robot web page (setting page).",
	    "parameters": [
	        {
	            "name": "pLanguage",
	            "description": "Language name. Must belong to the languages available in TTS (can be obtained with the getAvailableLanguages method).  It should be an identifier std::string."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "setLanguage", [pLanguage])

def getLanguage() -> str:
	"""
	Returns the language currently used by the text-to-speech engine.
	
	Returns
	----------
	Language of the current voice.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "s",
	    "name": "getLanguage",
	    "parametersSignature": "()",
	    "description": "Returns the language currently used by the text-to-speech engine.",
	    "parameters": [],
	    "returnDescription": "Language of the current voice."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getLanguage", [])

def getAvailableLanguages() -> List[str]:
	"""
	Outputs the languages installed on the system.
	
	Returns
	----------
	Array of std::string that contains the languages installed on the system.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "[s]",
	    "name": "getAvailableLanguages",
	    "parametersSignature": "()",
	    "description": "Outputs the languages installed on the system.",
	    "parameters": [],
	    "returnDescription": "Array of std::string that contains the languages installed on the system."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getAvailableLanguages", [])

def getSupportedLanguages() -> List[str]:
	"""
	Outputs all the languages supported (may be installed or not).
	
	Returns
	----------
	Array of std::string that contains all the supported languages (may be installed or not).
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[s]",
	    "name": "getSupportedLanguages",
	    "parametersSignature": "()",
	    "description": "Outputs all the languages supported (may be installed or not).",
	    "parameters": [],
	    "returnDescription": "Array of std::string that contains all the supported languages (may be installed or not)."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getSupportedLanguages", [])

def resetSpeed() -> None:
	"""
	*Parsing issues:*
		*Mismatch between 'parameters' and 'parametersSignature'*
		
	Changes the parameters of the voice. For now, it is only possible to reset the voice speed.
	
	Returns
	----------
	(int) >= 0 if successful, negative error code if failed Vincent : pas sûr que cette fonction balance un truc en sortie
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "resetSpeed",
	    "parametersSignature": "()",
	    "description": "Changes the parameters of the voice. For now, it is only possible to reset the voice speed.",
	    "parameters": [
	        {
	            "name": "pEffectName",
	            "description": "Name of the parameter."
	        }
	    ],
	    "returnDescription": "(int) >= 0 if successful, negative error code if failed Vincent : pas s\u00fbr que cette fonction balance un truc en sortie"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "resetSpeed", [])

def setParameter(pEffectName:str, pEffectValue:float) -> None:
	"""
	Changes the parameters of the voice. The available parameters are: 
	 	 pitchShift: applies a pitch shifting to the voice. The value indicates the ratio between the new fundamental frequencies and the old ones (examples: 2.0: an octave above, 1.5: a quint above). Correct range is (1.0 -- 4), or 0 to disable effect.
	 	 doubleVoice: adds a second voice to the first one. The value indicates the ratio between the second voice fundamental frequency and the first one. Correct range is (1.0 -- 4), or 0 to disable effect 
	 	 doubleVoiceLevel: the corresponding value is the level of the double voice (1.0: equal to the main voice one). Correct range is (0 -- 4). 
	 	 doubleVoiceTimeShift: the corresponding value is the delay between the double voice and the main one. Correct range is (0 -- 0.5) 
	 If the effect value is not available, the effect parameter remains unchanged.
	
	Parameters
	----------
	pEffectName:str
		Name of the parameter.
	pEffectValue:float
		Value of the parameter.
	
	Returns
	----------
	(int) >= 0 if successful, negative error code if failed Vincent : pas sûr que cette fonction balance un truc en sortie
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "setParameter",
	    "parametersSignature": "(sf)",
	    "description": "Changes the parameters of the voice. The available parameters are: \n \t pitchShift: applies a pitch shifting to the voice. The value indicates the ratio between the new fundamental frequencies and the old ones (examples: 2.0: an octave above, 1.5: a quint above). Correct range is (1.0 -- 4), or 0 to disable effect.\n \t doubleVoice: adds a second voice to the first one. The value indicates the ratio between the second voice fundamental frequency and the first one. Correct range is (1.0 -- 4), or 0 to disable effect \n \t doubleVoiceLevel: the corresponding value is the level of the double voice (1.0: equal to the main voice one). Correct range is (0 -- 4). \n \t doubleVoiceTimeShift: the corresponding value is the delay between the double voice and the main one. Correct range is (0 -- 0.5) \n If the effect value is not available, the effect parameter remains unchanged.",
	    "parameters": [
	        {
	            "name": "pEffectName",
	            "description": "Name of the parameter."
	        },
	        {
	            "name": "pEffectValue",
	            "description": "Value of the parameter."
	        }
	    ],
	    "returnDescription": "(int) >= 0 if successful, negative error code if failed Vincent : pas s\u00fbr que cette fonction balance un truc en sortie"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "setParameter", [pEffectName, pEffectValue])

def getParameter(pParameterName:str) -> float:
	"""
	Returns the value of one of the voice parameters. The available parameters are: "pitchShift", "doubleVoice","doubleVoiceLevel" and "doubleVoiceTimeShift"
	
	Parameters
	----------
	pParameterName:str
		Name of the parameter.
	
	Returns
	----------
	Value of the specified parameter
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "f",
	    "name": "getParameter",
	    "parametersSignature": "(s)",
	    "description": "Returns the value of one of the voice parameters. The available parameters are: \"pitchShift\", \"doubleVoice\",\"doubleVoiceLevel\" and \"doubleVoiceTimeShift\"",
	    "parameters": [
	        {
	            "name": "pParameterName",
	            "description": "Name of the parameter."
	        }
	    ],
	    "returnDescription": "Value of the specified parameter"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getParameter", [pParameterName])

def setVoice(pVoiceID:str) -> None:
	"""
	Changes the voice used by the text-to-speech engine. The voice identifier must belong to the installed voices, that can be listed using the 'getAvailableVoices' method. If the voice is not available, it remains unchanged. No exception is thrown in this case. For the time being, only two voices are available by default : Kenny22Enhanced (English voice) and Julie22Enhanced (French voice)
	
	Parameters
	----------
	pVoiceID:str
		The voice (as a std::string).
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "setVoice",
	    "parametersSignature": "(s)",
	    "description": "Changes the voice used by the text-to-speech engine. The voice identifier must belong to the installed voices, that can be listed using the 'getAvailableVoices' method. If the voice is not available, it remains unchanged. No exception is thrown in this case. For the time being, only two voices are available by default : Kenny22Enhanced (English voice) and Julie22Enhanced (French voice)",
	    "parameters": [
	        {
	            "name": "pVoiceID",
	            "description": "The voice (as a std::string)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "setVoice", [pVoiceID])

def getVoice() -> str:
	"""
	Returns the voice currently used by the text-to-speech engine.
	
	Returns
	----------
	Name of the current voice
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "s",
	    "name": "getVoice",
	    "parametersSignature": "()",
	    "description": "Returns the voice currently used by the text-to-speech engine.",
	    "parameters": [],
	    "returnDescription": "Name of the current voice"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getVoice", [])

def getAvailableVoices() -> List[str]:
	"""
	Outputs the available voices. The returned list contains the voice IDs.
	
	Returns
	----------
	 Array of std::string containing the voices installed on the system.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "[s]",
	    "name": "getAvailableVoices",
	    "parametersSignature": "()",
	    "description": "Outputs the available voices. The returned list contains the voice IDs.",
	    "parameters": [],
	    "returnDescription": " Array of std::string containing the voices installed on the system."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getAvailableVoices", [])

def setVolume(volume:float) -> None:
	"""
	Sets the volume of text-to-speech output.
	
	Parameters
	----------
	volume:float
		Volume (between 0.0 and 1.0).
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "setVolume",
	    "parametersSignature": "(f)",
	    "description": "Sets the volume of text-to-speech output.",
	    "parameters": [
	        {
	            "name": "volume",
	            "description": "Volume (between 0.0 and 1.0)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "setVolume", [volume])

def getVolume() -> float:
	"""
	Fetches the current volume the text to speech.
	
	Returns
	----------
	Volume (integer between 0 and 100).
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "f",
	    "name": "getVolume",
	    "parametersSignature": "()",
	    "description": "Fetches the current volume the text to speech.",
	    "parameters": [],
	    "returnDescription": "Volume (integer between 0 and 100)."
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "getVolume", [])

def locale() -> str:
	"""
	Get the locale associate to the current language.
	
	Returns
	----------
	A string with xx_XX format (region_country)
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "s",
	    "name": "locale",
	    "parametersSignature": "()",
	    "description": "Get the locale associate to the current language.",
	    "parameters": [],
	    "returnDescription": "A string with xx_XX format (region_country)"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "locale", [])

def loadVoicePreference(pPreferenceName:str) -> None:
	"""
	Loads a set of voice parameters defined in a xml file contained in the preferences folder.The name of the xml file must begin with ALTextToSpeech_Voice_ 
	
	Parameters
	----------
	pPreferenceName:str
		Name of the voice preference.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "loadVoicePreference",
	    "parametersSignature": "(s)",
	    "description": "Loads a set of voice parameters defined in a xml file contained in the preferences folder.The name of the xml file must begin with ALTextToSpeech_Voice_ ",
	    "parameters": [
	        {
	            "name": "pPreferenceName",
	            "description": "Name of the voice preference."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "loadVoicePreference", [pPreferenceName])

def _setDefaultLanguage(Language:str) -> None:
	"""
	Sets a language as the default language for the synthesis engine
	
	Parameters
	----------
	Language:str
		The language among those available on your robot as a String
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "_setDefaultLanguage",
	    "parametersSignature": "(s)",
	    "description": "Sets a language as the default language for the synthesis engine",
	    "parameters": [
	        {
	            "name": "Language",
	            "description": "The language among those available on your robot as a String"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_setDefaultLanguage", [Language])

def setLanguageDefaultVoice(Language:str, Voice:str) -> None:
	"""
	Sets a voice as the default voice for the corresponding language
	
	Parameters
	----------
	Language:str
		The language among those available on your robot as a String
	Voice:str
		The voice among those available on your robot as a String
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "setLanguageDefaultVoice",
	    "parametersSignature": "(ss)",
	    "description": "Sets a voice as the default voice for the corresponding language",
	    "parameters": [
	        {
	            "name": "Language",
	            "description": "The language among those available on your robot as a String"
	        },
	        {
	            "name": "Voice",
	            "description": "The voice among those available on your robot as a String"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "setLanguageDefaultVoice", [Language, Voice])

def _setDefaultVoice() -> None:
	"""
	Sets the default voice for the current language, if there's one.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "_setDefaultVoice",
	    "parametersSignature": "()",
	    "description": "Sets the default voice for the current language, if there's one.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_setDefaultVoice", [])

def _naoStoreApplicationInstalled(p0:str, p1:object, p2:str) -> None:
	"""
	reload the engine if new application installed is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "_naoStoreApplicationInstalled",
	    "parametersSignature": "(sms)",
	    "description": "reload the engine if new application installed is a language",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_naoStoreApplicationInstalled", [p0, p1, p2])

def _naoStoreApplicationUninstalled(p0:str, p1:object, p2:str) -> None:
	"""
	reload the engine if application uninstalled is a language
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_naoStoreApplicationUninstalled",
	    "parametersSignature": "(sms)",
	    "description": "reload the engine if application uninstalled is a language",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_naoStoreApplicationUninstalled", [p0, p1, p2])

def _pause() -> None:
	"""
	Pause the current synthesis
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_pause",
	    "parametersSignature": "()",
	    "description": "Pause the current synthesis",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_pause", [])

def _resume() -> None:
	"""
	Resume the current synthesis
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_resume",
	    "parametersSignature": "()",
	    "description": "Resume the current synthesis",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_resume", [])

def _enableFilter(enable:bool) -> None:
	"""
	Enables the filtering of audio output
	
	Parameters
	----------
	enable:bool
		activate or not
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_enableFilter",
	    "parametersSignature": "(b)",
	    "description": "Enables the filtering of audio output",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "activate or not"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_enableFilter", [enable])

def _loadEffect(effectPath:str) -> None:
	"""
	Load an effect on the voice.
	
	Parameters
	----------
	effectPath:str
		path to the file of the effect to load.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "_loadEffect",
	    "parametersSignature": "(s)",
	    "description": "Load an effect on the voice.",
	    "parameters": [
	        {
	            "name": "effectPath",
	            "description": "path to the file of the effect to load."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_loadEffect", [effectPath])

def _applyEffect(effectName:str, enable:bool) -> None:
	"""
	Enables the filtering of audio output
	
	Parameters
	----------
	effectName:str
		name of the effect
	enable:bool
		activate or not
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "_applyEffect",
	    "parametersSignature": "(sb)",
	    "description": "Enables the filtering of audio output",
	    "parameters": [
	        {
	            "name": "effectName",
	            "description": "name of the effect"
	        },
	        {
	            "name": "enable",
	            "description": "activate or not"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_applyEffect", [effectName, enable])

def _diagnosis() -> None:
	"""
	Logs info about the current state of the TTS.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_diagnosis",
	    "parametersSignature": "()",
	    "description": "Logs info about the current state of the TTS.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_diagnosis", [])

def _showVoiceSettings() -> None:
	"""
	Logs voice settings.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "_showVoiceSettings",
	    "parametersSignature": "()",
	    "description": "Logs voice settings.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_showVoiceSettings", [])

def showDictionary() -> None:
	"""
	Shows the Dictionary.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "showDictionary",
	    "parametersSignature": "()",
	    "description": "Shows the Dictionary.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "showDictionary", [])

def reset() -> None:
	"""
	Reset ALTextToSpeech to his default state.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "reset",
	    "parametersSignature": "()",
	    "description": "Reset ALTextToSpeech to his default state.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "reset", [])

def _unloadDictionary() -> None:
	"""
	Unload the dictionary.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "v",
	    "name": "_unloadDictionary",
	    "parametersSignature": "()",
	    "description": "Unload the dictionary.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_unloadDictionary", [])

def deleteFromDictionary_1(word:str, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (deleteFromDictionary)
	
	Unload the dictionary.
	
	Parameters
	----------
	word:str
		the word you wish to delete, does not have to be in japanese.
	p1:str
		
	
	Returns
	----------
	bool: true if succeeded, false if failed
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "b",
	    "name": "deleteFromDictionary",
	    "parametersSignature": "(ss)",
	    "description": "Unload the dictionary.",
	    "parameters": [
	        {
	            "name": "word",
	            "description": "the word you wish to delete, does not have to be in japanese."
	        }
	    ],
	    "returnDescription": "bool: true if succeeded, false if failed"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "deleteFromDictionary", [word, p1])

def deleteFromDictionary_2(word:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (deleteFromDictionary)
	
	Unload the dictionary.
	
	Parameters
	----------
	word:str
		the word you wish to delete, does not have to be in japanese.
	
	Returns
	----------
	bool: true if succeeded, false if failed
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "b",
	    "name": "deleteFromDictionary",
	    "parametersSignature": "(s)",
	    "description": "Unload the dictionary.",
	    "parameters": [
	        {
	            "name": "word",
	            "description": "the word you wish to delete, does not have to be in japanese."
	        }
	    ],
	    "returnDescription": "bool: true if succeeded, false if failed"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "deleteFromDictionary", [word])

def addToDictionary_1(type:str, word:str, priority:str, phonetic:str, accent:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (addToDictionary)
	
	Add a word to the library
	
	Parameters
	----------
	type:str
		the type of word you wish to insert, does not have to be in japanese.
	word:str
		the word you wish to insert, does not have to be in japanese.
	priority:str
		the priority of the word.
	phonetic:str
		the phonetic pronouciation in KATAKANA.
	accent:str
		syllabus and accentuation
	
	Returns
	----------
	bool: true if succeeded, false if failed
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "addToDictionary",
	    "parametersSignature": "(sssss)",
	    "description": "Add a word to the library",
	    "parameters": [
	        {
	            "name": "type",
	            "description": "the type of word you wish to insert, does not have to be in japanese."
	        },
	        {
	            "name": "word",
	            "description": "the word you wish to insert, does not have to be in japanese."
	        },
	        {
	            "name": "priority",
	            "description": "the priority of the word."
	        },
	        {
	            "name": "phonetic",
	            "description": "the phonetic pronouciation in KATAKANA."
	        },
	        {
	            "name": "accent",
	            "description": "syllabus and accentuation"
	        }
	    ],
	    "returnDescription": "bool: true if succeeded, false if failed"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "addToDictionary", [type, word, priority, phonetic, accent])

def addToDictionary_2(text:str, toReplace:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (addToDictionary)
	
	Add a word to the library
	
	Parameters
	----------
	text:str
		the text you wish to insert.
	toReplace:str
		text to replace.
	
	Returns
	----------
	bool: true if succeeded, false if failed
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "b",
	    "name": "addToDictionary",
	    "parametersSignature": "(ss)",
	    "description": "Add a word to the library",
	    "parameters": [
	        {
	            "name": "text",
	            "description": "the text you wish to insert."
	        },
	        {
	            "name": "toReplace",
	            "description": "text to replace."
	        }
	    ],
	    "returnDescription": "bool: true if succeeded, false if failed"
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "addToDictionary", [text, toReplace])

def _loadDictionary() -> None:
	"""
	TODO
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "_loadDictionary",
	    "parametersSignature": "()",
	    "description": "TODO",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTextToSpeech", "_loadDictionary", [])

