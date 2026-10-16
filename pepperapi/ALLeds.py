"""
This module allows you to control NAO's LEDs. It provides simple ways of setting or fading the intensity of single LEDs and groups of LEDs. 
Groups of LEDs typically include face LEDs, ear LEDs etc. It is also possible to control each LED separately (for example, each of the 8 LEDs in one NAO's eyes).
There are three primary colors of LEDs available - red, green and blue, so it is possible to combine them to obtain different colors. The ears contain blue LEDs only.
It is possible to control the LED's intensity (between 0 and 100%).
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
	return call_method("ALLeds", "version", [])

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
	return call_method("ALLeds", "ping", [])

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
	return call_method("ALLeds", "getMethodList", [])

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
	return call_method("ALLeds", "getMethodHelp", [methodName])

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
	return call_method("ALLeds", "getModuleHelp", [])

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
	return call_method("ALLeds", "getBrokerName", [])

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
	return call_method("ALLeds", "getUsage", [name])

def createGroup(groupName:str, ledNames:List[str]) -> None:
	"""
	Makes a group name for ease of setting multiple LEDs.
	
	Parameters
	----------
	groupName:str
		The name of the group.
	ledNames:List[str]
		A vector of the names of the LEDs in the group.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "createGroup",
	#     "parametersSignature": "(s[s])",
	#     "description": "Makes a group name for ease of setting multiple LEDs.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the group."
	#         },
	#         {
	#             "name": "ledNames",
	#             "description": "A vector of the names of the LEDs in the group."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "createGroup", [groupName, ledNames])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "earLedsSetAngle",
	#     "parametersSignature": "(ifb)",
	#     "description": "An animation to show a direction with the ears.",
	#     "parameters": [
	#         {
	#             "name": "degrees",
	#             "description": "The angle you want to show in degrees (int). 0 is up, 90 is forwards, 180 is down and 270 is back."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "The duration in seconds of the animation."
	#         },
	#         {
	#             "name": "leaveOnAtEnd",
	#             "description": "If true the last led is left on at the end of the animation."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "earLedsSetAngle", [degrees, duration, leaveOnAtEnd])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "fade",
	#     "parametersSignature": "(sff)",
	#     "description": "Sets the intensity of a LED or Group of LEDs within a given time.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "intensity",
	#             "description": "The intensity of the LED or Group (a value between 0 and 1)."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "The duration of the fade in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "fade", [name, intensity, duration])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "fadeListRGB",
	#     "parametersSignature": "(smm)",
	#     "description": "Chain a list of color for a device, as the motion.doMove command.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "rgbList",
	#             "description": "List of RGB led value, RGB as seen in hexa-decimal: 0x00RRGGBB."
	#         },
	#         {
	#             "name": "timeList",
	#             "description": "List of time to go to given intensity."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "fadeListRGB", [name, rgbList, timeList])

@overload
def fadeRGB(name:str, rgb:int, duration:float, /) -> None:
	"""
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	rgb:int
		The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB.
	duration:float
		Time used to fade in seconds.
	
	Bridge notes
	------------
	fadeRGB has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- fadeRGB_1(str, int, float)
	- fadeRGB_2(str, str, float)
	- fadeRGB_3(str, float, float, float, float)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(sif)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "rgb",
	#             "description": "The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def fadeRGB(name:str, colorName:str, duration:float, /) -> None:
	"""
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	colorName:str
		the name of the color (supported colors: "white", "red", "green", "blue", "yellow", "magenta", "cyan")
	duration:float
		Time used to fade in seconds.
	
	Bridge notes
	------------
	fadeRGB has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- fadeRGB_1(str, int, float)
	- fadeRGB_2(str, str, float)
	- fadeRGB_3(str, float, float, float, float)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(ssf)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "colorName",
	#             "description": "the name of the color (supported colors: \"white\", \"red\", \"green\", \"blue\", \"yellow\", \"magenta\", \"cyan\")"
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def fadeRGB(name:str, red:float, green:float, blue:float, duration:float, /) -> None:
	"""
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
	
	Bridge notes
	------------
	fadeRGB has 3 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- fadeRGB_1(str, int, float)
	- fadeRGB_2(str, str, float)
	- fadeRGB_3(str, float, float, float, float)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(sffff)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "red",
	#             "description": "the intensity of red channel (0-1)."
	#         },
	#         {
	#             "name": "green",
	#             "description": "the intensity of green channel (0-1)."
	#         },
	#         {
	#             "name": "blue",
	#             "description": "the intensity of blue channel (0-1)."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def fadeRGB(*args, **kwargs):
	"""
	Bridge notes
	------------
	fadeRGB has 3 variants on the robot:
	- fadeRGB(name:str, rgb:int, duration:float), explicitly fadeRGB_1
	- fadeRGB(name:str, colorName:str, duration:float), explicitly fadeRGB_2
	- fadeRGB(name:str, red:float, green:float, blue:float, duration:float), explicitly fadeRGB_3
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALLeds.fadeRGB has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALLeds", "fadeRGB", list(args))

def fadeRGB_1(name:str, rgb:int, duration:float) -> None:
	"""
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	rgb:int
		The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB.
	duration:float
		Time used to fade in seconds.
	
	Bridge notes
	------------
	Explicit variant of fadeRGB(str, int, float). Calling fadeRGB instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(sif)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "rgb",
	#             "description": "The RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "fadeRGB", [name, rgb, duration])

def fadeRGB_2(name:str, colorName:str, duration:float) -> None:
	"""
	Sets the color of an RGB led.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	colorName:str
		the name of the color (supported colors: "white", "red", "green", "blue", "yellow", "magenta", "cyan")
	duration:float
		Time used to fade in seconds.
	
	Bridge notes
	------------
	Explicit variant of fadeRGB(str, str, float). Calling fadeRGB instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(ssf)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "colorName",
	#             "description": "the name of the color (supported colors: \"white\", \"red\", \"green\", \"blue\", \"yellow\", \"magenta\", \"cyan\")"
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "fadeRGB", [name, colorName, duration])

def fadeRGB_3(name:str, red:float, green:float, blue:float, duration:float) -> None:
	"""
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
	
	Bridge notes
	------------
	Explicit variant of fadeRGB(str, float, float, float, float). Calling fadeRGB instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "fadeRGB",
	#     "parametersSignature": "(sffff)",
	#     "description": "Sets the color of an RGB led.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "red",
	#             "description": "the intensity of red channel (0-1)."
	#         },
	#         {
	#             "name": "green",
	#             "description": "the intensity of green channel (0-1)."
	#         },
	#         {
	#             "name": "blue",
	#             "description": "the intensity of blue channel (0-1)."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "fadeRGB", [name, red, green, blue, duration])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_fadeRGB",
	#     "parametersSignature": "(sffff)",
	#     "description": "Sets the color of an RGB led. This private method allows to use ChestLeds.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "red",
	#             "description": "the intensity of red channel (0-1)."
	#         },
	#         {
	#             "name": "green",
	#             "description": "the intensity of green channel (0-1)."
	#         },
	#         {
	#             "name": "blue",
	#             "description": "the intensity of blue channel (0-1)."
	#         },
	#         {
	#             "name": "duration",
	#             "description": "Time used to fade in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_fadeRGB", [name, red, green, blue, duration])

def reset(name:str) -> None:
	"""
	Resets the state of the leds to default (for ex, eye LEDs are white and fully on by default).
	
	Parameters
	----------
	name:str
		The name of the LED or Group (for now, only "AllLeds" are implemented).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "reset",
	#     "parametersSignature": "(s)",
	#     "description": "Resets the state of the leds to default (for ex, eye LEDs are white and fully on by default).",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group (for now, only \"AllLeds\" are implemented)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "reset", [name])

def _setIntensityRatio(name:str, intensity:float) -> None:
	"""
	Sets an intensity ratio for the leds. If the leds are asked to be set to a specific intensity, the real intensity applied on the leds will be the specific intensity multiplied by this ratio.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity ratio between 0.6 and 1.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_setIntensityRatio",
	#     "parametersSignature": "(sf)",
	#     "description": "Sets an intensity ratio for the leds. If the leds are asked to be set to a specific intensity, the real intensity applied on the leds will be the specific intensity multiplied by this ratio.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "intensity",
	#             "description": "The intensity ratio between 0.6 and 1."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_setIntensityRatio", [name, intensity])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "getIntensity",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the intensity of a LED or device",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         }
	#     ],
	#     "returnDescription": "The intensity of the LED or Group."
	# }
	return call_method("ALLeds", "getIntensity", [name])

def listLEDs() -> List[str]:
	"""
	Lists the short LED names.
	
	Returns
	----------
	A vector of LED names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "listLEDs",
	#     "parametersSignature": "()",
	#     "description": "Lists the short LED names.",
	#     "parameters": [],
	#     "returnDescription": "A vector of LED names."
	# }
	return call_method("ALLeds", "listLEDs", [])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "listLED",
	#     "parametersSignature": "(s)",
	#     "description": "Lists the devices aliased by a short LED name.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED to list"
	#         }
	#     ],
	#     "returnDescription": "A vector of device names."
	# }
	return call_method("ALLeds", "listLED", [name])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "[s]",
	#     "name": "listGroup",
	#     "parametersSignature": "(s)",
	#     "description": "Lists the devices in the group.",
	#     "parameters": [
	#         {
	#             "name": "groupName",
	#             "description": "The name of the Group."
	#         }
	#     ],
	#     "returnDescription": "A vector of string device names."
	# }
	return call_method("ALLeds", "listGroup", [groupName])

def listGroups() -> List[str]:
	"""
	Lists available group names.
	
	Returns
	----------
	A vector of group names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "[s]",
	#     "name": "listGroups",
	#     "parametersSignature": "()",
	#     "description": "Lists available group names.",
	#     "parameters": [],
	#     "returnDescription": "A vector of group names."
	# }
	return call_method("ALLeds", "listGroups", [])

def off(name:str) -> None:
	"""
	Switch to a minimum intensity a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "off",
	#     "parametersSignature": "(s)",
	#     "description": "Switch to a minimum intensity a LED or Group of LEDs.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "off", [name])

def on(name:str) -> None:
	"""
	Switch to a maximum intensity a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "on",
	#     "parametersSignature": "(s)",
	#     "description": "Switch to a maximum intensity a LED or Group of LEDs.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "on", [name])

def rasta(duration:float) -> None:
	"""
	Launch a green/yellow/red rasta animation on all body.
	
	Parameters
	----------
	duration:float
		Approximate duration of the animation in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "rasta",
	#     "parametersSignature": "(f)",
	#     "description": "Launch a green/yellow/red rasta animation on all body.",
	#     "parameters": [
	#         {
	#             "name": "duration",
	#             "description": "Approximate duration of the animation in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "rasta", [duration])

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
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "rotateEyes",
	#     "parametersSignature": "(iff)",
	#     "description": "Launch a rotation using the leds of the eyes.",
	#     "parameters": [
	#         {
	#             "name": "rgb",
	#             "description": "the RGB value led, RGB as seen in hexa-decimal: 0x00RRGGBB."
	#         },
	#         {
	#             "name": "timeForRotation",
	#             "description": "Approximate time to make one turn."
	#         },
	#         {
	#             "name": "totalDuration",
	#             "description": "Approximate duration of the animation in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "rotateEyes", [rgb, timeForRotation, totalDuration])

def randomEyes(duration:float) -> None:
	"""
	Launch a random animation in eyes
	
	Parameters
	----------
	duration:float
		Approximate duration of the animation in seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "randomEyes",
	#     "parametersSignature": "(f)",
	#     "description": "Launch a random animation in eyes",
	#     "parameters": [
	#         {
	#             "name": "duration",
	#             "description": "Approximate duration of the animation in seconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "randomEyes", [duration])

def setIntensity(name:str, intensity:float) -> None:
	"""
	Sets the intensity of a LED or Group of LEDs.
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity of the LED or Group (a value between 0 and 1).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "setIntensity",
	#     "parametersSignature": "(sf)",
	#     "description": "Sets the intensity of a LED or Group of LEDs.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "intensity",
	#             "description": "The intensity of the LED or Group (a value between 0 and 1)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "setIntensity", [name, intensity])

@overload
def _blink() -> None:
	"""
	Make the eyes blink once.
	
	Bridge notes
	------------
	_blink has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "_blink",
	#     "parametersSignature": "()",
	#     "description": "Make the eyes blink once.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _blink(p0:int, /) -> None:
	"""
	Make the eyes blink once with a eyeshadow color.
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	_blink has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "_blink",
	#     "parametersSignature": "(i)",
	#     "description": "Make the eyes blink once with a eyeshadow color.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _blink(*args, **kwargs):
	"""
	Bridge notes
	------------
	_blink has 2 variants on the robot:
	- _blink()
	- _blink(p0:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALLeds._blink has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALLeds", "_blink", list(args))

def _setAnyLedIntensity(name:str, intensity:float) -> None:
	"""
	Sets the intensity of a LED or Group of LEDs (even chest LED).
	
	Parameters
	----------
	name:str
		The name of the LED or Group.
	intensity:float
		The intensity of the LED or Group (a value between 0 and 1).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "_setAnyLedIntensity",
	#     "parametersSignature": "(sf)",
	#     "description": "Sets the intensity of a LED or Group of LEDs (even chest LED).",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the LED or Group."
	#         },
	#         {
	#             "name": "intensity",
	#             "description": "The intensity of the LED or Group (a value between 0 and 1)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_setAnyLedIntensity", [name, intensity])

@overload
def _startPassiveBlinking() -> None:
	"""
	Start passive blinking.
	
	Bridge notes
	------------
	_startPassiveBlinking has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "_startPassiveBlinking",
	#     "parametersSignature": "()",
	#     "description": "Start passive blinking.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _startPassiveBlinking(eyeShadow:int, /) -> None:
	"""
	Start passive blinking with a eyeshadow color.
	
	Parameters
	----------
	eyeShadow:int
		The color of the eye shadow during and after the blink.
	
	Bridge notes
	------------
	_startPassiveBlinking has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "v",
	#     "name": "_startPassiveBlinking",
	#     "parametersSignature": "(i)",
	#     "description": "Start passive blinking with a eyeshadow color.",
	#     "parameters": [
	#         {
	#             "name": "eyeShadow",
	#             "description": "The color of the eye shadow during and after the blink."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def _startPassiveBlinking(*args, **kwargs):
	"""
	Bridge notes
	------------
	_startPassiveBlinking has 2 variants on the robot:
	- _startPassiveBlinking()
	- _startPassiveBlinking(eyeShadow:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALLeds._startPassiveBlinking has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALLeds", "_startPassiveBlinking", list(args))

def _stopPassiveBlinking() -> None:
	"""
	Stop passive blinking.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "_stopPassiveBlinking",
	#     "parametersSignature": "()",
	#     "description": "Stop passive blinking.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_stopPassiveBlinking", [])

def _blinkWithShadow() -> None:
	"""
	Blink with a shadow.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "v",
	#     "name": "_blinkWithShadow",
	#     "parametersSignature": "()",
	#     "description": "Blink with a shadow.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_blinkWithShadow", [])

def _setTimeBetweenTwoBlinks(min:float, max:float) -> None:
	"""
	Set values for minimum and maximum time waited between two passive blinks.
	
	Parameters
	----------
	min:float
		The minimum (should be >= 0)
	max:float
		The maximum (should be >= min)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "_setTimeBetweenTwoBlinks",
	#     "parametersSignature": "(ff)",
	#     "description": "Set values for minimum and maximum time waited between two passive blinks.",
	#     "parameters": [
	#         {
	#             "name": "min",
	#             "description": "The minimum (should be >= 0)"
	#         },
	#         {
	#             "name": "max",
	#             "description": "The maximum (should be >= min)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLeds", "_setTimeBetweenTwoBlinks", [min, max])

