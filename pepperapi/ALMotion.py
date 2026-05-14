from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALMotion provides methods that help make Nao move. It contains commands for manipulating joint angles, joint stiffness, and a higher level API for controling walks.
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
	return send_mfc("ALMotion", "version", [])

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
	return send_mfc("ALMotion", "ping", [])

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
	return send_mfc("ALMotion", "getMethodList", [])

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
	return send_mfc("ALMotion", "getMethodHelp", [methodName])

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
	return send_mfc("ALMotion", "getModuleHelp", [])

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
	return send_mfc("ALMotion", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALMotion", "wait", [id])

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
	return send_mfc("ALMotion", "isRunning", [id])

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
	return send_mfc("ALMotion", "stop", [id])

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
	return send_mfc("ALMotion", "getBrokerName", [])

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
	return send_mfc("ALMotion", "getUsage", [name])

def wakeUp() -> bool:
	"""
	The robot will wake up: set Motor ON and go to initial position if needed
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "wakeUp",
	    "parametersSignature": "()",
	    "description": "The robot will wake up: set Motor ON and go to initial position if needed",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wakeUp", [])

def rest() -> None:
	"""
	The robot will rest: go to a relax and safe position and set Motor OFF
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "rest",
	    "parametersSignature": "()",
	    "description": "The robot will rest: go to a relax and safe position and set Motor OFF",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "rest", [])

def _rest(chainName:str) -> None:
	"""
	The robot will rest: go to a relax and safe position on the chain and set Motor OFF
	
	Parameters
	----------
	chainName:str
		The name of the chain to rest.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "v",
	    "name": "_rest",
	    "parametersSignature": "(s)",
	    "description": "The robot will rest: go to a relax and safe position on the chain and set Motor OFF",
	    "parameters": [
	        {
	            "name": "chainName",
	            "description": "The name of the chain to rest."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_rest", [chainName])

def _stopChain(chainName:str) -> None:
	"""
	The robot will immediately unstiffness the chain.
	
	Parameters
	----------
	chainName:str
		The name of the chain to rest. Can be "LArm", "RArm", or "Arms".
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "v",
	    "name": "_stopChain",
	    "parametersSignature": "(s)",
	    "description": "The robot will immediately unstiffness the chain.",
	    "parameters": [
	        {
	            "name": "chainName",
	            "description": "The name of the chain to rest. Can be \"LArm\", \"RArm\", or \"Arms\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_stopChain", [chainName])

def _restReflex(whyString:str, stateList:object) -> None:
	"""
	The robot propose several adapted rest.
	
	Parameters
	----------
	whyString:str
		A string describing the root cause of the request.
	stateList:object
		An ALValue [[[name list], a string or array of angles], ...].
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "_restReflex",
	    "parametersSignature": "(sm)",
	    "description": "The robot propose several adapted rest.",
	    "parameters": [
	        {
	            "name": "whyString",
	            "description": "A string describing the root cause of the request."
	        },
	        {
	            "name": "stateList",
	            "description": "An ALValue [[[name list], a string or array of angles], ...]."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_restReflex", [whyString, stateList])

def _blockedLegReflex() -> None:
	"""
	Go to a stable rest posture given the blocked joints
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "v",
	    "name": "_blockedLegReflex",
	    "parametersSignature": "()",
	    "description": "Go to a stable rest posture given the blocked joints",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_blockedLegReflex", [])

def _shutdown() -> None:
	"""
	The robot will rest: wakeUp is not allowed anymore.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "v",
	    "name": "_shutdown",
	    "parametersSignature": "()",
	    "description": "The robot will rest: wakeUp is not allowed anymore.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_shutdown", [])

def _setMotionPosture(postureName:str, bodyAngles:List[float]) -> bool:
	"""
	Set the reference posture for fallmanager, stand init, idle posture, breath, etc.
	
	Parameters
	----------
	postureName:str
		The posture name
	bodyAngles:List[float]
		The body angles. Use getBodyNames api with parameter JointActuators.
	
	Returns
	----------
	Success to set the desired motion posture.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "_setMotionPosture",
	    "parametersSignature": "(s[f])",
	    "description": "Set the reference posture for fallmanager, stand init, idle posture, breath, etc.",
	    "parameters": [
	        {
	            "name": "postureName",
	            "description": "The posture name"
	        },
	        {
	            "name": "bodyAngles",
	            "description": "The body angles. Use getBodyNames api with parameter JointActuators."
	        }
	    ],
	    "returnDescription": "Success to set the desired motion posture."
	}
	'''
	"""
	return send_mfc("ALMotion", "_setMotionPosture", [postureName, bodyAngles])

def _getMotionPosture(postureName:str) -> List[float]:
	"""
	
	
	Parameters
	----------
	postureName:str
		The posture name
	
	Returns
	----------
	Use getBodyNames api with parameter JointActuators.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "[f]",
	    "name": "_getMotionPosture",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "postureName",
	            "description": "The posture name"
	        }
	    ],
	    "returnDescription": "Use getBodyNames api with parameter JointActuators."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getMotionPosture", [postureName])

def _getMotionPostureList() -> List[str]:
	"""
	
	
	Returns
	----------
	All the postures in motion posture library
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "[s]",
	    "name": "_getMotionPostureList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": "All the postures in motion posture library"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getMotionPostureList", [])

def robotIsWakeUp() -> bool:
	"""
	return true if the robot is already wakeUp
	
	Returns
	----------
	True if the robot is already wakeUp.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "b",
	    "name": "robotIsWakeUp",
	    "parametersSignature": "()",
	    "description": "return true if the robot is already wakeUp",
	    "parameters": [],
	    "returnDescription": "True if the robot is already wakeUp."
	}
	'''
	"""
	return send_mfc("ALMotion", "robotIsWakeUp", [])

def stiffnessInterpolation(names:object, stiffnessLists:object, timeLists:object) -> None:
	"""
	Interpolates one or multiple joints to a target stiffness or along timed trajectories of stiffness. This is a blocking call.
	
	Parameters
	----------
	names:object
		Name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators".
	stiffnessLists:object
		An stiffness, list of stiffnesses or list of list of stiffnesses
	timeLists:object
		A time, list of times or list of list of times.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "stiffnessInterpolation",
	    "parametersSignature": "(mmm)",
	    "description": "Interpolates one or multiple joints to a target stiffness or along timed trajectories of stiffness. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        },
	        {
	            "name": "stiffnessLists",
	            "description": "An stiffness, list of stiffnesses or list of list of stiffnesses"
	        },
	        {
	            "name": "timeLists",
	            "description": "A time, list of times or list of list of times."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "stiffnessInterpolation", [names, stiffnessLists, timeLists])

def setStiffnesses(names:object, stiffnesses:object) -> None:
	"""
	Sets the stiffness of one or more joints. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		Names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators".
	stiffnesses:object
		One or more stiffnesses between zero and one.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "v",
	    "name": "setStiffnesses",
	    "parametersSignature": "(mm)",
	    "description": "Sets the stiffness of one or more joints. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        },
	        {
	            "name": "stiffnesses",
	            "description": "One or more stiffnesses between zero and one."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setStiffnesses", [names, stiffnesses])

def _setStiffnesses(names:object, stiffnesses:object) -> None:
	"""
	Sets the stiffness of one or more joints. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		Names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators".
	stiffnesses:object
		One or more stiffnesses between zero and one.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "v",
	    "name": "_setStiffnesses",
	    "parametersSignature": "(mm)",
	    "description": "Sets the stiffness of one or more joints. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        },
	        {
	            "name": "stiffnesses",
	            "description": "One or more stiffnesses between zero and one."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setStiffnesses", [names, stiffnesses])

def _setSafeStiffnesses(jointIndexes:List[int], actuatorIndexes:List[int], stiffness:float) -> None:
	"""
	Set the custom stiffnesses to maintain on the given joints and actuators to ensure safety. 
	
	Parameters
	----------
	jointIndexes:List[int]
		Vector of joint indexes
	actuatorIndexes:List[int]
		Vector of actuator indexes
	stiffness:float
		The stiffness to maintain between zero and one.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "v",
	    "name": "_setSafeStiffnesses",
	    "parametersSignature": "([I][I]f)",
	    "description": "Set the custom stiffnesses to maintain on the given joints and actuators to ensure safety. ",
	    "parameters": [
	        {
	            "name": "jointIndexes",
	            "description": "Vector of joint indexes"
	        },
	        {
	            "name": "actuatorIndexes",
	            "description": "Vector of actuator indexes"
	        },
	        {
	            "name": "stiffness",
	            "description": "The stiffness to maintain between zero and one."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setSafeStiffnesses", [jointIndexes, actuatorIndexes, stiffness])

def _disableSafeStiffnesses(jointIndexes:List[int], actuatorIndexes:List[int]) -> None:
	"""
	Disable the safe stiffnesses set for the given joints and actuators.
	
	Parameters
	----------
	jointIndexes:List[int]
		Vector of joint indexes
	actuatorIndexes:List[int]
		Vector of actuator indexes
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "_disableSafeStiffnesses",
	    "parametersSignature": "([I][I])",
	    "description": "Disable the safe stiffnesses set for the given joints and actuators.",
	    "parameters": [
	        {
	            "name": "jointIndexes",
	            "description": "Vector of joint indexes"
	        },
	        {
	            "name": "actuatorIndexes",
	            "description": "Vector of actuator indexes"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_disableSafeStiffnesses", [jointIndexes, actuatorIndexes])

def getStiffnesses(jointName:object) -> List[float]:
	"""
	Gets stiffness of a joint or group of joints
	
	Parameters
	----------
	jointName:object
		Name of the joints, chains, "Body", "Joints" or "Actuators".
	
	Returns
	----------
	One or more stiffnesses. 1.0 indicates maximum stiffness. 0.0 indicated minimum stiffness
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[f]",
	    "name": "getStiffnesses",
	    "parametersSignature": "(m)",
	    "description": "Gets stiffness of a joint or group of joints",
	    "parameters": [
	        {
	            "name": "jointName",
	            "description": "Name of the joints, chains, \"Body\", \"Joints\" or \"Actuators\"."
	        }
	    ],
	    "returnDescription": "One or more stiffnesses. 1.0 indicates maximum stiffness. 0.0 indicated minimum stiffness"
	}
	'''
	"""
	return send_mfc("ALMotion", "getStiffnesses", [jointName])

def angleInterpolation(names:object, angleLists:object, timeLists:object, isAbsolute:bool) -> None:
	"""
	Interpolates one or multiple joints to a target angle or along timed trajectories. This is a blocking call.
	
	Parameters
	----------
	names:object
		Name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators". 
	angleLists:object
		An angle, list of angles or list of list of angles in radians
	timeLists:object
		A time, list of times or list of list of times in seconds
	isAbsolute:bool
		If true, the movement is described in absolute angles, else the angles are relative to the current angle.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "angleInterpolation",
	    "parametersSignature": "(mmmb)",
	    "description": "Interpolates one or multiple joints to a target angle or along timed trajectories. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        },
	        {
	            "name": "angleLists",
	            "description": "An angle, list of angles or list of list of angles in radians"
	        },
	        {
	            "name": "timeLists",
	            "description": "A time, list of times or list of list of times in seconds"
	        },
	        {
	            "name": "isAbsolute",
	            "description": "If true, the movement is described in absolute angles, else the angles are relative to the current angle."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "angleInterpolation", [names, angleLists, timeLists, isAbsolute])

def angleInterpolationWithSpeed(names:object, targetAngles:object, maxSpeedFraction:float) -> None:
	"""
	Interpolates one or multiple joints to a target angle, using a fraction of max speed. Only one target angle is allowed for each joint. This is a blocking call.
	
	Parameters
	----------
	names:object
		Name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators".
	targetAngles:object
		An angle, or list of angles in radians
	maxSpeedFraction:float
		A fraction.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "v",
	    "name": "angleInterpolationWithSpeed",
	    "parametersSignature": "(mmf)",
	    "description": "Interpolates one or multiple joints to a target angle, using a fraction of max speed. Only one target angle is allowed for each joint. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        },
	        {
	            "name": "targetAngles",
	            "description": "An angle, or list of angles in radians"
	        },
	        {
	            "name": "maxSpeedFraction",
	            "description": "A fraction."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "angleInterpolationWithSpeed", [names, targetAngles, maxSpeedFraction])

def angleInterpolationBezier(jointNames:List[str], times:object, controlPoints:object) -> None:
	"""
	Interpolates a sequence of timed angles for several motors using bezier control points. This is a blocking call.
	
	Parameters
	----------
	jointNames:List[str]
		A vector of joint names
	times:object
		An ragged ALValue matrix of floats. Each line corresponding to a motor, and column element to a control point.
	controlPoints:object
		An ALValue array of arrays each containing [float angle, Handle1, Handle2], where Handle is [int InterpolationType, float dAngle, float dTime] descibing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceeding the point, the second describes the curve following the point.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "angleInterpolationBezier",
	    "parametersSignature": "([s]mm)",
	    "description": "Interpolates a sequence of timed angles for several motors using bezier control points. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "jointNames",
	            "description": "A vector of joint names"
	        },
	        {
	            "name": "times",
	            "description": "An ragged ALValue matrix of floats. Each line corresponding to a motor, and column element to a control point."
	        },
	        {
	            "name": "controlPoints",
	            "description": "An ALValue array of arrays each containing [float angle, Handle1, Handle2], where Handle is [int InterpolationType, float dAngle, float dTime] descibing the handle offsets relative to the angle and time of the point. The first bezier param describes the handle that controls the curve preceeding the point, the second describes the curve following the point."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "angleInterpolationBezier", [jointNames, times, controlPoints])

def setAngles_1(names:object, angles:object, fractionMaxSpeed:float) -> None:
	"""
	Note: This is one of the overloads of the original method (setAngles)
	
	Sets angles. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		The name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators". 
	angles:object
		One or more angles in radians
	fractionMaxSpeed:float
		The fraction of maximum speed to use
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "setAngles",
	    "parametersSignature": "(mmf)",
	    "description": "Sets angles. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "The name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        },
	        {
	            "name": "angles",
	            "description": "One or more angles in radians"
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "The fraction of maximum speed to use"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setAngles", [names, angles, fractionMaxSpeed])

def setAngles_2(names:object, angles:object, fractionMaxSpeeds:List[float]) -> None:
	"""
	Note: This is one of the overloads of the original method (setAngles)
	
	Sets angles. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		The name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators". 
	angles:object
		One or more angles in radians
	fractionMaxSpeeds:List[float]
		The vector of fraction of maximum speed to use
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "v",
	    "name": "setAngles",
	    "parametersSignature": "(mm[f])",
	    "description": "Sets angles. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "The name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        },
	        {
	            "name": "angles",
	            "description": "One or more angles in radians"
	        },
	        {
	            "name": "fractionMaxSpeeds",
	            "description": "The vector of fraction of maximum speed to use"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setAngles", [names, angles, fractionMaxSpeeds])

def changeAngles(names:object, changes:object, fractionMaxSpeed:float) -> None:
	"""
	Changes Angles. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		The name or names of joints, chains, "Body", "JointActuators", "Joints" or "Actuators".
	changes:object
		One or more changes in radians
	fractionMaxSpeed:float
		The fraction of maximum speed to use
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "changeAngles",
	    "parametersSignature": "(mmf)",
	    "description": "Changes Angles. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "The name or names of joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        },
	        {
	            "name": "changes",
	            "description": "One or more changes in radians"
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "The fraction of maximum speed to use"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "changeAngles", [names, changes, fractionMaxSpeed])

def getAngles(names:object, useSensors:bool) -> List[float]:
	"""
	Gets the angles of the joints
	
	Parameters
	----------
	names:object
		Names the joints, chains, "Body", "JointActuators", "Joints" or "Actuators". 
	useSensors:bool
		If true, sensor angles will be returned
	
	Returns
	----------
	Joint angles in radians.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "[f]",
	    "name": "getAngles",
	    "parametersSignature": "(mb)",
	    "description": "Gets the angles of the joints",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Names the joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        },
	        {
	            "name": "useSensors",
	            "description": "If true, sensor angles will be returned"
	        }
	    ],
	    "returnDescription": "Joint angles in radians."
	}
	'''
	"""
	return send_mfc("ALMotion", "getAngles", [names, useSensors])

def openHand(handName:str) -> None:
	"""
	NAO stiffens the motors of desired hand. Then, he opens the hand, then cuts motor current to conserve energy. This is a blocking call.
	
	Parameters
	----------
	handName:str
		The name of the hand. Could be: "RHand or "LHand"
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "v",
	    "name": "openHand",
	    "parametersSignature": "(s)",
	    "description": "NAO stiffens the motors of desired hand. Then, he opens the hand, then cuts motor current to conserve energy. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "handName",
	            "description": "The name of the hand. Could be: \"RHand or \"LHand\""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "openHand", [handName])

def closeHand(handName:str) -> None:
	"""
	NAO stiffens the motors of desired hand. Then, he closes the hand, then cuts motor current to conserve energy. This is a blocking call.
	
	Parameters
	----------
	handName:str
		The name of the hand. Could be: "RHand" or "LHand"
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "v",
	    "name": "closeHand",
	    "parametersSignature": "(s)",
	    "description": "NAO stiffens the motors of desired hand. Then, he closes the hand, then cuts motor current to conserve energy. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "handName",
	            "description": "The name of the hand. Could be: \"RHand\" or \"LHand\""
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "closeHand", [handName])

def move_1(x:float, y:float, theta:float) -> None:
	"""
	Note: This is one of the overloads of the original method (move)
	
	Makes the robot move at the given velocity. This is a non-blocking call.
	
	Parameters
	----------
	x:float
		The velocity along x axis [m.s-1].
	y:float
		The velocity along y axis [m.s-1].
	theta:float
		The velocity around z axis [rd.s-1].
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "v",
	    "name": "move",
	    "parametersSignature": "(fff)",
	    "description": "Makes the robot move at the given velocity. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The velocity along x axis [m.s-1]."
	        },
	        {
	            "name": "y",
	            "description": "The velocity along y axis [m.s-1]."
	        },
	        {
	            "name": "theta",
	            "description": "The velocity around z axis [rd.s-1]."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "move", [x, y, theta])

def move_2(x:float, y:float, theta:float, moveConfig:object) -> None:
	"""
	Note: This is one of the overloads of the original method (move)
	
	Makes the robot move at the given velocity. This is a non-blocking call.
	
	Parameters
	----------
	x:float
		The velocity along x axis [m.s-1].
	y:float
		The velocity along y axis [m.s-1].
	theta:float
		The velocity around z axis [rd.s-1].
	moveConfig:object
		An ALValue with custom move configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "v",
	    "name": "move",
	    "parametersSignature": "(fffm)",
	    "description": "Makes the robot move at the given velocity. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The velocity along x axis [m.s-1]."
	        },
	        {
	            "name": "y",
	            "description": "The velocity along y axis [m.s-1]."
	        },
	        {
	            "name": "theta",
	            "description": "The velocity around z axis [rd.s-1]."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "move", [x, y, theta, moveConfig])

def moveToward_1(x:float, y:float, theta:float) -> None:
	"""
	Note: This is one of the overloads of the original method (moveToward)
	
	Makes the robot move at the given normalized velocity. This is a non-blocking call.
	
	Parameters
	----------
	x:float
		The normalized velocity along x axis (between -1 and 1).
	y:float
		The normalized velocity along y axis (between -1 and 1).
	theta:float
		The normalized velocity around z axis (between -1 and 1).
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "v",
	    "name": "moveToward",
	    "parametersSignature": "(fff)",
	    "description": "Makes the robot move at the given normalized velocity. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The normalized velocity along x axis (between -1 and 1)."
	        },
	        {
	            "name": "y",
	            "description": "The normalized velocity along y axis (between -1 and 1)."
	        },
	        {
	            "name": "theta",
	            "description": "The normalized velocity around z axis (between -1 and 1)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "moveToward", [x, y, theta])

def moveToward_2(x:float, y:float, theta:float, moveConfig:object) -> None:
	"""
	Note: This is one of the overloads of the original method (moveToward)
	
	Makes the robot move at the given normalized velocity. This is a non-blocking call.
	
	Parameters
	----------
	x:float
		The normalized velocity along x axis (between -1 and 1).
	y:float
		The normalized velocity along y axis (between -1 and 1).
	theta:float
		The normalized velocity around z axis (between -1 and 1).
	moveConfig:object
		An ALValue with custom move configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "moveToward",
	    "parametersSignature": "(fffm)",
	    "description": "Makes the robot move at the given normalized velocity. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The normalized velocity along x axis (between -1 and 1)."
	        },
	        {
	            "name": "y",
	            "description": "The normalized velocity along y axis (between -1 and 1)."
	        },
	        {
	            "name": "theta",
	            "description": "The normalized velocity around z axis (between -1 and 1)."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "moveToward", [x, y, theta, moveConfig])

def moveTo_1(x:float, y:float, theta:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move at the given position. This is a blocking call.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(fff)",
	    "description": "Makes the robot move at the given position. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [x, y, theta])

def moveTo_2(x:float, y:float, theta:float, time:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move at the given position in fixed time. This is a blocking call.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	time:float
		The time to reach the target position [s].
	
	Returns
	----------
	a boolean equal to true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(ffff)",
	    "description": "Makes the robot move at the given position in fixed time. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        },
	        {
	            "name": "time",
	            "description": "The time to reach the target position [s]."
	        }
	    ],
	    "returnDescription": "a boolean equal to true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [x, y, theta, time])

def moveTo_3(x:float, y:float, theta:float, moveConfig:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move at the given position. This is a blocking call.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	moveConfig:object
		An ALValue with custom move configuration.
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(fffm)",
	    "description": "Makes the robot move at the given position. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [x, y, theta, moveConfig])

def moveTo_4(x:float, y:float, theta:float, time:float, moveConfig:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move at the given position in fixed time. This is a blocking call.
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	time:float
		The time to reach the target position [s].
	moveConfig:object
		An ALValue with custom move configuration.
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(ffffm)",
	    "description": "Makes the robot move at the given position in fixed time. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        },
	        {
	            "name": "time",
	            "description": "The time to reach the target position [s]."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [x, y, theta, time, moveConfig])

def moveTo_5(controlPoint:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move to the given relative positions. This is a blocking call.
	
	Parameters
	----------
	controlPoint:object
		An ALValue with the control points in FRAME_ROBOT.
		Each control point is relative to the previous one. [[x1, y1, theta1], ..., [xN, yN, thetaN]
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(m)",
	    "description": "Makes the robot move to the given relative positions. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "controlPoint",
	            "description": "An ALValue with the control points in FRAME_ROBOT.\nEach control point is relative to the previous one. [[x1, y1, theta1], ..., [xN, yN, thetaN]"
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [controlPoint])

def moveTo_6(controlPoint:object, moveConfig:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (moveTo)
	
	Makes the robot move to the given relative positions. This is a blocking call.
	
	Parameters
	----------
	controlPoint:object
		An ALValue with all the control points in FRAME_ROBOT.
		Each control point is relative to the previous one. [[x1, y1, theta1], ..., [xN, yN, thetaN]
	moveConfig:object
		An ALValue with custom move configuration.
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "b",
	    "name": "moveTo",
	    "parametersSignature": "(mm)",
	    "description": "Makes the robot move to the given relative positions. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "controlPoint",
	            "description": "An ALValue with all the control points in FRAME_ROBOT.\nEach control point is relative to the previous one. [[x1, y1, theta1], ..., [xN, yN, thetaN]"
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveTo", [controlPoint, moveConfig])

def _moveToPod_1(x:float, y:float, theta:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (_moveToPod)
	
	Makes the robot move at the given position, without taking into account ENABLE_MOVE_PROTECTION config
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "_moveToPod",
	    "parametersSignature": "(fff)",
	    "description": "Makes the robot move at the given position, without taking into account ENABLE_MOVE_PROTECTION config",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "_moveToPod", [x, y, theta])

def _moveToPod_2(x:float, y:float, theta:float, moveConfig:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (_moveToPod)
	
	Makes the robot move at the given position, without taking into account ENABLE_MOVE_PROTECTION config
	
	Parameters
	----------
	x:float
		The position along x axis [m].
	y:float
		The position along y axis [m].
	theta:float
		The position around z axis [rd].
	moveConfig:object
		An ALValue with custom move configuration.
	
	Returns
	----------
	true if the moveTo finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "b",
	    "name": "_moveToPod",
	    "parametersSignature": "(fffm)",
	    "description": "Makes the robot move at the given position, without taking into account ENABLE_MOVE_PROTECTION config",
	    "parameters": [
	        {
	            "name": "x",
	            "description": "The position along x axis [m]."
	        },
	        {
	            "name": "y",
	            "description": "The position along y axis [m]."
	        },
	        {
	            "name": "theta",
	            "description": "The position around z axis [rd]."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": "true if the moveTo finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "_moveToPod", [x, y, theta, moveConfig])

def _followPath_1(path:object, moveConfig:object) -> None:
	"""
	Note: This is one of the overloads of the original method (_followPath)
	
	Makes the robot follow a given path. This is a non-blocking call.
	
	Parameters
	----------
	path:object
		An ALValue describing a 2D path.
	moveConfig:object
		An ALValue with custom move configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "v",
	    "name": "_followPath",
	    "parametersSignature": "(mm)",
	    "description": "Makes the robot follow a given path. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "path",
	            "description": "An ALValue describing a 2D path."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_followPath", [path, moveConfig])

def _followPath_2(path:object) -> None:
	"""
	Note: This is one of the overloads of the original method (_followPath)
	
	Makes the robot follow a given path. This is a non-blocking call.
	
	Parameters
	----------
	path:object
		An ALValue describing a 2D path.
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "v",
	    "name": "_followPath",
	    "parametersSignature": "(m)",
	    "description": "Makes the robot follow a given path. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "path",
	            "description": "An ALValue describing a 2D path."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_followPath", [path])

def _followPathInWorld_1(poseStart:object, path:object, moveConfig:object) -> None:
	"""
	Note: This is one of the overloads of the original method (_followPathInWorld)
	
	Makes the robot follow a given path, in world frame. This is a non-blocking call.
	
	Parameters
	----------
	poseStart:object
		A Pose2D setting the start frame of the path, in World.
	path:object
		An ALValue describing a 2D Path.
	moveConfig:object
		An ALValue with custom move configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_followPathInWorld",
	    "parametersSignature": "(mmm)",
	    "description": "Makes the robot follow a given path, in world frame. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "poseStart",
	            "description": "A Pose2D setting the start frame of the path, in World."
	        },
	        {
	            "name": "path",
	            "description": "An ALValue describing a 2D Path."
	        },
	        {
	            "name": "moveConfig",
	            "description": "An ALValue with custom move configuration."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_followPathInWorld", [poseStart, path, moveConfig])

def _followPathInWorld_2(poseStart:object, path:object) -> None:
	"""
	Note: This is one of the overloads of the original method (_followPathInWorld)
	
	Makes the robot follow a given path, in world frame. This is a non-blocking call.
	
	Parameters
	----------
	poseStart:object
		A Pose2D setting the start frame of the path, in World.
	path:object
		An ALValue describing a 2D Path.
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "_followPathInWorld",
	    "parametersSignature": "(mm)",
	    "description": "Makes the robot follow a given path, in world frame. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "poseStart",
	            "description": "A Pose2D setting the start frame of the path, in World."
	        },
	        {
	            "name": "path",
	            "description": "An ALValue describing a 2D Path."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_followPathInWorld", [poseStart, path])

def _setFollowPathSpeedFactor(speedFactor:float) -> None:
	"""
	Changes the reference speed for trajectory following
	
	Parameters
	----------
	speedFactor:float
		Between 0 and 1, relative to max speed
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "v",
	    "name": "_setFollowPathSpeedFactor",
	    "parametersSignature": "(f)",
	    "description": "Changes the reference speed for trajectory following",
	    "parameters": [
	        {
	            "name": "speedFactor",
	            "description": "Between 0 and 1, relative to max speed"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setFollowPathSpeedFactor", [speedFactor])

def _moveAlong_1(trajectory:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (_moveAlong)
	
	Move along a trajectory
	
	Parameters
	----------
	trajectory:object
		An ALValue describing a trajectory.
	
	Returns
	----------
	true if the moveAlong finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "b",
	    "name": "_moveAlong",
	    "parametersSignature": "(m)",
	    "description": "Move along a trajectory",
	    "parameters": [
	        {
	            "name": "trajectory",
	            "description": "An ALValue describing a trajectory."
	        }
	    ],
	    "returnDescription": "true if the moveAlong finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "_moveAlong", [trajectory])

def _moveAlong_2(trajectory:object, scaleFactor:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (_moveAlong)
	
	Move along a trajectory
	
	Parameters
	----------
	trajectory:object
		An ALValue describing a trajectory.
	scaleFactor:float
		A float between 0 and 1 scaling the trajectory.
	
	Returns
	----------
	true if the moveAlong finished successfully
	
	*Reference struct*
	'''
	{
	    "uid": 161,
	    "returnSignature": "b",
	    "name": "_moveAlong",
	    "parametersSignature": "(mf)",
	    "description": "Move along a trajectory",
	    "parameters": [
	        {
	            "name": "trajectory",
	            "description": "An ALValue describing a trajectory."
	        },
	        {
	            "name": "scaleFactor",
	            "description": "A float between 0 and 1 scaling the trajectory."
	        }
	    ],
	    "returnDescription": "true if the moveAlong finished successfully"
	}
	'''
	"""
	return send_mfc("ALMotion", "_moveAlong", [trajectory, scaleFactor])

def _stopAndStitchMoveAlong() -> None:
	"""
	Stop current trajectory, then resync
	
	*Reference struct*
	'''
	{
	    "uid": 162,
	    "returnSignature": "v",
	    "name": "_stopAndStitchMoveAlong",
	    "parametersSignature": "()",
	    "description": "Stop current trajectory, then resync",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_stopAndStitchMoveAlong", [])

def _getRemainingPath(sampleStep:float) -> object:
	"""
	Get a vector of samples along the current path
	
	Parameters
	----------
	sampleStep:float
		Distance between two samples, in m
	
	Returns
	----------
	vector of samples along trajectory
	
	*Reference struct*
	'''
	{
	    "uid": 163,
	    "returnSignature": "m",
	    "name": "_getRemainingPath",
	    "parametersSignature": "(f)",
	    "description": "Get a vector of samples along the current path",
	    "parameters": [
	        {
	            "name": "sampleStep",
	            "description": "Distance between two samples, in m"
	        }
	    ],
	    "returnDescription": "vector of samples along trajectory"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getRemainingPath", [sampleStep])

def _getRemainingTrajectory(timeStep:float, preview:float) -> object:
	"""
	Get a vector of samples along the current trajectory
	
	Parameters
	----------
	timeStep:float
		Time between two samples, in s
	preview:float
		Duration of the preview, in s
	
	Returns
	----------
	vector of samples along trajectory
	
	*Reference struct*
	'''
	{
	    "uid": 164,
	    "returnSignature": "m",
	    "name": "_getRemainingTrajectory",
	    "parametersSignature": "(ff)",
	    "description": "Get a vector of samples along the current trajectory",
	    "parameters": [
	        {
	            "name": "timeStep",
	            "description": "Time between two samples, in s"
	        },
	        {
	            "name": "preview",
	            "description": "Duration of the preview, in s"
	        }
	    ],
	    "returnDescription": "vector of samples along trajectory"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getRemainingTrajectory", [timeStep, preview])

def _getTrajectoryCompletion() -> float:
	"""
	Get the ratio of executed trajectory, between 0 and 1
	
	Returns
	----------
	float between 0 and 1
	
	*Reference struct*
	'''
	{
	    "uid": 165,
	    "returnSignature": "f",
	    "name": "_getTrajectoryCompletion",
	    "parametersSignature": "()",
	    "description": "Get the ratio of executed trajectory, between 0 and 1",
	    "parameters": [],
	    "returnDescription": "float between 0 and 1"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getTrajectoryCompletion", [])

def setFootSteps(legName:List[str], footSteps:object, timeList:List[float], clearExisting:bool) -> None:
	"""
	Makes Nao do foot step planner. This is a non-blocking call.
	
	Parameters
	----------
	legName:List[str]
		name of the leg to move('LLeg'or 'RLeg')
	footSteps:object
		[x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]
	timeList:List[float]
		time list of each foot step
	clearExisting:bool
		Clear existing foot steps.
	
	*Reference struct*
	'''
	{
	    "uid": 170,
	    "returnSignature": "v",
	    "name": "setFootSteps",
	    "parametersSignature": "([s]m[f]b)",
	    "description": "Makes Nao do foot step planner. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "legName",
	            "description": "name of the leg to move('LLeg'or 'RLeg')"
	        },
	        {
	            "name": "footSteps",
	            "description": "[x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]"
	        },
	        {
	            "name": "timeList",
	            "description": "time list of each foot step"
	        },
	        {
	            "name": "clearExisting",
	            "description": "Clear existing foot steps."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setFootSteps", [legName, footSteps, timeList, clearExisting])

def setFootStepsWithSpeed(legName:List[str], footSteps:object, fractionMaxSpeed:List[float], clearExisting:bool) -> None:
	"""
	Makes Nao do foot step planner with speed. This is a blocking call.
	
	Parameters
	----------
	legName:List[str]
		name of the leg to move('LLeg'or 'RLeg')
	footSteps:object
		[x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]
	fractionMaxSpeed:List[float]
		speed of each foot step. Must be between 0 and 1.
	clearExisting:bool
		Clear existing foot steps.
	
	*Reference struct*
	'''
	{
	    "uid": 171,
	    "returnSignature": "v",
	    "name": "setFootStepsWithSpeed",
	    "parametersSignature": "([s]m[f]b)",
	    "description": "Makes Nao do foot step planner with speed. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "legName",
	            "description": "name of the leg to move('LLeg'or 'RLeg')"
	        },
	        {
	            "name": "footSteps",
	            "description": "[x, y, theta], [Position along X/Y, Orientation round Z axis] of the leg relative to the other Leg in [meters, meters, radians]. Must be less than [MaxStepX, MaxStepY, MaxStepTheta]"
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "speed of each foot step. Must be between 0 and 1."
	        },
	        {
	            "name": "clearExisting",
	            "description": "Clear existing foot steps."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setFootStepsWithSpeed", [legName, footSteps, fractionMaxSpeed, clearExisting])

def getFootSteps() -> object:
	"""
	Get the foot steps. This is a non-blocking call.
	
	Returns
	----------
	Give two list of foot steps. The first one give the unchangeable foot step. The second list give the changeable foot steps. Il you use setFootSteps or setFootStepsWithSpeed with clearExisting parmater equal true, walk engine execute unchangeable foot step and remove the other.
	
	*Reference struct*
	'''
	{
	    "uid": 172,
	    "returnSignature": "m",
	    "name": "getFootSteps",
	    "parametersSignature": "()",
	    "description": "Get the foot steps. This is a non-blocking call.",
	    "parameters": [],
	    "returnDescription": "Give two list of foot steps. The first one give the unchangeable foot step. The second list give the changeable foot steps. Il you use setFootSteps or setFootStepsWithSpeed with clearExisting parmater equal true, walk engine execute unchangeable foot step and remove the other."
	}
	'''
	"""
	return send_mfc("ALMotion", "getFootSteps", [])

def moveInit() -> None:
	"""
	Initialize the move process. Check the robot pose and take a right posture. This is blocking called.
	
	*Reference struct*
	'''
	{
	    "uid": 174,
	    "returnSignature": "v",
	    "name": "moveInit",
	    "parametersSignature": "()",
	    "description": "Initialize the move process. Check the robot pose and take a right posture. This is blocking called.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "moveInit", [])

def waitUntilMoveIsFinished() -> None:
	"""
	Waits until the move process is finished: This method can be used to block your script/code execution until the move task is totally finished.
	
	*Reference struct*
	'''
	{
	    "uid": 176,
	    "returnSignature": "v",
	    "name": "waitUntilMoveIsFinished",
	    "parametersSignature": "()",
	    "description": "Waits until the move process is finished: This method can be used to block your script/code execution until the move task is totally finished.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "waitUntilMoveIsFinished", [])

def moveIsActive() -> bool:
	"""
	Check if the move process is actif.
	
	Returns
	----------
	True if move is active
	
	*Reference struct*
	'''
	{
	    "uid": 178,
	    "returnSignature": "b",
	    "name": "moveIsActive",
	    "parametersSignature": "()",
	    "description": "Check if the move process is actif.",
	    "parameters": [],
	    "returnDescription": "True if move is active"
	}
	'''
	"""
	return send_mfc("ALMotion", "moveIsActive", [])

def stopMove() -> bool:
	"""
	Stop Move task safely as fast as possible. The move task is ended less brutally than killMove but more quickly than move(0.0, 0.0, 0.0).
	This is a blocking call.
	
	*Reference struct*
	'''
	{
	    "uid": 180,
	    "returnSignature": "b",
	    "name": "stopMove",
	    "parametersSignature": "()",
	    "description": "Stop Move task safely as fast as possible. The move task is ended less brutally than killMove but more quickly than move(0.0, 0.0, 0.0).\nThis is a blocking call.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "stopMove", [])

def getMoveConfig(config:str) -> object:
	"""
	Gets the move config.
	
	Parameters
	----------
	config:str
		a string should be "Max", "Min", "Default"
	
	Returns
	----------
	An ALvalue with the move config
	
	*Reference struct*
	'''
	{
	    "uid": 182,
	    "returnSignature": "m",
	    "name": "getMoveConfig",
	    "parametersSignature": "(s)",
	    "description": "Gets the move config.",
	    "parameters": [
	        {
	            "name": "config",
	            "description": "a string should be \"Max\", \"Min\", \"Default\""
	        }
	    ],
	    "returnDescription": "An ALvalue with the move config"
	}
	'''
	"""
	return send_mfc("ALMotion", "getMoveConfig", [config])

def getRobotPosition(useSensors:bool) -> List[float]:
	"""
	Gets the World Absolute Robot Position.
	
	Parameters
	----------
	useSensors:bool
		If true, use the sensor values
	
	Returns
	----------
	A vector containing the World Absolute Robot Position. (Absolute Position X, Absolute Position Y, Absolute Angle Z)
	
	*Reference struct*
	'''
	{
	    "uid": 183,
	    "returnSignature": "[f]",
	    "name": "getRobotPosition",
	    "parametersSignature": "(b)",
	    "description": "Gets the World Absolute Robot Position.",
	    "parameters": [
	        {
	            "name": "useSensors",
	            "description": "If true, use the sensor values"
	        }
	    ],
	    "returnDescription": "A vector containing the World Absolute Robot Position. (Absolute Position X, Absolute Position Y, Absolute Angle Z)"
	}
	'''
	"""
	return send_mfc("ALMotion", "getRobotPosition", [useSensors])

def getNextRobotPosition() -> List[float]:
	"""
	Gets the World Absolute next Robot Position.
	In fact in the walk algorithm some foot futur foot step are incompressible due to preview control, so this function give the next robot position which is incompressible.
	If the robot doesn't walk this function is equivalent to getRobotPosition(false)
	
	
	Returns
	----------
	A vector containing the World Absolute next Robot position.(Absolute Position X, Absolute Position Y, Absolute Angle Z)
	
	*Reference struct*
	'''
	{
	    "uid": 184,
	    "returnSignature": "[f]",
	    "name": "getNextRobotPosition",
	    "parametersSignature": "()",
	    "description": "Gets the World Absolute next Robot Position.\nIn fact in the walk algorithm some foot futur foot step are incompressible due to preview control, so this function give the next robot position which is incompressible.\nIf the robot doesn't walk this function is equivalent to getRobotPosition(false)\n",
	    "parameters": [],
	    "returnDescription": "A vector containing the World Absolute next Robot position.(Absolute Position X, Absolute Position Y, Absolute Angle Z)"
	}
	'''
	"""
	return send_mfc("ALMotion", "getNextRobotPosition", [])

def getRobotVelocity() -> List[float]:
	"""
	Gets the World Absolute Robot Velocity.
	
	Returns
	----------
	A vector containing the World Absolute Robot Velocity. (Absolute Velocity Translation X [m.s-1], Absolute Velocity Translation Y[m.s-1], Absolute Velocity Rotation WZ [rd.s-1])
	
	*Reference struct*
	'''
	{
	    "uid": 185,
	    "returnSignature": "[f]",
	    "name": "getRobotVelocity",
	    "parametersSignature": "()",
	    "description": "Gets the World Absolute Robot Velocity.",
	    "parameters": [],
	    "returnDescription": "A vector containing the World Absolute Robot Velocity. (Absolute Velocity Translation X [m.s-1], Absolute Velocity Translation Y[m.s-1], Absolute Velocity Rotation WZ [rd.s-1])"
	}
	'''
	"""
	return send_mfc("ALMotion", "getRobotVelocity", [])

def _getCumulatedDisplacement() -> List[float]:
	"""
	Get the absolute cumulated displacement since robot is up, in robot frame.
	
	Returns
	----------
	A vector containing the absolute cumulated displacement, in robot frame. (Absolute Displacement X [m], Absolute Displacement Y[m], Absolute Displacement Theta [rd])
	
	*Reference struct*
	'''
	{
	    "uid": 186,
	    "returnSignature": "[f]",
	    "name": "_getCumulatedDisplacement",
	    "parametersSignature": "()",
	    "description": "Get the absolute cumulated displacement since robot is up, in robot frame.",
	    "parameters": [],
	    "returnDescription": "A vector containing the absolute cumulated displacement, in robot frame. (Absolute Displacement X [m], Absolute Displacement Y[m], Absolute Displacement Theta [rd])"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getCumulatedDisplacement", [])

def getMoveArmsEnabled(chainName:str) -> bool:
	"""
	Gets if Arms Motions are enabled during the Move Process.
	
	Parameters
	----------
	chainName:str
		Name of the chain. Could be: "LArm", "RArm" or "Arms"
	
	Returns
	----------
	For LArm and RArm true if the corresponding arm is enabled. For Arms, true if both are enabled. False otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 189,
	    "returnSignature": "b",
	    "name": "getMoveArmsEnabled",
	    "parametersSignature": "(s)",
	    "description": "Gets if Arms Motions are enabled during the Move Process.",
	    "parameters": [
	        {
	            "name": "chainName",
	            "description": "Name of the chain. Could be: \"LArm\", \"RArm\" or \"Arms\""
	        }
	    ],
	    "returnDescription": "For LArm and RArm true if the corresponding arm is enabled. For Arms, true if both are enabled. False otherwise."
	}
	'''
	"""
	return send_mfc("ALMotion", "getMoveArmsEnabled", [chainName])

def setMoveArmsEnabled(leftArmEnabled:bool, rightArmEnabled:bool) -> None:
	"""
	Sets if Arms Motions are enabled during the Move Process.
	
	Parameters
	----------
	leftArmEnabled:bool
		if true Left Arm motions are controlled by the Move Task
	rightArmEnabled:bool
		if true Right Arm mMotions are controlled by the Move Task
	
	*Reference struct*
	'''
	{
	    "uid": 190,
	    "returnSignature": "v",
	    "name": "setMoveArmsEnabled",
	    "parametersSignature": "(bb)",
	    "description": "Sets if Arms Motions are enabled during the Move Process.",
	    "parameters": [
	        {
	            "name": "leftArmEnabled",
	            "description": "if true Left Arm motions are controlled by the Move Task"
	        },
	        {
	            "name": "rightArmEnabled",
	            "description": "if true Right Arm mMotions are controlled by the Move Task"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setMoveArmsEnabled", [leftArmEnabled, rightArmEnabled])

def positionInterpolations(effectorNames:object, taskSpaceForAllPaths:object, paths:object, axisMasks:object, relativeTimes:object) -> None:
	"""
	Moves end-effectors to the given positions and orientations over time. This is a blocking call.
	
	Parameters
	----------
	effectorNames:object
		Vector of chain names. Could be: "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso" 
	taskSpaceForAllPaths:object
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	paths:object
		Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians
	axisMasks:object
		Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both 
	relativeTimes:object
		Vector of times in seconds corresponding to the path points
	
	*Reference struct*
	'''
	{
	    "uid": 193,
	    "returnSignature": "v",
	    "name": "positionInterpolations",
	    "parametersSignature": "(mmmmm)",
	    "description": "Moves end-effectors to the given positions and orientations over time. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "effectorNames",
	            "description": "Vector of chain names. Could be: \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\" "
	        },
	        {
	            "name": "taskSpaceForAllPaths",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "paths",
	            "description": "Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians"
	        },
	        {
	            "name": "axisMasks",
	            "description": "Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both "
	        },
	        {
	            "name": "relativeTimes",
	            "description": "Vector of times in seconds corresponding to the path points"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "positionInterpolations", [effectorNames, taskSpaceForAllPaths, paths, axisMasks, relativeTimes])

def setPositions(names:object, spaces:object, positions:object, fractionMaxSpeed:float, axisMask:object) -> None:
	"""
	Moves multiple end-effectors to the given position and orientation position6d. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		The name or names of effector.
	spaces:object
		The task frame or task frames {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	positions:object
		Position6D arrays
	fractionMaxSpeed:float
		The fraction of maximum speed to use
	axisMask:object
		Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both 
	
	*Reference struct*
	'''
	{
	    "uid": 195,
	    "returnSignature": "v",
	    "name": "setPositions",
	    "parametersSignature": "(mmmfm)",
	    "description": "Moves multiple end-effectors to the given position and orientation position6d. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "The name or names of effector."
	        },
	        {
	            "name": "spaces",
	            "description": "The task frame or task frames {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "positions",
	            "description": "Position6D arrays"
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "The fraction of maximum speed to use"
	        },
	        {
	            "name": "axisMask",
	            "description": "Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setPositions", [names, spaces, positions, fractionMaxSpeed, axisMask])

def getPosition(name:str, space:int, useSensorValues:bool) -> List[float]:
	"""
	Gets a Position relative to the FRAME. Axis definition: the x axis is positive toward Nao's front, the y from right to left and the z is vertical. The angle convention of Position6D is Rot_z(wz).Rot_y(wy).Rot_x(wx).
	
	Parameters
	----------
	name:str
		Name of the item. Could be: Head, LArm, RArm, LLeg, RLeg, Torso, CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot.
	space:int
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	useSensorValues:bool
		If true, the sensor values will be used to determine the position.
	
	Returns
	----------
	Vector containing the Position6D using meters and radians (x, y, z, wx, wy, wz)
	
	*Reference struct*
	'''
	{
	    "uid": 197,
	    "returnSignature": "[f]",
	    "name": "getPosition",
	    "parametersSignature": "(sib)",
	    "description": "Gets a Position relative to the FRAME. Axis definition: the x axis is positive toward Nao's front, the y from right to left and the z is vertical. The angle convention of Position6D is Rot_z(wz).Rot_y(wy).Rot_x(wx).",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the item. Could be: Head, LArm, RArm, LLeg, RLeg, Torso, CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot."
	        },
	        {
	            "name": "space",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "useSensorValues",
	            "description": "If true, the sensor values will be used to determine the position."
	        }
	    ],
	    "returnDescription": "Vector containing the Position6D using meters and radians (x, y, z, wx, wy, wz)"
	}
	'''
	"""
	return send_mfc("ALMotion", "getPosition", [name, space, useSensorValues])

def transformInterpolations(effectorNames:object, taskSpaceForAllPaths:object, paths:object, axisMasks:object, relativeTimes:object) -> None:
	"""
	Moves end-effectors to the given positions and orientations over time. This is a blocking call.
	
	Parameters
	----------
	effectorNames:object
		Vector of chain names. Could be: "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso" 
	taskSpaceForAllPaths:object
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	paths:object
		Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians
	axisMasks:object
		Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both 
	relativeTimes:object
		Vector of times in seconds corresponding to the path points
	
	*Reference struct*
	'''
	{
	    "uid": 200,
	    "returnSignature": "v",
	    "name": "transformInterpolations",
	    "parametersSignature": "(mmmmm)",
	    "description": "Moves end-effectors to the given positions and orientations over time. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "effectorNames",
	            "description": "Vector of chain names. Could be: \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\" "
	        },
	        {
	            "name": "taskSpaceForAllPaths",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "paths",
	            "description": "Vector of 6D position arrays (x,y,z,wx,wy,wz) in meters and radians"
	        },
	        {
	            "name": "axisMasks",
	            "description": "Vector of Axis Masks. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both "
	        },
	        {
	            "name": "relativeTimes",
	            "description": "Vector of times in seconds corresponding to the path points"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "transformInterpolations", [effectorNames, taskSpaceForAllPaths, paths, axisMasks, relativeTimes])

def setTransforms(names:object, spaces:object, transforms:object, fractionMaxSpeed:float, axisMask:object) -> None:
	"""
	Moves multiple end-effectors to the given position and orientation transforms. This is a non-blocking call.
	
	Parameters
	----------
	names:object
		The name or names of effector.
	spaces:object
		The task frame or task frames {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	transforms:object
		Transform arrays
	fractionMaxSpeed:float
		The fraction of maximum speed to use
	axisMask:object
		Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both 
	
	*Reference struct*
	'''
	{
	    "uid": 202,
	    "returnSignature": "v",
	    "name": "setTransforms",
	    "parametersSignature": "(mmmfm)",
	    "description": "Moves multiple end-effectors to the given position and orientation transforms. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "The name or names of effector."
	        },
	        {
	            "name": "spaces",
	            "description": "The task frame or task frames {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "transforms",
	            "description": "Transform arrays"
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "The fraction of maximum speed to use"
	        },
	        {
	            "name": "axisMask",
	            "description": "Axis mask. True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setTransforms", [names, spaces, transforms, fractionMaxSpeed, axisMask])

def getTransform(name:str, space:int, useSensorValues:bool) -> List[float]:
	"""
	Gets an Homogenous Transform relative to the FRAME. Axis definition: the x axis is positive toward Nao's front, the y from right to left and the z is vertical.
	
	Parameters
	----------
	name:str
		Name of the item. Could be: any joint or chain or sensor (Head, LArm, RArm, LLeg, RLeg, Torso, HeadYaw, ..., CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot.
	space:int
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	useSensorValues:bool
		If true, the sensor values will be used to determine the position.
	
	Returns
	----------
	Vector of 16 floats corresponding to the values of the matrix, line by line.
	
	*Reference struct*
	'''
	{
	    "uid": 204,
	    "returnSignature": "[f]",
	    "name": "getTransform",
	    "parametersSignature": "(sib)",
	    "description": "Gets an Homogenous Transform relative to the FRAME. Axis definition: the x axis is positive toward Nao's front, the y from right to left and the z is vertical.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of the item. Could be: any joint or chain or sensor (Head, LArm, RArm, LLeg, RLeg, Torso, HeadYaw, ..., CameraTop, CameraBottom, MicroFront, MicroRear, MicroLeft, MicroRight, Accelerometer, Gyrometer, Laser, LFsrFR, LFsrFL, LFsrRR, LFsrRL, RFsrFR, RFsrFL, RFsrRR, RFsrRL, USSensor1, USSensor2, USSensor3, USSensor4. Use getSensorNames for the list of sensors supported on your robot."
	        },
	        {
	            "name": "space",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "useSensorValues",
	            "description": "If true, the sensor values will be used to determine the position."
	        }
	    ],
	    "returnDescription": "Vector of 16 floats corresponding to the values of the matrix, line by line."
	}
	'''
	"""
	return send_mfc("ALMotion", "getTransform", [name, space, useSensorValues])

def _getSensorTransformAtTime(sensorName:str, time:int) -> List[float]:
	"""
	Gets an Homogenous Transform in World. 
	
	Parameters
	----------
	sensorName:str
		Name of the sensor
	time:int
		A qi::ClockTimePoint
	
	Returns
	----------
	Vector of 16 floats corresponding to the values of the matrix, line by line.
	
	*Reference struct*
	'''
	{
	    "uid": 205,
	    "returnSignature": "[f]",
	    "name": "_getSensorTransformAtTime",
	    "parametersSignature": "(sL)",
	    "description": "Gets an Homogenous Transform in World. ",
	    "parameters": [
	        {
	            "name": "sensorName",
	            "description": "Name of the sensor"
	        },
	        {
	            "name": "time",
	            "description": "A qi::ClockTimePoint"
	        }
	    ],
	    "returnDescription": "Vector of 16 floats corresponding to the values of the matrix, line by line."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getSensorTransformAtTime", [sensorName, time])

def wbEnable(isEnabled:bool) -> None:
	"""
	UserFriendly Whole Body API: enable Whole Body Balancer. It's a Generalized Inverse Kinematics which deals with cartesian control, balance, redundancy and task priority. The main goal is to generate and stabilized consistent motions without precomputed trajectories and adapt nao's behaviour to the situation. The generalized inverse kinematic problem takes in account equality constraints (keep foot fix), inequality constraints (joint limits, balance, ...) and quadratic minimization (cartesian / articular desired trajectories). We solve each step a quadratic programming on the robot.
	
	Parameters
	----------
	isEnabled:bool
		Active / Disactive Whole Body Balancer.
	
	*Reference struct*
	'''
	{
	    "uid": 206,
	    "returnSignature": "v",
	    "name": "wbEnable",
	    "parametersSignature": "(b)",
	    "description": "UserFriendly Whole Body API: enable Whole Body Balancer. It's a Generalized Inverse Kinematics which deals with cartesian control, balance, redundancy and task priority. The main goal is to generate and stabilized consistent motions without precomputed trajectories and adapt nao's behaviour to the situation. The generalized inverse kinematic problem takes in account equality constraints (keep foot fix), inequality constraints (joint limits, balance, ...) and quadratic minimization (cartesian / articular desired trajectories). We solve each step a quadratic programming on the robot.",
	    "parameters": [
	        {
	            "name": "isEnabled",
	            "description": "Active / Disactive Whole Body Balancer."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbEnable", [isEnabled])

def _enableAutoBalance(isEnabled:bool) -> bool:
	"""
	Enable autobalance on your robot.
	
	Parameters
	----------
	isEnabled:bool
		Enable or Disable autobalance.
	
	Returns
	----------
	Success to enable autobalance.
	
	*Reference struct*
	'''
	{
	    "uid": 207,
	    "returnSignature": "b",
	    "name": "_enableAutoBalance",
	    "parametersSignature": "(b)",
	    "description": "Enable autobalance on your robot.",
	    "parameters": [
	        {
	            "name": "isEnabled",
	            "description": "Enable or Disable autobalance."
	        }
	    ],
	    "returnDescription": "Success to enable autobalance."
	}
	'''
	"""
	return send_mfc("ALMotion", "_enableAutoBalance", [isEnabled])

def _changeSupportMode(isEnabled:bool, name:str) -> bool:
	"""
	Change the support mode to keep balance on a define leg..
	
	Parameters
	----------
	isEnabled:bool
		Active / Disactive Whole Body Balancer.
	name:str
		The name of the support leg ("Legs", "LLeg" or "RLeg".
	
	Returns
	----------
	Successfully changed support mode.
	
	*Reference struct*
	'''
	{
	    "uid": 208,
	    "returnSignature": "b",
	    "name": "_changeSupportMode",
	    "parametersSignature": "(bs)",
	    "description": "Change the support mode to keep balance on a define leg..",
	    "parameters": [
	        {
	            "name": "isEnabled",
	            "description": "Active / Disactive Whole Body Balancer."
	        },
	        {
	            "name": "name",
	            "description": "The name of the support leg (\"Legs\", \"LLeg\" or \"RLeg\"."
	        }
	    ],
	    "returnDescription": "Successfully changed support mode."
	}
	'''
	"""
	return send_mfc("ALMotion", "_changeSupportMode", [isEnabled, name])

def wbFootState(stateName:str, supportLeg:str) -> None:
	"""
	UserFriendly Whole Body API: set the foot state: fixed foot, constrained in a plane or free.
	
	Parameters
	----------
	stateName:str
		Name of the foot state. "Fixed" set the foot fixed. "Plane" constrained the Foot in the plane. "Free" set the foot free.
	supportLeg:str
		Name of the foot. "LLeg", "RLeg" or "Legs".
	
	*Reference struct*
	'''
	{
	    "uid": 209,
	    "returnSignature": "v",
	    "name": "wbFootState",
	    "parametersSignature": "(ss)",
	    "description": "UserFriendly Whole Body API: set the foot state: fixed foot, constrained in a plane or free.",
	    "parameters": [
	        {
	            "name": "stateName",
	            "description": "Name of the foot state. \"Fixed\" set the foot fixed. \"Plane\" constrained the Foot in the plane. \"Free\" set the foot free."
	        },
	        {
	            "name": "supportLeg",
	            "description": "Name of the foot. \"LLeg\", \"RLeg\" or \"Legs\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbFootState", [stateName, supportLeg])

def wbEnableBalanceConstraint(isEnable:bool, supportLeg:str) -> None:
	"""
	UserFriendly Whole Body API: enable to keep balance in support polygon.
	
	Parameters
	----------
	isEnable:bool
		Enable Robot to keep balance.
	supportLeg:str
		Name of the support leg: "Legs", "LLeg", "RLeg".
	
	*Reference struct*
	'''
	{
	    "uid": 210,
	    "returnSignature": "v",
	    "name": "wbEnableBalanceConstraint",
	    "parametersSignature": "(bs)",
	    "description": "UserFriendly Whole Body API: enable to keep balance in support polygon.",
	    "parameters": [
	        {
	            "name": "isEnable",
	            "description": "Enable Robot to keep balance."
	        },
	        {
	            "name": "supportLeg",
	            "description": "Name of the support leg: \"Legs\", \"LLeg\", \"RLeg\"."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbEnableBalanceConstraint", [isEnable, supportLeg])

def wbGoToBalance(supportLeg:str, duration:float) -> bool:
	"""
	Advanced Whole Body API: "Com" go to a desired support polygon. This is a blocking call.
	
	Parameters
	----------
	supportLeg:str
		Name of the support leg: "Legs", "LLeg", "RLeg".
	duration:float
		Time in seconds. Must be upper 0.5 s.
	
	Returns
	----------
	A boolean of the success of the go to balance.
	
	*Reference struct*
	'''
	{
	    "uid": 211,
	    "returnSignature": "b",
	    "name": "wbGoToBalance",
	    "parametersSignature": "(sf)",
	    "description": "Advanced Whole Body API: \"Com\" go to a desired support polygon. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "supportLeg",
	            "description": "Name of the support leg: \"Legs\", \"LLeg\", \"RLeg\"."
	        },
	        {
	            "name": "duration",
	            "description": "Time in seconds. Must be upper 0.5 s."
	        }
	    ],
	    "returnDescription": "A boolean of the success of the go to balance."
	}
	'''
	"""
	return send_mfc("ALMotion", "wbGoToBalance", [supportLeg, duration])

def wbGoToBalanceWithSpeed(supportLeg:str, fractionMaxSpeed:float) -> bool:
	"""
	Advanced Whole Body API: "Com" go to a desired support polygon. This is a blocking call.
	
	Parameters
	----------
	supportLeg:str
		Name of the support leg: "Legs", "LLeg", "RLeg".
	fractionMaxSpeed:float
		The fraction of maximum speed to use.
	
	Returns
	----------
	A boolean of the success of the go to balance.
	
	*Reference struct*
	'''
	{
	    "uid": 212,
	    "returnSignature": "b",
	    "name": "wbGoToBalanceWithSpeed",
	    "parametersSignature": "(sf)",
	    "description": "Advanced Whole Body API: \"Com\" go to a desired support polygon. This is a blocking call.",
	    "parameters": [
	        {
	            "name": "supportLeg",
	            "description": "Name of the support leg: \"Legs\", \"LLeg\", \"RLeg\"."
	        },
	        {
	            "name": "fractionMaxSpeed",
	            "description": "The fraction of maximum speed to use."
	        }
	    ],
	    "returnDescription": "A boolean of the success of the go to balance."
	}
	'''
	"""
	return send_mfc("ALMotion", "wbGoToBalanceWithSpeed", [supportLeg, fractionMaxSpeed])

def wbEnableEffectorControl(effectorName:str, isEnabled:bool) -> None:
	"""
	UserFriendly Whole Body API: enable whole body cartesian control of an effector.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "Head", "LArm" or "RArm". Nao goes to posture init. He manages his balance and keep foot fix. "Head" is controlled in rotation. "LArm" and "RArm" are controlled in position.
	isEnabled:bool
		Active / Disactive Effector Control.
	
	*Reference struct*
	'''
	{
	    "uid": 213,
	    "returnSignature": "v",
	    "name": "wbEnableEffectorControl",
	    "parametersSignature": "(sb)",
	    "description": "UserFriendly Whole Body API: enable whole body cartesian control of an effector.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"Head\", \"LArm\" or \"RArm\". Nao goes to posture init. He manages his balance and keep foot fix. \"Head\" is controlled in rotation. \"LArm\" and \"RArm\" are controlled in position."
	        },
	        {
	            "name": "isEnabled",
	            "description": "Active / Disactive Effector Control."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbEnableEffectorControl", [effectorName, isEnabled])

def wbSetEffectorControl(effectorName:str, targetCoordinate:object) -> None:
	"""
	UserFriendly Whole Body API: set new target for controlled effector. This is a non-blocking call.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "Head", "LArm" or "RArm". Nao goes to posture init. He manages his balance and keep foot fix. "Head" is controlled in rotation. "LArm" and "RArm" are controlled in position.
	targetCoordinate:object
		"Head" is controlled in rotation (WX, WY, WZ). "LArm" and "RArm" are controlled in position (X, Y, Z). TargetCoordinate must be absolute and expressed in FRAME_ROBOT. If the desired position/orientation is unfeasible, target is resize to the nearest feasible motion.
	
	*Reference struct*
	'''
	{
	    "uid": 214,
	    "returnSignature": "v",
	    "name": "wbSetEffectorControl",
	    "parametersSignature": "(sm)",
	    "description": "UserFriendly Whole Body API: set new target for controlled effector. This is a non-blocking call.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"Head\", \"LArm\" or \"RArm\". Nao goes to posture init. He manages his balance and keep foot fix. \"Head\" is controlled in rotation. \"LArm\" and \"RArm\" are controlled in position."
	        },
	        {
	            "name": "targetCoordinate",
	            "description": "\"Head\" is controlled in rotation (WX, WY, WZ). \"LArm\" and \"RArm\" are controlled in position (X, Y, Z). TargetCoordinate must be absolute and expressed in FRAME_ROBOT. If the desired position/orientation is unfeasible, target is resize to the nearest feasible motion."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbSetEffectorControl", [effectorName, targetCoordinate])

def wbEnableEffectorOptimization(effectorName:str, isActive:bool) -> None:
	"""
	Advanced Whole Body API: enable to control an effector as an optimization.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "All", "Arms", "Legs", "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	isActive:bool
		if true, the effector control is taken in acount in the optimization criteria.
	
	*Reference struct*
	'''
	{
	    "uid": 215,
	    "returnSignature": "v",
	    "name": "wbEnableEffectorOptimization",
	    "parametersSignature": "(sb)",
	    "description": "Advanced Whole Body API: enable to control an effector as an optimization.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"All\", \"Arms\", \"Legs\", \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        },
	        {
	            "name": "isActive",
	            "description": "if true, the effector control is taken in acount in the optimization criteria."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "wbEnableEffectorOptimization", [effectorName, isActive])

def _wbGetBalanceState() -> str:
	"""
	UserFriendly Whole Body API: get Whole Body Balance State.
	
	Returns
	----------
	Name of the Whole Body Balance State ("None", "LLeg", "RLeg" or "Legs"). 
	
	*Reference struct*
	'''
	{
	    "uid": 216,
	    "returnSignature": "s",
	    "name": "_wbGetBalanceState",
	    "parametersSignature": "()",
	    "description": "UserFriendly Whole Body API: get Whole Body Balance State.",
	    "parameters": [],
	    "returnDescription": "Name of the Whole Body Balance State (\"None\", \"LLeg\", \"RLeg\" or \"Legs\"). "
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbGetBalanceState", [])

def _wbIsActive() -> bool:
	"""
	UserFriendly Whole Body API: get Whole Body is active.
	
	Returns
	----------
	Get Whole Body is active.
	
	*Reference struct*
	'''
	{
	    "uid": 217,
	    "returnSignature": "b",
	    "name": "_wbIsActive",
	    "parametersSignature": "()",
	    "description": "UserFriendly Whole Body API: get Whole Body is active.",
	    "parameters": [],
	    "returnDescription": "Get Whole Body is active."
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbIsActive", [])

def _wbDefaultConfiguration() -> None:
	"""
	UserFriendly Whole Body API: reset the default Whole Body Configuration.
	
	*Reference struct*
	'''
	{
	    "uid": 218,
	    "returnSignature": "v",
	    "name": "_wbDefaultConfiguration",
	    "parametersSignature": "()",
	    "description": "UserFriendly Whole Body API: reset the default Whole Body Configuration.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbDefaultConfiguration", [])

def _wbGetFootState(supportLeg:str) -> str:
	"""
	UserFriendly Whole Body API: get the foot state: fixed foot, constrained in a plane or free.
	
	Parameters
	----------
	supportLeg:str
		Name of the foot. "LLeg", "RLeg" or "Legs".
	
	Returns
	----------
	Name of the foot state. "Fixed" set the foot fixed. "Plane" constrained the Foot in the plane. "Free" set the foot free.
	
	*Reference struct*
	'''
	{
	    "uid": 219,
	    "returnSignature": "s",
	    "name": "_wbGetFootState",
	    "parametersSignature": "(s)",
	    "description": "UserFriendly Whole Body API: get the foot state: fixed foot, constrained in a plane or free.",
	    "parameters": [
	        {
	            "name": "supportLeg",
	            "description": "Name of the foot. \"LLeg\", \"RLeg\" or \"Legs\"."
	        }
	    ],
	    "returnDescription": "Name of the foot state. \"Fixed\" set the foot fixed. \"Plane\" constrained the Foot in the plane. \"Free\" set the foot free."
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbGetFootState", [supportLeg])

def _wbSetJointWeighting(jointNames:str, weightings:float) -> None:
	"""
	Advanced Whole Body API: weighting of Joint used in Whole Body Optimization criteria. It is the priority of Joint motion in front of all the other motion task in the quadratic programming optimization.
	
	Parameters
	----------
	jointNames:str
		Name or names of joints, chains, "Body" or "Joints".
	weightings:float
		Weight used in the Whole Body Articular Optimization.Limits : 0 &lt; weighting &lt;= 1000.0. "articularControl" default value : 1000.0.
	
	*Reference struct*
	'''
	{
	    "uid": 220,
	    "returnSignature": "v",
	    "name": "_wbSetJointWeighting",
	    "parametersSignature": "(sf)",
	    "description": "Advanced Whole Body API: weighting of Joint used in Whole Body Optimization criteria. It is the priority of Joint motion in front of all the other motion task in the quadratic programming optimization.",
	    "parameters": [
	        {
	            "name": "jointNames",
	            "description": "Name or names of joints, chains, \"Body\" or \"Joints\"."
	        },
	        {
	            "name": "weightings",
	            "description": "Weight used in the Whole Body Articular Optimization.Limits : 0 &lt; weighting &lt;= 1000.0. \"articularControl\" default value : 1000.0."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbSetJointWeighting", [jointNames, weightings])

def _wbSetJointStiffness(jointName:str, stiffness:float) -> None:
	"""
	Advanced Whole Body API: stiffness of Joint used in Whole Body Optimization criteria. It is the stiffness of Joint motion control used in the quadratic programming optimization.
	
	Parameters
	----------
	jointName:str
		Name or names of joints, chains, "Body" or "Joints".
	stiffness:float
		Stiffness used in the Whole Body Articular Optimization.Limits : 0 &lt; stiffness &lt;= 100.0."articularControl" default value : 30.0.
	
	*Reference struct*
	'''
	{
	    "uid": 221,
	    "returnSignature": "v",
	    "name": "_wbSetJointStiffness",
	    "parametersSignature": "(sf)",
	    "description": "Advanced Whole Body API: stiffness of Joint used in Whole Body Optimization criteria. It is the stiffness of Joint motion control used in the quadratic programming optimization.",
	    "parameters": [
	        {
	            "name": "jointName",
	            "description": "Name or names of joints, chains, \"Body\" or \"Joints\"."
	        },
	        {
	            "name": "stiffness",
	            "description": "Stiffness used in the Whole Body Articular Optimization.Limits : 0 &lt; stiffness &lt;= 100.0.\"articularControl\" default value : 30.0."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbSetJointStiffness", [jointName, stiffness])

def _wbSetArticularLimitPreview(jointName:str, preview:int) -> None:
	"""
	Advanced Whole Body API: preview of Joint Inequality Constraint. It constraint the max joint velocity computed by the quadratic programming. If preview = 1, joint limits can be achieved in 1 step. If preview = 5, joint limits can be achieved in 5 steps. The more preview is, the less desired motion is realised. But the more preview is, the motion safety is increased.
	
	Parameters
	----------
	jointName:str
		Name or names of joints, chains, "Body" or "Joints".
	preview:int
		Preview used in the Whole Body Inequality Constraints. Between [1 50].articularControl" default value : 1.
	
	*Reference struct*
	'''
	{
	    "uid": 222,
	    "returnSignature": "v",
	    "name": "_wbSetArticularLimitPreview",
	    "parametersSignature": "(si)",
	    "description": "Advanced Whole Body API: preview of Joint Inequality Constraint. It constraint the max joint velocity computed by the quadratic programming. If preview = 1, joint limits can be achieved in 1 step. If preview = 5, joint limits can be achieved in 5 steps. The more preview is, the less desired motion is realised. But the more preview is, the motion safety is increased.",
	    "parameters": [
	        {
	            "name": "jointName",
	            "description": "Name or names of joints, chains, \"Body\" or \"Joints\"."
	        },
	        {
	            "name": "preview",
	            "description": "Preview used in the Whole Body Inequality Constraints. Between [1 50].articularControl\" default value : 1."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbSetArticularLimitPreview", [jointName, preview])

def _wbEnableEffectorConstraint(effectorName:str, isActive:bool, axisMask:int) -> None:
	"""
	Advanced Whole Body API: enable to control an effector as a constraint.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "All", "Arms", "Legs", "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	isActive:bool
		if true, the effector control is taken in acount in the optimization criteria.
	axisMask:int
		True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both.
	
	*Reference struct*
	'''
	{
	    "uid": 223,
	    "returnSignature": "v",
	    "name": "_wbEnableEffectorConstraint",
	    "parametersSignature": "(sbi)",
	    "description": "Advanced Whole Body API: enable to control an effector as a constraint.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"All\", \"Arms\", \"Legs\", \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        },
	        {
	            "name": "isActive",
	            "description": "if true, the effector control is taken in acount in the optimization criteria."
	        },
	        {
	            "name": "axisMask",
	            "description": "True for axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbEnableEffectorConstraint", [effectorName, isActive, axisMask])

def _wbGetEffectorConstraint(effectorName:str) -> object:
	"""
	Advanced Whole Body API: get effector constraint state.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	
	Returns
	----------
	[isActive, axisMask].
	
	*Reference struct*
	'''
	{
	    "uid": 224,
	    "returnSignature": "m",
	    "name": "_wbGetEffectorConstraint",
	    "parametersSignature": "(s)",
	    "description": "Advanced Whole Body API: get effector constraint state.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        }
	    ],
	    "returnDescription": "[isActive, axisMask]."
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbGetEffectorConstraint", [effectorName])

def _wbAxisMaskEffector(effectorName:str, isOptimized:bool, axisMask:int) -> None:
	"""
	Advanced Whole Body API: enable to set the axis mask of an effector.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "All", "Arms", "Legs", "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	isOptimized:bool
		if true, the optimized effector axis mask is setting, else it is the constrained effector axis mask.
	axisMask:int
		Axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both.
	
	*Reference struct*
	'''
	{
	    "uid": 225,
	    "returnSignature": "v",
	    "name": "_wbAxisMaskEffector",
	    "parametersSignature": "(sbi)",
	    "description": "Advanced Whole Body API: enable to set the axis mask of an effector.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"All\", \"Arms\", \"Legs\", \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        },
	        {
	            "name": "isOptimized",
	            "description": "if true, the optimized effector axis mask is setting, else it is the constrained effector axis mask."
	        },
	        {
	            "name": "axisMask",
	            "description": "Axes that you wish to control. e.g. 7 for position only, 56 for rotation only and 63 for both."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbAxisMaskEffector", [effectorName, isOptimized, axisMask])

def _wbEnableJointOptimization(jointName:str, isActive:bool) -> None:
	"""
	Advanced Whole Body API: enable to control a joint as an optimization.
	
	Parameters
	----------
	jointName:str
		 "Body", name of the chain ("LLeg",...) or name of the joint : "HeadYaw", "LKneePitch".
	isActive:bool
		if true, the joint control is taken in acount in the optimization criteria.
	
	*Reference struct*
	'''
	{
	    "uid": 226,
	    "returnSignature": "v",
	    "name": "_wbEnableJointOptimization",
	    "parametersSignature": "(sb)",
	    "description": "Advanced Whole Body API: enable to control a joint as an optimization.",
	    "parameters": [
	        {
	            "name": "jointName",
	            "description": " \"Body\", name of the chain (\"LLeg\",...) or name of the joint : \"HeadYaw\", \"LKneePitch\"."
	        },
	        {
	            "name": "isActive",
	            "description": "if true, the joint control is taken in acount in the optimization criteria."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbEnableJointOptimization", [jointName, isActive])

def _wbGetEffectorOptimization(effectorName:str) -> object:
	"""
	Advanced Whole Body API: get effector constraint state.
	
	Parameters
	----------
	effectorName:str
		Name of the effector : "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	
	Returns
	----------
	[isActive, axisMask].
	
	*Reference struct*
	'''
	{
	    "uid": 227,
	    "returnSignature": "m",
	    "name": "_wbGetEffectorOptimization",
	    "parametersSignature": "(s)",
	    "description": "Advanced Whole Body API: get effector constraint state.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "Name of the effector : \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        }
	    ],
	    "returnDescription": "[isActive, axisMask]."
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbGetEffectorOptimization", [effectorName])

def _wbSetEffectorWeight(effectorName:str, weightingList:object) -> None:
	"""
	Advanced Whole Body API: set Effector Weighting in the Whole Body Optimization. It is the priority of Effector motion in front of all the other motion task in the quadratic programming optimization.
	
	Parameters
	----------
	effectorName:str
		"All", "Arms", "Legs", "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	weightingList:object
		Weighting used in the Whole Body Cartesian Optimization. Limits : 0 &lt; weighting &lt;= 1000.0. Default value is 1000.0. We can give the 6 weights corresponding to the 6 degree of freedom of cartesian motion. (WeightX, WeightY, WeightZ, WeightWX, WeightWY, WeightWZ). We can give 2 weights corresponding to translation and rotation axis (WeightTranslation, WeightTranslation, WeightTranslation, WeightRotation, WeightRotation, WeightRotation). We can give 1 weight, it is the same weight for all the axis (Weight, Weight, Weight, Weight, Weight, Weight).
	
	*Reference struct*
	'''
	{
	    "uid": 228,
	    "returnSignature": "v",
	    "name": "_wbSetEffectorWeight",
	    "parametersSignature": "(sm)",
	    "description": "Advanced Whole Body API: set Effector Weighting in the Whole Body Optimization. It is the priority of Effector motion in front of all the other motion task in the quadratic programming optimization.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "\"All\", \"Arms\", \"Legs\", \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        },
	        {
	            "name": "weightingList",
	            "description": "Weighting used in the Whole Body Cartesian Optimization. Limits : 0 &lt; weighting &lt;= 1000.0. Default value is 1000.0. We can give the 6 weights corresponding to the 6 degree of freedom of cartesian motion. (WeightX, WeightY, WeightZ, WeightWX, WeightWY, WeightWZ). We can give 2 weights corresponding to translation and rotation axis (WeightTranslation, WeightTranslation, WeightTranslation, WeightRotation, WeightRotation, WeightRotation). We can give 1 weight, it is the same weight for all the axis (Weight, Weight, Weight, Weight, Weight, Weight)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbSetEffectorWeight", [effectorName, weightingList])

def _wbSetEffectorStiffness(effectorName:str, stiffnessList:object) -> None:
	"""
	Advanced Whole Body API: set Effector Stiffness in Cartesian Control.
	
	Parameters
	----------
	effectorName:str
		"All", "Arms", "Legs", "Head", "LArm", "RArm", "LLeg", "RLeg", "Torso", "Com".
	stiffnessList:object
		Stiffness used in the Whole Body Cartesian Optimization. Limits : 0 &lt; stiffness &lt;= 100.0. Default value is 10.0. We can give the 6 stiffnesses corresponding to the 6 degree of freedom of cartesian motion. (StiffnessX, StiffnessY, StiffnessZ, StiffnessWX, StiffnessWY, StiffnessWZ). We can give 2 weights corresponding to translation and rotation axis (StiffnessTranslation, StiffnessTranslation, StiffnessTranslation, StiffnessRotation, StiffnessRotation, StiffnessRotation). We can give 1 stiffness, it is the same stiffness for all the axis (Stiffness, Stiffness, Stiffness, Stiffness, Stiffness, Stiffness).
	
	*Reference struct*
	'''
	{
	    "uid": 229,
	    "returnSignature": "v",
	    "name": "_wbSetEffectorStiffness",
	    "parametersSignature": "(sm)",
	    "description": "Advanced Whole Body API: set Effector Stiffness in Cartesian Control.",
	    "parameters": [
	        {
	            "name": "effectorName",
	            "description": "\"All\", \"Arms\", \"Legs\", \"Head\", \"LArm\", \"RArm\", \"LLeg\", \"RLeg\", \"Torso\", \"Com\"."
	        },
	        {
	            "name": "stiffnessList",
	            "description": "Stiffness used in the Whole Body Cartesian Optimization. Limits : 0 &lt; stiffness &lt;= 100.0. Default value is 10.0. We can give the 6 stiffnesses corresponding to the 6 degree of freedom of cartesian motion. (StiffnessX, StiffnessY, StiffnessZ, StiffnessWX, StiffnessWY, StiffnessWZ). We can give 2 weights corresponding to translation and rotation axis (StiffnessTranslation, StiffnessTranslation, StiffnessTranslation, StiffnessRotation, StiffnessRotation, StiffnessRotation). We can give 1 stiffness, it is the same stiffness for all the axis (Stiffness, Stiffness, Stiffness, Stiffness, Stiffness, Stiffness)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_wbSetEffectorStiffness", [effectorName, stiffnessList])

def setCollisionProtectionEnabled(pChainName:str, pEnable:bool) -> bool:
	"""
	Enable Anticollision protection of the arms of the robot. Use api isCollision to know if a chain is in collision and can be disactivated.
	
	Parameters
	----------
	pChainName:str
		The chain name {"Arms", "LArm" or "RArm"}.
	pEnable:bool
		Activate or disactivate the anticollision of the desired Chain.
	
	Returns
	----------
	A bool which return always true.
	
	*Reference struct*
	'''
	{
	    "uid": 230,
	    "returnSignature": "b",
	    "name": "setCollisionProtectionEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Enable Anticollision protection of the arms of the robot. Use api isCollision to know if a chain is in collision and can be disactivated.",
	    "parameters": [
	        {
	            "name": "pChainName",
	            "description": "The chain name {\"Arms\", \"LArm\" or \"RArm\"}."
	        },
	        {
	            "name": "pEnable",
	            "description": "Activate or disactivate the anticollision of the desired Chain."
	        }
	    ],
	    "returnDescription": "A bool which return always true."
	}
	'''
	"""
	return send_mfc("ALMotion", "setCollisionProtectionEnabled", [pChainName, pEnable])

def getCollisionProtectionEnabled(pChainName:str) -> bool:
	"""
	Allow to know if the collision protection is activated on the given chain.
	
	Parameters
	----------
	pChainName:str
		The chain name {"LArm" or "RArm"}.
	
	Returns
	----------
	Return true is the collision protection of the given Arm is activated.
	
	*Reference struct*
	'''
	{
	    "uid": 231,
	    "returnSignature": "b",
	    "name": "getCollisionProtectionEnabled",
	    "parametersSignature": "(s)",
	    "description": "Allow to know if the collision protection is activated on the given chain.",
	    "parameters": [
	        {
	            "name": "pChainName",
	            "description": "The chain name {\"LArm\" or \"RArm\"}."
	        }
	    ],
	    "returnDescription": "Return true is the collision protection of the given Arm is activated."
	}
	'''
	"""
	return send_mfc("ALMotion", "getCollisionProtectionEnabled", [pChainName])

def setExternalCollisionProtectionEnabled(pName:str, pEnable:bool) -> None:
	"""
	Enable Anticollision protection of the arms and base move  of the robot with external environment.
	
	Parameters
	----------
	pName:str
		The name {"All", "Move", "Arms", "LArm" or "RArm"}.
	pEnable:bool
		Activate or disactivate the anticollision of the desired name.
	
	*Reference struct*
	'''
	{
	    "uid": 232,
	    "returnSignature": "v",
	    "name": "setExternalCollisionProtectionEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Enable Anticollision protection of the arms and base move  of the robot with external environment.",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "The name {\"All\", \"Move\", \"Arms\", \"LArm\" or \"RArm\"}."
	        },
	        {
	            "name": "pEnable",
	            "description": "Activate or disactivate the anticollision of the desired name."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setExternalCollisionProtectionEnabled", [pName, pEnable])

def _enablePhysicalInteractionForChain(pChain:str, pEnabled:bool) -> None:
	"""
	Enable/Disable physical interaction on a chain without disabling safety completely
	
	Parameters
	----------
	pChain:str
		The chain name {"LArm", "RArm", "Arms"}
	pEnabled:bool
		True/False
	
	*Reference struct*
	'''
	{
	    "uid": 233,
	    "returnSignature": "v",
	    "name": "_enablePhysicalInteractionForChain",
	    "parametersSignature": "(sb)",
	    "description": "Enable/Disable physical interaction on a chain without disabling safety completely",
	    "parameters": [
	        {
	            "name": "pChain",
	            "description": "The chain name {\"LArm\", \"RArm\", \"Arms\"}"
	        },
	        {
	            "name": "pEnabled",
	            "description": "True/False"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_enablePhysicalInteractionForChain", [pChain, pEnabled])

def getChainClosestObstaclePosition(pName:str, space:int) -> List[float]:
	"""
	Gets chain closest obstacle Position .
	
	Parameters
	----------
	pName:str
		The Chain name {"LArm" or "RArm"}.
	space:int
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	
	Returns
	----------
	Vector containing the Position3D in meters (x, y, z)
	
	*Reference struct*
	'''
	{
	    "uid": 234,
	    "returnSignature": "[f]",
	    "name": "getChainClosestObstaclePosition",
	    "parametersSignature": "(si)",
	    "description": "Gets chain closest obstacle Position .",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "The Chain name {\"LArm\" or \"RArm\"}."
	        },
	        {
	            "name": "space",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        }
	    ],
	    "returnDescription": "Vector containing the Position3D in meters (x, y, z)"
	}
	'''
	"""
	return send_mfc("ALMotion", "getChainClosestObstaclePosition", [pName, space])

def getExternalCollisionProtectionEnabled(pName:str) -> bool:
	"""
	Allow to know if the external collision protection is activated on the given name.
	
	Parameters
	----------
	pName:str
		The name {"All", "Move", "Arms", "LArm" or "RArm"}.
	
	Returns
	----------
	Return true is the external collision protection of the given name is activated.
	
	*Reference struct*
	'''
	{
	    "uid": 235,
	    "returnSignature": "b",
	    "name": "getExternalCollisionProtectionEnabled",
	    "parametersSignature": "(s)",
	    "description": "Allow to know if the external collision protection is activated on the given name.",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "The name {\"All\", \"Move\", \"Arms\", \"LArm\" or \"RArm\"}."
	        }
	    ],
	    "returnDescription": "Return true is the external collision protection of the given name is activated."
	}
	'''
	"""
	return send_mfc("ALMotion", "getExternalCollisionProtectionEnabled", [pName])

def setOrthogonalSecurityDistance(securityDistance:float) -> None:
	"""
	Defines the orthogonal security distance used with external collision protection "Move".
	
	Parameters
	----------
	securityDistance:float
		The orthogonal security distance.
	
	*Reference struct*
	'''
	{
	    "uid": 236,
	    "returnSignature": "v",
	    "name": "setOrthogonalSecurityDistance",
	    "parametersSignature": "(f)",
	    "description": "Defines the orthogonal security distance used with external collision protection \"Move\".",
	    "parameters": [
	        {
	            "name": "securityDistance",
	            "description": "The orthogonal security distance."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setOrthogonalSecurityDistance", [securityDistance])

def getOrthogonalSecurityDistance() -> float:
	"""
	Gets the current orthogonal security distance.
	
	Returns
	----------
	The current orthogonal security distance.
	
	*Reference struct*
	'''
	{
	    "uid": 237,
	    "returnSignature": "f",
	    "name": "getOrthogonalSecurityDistance",
	    "parametersSignature": "()",
	    "description": "Gets the current orthogonal security distance.",
	    "parameters": [],
	    "returnDescription": "The current orthogonal security distance."
	}
	'''
	"""
	return send_mfc("ALMotion", "getOrthogonalSecurityDistance", [])

def setTangentialSecurityDistance(securityDistance:float) -> None:
	"""
	Defines the tangential security distance used with external collision protection "Move".
	
	Parameters
	----------
	securityDistance:float
		The tangential security distance.
	
	*Reference struct*
	'''
	{
	    "uid": 238,
	    "returnSignature": "v",
	    "name": "setTangentialSecurityDistance",
	    "parametersSignature": "(f)",
	    "description": "Defines the tangential security distance used with external collision protection \"Move\".",
	    "parameters": [
	        {
	            "name": "securityDistance",
	            "description": "The tangential security distance."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setTangentialSecurityDistance", [securityDistance])

def getTangentialSecurityDistance() -> float:
	"""
	Gets the current tangential security distance.
	
	Returns
	----------
	The current tangential security distance.
	
	*Reference struct*
	'''
	{
	    "uid": 239,
	    "returnSignature": "f",
	    "name": "getTangentialSecurityDistance",
	    "parametersSignature": "()",
	    "description": "Gets the current tangential security distance.",
	    "parameters": [],
	    "returnDescription": "The current tangential security distance."
	}
	'''
	"""
	return send_mfc("ALMotion", "getTangentialSecurityDistance", [])

def isCollision(pChainName:str) -> str:
	"""
	Give the collision state of a chain. If a chain has a collision state "none" or "near", it could be desactivated. 
	
	Parameters
	----------
	pChainName:str
		The chain name {"Arms", "LArm" or "RArm"}.
	
	Returns
	----------
	A string which notice the collision state: "none" there are no collision, "near" the collision is taking in account in the anti-collision algorithm, "collision" the chain is in contact with an other body. If the chain asked is "Arms" the most unfavorable result is given. 
	
	
	*Reference struct*
	'''
	{
	    "uid": 240,
	    "returnSignature": "s",
	    "name": "isCollision",
	    "parametersSignature": "(s)",
	    "description": "Give the collision state of a chain. If a chain has a collision state \"none\" or \"near\", it could be desactivated. ",
	    "parameters": [
	        {
	            "name": "pChainName",
	            "description": "The chain name {\"Arms\", \"LArm\" or \"RArm\"}."
	        }
	    ],
	    "returnDescription": "A string which notice the collision state: \"none\" there are no collision, \"near\" the collision is taking in account in the anti-collision algorithm, \"collision\" the chain is in contact with an other body. If the chain asked is \"Arms\" the most unfavorable result is given. \n"
	}
	'''
	"""
	return send_mfc("ALMotion", "isCollision", [pChainName])

def _getCollisionStateForObstacleSummary(pChainName:str) -> bool:
	"""
	Allow to know if the collision protection is activated on the given chain  and if stiffness of all chain joint is stricly positif.
	
	Parameters
	----------
	pChainName:str
		The chain name {"LArm" or "RArm"}.
	
	Returns
	----------
	Return true is the collision protection of the given Arm is activated.
	
	*Reference struct*
	'''
	{
	    "uid": 241,
	    "returnSignature": "b",
	    "name": "_getCollisionStateForObstacleSummary",
	    "parametersSignature": "(s)",
	    "description": "Allow to know if the collision protection is activated on the given chain  and if stiffness of all chain joint is stricly positif.",
	    "parameters": [
	        {
	            "name": "pChainName",
	            "description": "The chain name {\"LArm\" or \"RArm\"}."
	        }
	    ],
	    "returnDescription": "Return true is the collision protection of the given Arm is activated."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getCollisionStateForObstacleSummary", [pChainName])

def _getCollisionShapes(pName:str) -> object:
	"""
	Gets the list of dynamic collisions in torso frame.
	
	Parameters
	----------
	pName:str
		The name {"static" or "dynamic"}.
	
	Returns
	----------
	Vector of collisions name, radius, parent joint name andparent joint position.
	
	*Reference struct*
	'''
	{
	    "uid": 243,
	    "returnSignature": "m",
	    "name": "_getCollisionShapes",
	    "parametersSignature": "(s)",
	    "description": "Gets the list of dynamic collisions in torso frame.",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "The name {\"static\" or \"dynamic\"}."
	        }
	    ],
	    "returnDescription": "Vector of collisions name, radius, parent joint name andparent joint position."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getCollisionShapes", [pName])

def _setCollisionShapes(pNameList:List[str], pPairList:List[str], pBodyList:List[str], pTypeList:List[str], pShapeList:object, pPositionList:object) -> None:
	"""
	Set dynamic collision shape for people collision avoidance
	
	Parameters
	----------
	pNameList:List[str]
		A vector of names.
	pPairList:List[str]
		A vector of names. "All", "Sphere", "Pill" or the collision nameof LArm or RArm.
	pBodyList:List[str]
		A vector of body names. Dynamic collision is attached to this body.
	pTypeList:List[str]
		A vector of names. "Sphere", "Plan", "Pill" or "Tab".
	pShapeList:object
		A vector of shape data.
	pPositionList:object
		An ALValue containing a list of position of the shape.
	
	*Reference struct*
	'''
	{
	    "uid": 244,
	    "returnSignature": "v",
	    "name": "_setCollisionShapes",
	    "parametersSignature": "([s][s][s][s]mm)",
	    "description": "Set dynamic collision shape for people collision avoidance",
	    "parameters": [
	        {
	            "name": "pNameList",
	            "description": "A vector of names."
	        },
	        {
	            "name": "pPairList",
	            "description": "A vector of names. \"All\", \"Sphere\", \"Pill\" or the collision nameof LArm or RArm."
	        },
	        {
	            "name": "pBodyList",
	            "description": "A vector of body names. Dynamic collision is attached to this body."
	        },
	        {
	            "name": "pTypeList",
	            "description": "A vector of names. \"Sphere\", \"Plan\", \"Pill\" or \"Tab\"."
	        },
	        {
	            "name": "pShapeList",
	            "description": "A vector of shape data."
	        },
	        {
	            "name": "pPositionList",
	            "description": "An ALValue containing a list of position of the shape."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setCollisionShapes", [pNameList, pPairList, pBodyList, pTypeList, pShapeList, pPositionList])

def _getDetectedCollisions(pMinimumDistance:float) -> object:
	"""
	Gets the list of detected collisions supported on your robot.
	
	Parameters
	----------
	pMinimumDistance:float
		Distance to take into account collision pair.
	
	Returns
	----------
	Vector of collisions: [nameShape1, nameShape2, distance].
	
	*Reference struct*
	'''
	{
	    "uid": 246,
	    "returnSignature": "m",
	    "name": "_getDetectedCollisions",
	    "parametersSignature": "(f)",
	    "description": "Gets the list of detected collisions supported on your robot.",
	    "parameters": [
	        {
	            "name": "pMinimumDistance",
	            "description": "Distance to take into account collision pair."
	        }
	    ],
	    "returnDescription": "Vector of collisions: [nameShape1, nameShape2, distance]."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getDetectedCollisions", [pMinimumDistance])

def _getDetectedCollisionsFull() -> object:
	"""
	Gets the list of detected collisions supported on your robot.
	
	Returns
	----------
	Vector of collisions: [nameShape1, nameShape2, distance].
	
	*Reference struct*
	'''
	{
	    "uid": 247,
	    "returnSignature": "m",
	    "name": "_getDetectedCollisionsFull",
	    "parametersSignature": "()",
	    "description": "Gets the list of detected collisions supported on your robot.",
	    "parameters": [],
	    "returnDescription": "Vector of collisions: [nameShape1, nameShape2, distance]."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getDetectedCollisionsFull", [])

def _getDangerousRegion() -> object:
	"""
	Gets the polygon checked for safety during move.
	
	Returns
	----------
	A vector of Position2D.
	
	*Reference struct*
	'''
	{
	    "uid": 248,
	    "returnSignature": "m",
	    "name": "_getDangerousRegion",
	    "parametersSignature": "()",
	    "description": "Gets the polygon checked for safety during move.",
	    "parameters": [],
	    "returnDescription": "A vector of Position2D."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getDangerousRegion", [])

def setFallManagerEnabled(pEnable:bool) -> None:
	"""
	Enable The fall manager protection for the robot. When a fall is detected the robot adopt a joint configuration to protect himself and cut the stiffness.
	. An memory event called "robotHasFallen" is generated when the fallManager have been activated.
	
	Parameters
	----------
	pEnable:bool
		Activate or disactivate the smart stiffness.
	
	*Reference struct*
	'''
	{
	    "uid": 249,
	    "returnSignature": "v",
	    "name": "setFallManagerEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable The fall manager protection for the robot. When a fall is detected the robot adopt a joint configuration to protect himself and cut the stiffness.\n. An memory event called \"robotHasFallen\" is generated when the fallManager have been activated.",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Activate or disactivate the smart stiffness."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setFallManagerEnabled", [pEnable])

def getFallManagerEnabled() -> bool:
	"""
	Give the state of the fall manager.
	
	Returns
	----------
	Return true is the fall manager is activated. 
	
	
	*Reference struct*
	'''
	{
	    "uid": 250,
	    "returnSignature": "b",
	    "name": "getFallManagerEnabled",
	    "parametersSignature": "()",
	    "description": "Give the state of the fall manager.",
	    "parameters": [],
	    "returnDescription": "Return true is the fall manager is activated. \n"
	}
	'''
	"""
	return send_mfc("ALMotion", "getFallManagerEnabled", [])

def setPushRecoveryEnabled(pEnable:bool) -> None:
	"""
	Enable The push recovery protection for the robot. 
	
	Parameters
	----------
	pEnable:bool
		Enable the push recovery.
	
	*Reference struct*
	'''
	{
	    "uid": 251,
	    "returnSignature": "v",
	    "name": "setPushRecoveryEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable The push recovery protection for the robot. ",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Enable the push recovery."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setPushRecoveryEnabled", [pEnable])

def _setPushRecoveryEnabled(pEnable:bool) -> None:
	"""
	Enable The push recovery protection for the robot. 
	
	Parameters
	----------
	pEnable:bool
		Enable the push recovery.
	
	*Reference struct*
	'''
	{
	    "uid": 252,
	    "returnSignature": "v",
	    "name": "_setPushRecoveryEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable The push recovery protection for the robot. ",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Enable the push recovery."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setPushRecoveryEnabled", [pEnable])

def getPushRecoveryEnabled() -> bool:
	"""
	Give the state of the push recovery.
	
	Returns
	----------
	Return true is the push recovery is activated. 
	
	
	*Reference struct*
	'''
	{
	    "uid": 253,
	    "returnSignature": "b",
	    "name": "getPushRecoveryEnabled",
	    "parametersSignature": "()",
	    "description": "Give the state of the push recovery.",
	    "parameters": [],
	    "returnDescription": "Return true is the push recovery is activated. \n"
	}
	'''
	"""
	return send_mfc("ALMotion", "getPushRecoveryEnabled", [])

def setSmartStiffnessEnabled(pEnable:bool) -> None:
	"""
	Enable Smart Stiffness for all the joints (True by default), the update take one motion cycle for updating. The smart Stiffness is a gestion of joint maximum torque. More description is available on the red documentation of ALMotion module.
	
	Parameters
	----------
	pEnable:bool
		Activate or disactivate the smart stiffness.
	
	*Reference struct*
	'''
	{
	    "uid": 254,
	    "returnSignature": "v",
	    "name": "setSmartStiffnessEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable Smart Stiffness for all the joints (True by default), the update take one motion cycle for updating. The smart Stiffness is a gestion of joint maximum torque. More description is available on the red documentation of ALMotion module.",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Activate or disactivate the smart stiffness."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setSmartStiffnessEnabled", [pEnable])

def getSmartStiffnessEnabled() -> bool:
	"""
	Give the state of the smart Stiffness.
	
	Returns
	----------
	Return true is the smart Stiffnes is activated. 
	
	
	*Reference struct*
	'''
	{
	    "uid": 255,
	    "returnSignature": "b",
	    "name": "getSmartStiffnessEnabled",
	    "parametersSignature": "()",
	    "description": "Give the state of the smart Stiffness.",
	    "parameters": [],
	    "returnDescription": "Return true is the smart Stiffnes is activated. \n"
	}
	'''
	"""
	return send_mfc("ALMotion", "getSmartStiffnessEnabled", [])

def setDiagnosisEffectEnabled(pEnable:bool) -> None:
	"""
	Enable or disable the diagnosis effect into ALMotion
	
	Parameters
	----------
	pEnable:bool
		Enable or disable the diagnosis effect.
	
	*Reference struct*
	'''
	{
	    "uid": 256,
	    "returnSignature": "v",
	    "name": "setDiagnosisEffectEnabled",
	    "parametersSignature": "(b)",
	    "description": "Enable or disable the diagnosis effect into ALMotion",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Enable or disable the diagnosis effect."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setDiagnosisEffectEnabled", [pEnable])

def getDiagnosisEffectEnabled() -> bool:
	"""
	Give the state of the diagnosis effect.
	
	Returns
	----------
	Return true is the diagnosis reflex is activated. 
	
	
	*Reference struct*
	'''
	{
	    "uid": 257,
	    "returnSignature": "b",
	    "name": "getDiagnosisEffectEnabled",
	    "parametersSignature": "()",
	    "description": "Give the state of the diagnosis effect.",
	    "parameters": [],
	    "returnDescription": "Return true is the diagnosis reflex is activated. \n"
	}
	'''
	"""
	return send_mfc("ALMotion", "getDiagnosisEffectEnabled", [])

def getBodyNames(name:str) -> List[str]:
	"""
	Gets the names of all the joints and actuators in the collection.
	
	Parameters
	----------
	name:str
		Name of a chain, "Arms", "Legs", "Body", "Chains", "JointActuators", "Joints" or "Actuators".
	
	Returns
	----------
	Vector of strings, one for each joint and actuator in the collection
	
	*Reference struct*
	'''
	{
	    "uid": 259,
	    "returnSignature": "[s]",
	    "name": "getBodyNames",
	    "parametersSignature": "(s)",
	    "description": "Gets the names of all the joints and actuators in the collection.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of a chain, \"Arms\", \"Legs\", \"Body\", \"Chains\", \"JointActuators\", \"Joints\" or \"Actuators\"."
	        }
	    ],
	    "returnDescription": "Vector of strings, one for each joint and actuator in the collection"
	}
	'''
	"""
	return send_mfc("ALMotion", "getBodyNames", [name])

def getSensorNames() -> List[str]:
	"""
	Gets the list of sensors supported on your robot.
	
	Returns
	----------
	Vector of sensor names
	
	*Reference struct*
	'''
	{
	    "uid": 260,
	    "returnSignature": "[s]",
	    "name": "getSensorNames",
	    "parametersSignature": "()",
	    "description": "Gets the list of sensors supported on your robot.",
	    "parameters": [],
	    "returnDescription": "Vector of sensor names"
	}
	'''
	"""
	return send_mfc("ALMotion", "getSensorNames", [])

def getLimits(name:str) -> object:
	"""
	Get the minAngle (rad), maxAngle (rad), and maxVelocity (rad.s-1) for a given joint or actuator in the body.
	
	Parameters
	----------
	name:str
		Name of a joint, chain, "Body", "JointActuators", "Joints" or "Actuators". 
	
	Returns
	----------
	Array of ALValue arrays containing the minAngle, maxAngle, maxVelocity and maxTorque for all the bodies specified.
	
	*Reference struct*
	'''
	{
	    "uid": 261,
	    "returnSignature": "m",
	    "name": "getLimits",
	    "parametersSignature": "(s)",
	    "description": "Get the minAngle (rad), maxAngle (rad), and maxVelocity (rad.s-1) for a given joint or actuator in the body.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of a joint, chain, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        }
	    ],
	    "returnDescription": "Array of ALValue arrays containing the minAngle, maxAngle, maxVelocity and maxTorque for all the bodies specified."
	}
	'''
	"""
	return send_mfc("ALMotion", "getLimits", [name])

def _getFullLimits(name:str) -> object:
	"""
	Get the minAngle (rad), maxAngle (rad), and maxVelocity (rad.s-1) for a given joint or actuator in the body.
	
	Parameters
	----------
	name:str
		Name of a joint, chain, "Body", "JointActuators", "Joints" or "Actuators". 
	
	Returns
	----------
	Array of ALValue arrays containing the minAngle, maxAngle, maxVelocity, maxTorque, Kc, reduction, efficiency and maxCurrent for all the bodies specified.
	
	*Reference struct*
	'''
	{
	    "uid": 262,
	    "returnSignature": "m",
	    "name": "_getFullLimits",
	    "parametersSignature": "(s)",
	    "description": "Get the minAngle (rad), maxAngle (rad), and maxVelocity (rad.s-1) for a given joint or actuator in the body.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "Name of a joint, chain, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        }
	    ],
	    "returnDescription": "Array of ALValue arrays containing the minAngle, maxAngle, maxVelocity, maxTorque, Kc, reduction, efficiency and maxCurrent for all the bodies specified."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getFullLimits", [name])

def getMotionCycleTime() -> int:
	"""
	Get the motion cycle time in milliseconds.
	
	Returns
	----------
	Expressed in milliseconds
	
	*Reference struct*
	'''
	{
	    "uid": 263,
	    "returnSignature": "i",
	    "name": "getMotionCycleTime",
	    "parametersSignature": "()",
	    "description": "Get the motion cycle time in milliseconds.",
	    "parameters": [],
	    "returnDescription": "Expressed in milliseconds"
	}
	'''
	"""
	return send_mfc("ALMotion", "getMotionCycleTime", [])

def _getMotionCycleNumber() -> int:
	"""
	Get the motion cycle number in int.
	
	Returns
	----------
	Expressed in int.
	
	*Reference struct*
	'''
	{
	    "uid": 264,
	    "returnSignature": "i",
	    "name": "_getMotionCycleNumber",
	    "parametersSignature": "()",
	    "description": "Get the motion cycle number in int.",
	    "parameters": [],
	    "returnDescription": "Expressed in int."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getMotionCycleNumber", [])

def getSummary() -> str:
	"""
	Returns a string representation of the Model's state
	
	Returns
	----------
	A formated string
	
	*Reference struct*
	'''
	{
	    "uid": 266,
	    "returnSignature": "s",
	    "name": "getSummary",
	    "parametersSignature": "()",
	    "description": "Returns a string representation of the Model's state",
	    "parameters": [],
	    "returnDescription": "A formated string"
	}
	'''
	"""
	return send_mfc("ALMotion", "getSummary", [])

def _getSummary() -> str:
	"""
	Returns a string representation of the Model's state
	
	Returns
	----------
	A formated string
	
	*Reference struct*
	'''
	{
	    "uid": 267,
	    "returnSignature": "s",
	    "name": "_getSummary",
	    "parametersSignature": "()",
	    "description": "Returns a string representation of the Model's state",
	    "parameters": [],
	    "returnDescription": "A formated string"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getSummary", [])

def getMass(pName:str) -> float:
	"""
	Gets the mass of a joint, chain, "Body" or "Joints".
	
	Parameters
	----------
	pName:str
		Name of the body which we want the mass. "Body", "Joints" and "Com" give the total mass of nao. For the chain, it gives the total mass of the chain.
	
	Returns
	----------
	The mass in kg.
	
	*Reference struct*
	'''
	{
	    "uid": 268,
	    "returnSignature": "f",
	    "name": "getMass",
	    "parametersSignature": "(s)",
	    "description": "Gets the mass of a joint, chain, \"Body\" or \"Joints\".",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "Name of the body which we want the mass. \"Body\", \"Joints\" and \"Com\" give the total mass of nao. For the chain, it gives the total mass of the chain."
	        }
	    ],
	    "returnDescription": "The mass in kg."
	}
	'''
	"""
	return send_mfc("ALMotion", "getMass", [pName])

def getCOM(pName:str, pSpace:int, pUseSensorValues:bool) -> List[float]:
	"""
	Gets the COM of a joint, chain, "Body" or "Joints".
	
	Parameters
	----------
	pName:str
		Name of the body which we want the mass. In chain name case, this function give the com of the chain.
	pSpace:int
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pUseSensorValues:bool
		If true, the sensor values will be used to determine the position.
	
	Returns
	----------
	The COM position (meter).
	
	*Reference struct*
	'''
	{
	    "uid": 269,
	    "returnSignature": "[f]",
	    "name": "getCOM",
	    "parametersSignature": "(sib)",
	    "description": "Gets the COM of a joint, chain, \"Body\" or \"Joints\".",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "Name of the body which we want the mass. In chain name case, this function give the com of the chain."
	        },
	        {
	            "name": "pSpace",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pUseSensorValues",
	            "description": "If true, the sensor values will be used to determine the position."
	        }
	    ],
	    "returnDescription": "The COM position (meter)."
	}
	'''
	"""
	return send_mfc("ALMotion", "getCOM", [pName, pSpace, pUseSensorValues])

def getSupportPolygon(pSpace:int, pUseSensorValues:bool) -> List[List[float]]:
	"""
	Gets the support polygon
	
	Parameters
	----------
	pSpace:int
		Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pUseSensorValues:bool
		If true, the sensor values will be used to determine the position.
	
	Returns
	----------
	A vector containing the x,y coordinates of each of the outer points of the support polygon in specified frame.
	
	*Reference struct*
	'''
	{
	    "uid": 270,
	    "returnSignature": "[[f]]",
	    "name": "getSupportPolygon",
	    "parametersSignature": "(ib)",
	    "description": "Gets the support polygon",
	    "parameters": [
	        {
	            "name": "pSpace",
	            "description": "Task frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pUseSensorValues",
	            "description": "If true, the sensor values will be used to determine the position."
	        }
	    ],
	    "returnDescription": "A vector containing the x,y coordinates of each of the outer points of the support polygon in specified frame."
	}
	'''
	"""
	return send_mfc("ALMotion", "getSupportPolygon", [pSpace, pUseSensorValues])

def _getSupportPolygonBipedDebug(pName:str) -> List[List[float]]:
	"""
	Gets the support polygon
	
	Parameters
	----------
	pName:str
		LLeg or RLeg
	
	Returns
	----------
	A vector containing the x,y coordinates of each of the outer points of the support polygon in specified frame.
	
	*Reference struct*
	'''
	{
	    "uid": 271,
	    "returnSignature": "[[f]]",
	    "name": "_getSupportPolygonBipedDebug",
	    "parametersSignature": "(s)",
	    "description": "Gets the support polygon",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "LLeg or RLeg"
	        }
	    ],
	    "returnDescription": "A vector containing the x,y coordinates of each of the outer points of the support polygon in specified frame."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getSupportPolygonBipedDebug", [pName])

def _getTorque(names:object, useSensor:bool) -> List[float]:
	"""
	Gets the torque of the joints
	
	Parameters
	----------
	names:object
		Names the joints, chains, "Body", "Joints". 
	useSensor:bool
		If true, return the sensor torque.
	
	Returns
	----------
	Torques in N.m.
	
	*Reference struct*
	'''
	{
	    "uid": 272,
	    "returnSignature": "[f]",
	    "name": "_getTorque",
	    "parametersSignature": "(mb)",
	    "description": "Gets the torque of the joints",
	    "parameters": [
	        {
	            "name": "names",
	            "description": "Names the joints, chains, \"Body\", \"Joints\". "
	        },
	        {
	            "name": "useSensor",
	            "description": "If true, return the sensor torque."
	        }
	    ],
	    "returnDescription": "Torques in N.m."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getTorque", [names, useSensor])

def _getInertia(pName:str) -> List[float]:
	"""
	Gets the inertia matrice of a joint or "Torso".
	
	Parameters
	----------
	pName:str
		Name of the joint or "Torso". Inertia is given in the COM of the body, in poseZero orientation.
	
	Returns
	----------
	The inertia matrix (kg.m2).
	
	*Reference struct*
	'''
	{
	    "uid": 273,
	    "returnSignature": "[f]",
	    "name": "_getInertia",
	    "parametersSignature": "(s)",
	    "description": "Gets the inertia matrice of a joint or \"Torso\".",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "Name of the joint or \"Torso\". Inertia is given in the COM of the body, in poseZero orientation."
	        }
	    ],
	    "returnDescription": "The inertia matrix (kg.m2)."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getInertia", [pName])

def setMotionConfig(config:object) -> None:
	"""
	Internal Use.
	
	Parameters
	----------
	config:object
		Internal: An array of ALValues [i][0]: name, [i][1]: value
	
	*Reference struct*
	'''
	{
	    "uid": 274,
	    "returnSignature": "v",
	    "name": "setMotionConfig",
	    "parametersSignature": "(m)",
	    "description": "Internal Use.",
	    "parameters": [
	        {
	            "name": "config",
	            "description": "Internal: An array of ALValues [i][0]: name, [i][1]: value"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setMotionConfig", [config])

def _naoqiIsReadyCallback() -> None:
	"""
	Callback naoqi is ready.
	
	*Reference struct*
	'''
	{
	    "uid": 275,
	    "returnSignature": "v",
	    "name": "_naoqiIsReadyCallback",
	    "parametersSignature": "()",
	    "description": "Callback naoqi is ready.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_naoqiIsReadyCallback", [])

def _preferenceUpdatedCallback(p0:str, p1:object, p2:str) -> None:
	"""
	Callback preferences changed.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 276,
	    "returnSignature": "v",
	    "name": "_preferenceUpdatedCallback",
	    "parametersSignature": "(sms)",
	    "description": "Callback preferences changed.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_preferenceUpdatedCallback", [p0, p1, p2])

def _trackerLookAt(pNames:List[str], pTargetPositions:List[float], pLimits:List[object]) -> None:
	"""
	Interpolate with head with prediction.
	This function is mainly use by the tracker modules.
	
	
	Parameters
	----------
	pNames:List[str]
		list of Joints Names.
	pTargetPositions:List[float]
		list of Joints angles.
	pLimits:List[object]
		list of Joints limits.
	
	*Reference struct*
	'''
	{
	    "uid": 277,
	    "returnSignature": "v",
	    "name": "_trackerLookAt",
	    "parametersSignature": "([s][f][X])",
	    "description": "Interpolate with head with prediction.\nThis function is mainly use by the tracker modules.\n",
	    "parameters": [
	        {
	            "name": "pNames",
	            "description": "list of Joints Names."
	        },
	        {
	            "name": "pTargetPositions",
	            "description": "list of Joints angles."
	        },
	        {
	            "name": "pLimits",
	            "description": "list of Joints limits."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_trackerLookAt", [pNames, pTargetPositions, pLimits])

def _lookAtWbPersistent(pTargetWy:float, pTargetWz:float) -> None:
	"""
	lookAt in Whole Body mode.
	
	Parameters
	----------
	pTargetWy:float
		The target position wy in FRAME_ROBOT
	pTargetWz:float
		The target position wz in FRAME_ROBOT
	
	*Reference struct*
	'''
	{
	    "uid": 278,
	    "returnSignature": "v",
	    "name": "_lookAtWbPersistent",
	    "parametersSignature": "(ff)",
	    "description": "lookAt in Whole Body mode.",
	    "parameters": [
	        {
	            "name": "pTargetWy",
	            "description": "The target position wy in FRAME_ROBOT"
	        },
	        {
	            "name": "pTargetWz",
	            "description": "The target position wz in FRAME_ROBOT"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_lookAtWbPersistent", [pTargetWy, pTargetWz])

def _lookAtWb(pTargetWy:float, pTargetWz:float) -> None:
	"""
	lookAt in Whole Body mode.
	
	Parameters
	----------
	pTargetWy:float
		The target position wy in FRAME_ROBOT
	pTargetWz:float
		The target position wz in FRAME_ROBOT
	
	*Reference struct*
	'''
	{
	    "uid": 279,
	    "returnSignature": "v",
	    "name": "_lookAtWb",
	    "parametersSignature": "(ff)",
	    "description": "lookAt in Whole Body mode.",
	    "parameters": [
	        {
	            "name": "pTargetWy",
	            "description": "The target position wy in FRAME_ROBOT"
	        },
	        {
	            "name": "pTargetWz",
	            "description": "The target position wz in FRAME_ROBOT"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_lookAtWb", [pTargetWy, pTargetWz])

def _trackerPointAt(pNames:List[str], pTargetPositions:List[float]) -> None:
	"""
	Interpolate with hands with prediction.
	This function is mainly use by the tracker modules.
	
	
	Parameters
	----------
	pNames:List[str]
		list of Joints Names.
	pTargetPositions:List[float]
		list of Joints angles.
	
	*Reference struct*
	'''
	{
	    "uid": 280,
	    "returnSignature": "v",
	    "name": "_trackerPointAt",
	    "parametersSignature": "([s][f])",
	    "description": "Interpolate with hands with prediction.\nThis function is mainly use by the tracker modules.\n",
	    "parameters": [
	        {
	            "name": "pNames",
	            "description": "list of Joints Names."
	        },
	        {
	            "name": "pTargetPositions",
	            "description": "list of Joints angles."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_trackerPointAt", [pNames, pTargetPositions])

def _trackerWithSpeed(pNames:List[str], pTargetPositions:List[float], pTimeSinceDetectionMs:List[float], pMaxSpeedFraction:bool, pUseOfWholeBody:bool) -> None:
	"""
	Interpolate with speed without prediction.
	
	Parameters
	----------
	pNames:List[str]
		list of Joints Names.
	pTargetPositions:List[float]
		list of Joints angles.
	pTimeSinceDetectionMs:List[float]
		The time in Ms since the target was detected
	pMaxSpeedFraction:bool
		fraction max speed list.
	pUseOfWholeBody:bool
		If true, the target is follow in cartesian space by the Head with whole Body constraints.
	
	*Reference struct*
	'''
	{
	    "uid": 281,
	    "returnSignature": "v",
	    "name": "_trackerWithSpeed",
	    "parametersSignature": "([s][f][f]bb)",
	    "description": "Interpolate with speed without prediction.",
	    "parameters": [
	        {
	            "name": "pNames",
	            "description": "list of Joints Names."
	        },
	        {
	            "name": "pTargetPositions",
	            "description": "list of Joints angles."
	        },
	        {
	            "name": "pTimeSinceDetectionMs",
	            "description": "The time in Ms since the target was detected"
	        },
	        {
	            "name": "pMaxSpeedFraction",
	            "description": "fraction max speed list."
	        },
	        {
	            "name": "pUseOfWholeBody",
	            "description": "If true, the target is follow in cartesian space by the Head with whole Body constraints."
	        },
	        {
	            "name": "pIsPointAt",
	            "description": "if true use pointAt task else lookAt task."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_trackerWithSpeed", [pNames, pTargetPositions, pTimeSinceDetectionMs, pMaxSpeedFraction, pUseOfWholeBody])

def _lookAt_1(pTargetPosition:List[float], pFrame:int, pMaxSpeedFraction:float) -> None:
	"""
	Note: This is one of the overloads of the original method (_lookAt)
	
	lookAt
	
	Parameters
	----------
	pTargetPosition:List[float]
		position 3D to look at.
	pFrame:int
		Target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pMaxSpeedFraction:float
		fraction max speed.
	
	*Reference struct*
	'''
	{
	    "uid": 282,
	    "returnSignature": "v",
	    "name": "_lookAt",
	    "parametersSignature": "([f]if)",
	    "description": "lookAt",
	    "parameters": [
	        {
	            "name": "pTargetPosition",
	            "description": "position 3D to look at."
	        },
	        {
	            "name": "pFrame",
	            "description": "Target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pMaxSpeedFraction",
	            "description": "fraction max speed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_lookAt", [pTargetPosition, pFrame, pMaxSpeedFraction])

def _lookAt_2(pTargetPosition:List[float], pFrame:int, pEffectorId:int, pMaxSpeedFraction:float) -> None:
	"""
	Note: This is one of the overloads of the original method (_lookAt)
	
	lookAt
	
	Parameters
	----------
	pTargetPosition:List[float]
		position 3D to look at.
	pFrame:int
		Target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}.
	pEffectorId:int
		effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}.
	pMaxSpeedFraction:float
		fraction max speed.
	
	*Reference struct*
	'''
	{
	    "uid": 283,
	    "returnSignature": "v",
	    "name": "_lookAt",
	    "parametersSignature": "([f]iif)",
	    "description": "lookAt",
	    "parameters": [
	        {
	            "name": "pTargetPosition",
	            "description": "position 3D to look at."
	        },
	        {
	            "name": "pFrame",
	            "description": "Target frame {FRAME_TORSO = 0, FRAME_WORLD = 1, FRAME_ROBOT = 2}."
	        },
	        {
	            "name": "pEffectorId",
	            "description": "effector id {Middle of eyes = 0, Camera Top = 1, Camera Bottom = 2}."
	        },
	        {
	            "name": "pMaxSpeedFraction",
	            "description": "fraction max speed."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_lookAt", [pTargetPosition, pFrame, pEffectorId, pMaxSpeedFraction])

def _stopLookAt(pWithSpeed:bool) -> None:
	"""
	Stop lookAt task
	This function is mainly use by the tracker modules.
	
	
	Parameters
	----------
	pWithSpeed:bool
		if True stop lookAtWithSpeed task.
	
	*Reference struct*
	'''
	{
	    "uid": 284,
	    "returnSignature": "v",
	    "name": "_stopLookAt",
	    "parametersSignature": "(b)",
	    "description": "Stop lookAt task\nThis function is mainly use by the tracker modules.\n",
	    "parameters": [
	        {
	            "name": "pWithSpeed",
	            "description": "if True stop lookAtWithSpeed task."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_stopLookAt", [pWithSpeed])

def _stopPointAt(pWithSpeed:bool) -> None:
	"""
	Stop PointAt task
	This function is mainly use by the tracker modules.
	
	
	Parameters
	----------
	pWithSpeed:bool
		if True stop pointAtWithSpeed task.
	
	*Reference struct*
	'''
	{
	    "uid": 285,
	    "returnSignature": "v",
	    "name": "_stopPointAt",
	    "parametersSignature": "(b)",
	    "description": "Stop PointAt task\nThis function is mainly use by the tracker modules.\n",
	    "parameters": [
	        {
	            "name": "pWithSpeed",
	            "description": "if True stop pointAtWithSpeed task."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_stopPointAt", [pWithSpeed])

def _updateObstacles(obstacles:List[List[float]], blindZones:List[List[List[float]]]) -> None:
	"""
	Update obstacles
	
	Parameters
	----------
	obstacles:List[List[float]]
		List of closest obstacles [[x, y, z]...]
	blindZones:List[List[List[float]]]
		List of blind zones [[Position2D, Position2D...]...]
	
	*Reference struct*
	'''
	{
	    "uid": 286,
	    "returnSignature": "v",
	    "name": "_updateObstacles",
	    "parametersSignature": "([[f]][[[f]]])",
	    "description": "Update obstacles",
	    "parameters": [
	        {
	            "name": "obstacles",
	            "description": "List of closest obstacles [[x, y, z]...]"
	        },
	        {
	            "name": "blindZones",
	            "description": "List of blind zones [[Position2D, Position2D...]...]"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_updateObstacles", [obstacles, blindZones])

def setBreathEnabled(pChain:str, pIsEnabled:bool) -> None:
	"""
	This function starts or stops breathing animation on a chain.
	Chain name can be "Body", "Arms", "LArm", "RArm", "Legs" or "Head".
	Head breathing animation will work only if Leg animation is active.
	
	Parameters
	----------
	pChain:str
		Chain name.
	pIsEnabled:bool
		Enables / disables the chain.
	
	*Reference struct*
	'''
	{
	    "uid": 287,
	    "returnSignature": "v",
	    "name": "setBreathEnabled",
	    "parametersSignature": "(sb)",
	    "description": "This function starts or stops breathing animation on a chain.\nChain name can be \"Body\", \"Arms\", \"LArm\", \"RArm\", \"Legs\" or \"Head\".\nHead breathing animation will work only if Leg animation is active.",
	    "parameters": [
	        {
	            "name": "pChain",
	            "description": "Chain name."
	        },
	        {
	            "name": "pIsEnabled",
	            "description": "Enables / disables the chain."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setBreathEnabled", [pChain, pIsEnabled])

def getBreathEnabled(pChain:str) -> bool:
	"""
	This function gets the status of breathing animation on a chain.
	Chain name can be "Body", "Arms", "LArm", "RArm", "Legs" or "Head".
	
	
	Parameters
	----------
	pChain:str
		Chain name.
	
	Returns
	----------
	True if breathing animation is enabled on the chain.
	
	*Reference struct*
	'''
	{
	    "uid": 288,
	    "returnSignature": "b",
	    "name": "getBreathEnabled",
	    "parametersSignature": "(s)",
	    "description": "This function gets the status of breathing animation on a chain.\nChain name can be \"Body\", \"Arms\", \"LArm\", \"RArm\", \"Legs\" or \"Head\".\n",
	    "parameters": [
	        {
	            "name": "pChain",
	            "description": "Chain name."
	        }
	    ],
	    "returnDescription": "True if breathing animation is enabled on the chain."
	}
	'''
	"""
	return send_mfc("ALMotion", "getBreathEnabled", [pChain])

def setIdlePostureEnabled(pChain:str, pIsEnabled:bool) -> None:
	"""
	Starts or stops idle posture management on a chain.
	Chain name can be "Body", "Arms", "LArm", "RArm", "Legs" or "Head".
	
	Parameters
	----------
	pChain:str
		Chain name.
	pIsEnabled:bool
		Enables / disables the chain.
	
	*Reference struct*
	'''
	{
	    "uid": 291,
	    "returnSignature": "v",
	    "name": "setIdlePostureEnabled",
	    "parametersSignature": "(sb)",
	    "description": "Starts or stops idle posture management on a chain.\nChain name can be \"Body\", \"Arms\", \"LArm\", \"RArm\", \"Legs\" or \"Head\".",
	    "parameters": [
	        {
	            "name": "pChain",
	            "description": "Chain name."
	        },
	        {
	            "name": "pIsEnabled",
	            "description": "Enables / disables the chain."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setIdlePostureEnabled", [pChain, pIsEnabled])

def getIdlePostureEnabled(pChain:str) -> bool:
	"""
	This function gets the status of idle posture management on a chain.
	Chain name can be "Body", "Arms", "LArm", "RArm", "Legs" or "Head".
	
	
	Parameters
	----------
	pChain:str
		Chain name.
	
	Returns
	----------
	True if breathing animation is enabled on the chain.
	
	*Reference struct*
	'''
	{
	    "uid": 292,
	    "returnSignature": "b",
	    "name": "getIdlePostureEnabled",
	    "parametersSignature": "(s)",
	    "description": "This function gets the status of idle posture management on a chain.\nChain name can be \"Body\", \"Arms\", \"LArm\", \"RArm\", \"Legs\" or \"Head\".\n",
	    "parameters": [
	        {
	            "name": "pChain",
	            "description": "Chain name."
	        }
	    ],
	    "returnDescription": "True if breathing animation is enabled on the chain."
	}
	'''
	"""
	return send_mfc("ALMotion", "getIdlePostureEnabled", [pChain])

def _setIdleAnimation(AnimFile:object) -> None:
	"""
	This function sets the breathing animation.
	
	Parameters
	----------
	AnimFile:object
		Animation file (.anim).
	
	*Reference struct*
	'''
	{
	    "uid": 293,
	    "returnSignature": "v",
	    "name": "_setIdleAnimation",
	    "parametersSignature": "(o)",
	    "description": "This function sets the breathing animation.",
	    "parameters": [
	        {
	            "name": "AnimFile",
	            "description": "Animation file (.anim)."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setIdleAnimation", [AnimFile])

def _resetIdleDefaultAnimation() -> None:
	"""
	This function reset the default breathing animation.
	
	*Reference struct*
	'''
	{
	    "uid": 294,
	    "returnSignature": "v",
	    "name": "_resetIdleDefaultAnimation",
	    "parametersSignature": "()",
	    "description": "This function reset the default breathing animation.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_resetIdleDefaultAnimation", [])

def getTaskList() -> object:
	"""
	Gets an ALValue structure describing the tasks in the Task List
	
	Returns
	----------
	An ALValue containing an ALValue for each task. The inner ALValue contains: Name, MotionID
	
	*Reference struct*
	'''
	{
	    "uid": 295,
	    "returnSignature": "m",
	    "name": "getTaskList",
	    "parametersSignature": "()",
	    "description": "Gets an ALValue structure describing the tasks in the Task List",
	    "parameters": [],
	    "returnDescription": "An ALValue containing an ALValue for each task. The inner ALValue contains: Name, MotionID"
	}
	'''
	"""
	return send_mfc("ALMotion", "getTaskList", [])

def areResourcesAvailable(resourceNames:List[str]) -> bool:
	"""
	Returns true if all the desired resources are available. Only motion API's' blocking call takes resources.
	
	Parameters
	----------
	resourceNames:List[str]
		A vector of resource names such as joints. Use getBodyNames("Body") to have the list of the available joint for your robot.
	
	Returns
	----------
	True if the resources are available
	
	*Reference struct*
	'''
	{
	    "uid": 296,
	    "returnSignature": "b",
	    "name": "areResourcesAvailable",
	    "parametersSignature": "([s])",
	    "description": "Returns true if all the desired resources are available. Only motion API's' blocking call takes resources.",
	    "parameters": [
	        {
	            "name": "resourceNames",
	            "description": "A vector of resource names such as joints. Use getBodyNames(\"Body\") to have the list of the available joint for your robot."
	        }
	    ],
	    "returnDescription": "True if the resources are available"
	}
	'''
	"""
	return send_mfc("ALMotion", "areResourcesAvailable", [resourceNames])

def killTask(motionTaskID:int) -> bool:
	"""
	Kills a motion task.
	
	Parameters
	----------
	motionTaskID:int
		TaskID of the motion task you want to kill.
	
	Returns
	----------
	Return true if the specified motionTaskId has been killed.
	
	*Reference struct*
	'''
	{
	    "uid": 297,
	    "returnSignature": "b",
	    "name": "killTask",
	    "parametersSignature": "(i)",
	    "description": "Kills a motion task.",
	    "parameters": [
	        {
	            "name": "motionTaskID",
	            "description": "TaskID of the motion task you want to kill."
	        }
	    ],
	    "returnDescription": "Return true if the specified motionTaskId has been killed."
	}
	'''
	"""
	return send_mfc("ALMotion", "killTask", [motionTaskID])

def killTasksUsingResources(resourceNames:List[str]) -> None:
	"""
	Kills all tasks that use any of the resources given. Only motion API's' blocking call takes resources and can be killed. Use getBodyNames("Body") to have the list of the available joint for your robot.
	
	Parameters
	----------
	resourceNames:List[str]
		A vector of resource joint names
	
	*Reference struct*
	'''
	{
	    "uid": 298,
	    "returnSignature": "v",
	    "name": "killTasksUsingResources",
	    "parametersSignature": "([s])",
	    "description": "Kills all tasks that use any of the resources given. Only motion API's' blocking call takes resources and can be killed. Use getBodyNames(\"Body\") to have the list of the available joint for your robot.",
	    "parameters": [
	        {
	            "name": "resourceNames",
	            "description": "A vector of resource joint names"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "killTasksUsingResources", [resourceNames])

def killMove() -> None:
	"""
	Emergency Stop on Move task: This method will end the move task brutally, without attempting to return to a balanced state. The robot could easily fall.
	
	*Reference struct*
	'''
	{
	    "uid": 300,
	    "returnSignature": "v",
	    "name": "killMove",
	    "parametersSignature": "()",
	    "description": "Emergency Stop on Move task: This method will end the move task brutally, without attempting to return to a balanced state. The robot could easily fall.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "killMove", [])

def killAll() -> None:
	"""
	Kills all tasks.
	
	*Reference struct*
	'''
	{
	    "uid": 301,
	    "returnSignature": "v",
	    "name": "killAll",
	    "parametersSignature": "()",
	    "description": "Kills all tasks.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "killAll", [])

def setEnableNotifications(enable:bool) -> None:
	"""
	Enable / Disable notifications.
	
	Parameters
	----------
	enable:bool
		If True enable notifications. If False disable notifications.
	
	*Reference struct*
	'''
	{
	    "uid": 302,
	    "returnSignature": "v",
	    "name": "setEnableNotifications",
	    "parametersSignature": "(b)",
	    "description": "Enable / Disable notifications.",
	    "parameters": [
	        {
	            "name": "enable",
	            "description": "If True enable notifications. If False disable notifications."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "setEnableNotifications", [enable])

def areNotificationsEnabled() -> bool:
	"""
	Return true if notifications are active.
	
	Returns
	----------
	Return True if notifications are active.
	
	*Reference struct*
	'''
	{
	    "uid": 303,
	    "returnSignature": "b",
	    "name": "areNotificationsEnabled",
	    "parametersSignature": "()",
	    "description": "Return true if notifications are active.",
	    "parameters": [],
	    "returnDescription": "Return True if notifications are active."
	}
	'''
	"""
	return send_mfc("ALMotion", "areNotificationsEnabled", [])

def _getGroundCollision() -> object:
	"""
	Gets the list of collision with the ground.
	
	Returns
	----------
	Vector of collision names and position in torso frame
	
	*Reference struct*
	'''
	{
	    "uid": 304,
	    "returnSignature": "m",
	    "name": "_getGroundCollision",
	    "parametersSignature": "()",
	    "description": "Gets the list of collision with the ground.",
	    "parameters": [],
	    "returnDescription": "Vector of collision names and position in torso frame"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getGroundCollision", [])

def _getGroundCollisionForForceContact() -> object:
	"""
	Gets the list of collision with the ground.
	
	Returns
	----------
	Vector of collision names and position in torso frame
	
	*Reference struct*
	'''
	{
	    "uid": 305,
	    "returnSignature": "m",
	    "name": "_getGroundCollisionForForceContact",
	    "parametersSignature": "()",
	    "description": "Gets the list of collision with the ground.",
	    "parameters": [],
	    "returnDescription": "Vector of collision names and position in torso frame"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getGroundCollisionForForceContact", [])

def _getGroundCollisionForFallManager() -> object:
	"""
	Gets the list of collision with the ground.
	
	Returns
	----------
	Vector of collision names and position in torso frame
	
	*Reference struct*
	'''
	{
	    "uid": 306,
	    "returnSignature": "m",
	    "name": "_getGroundCollisionForFallManager",
	    "parametersSignature": "()",
	    "description": "Gets the list of collision with the ground.",
	    "parameters": [],
	    "returnDescription": "Vector of collision names and position in torso frame"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getGroundCollisionForFallManager", [])

def _getGroundPlaneTf() -> List[float]:
	"""
	Gets the ground plane transform in torso frame.
	
	Returns
	----------
	the ground plane transform in torso frame
	
	*Reference struct*
	'''
	{
	    "uid": 307,
	    "returnSignature": "[f]",
	    "name": "_getGroundPlaneTf",
	    "parametersSignature": "()",
	    "description": "Gets the ground plane transform in torso frame.",
	    "parameters": [],
	    "returnDescription": "the ground plane transform in torso frame"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getGroundPlaneTf", [])

def _getNormalForceContact() -> List[float]:
	"""
	Gets the Normal Force Contact.
	
	Returns
	----------
	Vector of normal Force contact
	
	*Reference struct*
	'''
	{
	    "uid": 308,
	    "returnSignature": "[f]",
	    "name": "_getNormalForceContact",
	    "parametersSignature": "()",
	    "description": "Gets the Normal Force Contact.",
	    "parameters": [],
	    "returnDescription": "Vector of normal Force contact"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getNormalForceContact", [])

def _getRealTorsoInWorld() -> List[float]:
	"""
	It's a getPosition on Torso with inertial Information.This function is used in chorgraphe in 3D View
	
	Returns
	----------
	a transform of the Torso position
	
	*Reference struct*
	'''
	{
	    "uid": 309,
	    "returnSignature": "[f]",
	    "name": "_getRealTorsoInWorld",
	    "parametersSignature": "()",
	    "description": "It's a getPosition on Torso with inertial Information.This function is used in chorgraphe in 3D View",
	    "parameters": [],
	    "returnDescription": "a transform of the Torso position"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getRealTorsoInWorld", [])

def _getRobotGroundConvexHullDebug() -> object:
	"""
	
	
	Returns
	----------
	Array of ALValue arrays containing the sphere position2D and radius.
	
	*Reference struct*
	'''
	{
	    "uid": 310,
	    "returnSignature": "m",
	    "name": "_getRobotGroundConvexHullDebug",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": "Array of ALValue arrays containing the sphere position2D and radius."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getRobotGroundConvexHullDebug", [])

def _getRobotGroundConvexHull() -> object:
	"""
	Get the robot convex hull projected on the ground in the ROBOT_FRAME.
	
	Returns
	----------
	Array of ALValue arrays containing the position2D of each convex hull points.
	
	*Reference struct*
	'''
	{
	    "uid": 311,
	    "returnSignature": "m",
	    "name": "_getRobotGroundConvexHull",
	    "parametersSignature": "()",
	    "description": "Get the robot convex hull projected on the ground in the ROBOT_FRAME.",
	    "parameters": [],
	    "returnDescription": "Array of ALValue arrays containing the position2D of each convex hull points."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getRobotGroundConvexHull", [])

def _getJointIsMoving(useSensors:bool) -> List[int]:
	"""
	Gets if the joints is moving
	
	Parameters
	----------
	useSensors:bool
		If true, sensor information will be returned
	
	Returns
	----------
	a vector of boolean.
	
	*Reference struct*
	'''
	{
	    "uid": 312,
	    "returnSignature": "[i]",
	    "name": "_getJointIsMoving",
	    "parametersSignature": "(b)",
	    "description": "Gets if the joints is moving",
	    "parameters": [
	        {
	            "name": "useSensors",
	            "description": "If true, sensor information will be returned"
	        }
	    ],
	    "returnDescription": "a vector of boolean."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getJointIsMoving", [useSensors])

def _getChainIsMoving(useSensors:bool) -> List[int]:
	"""
	Gets if the chain is moving
	
	Parameters
	----------
	useSensors:bool
		If true, sensor information will be returned
	
	Returns
	----------
	a vector of boolean.
	
	*Reference struct*
	'''
	{
	    "uid": 313,
	    "returnSignature": "[i]",
	    "name": "_getChainIsMoving",
	    "parametersSignature": "(b)",
	    "description": "Gets if the chain is moving",
	    "parameters": [
	        {
	            "name": "useSensors",
	            "description": "If true, sensor information will be returned"
	        }
	    ],
	    "returnDescription": "a vector of boolean."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getChainIsMoving", [useSensors])

def _setAnimationModeEnabled(pEnable:bool) -> None:
	"""
	In fact, it's an hide way to allow the fall manager to disable the fall manager. Note, it's inverse (true set fall to false)
	
	Parameters
	----------
	pEnable:bool
		Activate or disactivate the animation Mode.
	
	*Reference struct*
	'''
	{
	    "uid": 314,
	    "returnSignature": "v",
	    "name": "_setAnimationModeEnabled",
	    "parametersSignature": "(b)",
	    "description": "In fact, it's an hide way to allow the fall manager to disable the fall manager. Note, it's inverse (true set fall to false)",
	    "parameters": [
	        {
	            "name": "pEnable",
	            "description": "Activate or disactivate the animation Mode."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setAnimationModeEnabled", [pEnable])

def _getMotionConfig(pName:str) -> str:
	"""
	Get the motion configuration.
	
	Parameters
	----------
	pName:str
		"All", "State", "Mode", "Protection", "Collision", "Basic", "Move", "Tracker", "Walk", "OmniWheel", "Log", "RobotState", "Duration", "Control", "SmartStiffness","WB", "FallManager".
	
	Returns
	----------
	string contraining all the information.
	
	*Reference struct*
	'''
	{
	    "uid": 315,
	    "returnSignature": "s",
	    "name": "_getMotionConfig",
	    "parametersSignature": "(s)",
	    "description": "Get the motion configuration.",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "\"All\", \"State\", \"Mode\", \"Protection\", \"Collision\", \"Basic\", \"Move\", \"Tracker\", \"Walk\", \"OmniWheel\", \"Log\", \"RobotState\", \"Duration\", \"Control\", \"SmartStiffness\",\"WB\", \"FallManager\"."
	        }
	    ],
	    "returnDescription": "string contraining all the information."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getMotionConfig", [pName])

def _getSupportPolygonCenter() -> List[float]:
	"""
	Gets the center of the support polygon in frame robot.
	
	Returns
	----------
	A vector containing the x,y coordinates of the center of the support polygon
	
	*Reference struct*
	'''
	{
	    "uid": 316,
	    "returnSignature": "[f]",
	    "name": "_getSupportPolygonCenter",
	    "parametersSignature": "()",
	    "description": "Gets the center of the support polygon in frame robot.",
	    "parameters": [],
	    "returnDescription": "A vector containing the x,y coordinates of the center of the support polygon"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getSupportPolygonCenter", [])

def _getComWorld() -> List[float]:
	"""
	Gets the support polygon
	
	Returns
	----------
	A Position3D (x,y,z) coordinates of com in World Space
	
	*Reference struct*
	'''
	{
	    "uid": 317,
	    "returnSignature": "[f]",
	    "name": "_getComWorld",
	    "parametersSignature": "()",
	    "description": "Gets the support polygon",
	    "parameters": [],
	    "returnDescription": "A Position3D (x,y,z) coordinates of com in World Space"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getComWorld", [])

def _getWorldRotation() -> List[float]:
	"""
	Gets the support polygon
	
	Returns
	----------
	A Rotation3D (wx,wy,0) coresponding to world rotation
	
	*Reference struct*
	'''
	{
	    "uid": 318,
	    "returnSignature": "[f]",
	    "name": "_getWorldRotation",
	    "parametersSignature": "()",
	    "description": "Gets the support polygon",
	    "parameters": [],
	    "returnDescription": "A Rotation3D (wx,wy,0) coresponding to world rotation"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getWorldRotation", [])

def _fall(pFallAngle:float) -> None:
	"""
	Activate the fall task
	
	Parameters
	----------
	pFallAngle:float
		The fall angle in degree.
	
	*Reference struct*
	'''
	{
	    "uid": 319,
	    "returnSignature": "v",
	    "name": "_fall",
	    "parametersSignature": "(f)",
	    "description": "Activate the fall task",
	    "parameters": [
	        {
	            "name": "pFallAngle",
	            "description": "The fall angle in degree."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_fall", [pFallAngle])

def _relaxMotorsWhenSitting() -> None:
	"""
	A patch to avoid to consume too much current after a SitDown.
	
	*Reference struct*
	'''
	{
	    "uid": 320,
	    "returnSignature": "v",
	    "name": "_relaxMotorsWhenSitting",
	    "parametersSignature": "()",
	    "description": "A patch to avoid to consume too much current after a SitDown.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_relaxMotorsWhenSitting", [])

def _relax(chainName:object, delayInSeconds:float) -> None:
	"""
	Relax a chain.
	
	Parameters
	----------
	chainName:object
		The name of the chain to relax.
	delayInSeconds:float
		The duration the low stiffness time.
	
	*Reference struct*
	'''
	{
	    "uid": 321,
	    "returnSignature": "v",
	    "name": "_relax",
	    "parametersSignature": "(mf)",
	    "description": "Relax a chain.",
	    "parameters": [
	        {
	            "name": "chainName",
	            "description": "The name of the chain to relax."
	        },
	        {
	            "name": "delayInSeconds",
	            "description": "The duration the low stiffness time."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_relax", [chainName, delayInSeconds])

def _resetCartesianUnfeasible() -> None:
	"""
	Reset to false the bool Cartesian Unfeasible: used for testing motion.
	
	*Reference struct*
	'''
	{
	    "uid": 322,
	    "returnSignature": "v",
	    "name": "_resetCartesianUnfeasible",
	    "parametersSignature": "()",
	    "description": "Reset to false the bool Cartesian Unfeasible: used for testing motion.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_resetCartesianUnfeasible", [])

def _setCartesianUnfeasible() -> None:
	"""
	et to true the bool Cartesian Unfeasible: used for testing motion.
	
	*Reference struct*
	'''
	{
	    "uid": 323,
	    "returnSignature": "v",
	    "name": "_setCartesianUnfeasible",
	    "parametersSignature": "()",
	    "description": "et to true the bool Cartesian Unfeasible: used for testing motion.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_setCartesianUnfeasible", [])

def _getCartesianUnfeasible() -> int:
	"""
	Get the Cartesian Unfeasible state since last reset: used for testing motion.
	
	Returns
	----------
	True if there are one cartesian unfeasible during one motion cycle since last reset.
	
	*Reference struct*
	'''
	{
	    "uid": 324,
	    "returnSignature": "i",
	    "name": "_getCartesianUnfeasible",
	    "parametersSignature": "()",
	    "description": "Get the Cartesian Unfeasible state since last reset: used for testing motion.",
	    "parameters": [],
	    "returnDescription": "True if there are one cartesian unfeasible during one motion cycle since last reset."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getCartesianUnfeasible", [])

def _saveWholeBodyDump() -> None:
	"""
	Save current whole body dump
	
	*Reference struct*
	'''
	{
	    "uid": 325,
	    "returnSignature": "v",
	    "name": "_saveWholeBodyDump",
	    "parametersSignature": "()",
	    "description": "Save current whole body dump",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_saveWholeBodyDump", [])

def _resetNumJointCommandDiscontinuities() -> None:
	"""
	Reset the number of joint command discontinuous updates.
	
	*Reference struct*
	'''
	{
	    "uid": 326,
	    "returnSignature": "v",
	    "name": "_resetNumJointCommandDiscontinuities",
	    "parametersSignature": "()",
	    "description": "Reset the number of joint command discontinuous updates.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_resetNumJointCommandDiscontinuities", [])

def _getNumJointCommandDiscontinuities() -> int:
	"""
	Get the number of joint command discontinuous updates since last reset.
	
	Returns
	----------
	The number of discontinuities since last reset.
	
	*Reference struct*
	'''
	{
	    "uid": 327,
	    "returnSignature": "I",
	    "name": "_getNumJointCommandDiscontinuities",
	    "parametersSignature": "()",
	    "description": "Get the number of joint command discontinuous updates since last reset.",
	    "parameters": [],
	    "returnDescription": "The number of discontinuities since last reset."
	}
	'''
	"""
	return send_mfc("ALMotion", "_getNumJointCommandDiscontinuities", [])

def _resetMotionCommandModelToSensors(pName:object) -> None:
	"""
	Usefull function to resynchronize ALMotion and DCM 
	In fact we set motion command model with sensors information
	
	Parameters
	----------
	pName:object
		Names the joints, chains, "Body", "JointActuators", "Joints" or "Actuators". 
	
	*Reference struct*
	'''
	{
	    "uid": 328,
	    "returnSignature": "v",
	    "name": "_resetMotionCommandModelToSensors",
	    "parametersSignature": "(m)",
	    "description": "Usefull function to resynchronize ALMotion and DCM \nIn fact we set motion command model with sensors information",
	    "parameters": [
	        {
	            "name": "pName",
	            "description": "Names the joints, chains, \"Body\", \"JointActuators\", \"Joints\" or \"Actuators\". "
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_resetMotionCommandModelToSensors", [pName])

def _getMotionToDCM() -> MotionToDCM:
	"""
	Get motion to dcm commands
	
	*Reference struct*
	'''
	{
	    "uid": 329,
	    "returnSignature": "(iXXXXXXXXb)<MotionToDCM,whenToSendToDcm,anglesJoint,anglesActuator,stiffnessesJoint,stiffnessesActuator,stiffnessesWheel,velocitiesJoint,velocitiesWheel,torquesJoint,enableFuseProtection>",
	    "name": "_getMotionToDCM",
	    "parametersSignature": "()",
	    "description": "Get motion to dcm commands",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_getMotionToDCM", [])

def _getBlindZones() -> object:
	"""
	Get the blind zones convex polygon.
	
	Returns
	----------
	the blind zones [[[x, y], ..., [x, y]]...]
	
	*Reference struct*
	'''
	{
	    "uid": 330,
	    "returnSignature": "m",
	    "name": "_getBlindZones",
	    "parametersSignature": "()",
	    "description": "Get the blind zones convex polygon.",
	    "parameters": [],
	    "returnDescription": "the blind zones [[[x, y], ..., [x, y]]...]"
	}
	'''
	"""
	return send_mfc("ALMotion", "_getBlindZones", [])

def _freeze(pChainName:str, pDuration:float) -> None:
	"""
	Freeze chain movement.
	
	Parameters
	----------
	pChainName:str
		Name of the chain to freeze.
	pDuration:float
		Freeze duration in seconds.
	
	Returns
	----------
	A cancellable future to unfreeze the chain.
	
	*Reference struct*
	'''
	{
	    "uid": 331,
	    "returnSignature": "v",
	    "name": "_freeze",
	    "parametersSignature": "(sf)",
	    "description": "Freeze chain movement.",
	    "parameters": [
	        {
	            "name": "pChainName",
	            "description": "Name of the chain to freeze."
	        },
	        {
	            "name": "pDuration",
	            "description": "Freeze duration in seconds."
	        }
	    ],
	    "returnDescription": "A cancellable future to unfreeze the chain."
	}
	'''
	"""
	return send_mfc("ALMotion", "_freeze", [pChainName, pDuration])

def _dumpBlackBoxUntil(pPath:str, pTime:int) -> None:
	"""
	
	
	Parameters
	----------
	pPath:str
		The path where the blackbox shall be written.
	pTime:int
		The dump will include data until `pTime`.
	
	*Reference struct*
	'''
	{
	    "uid": 332,
	    "returnSignature": "v",
	    "name": "_dumpBlackBoxUntil",
	    "parametersSignature": "(sL)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "pPath",
	            "description": "The path where the blackbox shall be written."
	        },
	        {
	            "name": "pTime",
	            "description": "The dump will include data until `pTime`."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_dumpBlackBoxUntil", [pPath, pTime])

def _dumpBlackBox(pPath:str, pDeltaTime:int) -> None:
	"""
	
	
	Parameters
	----------
	pPath:str
		The path where the blackbox shall be written.
	pDeltaTime:int
		The dump will include data until `qi::Clock::now() + pDeltaTime`. Default to zero.
	
	*Reference struct*
	'''
	{
	    "uid": 333,
	    "returnSignature": "v",
	    "name": "_dumpBlackBox",
	    "parametersSignature": "(sL)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "pPath",
	            "description": "The path where the blackbox shall be written."
	        },
	        {
	            "name": "pDeltaTime",
	            "description": "The dump will include data until `qi::Clock::now() + pDeltaTime`. Default to zero."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMotion", "_dumpBlackBox", [pPath, pDeltaTime])

