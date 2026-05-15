from .gentypes import *
from .robot_client import send_mfc
import json
"""
This module allows you to control NAO's LEDs. It provides simple ways of setting or fading the intensity of single LEDs and groups of LEDs. 
Groups of LEDs typically include face LEDs, ear LEDs etc. It is also possible to control each LED separately (for example, each of the 8 LEDs in one NAO's eyes).
There are three primary colors of LEDs available - red, green and blue, so it is possible to combine them to obtain different colors. The ears contain blue LEDs only.
It is possible to control the LED's intensity (between 0 and 100%).
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
	return send_mfc("ALLeds", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALLeds", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALLeds", "metaObject", [p0])

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
	return send_mfc("ALLeds", "terminate", [p0])

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
	return send_mfc("ALLeds", "property", [p0])

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
	return send_mfc("ALLeds", "setProperty", [p0, p1])

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
	return send_mfc("ALLeds", "properties", [])

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
	return send_mfc("ALLeds", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALLeds", "isStatsEnabled", [])

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
	return send_mfc("ALLeds", "enableStats", [p0])

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
	return send_mfc("ALLeds", "stats", [])

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
	return send_mfc("ALLeds", "clearStats", [])

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
	return send_mfc("ALLeds", "isTraceEnabled", [])

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
	return send_mfc("ALLeds", "enableTrace", [p0])

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
	return send_mfc("ALLeds", "version", [])

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
	return send_mfc("ALLeds", "ping", [])

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
	return send_mfc("ALLeds", "getMethodList", [])

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
	return send_mfc("ALLeds", "getMethodHelp", [methodName])

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
	return send_mfc("ALLeds", "getModuleHelp", [])

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
	return send_mfc("ALLeds", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALLeds", "wait", [id])

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
	return send_mfc("ALLeds", "isRunning", [id])

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
	return send_mfc("ALLeds", "stop", [id])

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
	return send_mfc("ALLeds", "getBrokerName", [])

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
	return send_mfc("ALLeds", "getUsage", [name])

def createGroup(groupName:str, ledNames:List[str]) -> None:
	"""
	Makes a group name for ease of setting multiple LEDs.
	
	Parameters
	----------
	groupName:str
		The name of the group.
	ledNames:List[str]
		A vector of the names of the LEDs in the group.
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "createGroup",
	    "parametersSignature": "(s[s])",
	    "description": "Makes a group name for ease of setting multiple LEDs.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the group."
	        },
	        {
	            "name": "ledNames",
	            "description": "A vector of the names of the LEDs in the group."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "createGroup", [groupName, ledNames])

def earLedsSetAngle(degrees:int, duration:float, leaveOnAtEnd:bool) -> None:
	"""
	An animation to show a direction with the ears.
	
	Parameters
	----------
	degrees:int
		The angle you want to show in degrees (int). 0 is up, 90 is forwards, 180 is down and 270 is back.
	duration:float
		The duration in seconds of the animation.
	leaveOnAtEnd:bool
		If true the last led is left on at the end of the animation.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "earLedsSetAngle",
	    "parametersSignature": "(ifb)",
	    "description": "An animation to show a direction with the ears.",
	    "parameters": [
	        {
	            "name": "degrees",
	            "description": "The angle you want to show in degrees (int). 0 is up, 90 is forwards, 180 is down and 270 is back."
	        },
	        {
	            "name": "duration",
	            "description": "The duration in seconds of the animation."
	        },
	        {
	            "name": "leaveOnAtEnd",
	            "description": "If true the last led is left on at the end of the animation."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "earLedsSetAngle", [degrees, duration, leaveOnAtEnd])

def fade(name:str, intensity:float, duration:float) -> None:
	"""
	Sets the intensity of a LED or Group of LEDs within a given time.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity of the LED or Group (a value between 0 and 1).
	duration:float
		The duration of the fade in seconds
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "fade",
	    "parametersSignature": "(sff)",
	    "description": "Sets the intensity of a LED or Group of LEDs within a given time.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "intensity",
	            "description": "The intensity of the LED or Group (a value between 0 and 1)."
	        },
	        {
	            "name": "duration",
	            "description": "The duration of the fade in seconds"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "fade", [name, intensity, duration])

def fadeListRGB(name:str, rgbList:object, timeList:object) -> None:
	"""
	Chain a list of color for a device, as the motion.doMove command.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	rgbList:object
		List of RGB led value, RGB as seen in hexa-decimal: 0x00RRGGBB.
	timeList:object
		List of time to go to given intensity.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "fadeListRGB",
	    "parametersSignature": "(smm)",
	    "description": "Chain a list of color for a device, as the motion.doMove command.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "rgbList",
	            "description": "List of RGB led value, RGB as seen in hexa-decimal: 0x00RRGGBB."
	        },
	        {
	            "name": "timeList",
	            "description": "List of time to go to given intensity."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "fadeListRGB", [name, rgbList, timeList])

def fadeRGB_1(name:str, red:float, green:float, blue:float, duration:float) -> None:
	"""
	Note: This is one of the overloads of the original method (fadeRGB)
	
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	red:float
		the intensity of red channel (0-1).
	green:float
		the intensity of green channel (0-1).
	blue:float
		the intensity of blue channel (0-1).
	duration:float
		Time used to fade in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "fadeRGB",
	    "parametersSignature": "(sffff)",
	    "description": "Sets the color of an RGB led.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "red",
	            "description": "the intensity of red channel (0-1)."
	        },
	        {
	            "name": "green",
	            "description": "the intensity of green channel (0-1)."
	        },
	        {
	            "name": "blue",
	            "description": "the intensity of blue channel (0-1)."
	        },
	        {
	            "name": "duration",
	            "description": "Time used to fade in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "fadeRGB", [name, red, green, blue, duration])

def fadeRGB_2(name:str, colorName:str, duration:float) -> None:
	"""
	Note: This is one of the overloads of the original method (fadeRGB)
	
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	colorName:str
		the name of the color (supported colors: "white", "red", "green", "blue", "yellow", "magenta", "cyan")
	duration:float
		Time used to fade in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "fadeRGB",
	    "parametersSignature": "(ssf)",
	    "description": "Sets the color of an RGB led.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "colorName",
	            "description": "the name of the color (supported colors: \"white\", \"red\", \"green\", \"blue\", \"yellow\", \"magenta\", \"cyan\")"
	        },
	        {
	            "name": "duration",
	            "description": "Time used to fade in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "fadeRGB", [name, colorName, duration])

def fadeRGB_3(name:str, rgb:int, duration:float) -> None:
	"""
	Note: This is one of the overloads of the original method (fadeRGB)
	
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	rgb:int
		The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB.
	duration:float
		Time used to fade in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "fadeRGB",
	    "parametersSignature": "(sif)",
	    "description": "Sets the color of an RGB led.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "rgb",
	            "description": "The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB."
	        },
	        {
	            "name": "duration",
	            "description": "Time used to fade in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "fadeRGB", [name, rgb, duration])

def _fadeRGB(name:str, red:float, green:float, blue:float, duration:float) -> None:
	"""
	Sets the color of an RGB led. This private method allows to use ChestLeds.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	red:float
		the intensity of red channel (0-1).
	green:float
		the intensity of green channel (0-1).
	blue:float
		the intensity of blue channel (0-1).
	duration:float
		Time used to fade in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_fadeRGB",
	    "parametersSignature": "(sffff)",
	    "description": "Sets the color of an RGB led. This private method allows to use ChestLeds.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "red",
	            "description": "the intensity of red channel (0-1)."
	        },
	        {
	            "name": "green",
	            "description": "the intensity of green channel (0-1)."
	        },
	        {
	            "name": "blue",
	            "description": "the intensity of blue channel (0-1)."
	        },
	        {
	            "name": "duration",
	            "description": "Time used to fade in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_fadeRGB", [name, red, green, blue, duration])

def reset(name:str) -> None:
	"""
	Resets the state of the leds to default (for ex, eye LEDs are white and fully on by default).
	
	Parameters
	----------
	name:str
		The name of the LED or Group (for now, only "AllLeds" are implemented).
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "reset",
	    "parametersSignature": "(s)",
	    "description": "Resets the state of the leds to default (for ex, eye LEDs are white and fully on by default).",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group (for now, only \"AllLeds\" are implemented)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "reset", [name])

def _setIntensityRatio(name:str, intensity:float) -> None:
	"""
	Sets an intensity ratio for the leds. If the leds are asked to be set to a specific intensity, the real intensity applied on the leds will be the specific intensity multiplied by this ratio.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity ratio between 0.6 and 1.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "_setIntensityRatio",
	    "parametersSignature": "(sf)",
	    "description": "Sets an intensity ratio for the leds. If the leds are asked to be set to a specific intensity, the real intensity applied on the leds will be the specific intensity multiplied by this ratio.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "intensity",
	            "description": "The intensity ratio between 0.6 and 1."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_setIntensityRatio", [name, intensity])

def getIntensity(name:str) -> object:
	"""
	Gets the intensity of a LED or device
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	
	Returns
	----------
	The intensity of the LED or Group.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "getIntensity",
	    "parametersSignature": "(s)",
	    "description": "Gets the intensity of a LED or device",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        }
	    ],
	    "returnDescription": "The intensity of the LED or Group."
	}
	'''
	"""
	return send_mfc("ALLeds", "getIntensity", [name])

def listLEDs() -> List[str]:
	"""
	Lists the short LED names.
	
	Returns
	----------
	A vector of LED names.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "[s]",
	    "name": "listLEDs",
	    "parametersSignature": "()",
	    "description": "Lists the short LED names.",
	    "parameters": [],
	    "returnDescription": "A vector of LED names."
	}
	'''
	"""
	return send_mfc("ALLeds", "listLEDs", [])

def listLED(name:str) -> List[str]:
	"""
	Lists the devices aliased by a short LED name.
	
	Parameters
	----------
	name:str
		The name of the LED to list
	
	Returns
	----------
	A vector of device names.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "[s]",
	    "name": "listLED",
	    "parametersSignature": "(s)",
	    "description": "Lists the devices aliased by a short LED name.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED to list"
	        }
	    ],
	    "returnDescription": "A vector of device names."
	}
	'''
	"""
	return send_mfc("ALLeds", "listLED", [name])

def listGroup(groupName:str) -> List[str]:
	"""
	Lists the devices in the group.
	
	Parameters
	----------
	groupName:str
		The name of the Group.
	
	Returns
	----------
	A vector of string device names.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "[s]",
	    "name": "listGroup",
	    "parametersSignature": "(s)",
	    "description": "Lists the devices in the group.",
	    "parameters": [
	        {
	            "name": "groupName",
	            "description": "The name of the Group."
	        }
	    ],
	    "returnDescription": "A vector of string device names."
	}
	'''
	"""
	return send_mfc("ALLeds", "listGroup", [groupName])

def listGroups() -> List[str]:
	"""
	Lists available group names.
	
	Returns
	----------
	A vector of group names.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "[s]",
	    "name": "listGroups",
	    "parametersSignature": "()",
	    "description": "Lists available group names.",
	    "parameters": [],
	    "returnDescription": "A vector of group names."
	}
	'''
	"""
	return send_mfc("ALLeds", "listGroups", [])

def off(name:str) -> None:
	"""
	Switch to a minimum intensity a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "off",
	    "parametersSignature": "(s)",
	    "description": "Switch to a minimum intensity a LED or Group of LEDs.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "off", [name])

def on(name:str) -> None:
	"""
	Switch to a maximum intensity a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "v",
	    "name": "on",
	    "parametersSignature": "(s)",
	    "description": "Switch to a maximum intensity a LED or Group of LEDs.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "on", [name])

def rasta(duration:float) -> None:
	"""
	Launch a green/yellow/red rasta animation on all body.
	
	Parameters
	----------
	duration:float
		Approximate duration of the animation in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "rasta",
	    "parametersSignature": "(f)",
	    "description": "Launch a green/yellow/red rasta animation on all body.",
	    "parameters": [
	        {
	            "name": "duration",
	            "description": "Approximate duration of the animation in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "rasta", [duration])

def rotateEyes(rgb:int, timeForRotation:float, totalDuration:float) -> None:
	"""
	Launch a rotation using the leds of the eyes.
	
	Parameters
	----------
	rgb:int
		the RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB.
	timeForRotation:float
		Approximate time to make one turn.
	totalDuration:float
		Approximate duration of the animation in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "rotateEyes",
	    "parametersSignature": "(iff)",
	    "description": "Launch a rotation using the leds of the eyes.",
	    "parameters": [
	        {
	            "name": "rgb",
	            "description": "the RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB."
	        },
	        {
	            "name": "timeForRotation",
	            "description": "Approximate time to make one turn."
	        },
	        {
	            "name": "totalDuration",
	            "description": "Approximate duration of the animation in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "rotateEyes", [rgb, timeForRotation, totalDuration])

def randomEyes(duration:float) -> None:
	"""
	Launch a random animation in eyes
	
	Parameters
	----------
	duration:float
		Approximate duration of the animation in seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "randomEyes",
	    "parametersSignature": "(f)",
	    "description": "Launch a random animation in eyes",
	    "parameters": [
	        {
	            "name": "duration",
	            "description": "Approximate duration of the animation in seconds."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "randomEyes", [duration])

def setIntensity(name:str, intensity:float) -> None:
	"""
	Sets the intensity of a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity of the LED or Group (a value between 0 and 1).
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "setIntensity",
	    "parametersSignature": "(sf)",
	    "description": "Sets the intensity of a LED or Group of LEDs.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "intensity",
	            "description": "The intensity of the LED or Group (a value between 0 and 1)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "setIntensity", [name, intensity])

def _blink_1() -> None:
	"""
	Note: This is one of the overloads of the original method (_blink)
	
	Make the eyes blink once.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "_blink",
	    "parametersSignature": "()",
	    "description": "Make the eyes blink once.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_blink", [])

def _blink_2(p0:int) -> None:
	"""
	Note: This is one of the overloads of the original method (_blink)
	
	Make the eyes blink once with a eyeshadow color.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_blink",
	    "parametersSignature": "(i)",
	    "description": "Make the eyes blink once with a eyeshadow color.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_blink", [p0])

def _setAnyLedIntensity(name:str, intensity:float) -> None:
	"""
	Sets the intensity of a LED or Group of LEDs (even chest LED).
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity of the LED or Group (a value between 0 and 1).
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "v",
	    "name": "_setAnyLedIntensity",
	    "parametersSignature": "(sf)",
	    "description": "Sets the intensity of a LED or Group of LEDs (even chest LED).",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the LED or Group."
	        },
	        {
	            "name": "intensity",
	            "description": "The intensity of the LED or Group (a value between 0 and 1)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_setAnyLedIntensity", [name, intensity])

def _startPassiveBlinking_1() -> None:
	"""
	Note: This is one of the overloads of the original method (_startPassiveBlinking)
	
	Start passive blinking.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "_startPassiveBlinking",
	    "parametersSignature": "()",
	    "description": "Start passive blinking.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_startPassiveBlinking", [])

def _startPassiveBlinking_2(eyeShadow:int) -> None:
	"""
	Note: This is one of the overloads of the original method (_startPassiveBlinking)
	
	Start passive blinking with a eyeshadow color.
	
	Parameters
	----------
	eyeShadow:int
		The color of the eye shadow during and after the blink.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "_startPassiveBlinking",
	    "parametersSignature": "(i)",
	    "description": "Start passive blinking with a eyeshadow color.",
	    "parameters": [
	        {
	            "name": "eyeShadow",
	            "description": "The color of the eye shadow during and after the blink."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_startPassiveBlinking", [eyeShadow])

def _stopPassiveBlinking() -> None:
	"""
	Stop passive blinking.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "_stopPassiveBlinking",
	    "parametersSignature": "()",
	    "description": "Stop passive blinking.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_stopPassiveBlinking", [])

def _blinkWithShadow() -> None:
	"""
	Blink with a shadow.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "_blinkWithShadow",
	    "parametersSignature": "()",
	    "description": "Blink with a shadow.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_blinkWithShadow", [])

def _setTimeBetweenTwoBlinks(min:float, max:float) -> None:
	"""
	Set values for minimum and maximum time waited between two passive blinks.
	
	Parameters
	----------
	min:float
		The minimum (should be >= 0)
	max:float
		The maximum (should be >= min)
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "_setTimeBetweenTwoBlinks",
	    "parametersSignature": "(ff)",
	    "description": "Set values for minimum and maximum time waited between two passive blinks.",
	    "parameters": [
	        {
	            "name": "min",
	            "description": "The minimum (should be >= 0)"
	        },
	        {
	            "name": "max",
	            "description": "The maximum (should be >= min)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLeds", "_setTimeBetweenTwoBlinks", [min, max])

