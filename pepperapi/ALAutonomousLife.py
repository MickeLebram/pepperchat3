"""
Manages the focused Activity and Autonomous Life state
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class AutonomousAbilityStatus:
	"""NAOqi signature: (sbb)<AutonomousAbilityStatus,name,enabled,running>"""
	name: str
	enabled: bool
	running: bool


@dataclass
class ActivityTransitionInfo:
	"""NAOqi signature: (Lssss)<ActivityTransitionInfo,TransitionTime,PreviousActivityName,PreviousActivityStopReason,FocusedActivityName,FocusedActivityStartReason>"""
	TransitionTime: int
	PreviousActivityName: str
	PreviousActivityStopReason: str
	FocusedActivityName: str
	FocusedActivityStartReason: str


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
	return call_method("ALAutonomousLife", "version", [])

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
	return call_method("ALAutonomousLife", "ping", [])

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
	return call_method("ALAutonomousLife", "getMethodList", [])

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
	return call_method("ALAutonomousLife", "getMethodHelp", [methodName])

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
	return call_method("ALAutonomousLife", "getModuleHelp", [])

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
	return call_method("ALAutonomousLife", "getBrokerName", [])

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
	return call_method("ALAutonomousLife", "getUsage", [name])

def _onPreferenceChanged(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_onPreferenceChanged", [p1, p2, p3])

def onReady(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "onReady",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "onReady", [p1, p2, p3])

def _onRobotHealthChanged(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_onRobotHealthChanged",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_onRobotHealthChanged", [p1, p2, p3])

def _onPushRecovery(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_onPushRecovery",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_onPushRecovery", [p1, p2, p3])

def _onFallRecovery(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_onFallRecovery",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_onFallRecovery", [p1, p2, p3])

def _onRobotMoved(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_onRobotMoved",
	#     "parametersSignature": "(sms)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         },
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_onRobotMoved", [p1, p2, p3])

def _setStateChangeEnabled(enabled:bool) -> None:
	"""
	
	
	Parameters
	----------
	enabled:bool
		Enabled/Disable the setState() method.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "_setStateChangeEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "enabled",
	#             "description": "Enabled/Disable the setState() method."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_setStateChangeEnabled", [enabled])

def _loadConfigFile(p:str) -> None:
	"""
	
	
	Parameters
	----------
	p:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_loadConfigFile",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_loadConfigFile", [p])

def setState(state:str) -> None:
	"""
	Programatically control the state of Autonomous Life
	
	Parameters
	----------
	state:str
		The possible states of AutonomousLife are: interactive, solitary, safeguard, disabled
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "setState",
	#     "parametersSignature": "(s)",
	#     "description": "Programatically control the state of Autonomous Life",
	#     "parameters": [
	#         {
	#             "name": "state",
	#             "description": "The possible states of AutonomousLife are: interactive, solitary, safeguard, disabled"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "setState", [state])

def getState() -> str:
	"""
	Returns the current state of AutonomousLife
	
	Returns
	----------
	Can be: solitary, interactive, safeguard, disabled
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getState",
	#     "parametersSignature": "()",
	#     "description": "Returns the current state of AutonomousLife",
	#     "parameters": [],
	#     "returnDescription": "Can be: solitary, interactive, safeguard, disabled"
	# }
	return call_method("ALAutonomousLife", "getState", [])

def focusedActivity() -> str:
	"""
	Returns the currently focused activity
	
	Returns
	----------
	The name of the focused activity
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "s",
	#     "name": "focusedActivity",
	#     "parametersSignature": "()",
	#     "description": "Returns the currently focused activity",
	#     "parameters": [],
	#     "returnDescription": "The name of the focused activity"
	# }
	return call_method("ALAutonomousLife", "focusedActivity", [])

@overload
def switchFocus(activity_name:str, /) -> None:
	"""
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	
	Bridge notes
	------------
	switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "switchFocus",
	#     "parametersSignature": "(s)",
	#     "description": "Set an activity as running with user focus",
	#     "parameters": [
	#         {
	#             "name": "activity_name",
	#             "description": "The package_name/activity_name to run"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def switchFocus(activity_name:str, flags:int, /) -> None:
	"""
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	flags:int
		Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)
	
	Bridge notes
	------------
	switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "switchFocus",
	#     "parametersSignature": "(si)",
	#     "description": "Set an activity as running with user focus",
	#     "parameters": [
	#         {
	#             "name": "activity_name",
	#             "description": "The package_name/activity_name to run"
	#         },
	#         {
	#             "name": "flags",
	#             "description": "Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def switchFocus(activity_name:str, flags:int, parameters:object, /) -> None:
	"""
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	flags:int
		Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)
	parameters:object
		AnyValue to be passed to activity
	
	Bridge notes
	------------
	switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "switchFocus",
	#     "parametersSignature": "(sim)",
	#     "description": "Set an activity as running with user focus",
	#     "parameters": [
	#         {
	#             "name": "activity_name",
	#             "description": "The package_name/activity_name to run"
	#         },
	#         {
	#             "name": "flags",
	#             "description": "Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)"
	#         },
	#         {
	#             "name": "parameters",
	#             "description": "AnyValue to be passed to activity"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def switchFocus(*args, **kwargs):
	"""
	Bridge notes
	------------
	switchFocus has 3 variants on the robot:
	- switchFocus(activity_name:str)
	- switchFocus(activity_name:str, flags:int)
	- switchFocus(activity_name:str, flags:int, parameters:object)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAutonomousLife.switchFocus has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAutonomousLife", "switchFocus", list(args))

@overload
def _switchFocus(p0:str, p1:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	_switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "_switchFocus",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _switchFocus(p0:str, p1:int, p2:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	Bridge notes
	------------
	_switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "_switchFocus",
	#     "parametersSignature": "(sis)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _switchFocus(p0:str, p1:int, p2:object, p3:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:object
		
	p3:str
		
	
	Bridge notes
	------------
	_switchFocus has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "_switchFocus",
	#     "parametersSignature": "(sims)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _switchFocus(*args, **kwargs):
	"""
	Bridge notes
	------------
	_switchFocus has 3 variants on the robot:
	- _switchFocus(p0:str, p1:str)
	- _switchFocus(p0:str, p1:int, p2:str)
	- _switchFocus(p0:str, p1:int, p2:object, p3:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAutonomousLife._switchFocus has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAutonomousLife", "_switchFocus", list(args))

def stopFocus() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "stopFocus",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "stopFocus", [])

def _stopFocus(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_stopFocus",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_stopFocus", [p0])

def stopAll() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "stopAll",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "stopAll", [])

def _stopAll(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "_stopAll",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_stopAll", [p0])

def getFocusContext(name:str) -> object:
	"""
	Get a value of an ALMemory key that is used in a condition, which is the value at the previous autonomous activity focus.
	
	Parameters
	----------
	name:str
		Name of the ALMemory key to get.  Will throw if key is not used in any activity conditions.
	
	Returns
	----------
	An array of the ALValue of the memory key and timestamp of when it was set: [seconds, microseconds, value]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "m",
	#     "name": "getFocusContext",
	#     "parametersSignature": "(s)",
	#     "description": "Get a value of an ALMemory key that is used in a condition, which is the value at the previous autonomous activity focus.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the ALMemory key to get.  Will throw if key is not used in any activity conditions."
	#         }
	#     ],
	#     "returnDescription": "An array of the ALValue of the memory key and timestamp of when it was set: [seconds, microseconds, value]"
	# }
	return call_method("ALAutonomousLife", "getFocusContext", [name])

def getActivityContextPermissionViolations(name:str) -> List[str]:
	"""
	Get a list of permissions that would be violated by a given activity in the current context.
	
	Parameters
	----------
	name:str
		The name of the activity to check.
	
	Returns
	----------
	An array of strings of the violated permissions. EG: ["nature", "canRunOnPod", "canRunInSleep"]
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "[s]",
	#     "name": "getActivityContextPermissionViolations",
	#     "parametersSignature": "(s)",
	#     "description": "Get a list of permissions that would be violated by a given activity in the current context.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the activity to check."
	#         }
	#     ],
	#     "returnDescription": "An array of strings of the violated permissions. EG: [\"nature\", \"canRunOnPod\", \"canRunInSleep\"]"
	# }
	return call_method("ALAutonomousLife", "getActivityContextPermissionViolations", [name])

def getActivityNature(activity_name:str) -> str:
	"""
	Returns the nature of an activity
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to check
	
	Returns
	----------
	Possible values are: solitary, interactive
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "s",
	#     "name": "getActivityNature",
	#     "parametersSignature": "(s)",
	#     "description": "Returns the nature of an activity",
	#     "parameters": [
	#         {
	#             "name": "activity_name",
	#             "description": "The package_name/activity_name to check"
	#         }
	#     ],
	#     "returnDescription": "Possible values are: solitary, interactive"
	# }
	return call_method("ALAutonomousLife", "getActivityNature", [activity_name])

def getActivityStatistics() -> Dict[str,Dict[str,int]]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "{s{si}}",
	#     "name": "getActivityStatistics",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "getActivityStatistics", [])

def getAutonomousActivityStatistics() -> Dict[str,Dict[str,int]]:
	"""
	Get launch count, last completion time, etc for activities with autonomous launch trigger conditions.
	
	Returns
	----------
	A map of activity names, with a cooresponding map of  "prevStartTime", "prevCompletionTime", "startCount", "totalDuration". Times are 0 for unlaunched Activities
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "{s{si}}",
	#     "name": "getAutonomousActivityStatistics",
	#     "parametersSignature": "()",
	#     "description": "Get launch count, last completion time, etc for activities with autonomous launch trigger conditions.",
	#     "parameters": [],
	#     "returnDescription": "A map of activity names, with a cooresponding map of  \"prevStartTime\", \"prevCompletionTime\", \"startCount\", \"totalDuration\". Times are 0 for unlaunched Activities"
	# }
	return call_method("ALAutonomousLife", "getAutonomousActivityStatistics", [])

@overload
def getFocusHistory() -> List[Tuple[str,int]]:
	"""
	
	
	Bridge notes
	------------
	getFocusHistory has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "[(si)]",
	#     "name": "getFocusHistory",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def getFocusHistory(p0:int, /) -> List[Tuple[str,int]]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	getFocusHistory has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "[(si)]",
	#     "name": "getFocusHistory",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def getFocusHistory(*args, **kwargs):
	"""
	Bridge notes
	------------
	getFocusHistory has 2 variants on the robot:
	- getFocusHistory()
	- getFocusHistory(p0:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAutonomousLife.getFocusHistory has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAutonomousLife", "getFocusHistory", list(args))

@overload
def getStateHistory() -> List[Tuple[str,int]]:
	"""
	
	
	Bridge notes
	------------
	getStateHistory has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "[(si)]",
	#     "name": "getStateHistory",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def getStateHistory(p0:int, /) -> List[Tuple[str,int]]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	getStateHistory has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "[(si)]",
	#     "name": "getStateHistory",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def getStateHistory(*args, **kwargs):
	"""
	Bridge notes
	------------
	getStateHistory has 2 variants on the robot:
	- getStateHistory()
	- getStateHistory(p0:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAutonomousLife.getStateHistory has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAutonomousLife", "getStateHistory", list(args))

def getLifeTime() -> int:
	"""
	Get the time in seconds as life sees it.  Based on gettimeofday()
	
	Returns
	----------
	The int time in seconds as Autonomous Life sees it
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "i",
	#     "name": "getLifeTime",
	#     "parametersSignature": "()",
	#     "description": "Get the time in seconds as life sees it.  Based on gettimeofday()",
	#     "parameters": [],
	#     "returnDescription": "The int time in seconds as Autonomous Life sees it"
	# }
	return call_method("ALAutonomousLife", "getLifeTime", [])

def setAutonomousAbilityEnabled(p0:str, p1:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "setAutonomousAbilityEnabled",
	#     "parametersSignature": "(sb)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "setAutonomousAbilityEnabled", [p0, p1])

def getAutonomousAbilityEnabled(autonomousAbility:str) -> bool:
	"""
	Know is an Autonomous Ability is enabled or not
	
	Parameters
	----------
	autonomousAbility:str
		The Autonomous Ability.
	
	Returns
	----------
	True if the Autonomous Ability is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "b",
	#     "name": "getAutonomousAbilityEnabled",
	#     "parametersSignature": "(s)",
	#     "description": "Know is an Autonomous Ability is enabled or not",
	#     "parameters": [
	#         {
	#             "name": "autonomousAbility",
	#             "description": "The Autonomous Ability."
	#         }
	#     ],
	#     "returnDescription": "True if the Autonomous Ability is enabled, False otherwise."
	# }
	return call_method("ALAutonomousLife", "getAutonomousAbilityEnabled", [autonomousAbility])

def getAutonomousAbilitiesStatus() -> List[AutonomousAbilityStatus]:
	"""
	Get the Autonomous Abilities status (get the autonomous abilities name and booleans to know if they are enabled or running
	
	Returns
	----------
	The Autonomous Abilities status. A vector containing a status for each autonomous ability. Each status is composed of the autonomous ability name, a boolean to know if it's enabled and another boolean to know if it's running.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "[(sbb)<AutonomousAbilityStatus,name,enabled,running>]",
	#     "name": "getAutonomousAbilitiesStatus",
	#     "parametersSignature": "()",
	#     "description": "Get the Autonomous Abilities status (get the autonomous abilities name and booleans to know if they are enabled or running",
	#     "parameters": [],
	#     "returnDescription": "The Autonomous Abilities status. A vector containing a status for each autonomous ability. Each status is composed of the autonomous ability name, a boolean to know if it's enabled and another boolean to know if it's running."
	# }
	return call_method("ALAutonomousLife", "getAutonomousAbilitiesStatus", [], returns=List[AutonomousAbilityStatus])

def startMonitoringLaunchpadConditions() -> None:
	"""
	Start monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "startMonitoringLaunchpadConditions",
	#     "parametersSignature": "()",
	#     "description": "Start monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "startMonitoringLaunchpadConditions", [])

def stopMonitoringLaunchpadConditions() -> None:
	"""
	Stop monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "stopMonitoringLaunchpadConditions",
	#     "parametersSignature": "()",
	#     "description": "Stop monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "stopMonitoringLaunchpadConditions", [])

def isMonitoringLaunchpadConditions() -> bool:
	"""
	Gets running status of AutonomousLaunchpad
	
	Returns
	----------
	True if AutonomousLaunchpad is monitoring ALMemory and reporting conditional triggers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "b",
	#     "name": "isMonitoringLaunchpadConditions",
	#     "parametersSignature": "()",
	#     "description": "Gets running status of AutonomousLaunchpad",
	#     "parameters": [],
	#     "returnDescription": "True if AutonomousLaunchpad is monitoring ALMemory and reporting conditional triggers."
	# }
	return call_method("ALAutonomousLife", "isMonitoringLaunchpadConditions", [])

def setLaunchpadPluginEnabled(plugin_name:str, enabled:bool) -> None:
	"""
	Temporarily enables/disables AutonomousLaunchpad Plugins
	
	Parameters
	----------
	plugin_name:str
		The name of the plugin to enable/disable
	enabled:bool
		Whether or not to enable this plugin
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "setLaunchpadPluginEnabled",
	#     "parametersSignature": "(sb)",
	#     "description": "Temporarily enables/disables AutonomousLaunchpad Plugins",
	#     "parameters": [
	#         {
	#             "name": "plugin_name",
	#             "description": "The name of the plugin to enable/disable"
	#         },
	#         {
	#             "name": "enabled",
	#             "description": "Whether or not to enable this plugin"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "setLaunchpadPluginEnabled", [plugin_name, enabled])

def getEnabledLaunchpadPlugins() -> List[str]:
	"""
	Get a list of enabled AutonomousLaunchpad Plugins.  Enabled plugins will run when AutonomousLaunchpad is started
	
	Returns
	----------
	A list of strings of enabled plugins.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "[s]",
	#     "name": "getEnabledLaunchpadPlugins",
	#     "parametersSignature": "()",
	#     "description": "Get a list of enabled AutonomousLaunchpad Plugins.  Enabled plugins will run when AutonomousLaunchpad is started",
	#     "parameters": [],
	#     "returnDescription": "A list of strings of enabled plugins."
	# }
	return call_method("ALAutonomousLife", "getEnabledLaunchpadPlugins", [])

def getLaunchpadPluginsForGroup(group:str) -> List[str]:
	"""
	Get a list of AutonomousLaunchpad Plugins that belong to specified group
	
	Parameters
	----------
	group:str
		The group to search for the plugins
	
	Returns
	----------
	A list of strings of the plugins belonging to the group.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "[s]",
	#     "name": "getLaunchpadPluginsForGroup",
	#     "parametersSignature": "(s)",
	#     "description": "Get a list of AutonomousLaunchpad Plugins that belong to specified group",
	#     "parameters": [
	#         {
	#             "name": "group",
	#             "description": "The group to search for the plugins"
	#         }
	#     ],
	#     "returnDescription": "A list of strings of the plugins belonging to the group."
	# }
	return call_method("ALAutonomousLife", "getLaunchpadPluginsForGroup", [group])

def setRobotOffsetFromFloor(offset:float) -> None:
	"""
	Set the vertical offset (in meters) of the base of the robot with respect to the floor
	
	Parameters
	----------
	offset:float
		The new vertical offset (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "v",
	#     "name": "setRobotOffsetFromFloor",
	#     "parametersSignature": "(f)",
	#     "description": "Set the vertical offset (in meters) of the base of the robot with respect to the floor",
	#     "parameters": [
	#         {
	#             "name": "offset",
	#             "description": "The new vertical offset (in meters)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "setRobotOffsetFromFloor", [offset])

def getRobotOffsetFromFloor() -> float:
	"""
	Get the vertical offset (in meters) of the base of the robot with respect to the floor
	
	Returns
	----------
	Current vertical offset (in meters)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "f",
	#     "name": "getRobotOffsetFromFloor",
	#     "parametersSignature": "()",
	#     "description": "Get the vertical offset (in meters) of the base of the robot with respect to the floor",
	#     "parameters": [],
	#     "returnDescription": "Current vertical offset (in meters)"
	# }
	return call_method("ALAutonomousLife", "getRobotOffsetFromFloor", [])

def _forbidAutonomousInteractiveStateChange(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "v",
	#     "name": "_forbidAutonomousInteractiveStateChange",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "is_forbidden",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_forbidAutonomousInteractiveStateChange", [is_forbidden])

def _forbidAutonomousActivityFocusSwitch(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "_forbidAutonomousActivityFocusSwitch",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "is_forbidden",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_forbidAutonomousActivityFocusSwitch", [is_forbidden])

def setSafeguardEnabled(name:str, enabled:bool) -> None:
	"""
	Set if a given safeguard will be handled by Autonomous Life or not.
	
	Parameters
	----------
	name:str
		Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature
	enabled:bool
		True if life handles the safeguard.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "setSafeguardEnabled",
	#     "parametersSignature": "(sb)",
	#     "description": "Set if a given safeguard will be handled by Autonomous Life or not.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature"
	#         },
	#         {
	#             "name": "enabled",
	#             "description": "True if life handles the safeguard."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "setSafeguardEnabled", [name, enabled])

def isSafeguardEnabled(name:str) -> bool:
	"""
	Get if a given safeguard will be handled by Autonomous Life or not.
	
	Parameters
	----------
	name:str
		Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature
	
	Returns
	----------
	True if life handles the safeguard.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "b",
	#     "name": "isSafeguardEnabled",
	#     "parametersSignature": "(s)",
	#     "description": "Get if a given safeguard will be handled by Autonomous Life or not.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature"
	#         }
	#     ],
	#     "returnDescription": "True if life handles the safeguard."
	# }
	return call_method("ALAutonomousLife", "isSafeguardEnabled", [name])

def _isMovedSafeguardInstantaneous() -> bool:
	"""
	Get if the movedsafeguard will be instantaneous, or end when move is stopped
	
	Returns
	----------
	True if safeguard is instantaneous, false if safeguard exited after move stopped.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "b",
	#     "name": "_isMovedSafeguardInstantaneous",
	#     "parametersSignature": "()",
	#     "description": "Get if the movedsafeguard will be instantaneous, or end when move is stopped",
	#     "parameters": [],
	#     "returnDescription": "True if safeguard is instantaneous, false if safeguard exited after move stopped."
	# }
	return call_method("ALAutonomousLife", "_isMovedSafeguardInstantaneous", [])

def _setPushRecoverySafeguardDuration(duration_ms:int) -> None:
	"""
	Set how long to stay in safeguard state if robot pushed.
	
	Parameters
	----------
	duration_ms:int
		Time in milliseconds to stay in safeguard state.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "v",
	#     "name": "_setPushRecoverySafeguardDuration",
	#     "parametersSignature": "(i)",
	#     "description": "Set how long to stay in safeguard state if robot pushed.",
	#     "parameters": [
	#         {
	#             "name": "duration_ms",
	#             "description": "Time in milliseconds to stay in safeguard state."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_setPushRecoverySafeguardDuration", [duration_ms])

def _getPushRecoverySafeguardDuration() -> int:
	"""
	Get how long to stay in safeguard state if robot pushed.
	
	Returns
	----------
	Time in milliseconds to stay in safeguard state.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "i",
	#     "name": "_getPushRecoverySafeguardDuration",
	#     "parametersSignature": "()",
	#     "description": "Get how long to stay in safeguard state if robot pushed.",
	#     "parameters": [],
	#     "returnDescription": "Time in milliseconds to stay in safeguard state."
	# }
	return call_method("ALAutonomousLife", "_getPushRecoverySafeguardDuration", [])

def _sleep() -> None:
	"""
	Put the robot to sleep.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "v",
	#     "name": "_sleep",
	#     "parametersSignature": "()",
	#     "description": "Put the robot to sleep.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_sleep", [])

def _wakeUp() -> None:
	"""
	Wake the robot up.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "v",
	#     "name": "_wakeUp",
	#     "parametersSignature": "()",
	#     "description": "Wake the robot up.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_wakeUp", [])

def _forbidStopCommands(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "v",
	#     "name": "_forbidStopCommands",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "is_forbidden",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_forbidStopCommands", [is_forbidden])

def _loadModule(module_name:str) -> None:
	"""
	
	
	Parameters
	----------
	module_name:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "v",
	#     "name": "_loadModule",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "module name",
	#             "description": ""
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALAutonomousLife", "_loadModule", [module_name])

class _Signals:
	activityTransition: Signal[[ActivityTransitionInfo]] = Signal("ALAutonomousLife", "activityTransition", (ActivityTransitionInfo,))
	"""
	Bridge notes
	------------
	A signal sent by ALAutonomousLife on the robot.
	
	subscribe(callback) calls callback(ActivityTransitionInfo) each time the robot sends it.
	"""
	_actionTransition: Signal[[str, str, int]] = Signal("ALAutonomousLife", "_actionTransition")
	"""
	Bridge notes
	------------
	A signal sent by ALAutonomousLife on the robot.
	
	subscribe(callback) calls callback(str, str, int) each time the robot sends it.
	"""
signals = _Signals()

class _Properties:
	userRequestableActivitiesViolations: Property[Dict[str,List[str]]] = Property("ALAutonomousLife", "userRequestableActivitiesViolations")
	"""
	Bridge notes
	------------
	A property of ALAutonomousLife on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(Dict[str,List[str]]) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

