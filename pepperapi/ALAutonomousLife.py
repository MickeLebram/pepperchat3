from .gentypes import *
from .robot_client import send_mfc
import json
"""
Manages the focused Activity and Autonomous Life state
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
	return send_mfc("ALAutonomousLife", "version", [])

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
	return send_mfc("ALAutonomousLife", "ping", [])

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
	return send_mfc("ALAutonomousLife", "getMethodList", [])

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
	return send_mfc("ALAutonomousLife", "getMethodHelp", [methodName])

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
	return send_mfc("ALAutonomousLife", "getModuleHelp", [])

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
	return send_mfc("ALAutonomousLife", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALAutonomousLife", "wait", [id])

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
	return send_mfc("ALAutonomousLife", "isRunning", [id])

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
	return send_mfc("ALAutonomousLife", "stop", [id])

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
	return send_mfc("ALAutonomousLife", "getBrokerName", [])

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
	return send_mfc("ALAutonomousLife", "getUsage", [name])

def _onPreferenceChanged(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "v",
	    "name": "_onPreferenceChanged",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_onPreferenceChanged", [p1, p2, p3])

def onReady(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "onReady",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "onReady", [p1, p2, p3])

def _onRobotHealthChanged(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_onRobotHealthChanged",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_onRobotHealthChanged", [p1, p2, p3])

def _onPushRecovery(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_onPushRecovery",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_onPushRecovery", [p1, p2, p3])

def _onFallRecovery(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_onFallRecovery",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_onFallRecovery", [p1, p2, p3])

def _onRobotMoved(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "_onRobotMoved",
	    "parametersSignature": "(sms)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        },
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_onRobotMoved", [p1, p2, p3])

def _setStateChangeEnabled(enabled:bool) -> None:
	"""
	
	
	Parameters
	----------
	enabled:bool
		Enabled/Disable the setState() method.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "_setStateChangeEnabled",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "enabled",
	            "description": "Enabled/Disable the setState() method."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_setStateChangeEnabled", [enabled])

def _loadConfigFile(p:str) -> None:
	"""
	
	
	Parameters
	----------
	p:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "_loadConfigFile",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_loadConfigFile", [p])

def setState(state:str) -> None:
	"""
	Programatically control the state of Autonomous Life
	
	Parameters
	----------
	state:str
		The possible states of AutonomousLife are: interactive, solitary, safeguard, disabled
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "v",
	    "name": "setState",
	    "parametersSignature": "(s)",
	    "description": "Programatically control the state of Autonomous Life",
	    "parameters": [
	        {
	            "name": "state",
	            "description": "The possible states of AutonomousLife are: interactive, solitary, safeguard, disabled"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "setState", [state])

def getState() -> str:
	"""
	Returns the current state of AutonomousLife
	
	Returns
	----------
	Can be: solitary, interactive, safeguard, disabled
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "s",
	    "name": "getState",
	    "parametersSignature": "()",
	    "description": "Returns the current state of AutonomousLife",
	    "parameters": [],
	    "returnDescription": "Can be: solitary, interactive, safeguard, disabled"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getState", [])

def focusedActivity() -> str:
	"""
	Returns the currently focused activity
	
	Returns
	----------
	The name of the focused activity
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "s",
	    "name": "focusedActivity",
	    "parametersSignature": "()",
	    "description": "Returns the currently focused activity",
	    "parameters": [],
	    "returnDescription": "The name of the focused activity"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "focusedActivity", [])

def switchFocus_1(activity_name:str) -> None:
	"""
	Note: This is one of the overloads of the original method (switchFocus)
	
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "switchFocus",
	    "parametersSignature": "(s)",
	    "description": "Set an activity as running with user focus",
	    "parameters": [
	        {
	            "name": "activity_name",
	            "description": "The package_name/activity_name to run"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "switchFocus", [activity_name])

def switchFocus_2(activity_name:str, flags:int) -> None:
	"""
	Note: This is one of the overloads of the original method (switchFocus)
	
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	flags:int
		Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "switchFocus",
	    "parametersSignature": "(si)",
	    "description": "Set an activity as running with user focus",
	    "parameters": [
	        {
	            "name": "activity_name",
	            "description": "The package_name/activity_name to run"
	        },
	        {
	            "name": "flags",
	            "description": "Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "switchFocus", [activity_name, flags])

def switchFocus_3(activity_name:str, flags:int, parameters:object) -> None:
	"""
	Note: This is one of the overloads of the original method (switchFocus)
	
	Set an activity as running with user focus
	
	Parameters
	----------
	activity_name:str
		The package_name/activity_name to run
	flags:int
		Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)
	parameters:object
		AnyValue to be passed to activity
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "switchFocus",
	    "parametersSignature": "(sim)",
	    "description": "Set an activity as running with user focus",
	    "parameters": [
	        {
	            "name": "activity_name",
	            "description": "The package_name/activity_name to run"
	        },
	        {
	            "name": "flags",
	            "description": "Int flags for focus changing. STOP_CURRENT(0) or STOP_AND_STACK_CURRENT(1)"
	        },
	        {
	            "name": "parameters",
	            "description": "AnyValue to be passed to activity"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "switchFocus", [activity_name, flags, parameters])

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
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "m",
	    "name": "getFocusContext",
	    "parametersSignature": "(s)",
	    "description": "Get a value of an ALMemory key that is used in a condition, which is the value at the previous autonomous activity focus.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the ALMemory key to get.  Will throw if key is not used in any activity conditions."
	        }
	    ],
	    "returnDescription": "An array of the ALValue of the memory key and timestamp of when it was set: [seconds, microseconds, value]"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getFocusContext", [name])

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
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "[s]",
	    "name": "getActivityContextPermissionViolations",
	    "parametersSignature": "(s)",
	    "description": "Get a list of permissions that would be violated by a given activity in the current context.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the activity to check."
	        }
	    ],
	    "returnDescription": "An array of strings of the violated permissions. EG: [\"nature\", \"canRunOnPod\", \"canRunInSleep\"]"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getActivityContextPermissionViolations", [name])

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
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "s",
	    "name": "getActivityNature",
	    "parametersSignature": "(s)",
	    "description": "Returns the nature of an activity",
	    "parameters": [
	        {
	            "name": "activity_name",
	            "description": "The package_name/activity_name to check"
	        }
	    ],
	    "returnDescription": "Possible values are: solitary, interactive"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getActivityNature", [activity_name])

def getAutonomousActivityStatistics() -> Dict[str,Dict[str,int]]:
	"""
	Get launch count, last completion time, etc for activities with autonomous launch trigger conditions.
	
	Returns
	----------
	A map of activity names, with a cooresponding map of  "prevStartTime", "prevCompletionTime", "startCount", "totalDuration". Times are 0 for unlaunched Activities
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "{s{si}}",
	    "name": "getAutonomousActivityStatistics",
	    "parametersSignature": "()",
	    "description": "Get launch count, last completion time, etc for activities with autonomous launch trigger conditions.",
	    "parameters": [],
	    "returnDescription": "A map of activity names, with a cooresponding map of  \"prevStartTime\", \"prevCompletionTime\", \"startCount\", \"totalDuration\". Times are 0 for unlaunched Activities"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getAutonomousActivityStatistics", [])

def getLifeTime() -> int:
	"""
	Get the time in seconds as life sees it.  Based on gettimeofday()
	
	Returns
	----------
	The int time in seconds as Autonomous Life sees it
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "i",
	    "name": "getLifeTime",
	    "parametersSignature": "()",
	    "description": "Get the time in seconds as life sees it.  Based on gettimeofday()",
	    "parameters": [],
	    "returnDescription": "The int time in seconds as Autonomous Life sees it"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getLifeTime", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "b",
	    "name": "getAutonomousAbilityEnabled",
	    "parametersSignature": "(s)",
	    "description": "Know is an Autonomous Ability is enabled or not",
	    "parameters": [
	        {
	            "name": "autonomousAbility",
	            "description": "The Autonomous Ability."
	        }
	    ],
	    "returnDescription": "True if the Autonomous Ability is enabled, False otherwise."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getAutonomousAbilityEnabled", [autonomousAbility])

def getAutonomousAbilitiesStatus() -> List[AutonomousAbilityStatus]:
	"""
	Get the Autonomous Abilities status (get the autonomous abilities name and booleans to know if they are enabled or running
	
	Returns
	----------
	The Autonomous Abilities status. A vector containing a status for each autonomous ability. Each status is composed of the autonomous ability name, a boolean to know if it's enabled and another boolean to know if it's running.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "[(sbb)<AutonomousAbilityStatus,name,enabled,running>]",
	    "name": "getAutonomousAbilitiesStatus",
	    "parametersSignature": "()",
	    "description": "Get the Autonomous Abilities status (get the autonomous abilities name and booleans to know if they are enabled or running",
	    "parameters": [],
	    "returnDescription": "The Autonomous Abilities status. A vector containing a status for each autonomous ability. Each status is composed of the autonomous ability name, a boolean to know if it's enabled and another boolean to know if it's running."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getAutonomousAbilitiesStatus", [])

def startMonitoringLaunchpadConditions() -> None:
	"""
	Start monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "startMonitoringLaunchpadConditions",
	    "parametersSignature": "()",
	    "description": "Start monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "startMonitoringLaunchpadConditions", [])

def stopMonitoringLaunchpadConditions() -> None:
	"""
	Stop monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "v",
	    "name": "stopMonitoringLaunchpadConditions",
	    "parametersSignature": "()",
	    "description": "Stop monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "stopMonitoringLaunchpadConditions", [])

def isMonitoringLaunchpadConditions() -> bool:
	"""
	Gets running status of AutonomousLaunchpad
	
	Returns
	----------
	True if AutonomousLaunchpad is monitoring ALMemory and reporting conditional triggers.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "b",
	    "name": "isMonitoringLaunchpadConditions",
	    "parametersSignature": "()",
	    "description": "Gets running status of AutonomousLaunchpad",
	    "parameters": [],
	    "returnDescription": "True if AutonomousLaunchpad is monitoring ALMemory and reporting conditional triggers."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "isMonitoringLaunchpadConditions", [])

def setLaunchpadPluginEnabled(plugin_name:str, enabled:bool) -> None:
	"""
	Temporarily enables/disables AutonomousLaunchpad Plugins
	
	Parameters
	----------
	plugin_name:str
		The name of the plugin to enable/disable
	enabled:bool
		Whether or not to enable this plugin
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "setLaunchpadPluginEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Temporarily enables/disables AutonomousLaunchpad Plugins",
	    "parameters": [
	        {
	            "name": "plugin_name",
	            "description": "The name of the plugin to enable/disable"
	        },
	        {
	            "name": "enabled",
	            "description": "Whether or not to enable this plugin"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "setLaunchpadPluginEnabled", [plugin_name, enabled])

def getEnabledLaunchpadPlugins() -> List[str]:
	"""
	Get a list of enabled AutonomousLaunchpad Plugins.  Enabled plugins will run when AutonomousLaunchpad is started
	
	Returns
	----------
	A list of strings of enabled plugins.
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "[s]",
	    "name": "getEnabledLaunchpadPlugins",
	    "parametersSignature": "()",
	    "description": "Get a list of enabled AutonomousLaunchpad Plugins.  Enabled plugins will run when AutonomousLaunchpad is started",
	    "parameters": [],
	    "returnDescription": "A list of strings of enabled plugins."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getEnabledLaunchpadPlugins", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "[s]",
	    "name": "getLaunchpadPluginsForGroup",
	    "parametersSignature": "(s)",
	    "description": "Get a list of AutonomousLaunchpad Plugins that belong to specified group",
	    "parameters": [
	        {
	            "name": "group",
	            "description": "The group to search for the plugins"
	        }
	    ],
	    "returnDescription": "A list of strings of the plugins belonging to the group."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getLaunchpadPluginsForGroup", [group])

def setRobotOffsetFromFloor(offset:float) -> None:
	"""
	Set the vertical offset (in meters) of the base of the robot with respect to the floor
	
	Parameters
	----------
	offset:float
		The new vertical offset (in meters)
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "v",
	    "name": "setRobotOffsetFromFloor",
	    "parametersSignature": "(f)",
	    "description": "Set the vertical offset (in meters) of the base of the robot with respect to the floor",
	    "parameters": [
	        {
	            "name": "offset",
	            "description": "The new vertical offset (in meters)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "setRobotOffsetFromFloor", [offset])

def getRobotOffsetFromFloor() -> float:
	"""
	Get the vertical offset (in meters) of the base of the robot with respect to the floor
	
	Returns
	----------
	Current vertical offset (in meters)
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "f",
	    "name": "getRobotOffsetFromFloor",
	    "parametersSignature": "()",
	    "description": "Get the vertical offset (in meters) of the base of the robot with respect to the floor",
	    "parameters": [],
	    "returnDescription": "Current vertical offset (in meters)"
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "getRobotOffsetFromFloor", [])

def _forbidAutonomousInteractiveStateChange(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "_forbidAutonomousInteractiveStateChange",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "is_forbidden",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_forbidAutonomousInteractiveStateChange", [is_forbidden])

def _forbidAutonomousActivityFocusSwitch(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_forbidAutonomousActivityFocusSwitch",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "is_forbidden",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_forbidAutonomousActivityFocusSwitch", [is_forbidden])

def setSafeguardEnabled(name:str, enabled:bool) -> None:
	"""
	Set if a given safeguard will be handled by Autonomous Life or not.
	
	Parameters
	----------
	name:str
		Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature
	enabled:bool
		True if life handles the safeguard.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "setSafeguardEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Set if a given safeguard will be handled by Autonomous Life or not.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature"
	        },
	        {
	            "name": "enabled",
	            "description": "True if life handles the safeguard."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "setSafeguardEnabled", [name, enabled])

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
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "b",
	    "name": "isSafeguardEnabled",
	    "parametersSignature": "(s)",
	    "description": "Get if a given safeguard will be handled by Autonomous Life or not.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature"
	        }
	    ],
	    "returnDescription": "True if life handles the safeguard."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "isSafeguardEnabled", [name])

def _isMovedSafeguardInstantaneous() -> bool:
	"""
	Get if the movedsafeguard will be instantaneous, or end when move is stopped
	
	Returns
	----------
	True if safeguard is instantaneous, false if safeguard exited after move stopped.
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "b",
	    "name": "_isMovedSafeguardInstantaneous",
	    "parametersSignature": "()",
	    "description": "Get if the movedsafeguard will be instantaneous, or end when move is stopped",
	    "parameters": [],
	    "returnDescription": "True if safeguard is instantaneous, false if safeguard exited after move stopped."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_isMovedSafeguardInstantaneous", [])

def _setPushRecoverySafeguardDuration(duration_ms:int) -> None:
	"""
	Set how long to stay in safeguard state if robot pushed.
	
	Parameters
	----------
	duration_ms:int
		Time in milliseconds to stay in safeguard state.
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "v",
	    "name": "_setPushRecoverySafeguardDuration",
	    "parametersSignature": "(i)",
	    "description": "Set how long to stay in safeguard state if robot pushed.",
	    "parameters": [
	        {
	            "name": "duration_ms",
	            "description": "Time in milliseconds to stay in safeguard state."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_setPushRecoverySafeguardDuration", [duration_ms])

def _getPushRecoverySafeguardDuration() -> int:
	"""
	Get how long to stay in safeguard state if robot pushed.
	
	Returns
	----------
	Time in milliseconds to stay in safeguard state.
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "i",
	    "name": "_getPushRecoverySafeguardDuration",
	    "parametersSignature": "()",
	    "description": "Get how long to stay in safeguard state if robot pushed.",
	    "parameters": [],
	    "returnDescription": "Time in milliseconds to stay in safeguard state."
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_getPushRecoverySafeguardDuration", [])

def _sleep() -> None:
	"""
	Put the robot to sleep.
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "v",
	    "name": "_sleep",
	    "parametersSignature": "()",
	    "description": "Put the robot to sleep.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_sleep", [])

def _wakeUp() -> None:
	"""
	Wake the robot up.
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "v",
	    "name": "_wakeUp",
	    "parametersSignature": "()",
	    "description": "Wake the robot up.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_wakeUp", [])

def _forbidStopCommands(is_forbidden:bool) -> None:
	"""
	
	
	Parameters
	----------
	is_forbidden:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "v",
	    "name": "_forbidStopCommands",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "is_forbidden",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_forbidStopCommands", [is_forbidden])

def _loadModule(module_name:str) -> None:
	"""
	
	
	Parameters
	----------
	module_name:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 166,
	    "returnSignature": "v",
	    "name": "_loadModule",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "module name",
	            "description": ""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAutonomousLife", "_loadModule", [module_name])

