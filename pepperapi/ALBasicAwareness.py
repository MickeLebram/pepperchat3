"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

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
	return call_method("ALBasicAwareness", "version", [])

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
	return call_method("ALBasicAwareness", "ping", [])

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
	return call_method("ALBasicAwareness", "getMethodList", [])

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
	return call_method("ALBasicAwareness", "getMethodHelp", [methodName])

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
	return call_method("ALBasicAwareness", "getModuleHelp", [])

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
	return call_method("ALBasicAwareness", "getBrokerName", [])

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
	return call_method("ALBasicAwareness", "getUsage", [name])

def _onPeopleDetected(name:str, populationUpdated:object, message:str) -> None:
	"""
	Population Updated (event: PeoplePerception/PopulationUpdated)
	
	Parameters
	----------
	name:str
		Name of the event
	populationUpdated:object
		Boolean value for people detection event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "_onPeopleDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Population Updated (event: PeoplePerception/PopulationUpdated)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "populationUpdated",
	#             "description": "Boolean value for people detection event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onPeopleDetected", [name, populationUpdated, message])

def _onMovementDetected(name:str, movementDetected:object, message:str) -> None:
	"""
	Movement Detected (event: MovementDetection3D/MovementDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	movementDetected:object
		Boolean value for movement event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "_onMovementDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Movement Detected (event: MovementDetection3D/MovementDetected)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "movementDetected",
	#             "description": "Boolean value for movement event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onMovementDetected", [name, movementDetected, message])

def _onNavigationMotionDetected(name:str, movementDetected:object, message:str) -> None:
	"""
	Navigation Motion Detected (event: Navigation/MotionDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	movementDetected:object
		Boolean value for movement event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "_onNavigationMotionDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Navigation Motion Detected (event: Navigation/MotionDetected)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "movementDetected",
	#             "description": "Boolean value for movement event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onNavigationMotionDetected", [name, movementDetected, message])

def _onCloseMovementDetected(name:str, closeMovementDetected:object, message:str) -> None:
	"""
	Close Movement Detected (event: WavingDetection/Waving)
	
	Parameters
	----------
	name:str
		Name of the event
	closeMovementDetected:object
		Boolean value for close movement event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "_onCloseMovementDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Close Movement Detected (event: WavingDetection/Waving)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "closeMovementDetected",
	#             "description": "Boolean value for close movement event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onCloseMovementDetected", [name, closeMovementDetected, message])

def _onSoundDetected(name:str, SoundLocated:object, message:str) -> None:
	"""
	Sound Detected (event: SoundLocated)
	
	Parameters
	----------
	name:str
		Name of the event
	SoundLocated:object
		Boolean value for movement event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_onSoundDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Sound Detected (event: SoundLocated)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "SoundLocated",
	#             "description": "Boolean value for movement event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onSoundDetected", [name, SoundLocated, message])

def _onTouchDetected(name:str, touchDetected:object, message:str) -> None:
	"""
	Touch Detected (event: TouchDetection3D/TouchDetected)
	
	Parameters
	----------
	name:str
		Name of the event
	touchDetected:object
		Boolean value for touch event
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "_onTouchDetected",
	#     "parametersSignature": "(sms)",
	#     "description": "Touch Detected (event: TouchDetection3D/TouchDetected)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "touchDetected",
	#             "description": "Boolean value for touch event"
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onTouchDetected", [name, touchDetected, message])

def _onFastPersonTracking(name:str, tackerValue:object, message:str) -> None:
	"""
	Servoing event callback (event:ALTracker/FastPersonTracking)
	
	Parameters
	----------
	name:str
		Name of the event
	tackerValue:object
		Position to track.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "_onFastPersonTracking",
	#     "parametersSignature": "(sms)",
	#     "description": "Servoing event callback (event:ALTracker/FastPersonTracking)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "tackerValue",
	#             "description": "Position to track."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onFastPersonTracking", [name, tackerValue, message])

def _onNoFastPersonFound(name:str, val:object, message:str) -> None:
	"""
	No person found by fast tracking callback (event:ALFastPersonTracking/TrackedPersonNotFound)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "_onNoFastPersonFound",
	#     "parametersSignature": "(sms)",
	#     "description": "No person found by fast tracking callback (event:ALFastPersonTracking/TrackedPersonNotFound)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "val",
	#             "description": "Content of the event."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onNoFastPersonFound", [name, val, message])

def _onHeadTracking(name:str, tackerValue:object, message:str) -> None:
	"""
	Servoing event callback (event:ALTracker/FindPersonHead)
	
	Parameters
	----------
	name:str
		Name of the event
	tackerValue:object
		Position to track.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "_onHeadTracking",
	#     "parametersSignature": "(sms)",
	#     "description": "Servoing event callback (event:ALTracker/FindPersonHead)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "tackerValue",
	#             "description": "Position to track."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onHeadTracking", [name, tackerValue, message])

def _onHeadNotFound(name:str, val:object, message:str) -> None:
	"""
	HeadNotFound event callback (event:ALFindPersonHead/HeadNotFound)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_onHeadNotFound",
	#     "parametersSignature": "(sms)",
	#     "description": "HeadNotFound event callback (event:ALFindPersonHead/HeadNotFound)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "val",
	#             "description": "Content of the event."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onHeadNotFound", [name, val, message])

def _onHeadReached(name:str, val:object, message:str) -> None:
	"""
	HeadReached event callback (event:ALFindPersonHead/HeadReached)
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_onHeadReached",
	#     "parametersSignature": "(sms)",
	#     "description": "HeadReached event callback (event:ALFindPersonHead/HeadReached)",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "val",
	#             "description": "Content of the event."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onHeadReached", [name, val, message])

def _onHeadTrackingStopped(name:str, val:object, message:str) -> None:
	"""
	tracking interruption
	
	Parameters
	----------
	name:str
		Name of the event
	val:object
		Content of the event.
	message:str
		Event message
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_onHeadTrackingStopped",
	#     "parametersSignature": "(sms)",
	#     "description": "tracking interruption",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the event"
	#         },
	#         {
	#             "name": "val",
	#             "description": "Content of the event."
	#         },
	#         {
	#             "name": "message",
	#             "description": "Event message"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_onHeadTrackingStopped", [name, val, message])

def setEnabled(enabled:bool) -> None:
	"""
	Enable/Disable BasicAwareness.
	
	Parameters
	----------
	enabled:bool
		True to enable BasicAwareness, False to disable BasicAwareness.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "setEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Enable/Disable BasicAwareness.",
	#     "parameters": [
	#         {
	#             "name": "enabled",
	#             "description": "True to enable BasicAwareness, False to disable BasicAwareness."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "setEnabled", [enabled])

def isEnabled() -> bool:
	"""
	Return whether BasicAwareness is enabled or not.
	
	Returns
	----------
	Boolean value, true if enabled else false
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "isEnabled",
	#     "parametersSignature": "()",
	#     "description": "Return whether BasicAwareness is enabled or not.",
	#     "parameters": [],
	#     "returnDescription": "Boolean value, true if enabled else false"
	# }
	return call_method("ALBasicAwareness", "isEnabled", [])

def isRunning() -> bool:
	"""
	Return whether BasicAwareness is running.
	
	Returns
	----------
	Boolean value, true if running else false
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "isRunning",
	#     "parametersSignature": "()",
	#     "description": "Return whether BasicAwareness is running.",
	#     "parameters": [],
	#     "returnDescription": "Boolean value, true if running else false"
	# }
	return call_method("ALBasicAwareness", "isRunning", [])

def pauseAwareness() -> None:
	"""
	Pause BasicAwareness.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "pauseAwareness",
	#     "parametersSignature": "()",
	#     "description": "Pause BasicAwareness.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "pauseAwareness", [])

def resumeAwareness() -> None:
	"""
	Resume BasicAwareness.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "resumeAwareness",
	#     "parametersSignature": "()",
	#     "description": "Resume BasicAwareness.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "resumeAwareness", [])

def isAwarenessPaused() -> bool:
	"""
	Get the pause status of the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "b",
	#     "name": "isAwarenessPaused",
	#     "parametersSignature": "()",
	#     "description": "Get the pause status of the module.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "isAwarenessPaused", [])

def setStimulusDetectionEnabled(stimulusName:str, isStimulusDetectionEnabled:bool) -> None:
	"""
	Enable/Disable Stimulus Detection.
	
	Parameters
	----------
	stimulusName:str
		Name of the stimulus to enable/disable
	isStimulusDetectionEnabled:bool
		Boolean value: true to enable, false to disable.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "setStimulusDetectionEnabled",
	#     "parametersSignature": "(sb)",
	#     "description": "Enable/Disable Stimulus Detection.",
	#     "parameters": [
	#         {
	#             "name": "stimulusName",
	#             "description": "Name of the stimulus to enable/disable"
	#         },
	#         {
	#             "name": "isStimulusDetectionEnabled",
	#             "description": "Boolean value: true to enable, false to disable."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "setStimulusDetectionEnabled", [stimulusName, isStimulusDetectionEnabled])

def isStimulusDetectionEnabled(stimulusName:str) -> bool:
	"""
	Get status enabled/disabled for Stimulus Detection.
	
	Parameters
	----------
	stimulusName:str
		Name of the stimulus to check
	
	Returns
	----------
	Boolean value for status enabled/disabled
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "isStimulusDetectionEnabled",
	#     "parametersSignature": "(s)",
	#     "description": "Get status enabled/disabled for Stimulus Detection.",
	#     "parameters": [
	#         {
	#             "name": "stimulusName",
	#             "description": "Name of the stimulus to check"
	#         }
	#     ],
	#     "returnDescription": "Boolean value for status enabled/disabled"
	# }
	return call_method("ALBasicAwareness", "isStimulusDetectionEnabled", [stimulusName])

def setParameter(paramName:str, newVal:object) -> None:
	"""
	Set the specified parameter 
	
	Parameters
	----------
	paramName:str
		"LookStimulusSpeed" : Speed of head moves when looking at a stimulus, as fraction of max speed
		 "LookBackSpeed" : Speed of head moves when looking back to previous position, as fraction of max speed
		 "NobodyFoundTimeOut" : timeout to send HumanLost event when no blob is found, in seconds
		 "MinTimeTracking" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds
		 "TimeSleepBeforeResumeMS" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds
		 "TimeOutResetHead" : Timeout to reset the head, in seconds
		 "AmplitudeYawTracking" : max absolute value for head yaw in tracking, in degrees
		 "PeoplePerceptionPeriod" : Period for people perception, in milliseconds
		 "SlowPeoplePerceptionPeriod" : Period for people perception in FullyEngaged mode, in milliseconds
		 "HeadThreshold" : Yaw threshold for tracking, in degrees
		 "BodyRotationThreshold" : Angular threshold for BodyRotation tracking mode, in degrees
		 "BodyRotationThresholdNao" : Angular threshold for BodyRotation tracking mode on Nao, in degrees
		 "MoveDistanceX" : X Distance for the Move tracking mode, in meters
		 "MoveDistanceY" : Y Distance for the Move tracking mode, in meters
		 "MoveAngleTheta" : Angle for the Move tracking mode, in degrees
		 "MoveThresholdX" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdY" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdTheta" : Theta Threshold for the Move tracking mode, in degrees
		 "MaxDistanceFullyEngaged" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters
		 "MaxDistanceNotFullyEngaged" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters
		 "MaxHumanSearchTime" : Maximum time to find a human after observing stimulus, in seconds
		 "DeltaPitchComfortZone" : Pitch width of the comfort zone, in degree
		 "CenterPitchComfortZone" : Pitch center of the confort zone, in degree
		 "SoundHeight" : Default Height for sound detection, in meters
		 "MoveSpeed" : Speed of the robot moves
		 "MC_Interactive_MinTime" : Minimum time between 2 contextual moves (when the robot is tracking somebody)
		 "MC_Interactive_MaxOffsetTime" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)
		 "MC_Interactive_DistanceXY" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody
		 "MC_Interactive_MinTheta" : Minimum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_MaxTheta" : Maximum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_DistanceHumanRobot" : Distance between the human and the robot
		 "MC_Interactive_MaxDistanceHumanRobot" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)
		 
	newVal:object
		"LookStimulusSpeed" : Float in range [0.01;1]
		 "LookBackSpeed" : Float in range [0.01;1]
		 "NobodyFoundTimeOut" : Float > 0
		 "MinTimeTracking" : Float in range [0;20]
		 "TimeSleepBeforeResumeMS" : Int > 0
		 "TimeOutResetHead" : Float in range [0;30]
		 "AmplitudeYawTracking" : Float in range [10;120]
		 "PeoplePerceptionPeriod" : Int > 1
		 "SlowPeoplePerceptionPeriod" : Int > 1
		 "HeadThreshold" : Float in range [0;180]
		 "BodyRotationThreshold" : Float in range [-180;180]
		 "BodyRotationThresholdNao" : Float in range [-180;180]
		 "MoveDistanceX" : Float in range [-5;5]
		 "MoveDistanceY" : Float in range [-5;5]
		 "MoveAngleTheta" : Float in range [-180;180]
		 "MoveThresholdX" : Float in range [0;5]
		 "MoveThresholdY" : Float in range [0;5]
		 "MoveThresholdTheta" : Float in range [-180;180]
		 "MaxDistanceFullyEngaged" : Float in range [0.5;5]
		 "MaxDistanceNotFullyEngaged" : Float in range [0.5;5]
		 "MaxHumanSearchTime" : Float in range [0.1;10]
		 "DeltaPitchComfortZone" : Float in range [0;90]
		 "CenterPitchComfortZone" : Float in range [-90;90]
		 "SoundHeight" : Float in range [0;2]
		 "MoveSpeed" : Float in range [0.1;0.55]
		 "MC_Interactive_MinTime" : Int in range [0;100]
		 "MC_Interactive_MaxOffsetTime" : Int in range [0;100]
		 "MC_Interactive_DistanceXY" : Float in range [0;1]
		 "MC_Interactive_MinTheta" : Float in range [-40;0]
		 "MC_Interactive_MaxTheta" : Float in range [0;40]
		 "MC_Interactive_DistanceHumanRobot" : Float in range [0.1;2]
		 "MC_Interactive_MaxDistanceHumanRobot" : Float in range [0.1;3]
		 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "setParameter",
	#     "parametersSignature": "(sm)",
	#     "description": "Set the specified parameter ",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "\"LookStimulusSpeed\" : Speed of head moves when looking at a stimulus, as fraction of max speed\n \"LookBackSpeed\" : Speed of head moves when looking back to previous position, as fraction of max speed\n \"NobodyFoundTimeOut\" : timeout to send HumanLost event when no blob is found, in seconds\n \"MinTimeTracking\" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds\n \"TimeSleepBeforeResumeMS\" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds\n \"TimeOutResetHead\" : Timeout to reset the head, in seconds\n \"AmplitudeYawTracking\" : max absolute value for head yaw in tracking, in degrees\n \"PeoplePerceptionPeriod\" : Period for people perception, in milliseconds\n \"SlowPeoplePerceptionPeriod\" : Period for people perception in FullyEngaged mode, in milliseconds\n \"HeadThreshold\" : Yaw threshold for tracking, in degrees\n \"BodyRotationThreshold\" : Angular threshold for BodyRotation tracking mode, in degrees\n \"BodyRotationThresholdNao\" : Angular threshold for BodyRotation tracking mode on Nao, in degrees\n \"MoveDistanceX\" : X Distance for the Move tracking mode, in meters\n \"MoveDistanceY\" : Y Distance for the Move tracking mode, in meters\n \"MoveAngleTheta\" : Angle for the Move tracking mode, in degrees\n \"MoveThresholdX\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdY\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdTheta\" : Theta Threshold for the Move tracking mode, in degrees\n \"MaxDistanceFullyEngaged\" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters\n \"MaxDistanceNotFullyEngaged\" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters\n \"MaxHumanSearchTime\" : Maximum time to find a human after observing stimulus, in seconds\n \"DeltaPitchComfortZone\" : Pitch width of the comfort zone, in degree\n \"CenterPitchComfortZone\" : Pitch center of the confort zone, in degree\n \"SoundHeight\" : Default Height for sound detection, in meters\n \"MoveSpeed\" : Speed of the robot moves\n \"MC_Interactive_MinTime\" : Minimum time between 2 contextual moves (when the robot is tracking somebody)\n \"MC_Interactive_MaxOffsetTime\" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)\n \"MC_Interactive_DistanceXY\" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody\n \"MC_Interactive_MinTheta\" : Minimum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_MaxTheta\" : Maximum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_DistanceHumanRobot\" : Distance between the human and the robot\n \"MC_Interactive_MaxDistanceHumanRobot\" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)\n "
	#         },
	#         {
	#             "name": "newVal",
	#             "description": "\"LookStimulusSpeed\" : Float in range [0.01;1]\n \"LookBackSpeed\" : Float in range [0.01;1]\n \"NobodyFoundTimeOut\" : Float > 0\n \"MinTimeTracking\" : Float in range [0;20]\n \"TimeSleepBeforeResumeMS\" : Int > 0\n \"TimeOutResetHead\" : Float in range [0;30]\n \"AmplitudeYawTracking\" : Float in range [10;120]\n \"PeoplePerceptionPeriod\" : Int > 1\n \"SlowPeoplePerceptionPeriod\" : Int > 1\n \"HeadThreshold\" : Float in range [0;180]\n \"BodyRotationThreshold\" : Float in range [-180;180]\n \"BodyRotationThresholdNao\" : Float in range [-180;180]\n \"MoveDistanceX\" : Float in range [-5;5]\n \"MoveDistanceY\" : Float in range [-5;5]\n \"MoveAngleTheta\" : Float in range [-180;180]\n \"MoveThresholdX\" : Float in range [0;5]\n \"MoveThresholdY\" : Float in range [0;5]\n \"MoveThresholdTheta\" : Float in range [-180;180]\n \"MaxDistanceFullyEngaged\" : Float in range [0.5;5]\n \"MaxDistanceNotFullyEngaged\" : Float in range [0.5;5]\n \"MaxHumanSearchTime\" : Float in range [0.1;10]\n \"DeltaPitchComfortZone\" : Float in range [0;90]\n \"CenterPitchComfortZone\" : Float in range [-90;90]\n \"SoundHeight\" : Float in range [0;2]\n \"MoveSpeed\" : Float in range [0.1;0.55]\n \"MC_Interactive_MinTime\" : Int in range [0;100]\n \"MC_Interactive_MaxOffsetTime\" : Int in range [0;100]\n \"MC_Interactive_DistanceXY\" : Float in range [0;1]\n \"MC_Interactive_MinTheta\" : Float in range [-40;0]\n \"MC_Interactive_MaxTheta\" : Float in range [0;40]\n \"MC_Interactive_DistanceHumanRobot\" : Float in range [0.1;2]\n \"MC_Interactive_MaxDistanceHumanRobot\" : Float in range [0.1;3]\n "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "setParameter", [paramName, newVal])

def resetAllParameters() -> None:
	"""
	Reset all parameters, including enabled/disabled stimulus.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "resetAllParameters",
	#     "parametersSignature": "()",
	#     "description": "Reset all parameters, including enabled/disabled stimulus.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "resetAllParameters", [])

def getParameter(paramName:str) -> object:
	"""
	Get the specified parameter.
	
	Parameters
	----------
	paramName:str
		"LookStimulusSpeed" : Speed of head moves when looking at a stimulus, as fraction of max speed
		 "LookBackSpeed" : Speed of head moves when looking back to previous position, as fraction of max speed
		 "NobodyFoundTimeOut" : timeout to send HumanLost event when no blob is found, in seconds
		 "MinTimeTracking" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds
		 "TimeSleepBeforeResumeMS" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds
		 "TimeOutResetHead" : Timeout to reset the head, in seconds
		 "AmplitudeYawTracking" : max absolute value for head yaw in tracking, in degrees
		 "PeoplePerceptionPeriod" : Period for people perception, in milliseconds
		 "SlowPeoplePerceptionPeriod" : Period for people perception in FullyEngaged mode, in milliseconds
		 "HeadThreshold" : Yaw threshold for tracking, in degrees
		 "BodyRotationThreshold" : Angular threshold for BodyRotation tracking mode, in degrees
		 "BodyRotationThresholdNao" : Angular threshold for BodyRotation tracking mode on Nao, in degrees
		 "MoveDistanceX" : X Distance for the Move tracking mode, in meters
		 "MoveDistanceY" : Y Distance for the Move tracking mode, in meters
		 "MoveAngleTheta" : Angle for the Move tracking mode, in degrees
		 "MoveThresholdX" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdY" : Threshold for the Move tracking mode, in meters
		 "MoveThresholdTheta" : Theta Threshold for the Move tracking mode, in degrees
		 "MaxDistanceFullyEngaged" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters
		 "MaxDistanceNotFullyEngaged" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters
		 "MaxHumanSearchTime" : Maximum time to find a human after observing stimulus, in seconds
		 "DeltaPitchComfortZone" : Pitch width of the comfort zone, in degree
		 "CenterPitchComfortZone" : Pitch center of the confort zone, in degree
		 "SoundHeight" : Default Height for sound detection, in meters
		 "MoveSpeed" : Speed of the robot moves
		 "MC_Interactive_MinTime" : Minimum time between 2 contextual moves (when the robot is tracking somebody)
		 "MC_Interactive_MaxOffsetTime" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)
		 "MC_Interactive_DistanceXY" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody
		 "MC_Interactive_MinTheta" : Minimum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_MaxTheta" : Maximum theta that the robot can apply when he tracks somebody
		 "MC_Interactive_DistanceHumanRobot" : Distance between the human and the robot
		 "MC_Interactive_MaxDistanceHumanRobot" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)
		 
	
	Returns
	----------
	ALValue format for required parameter
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "m",
	#     "name": "getParameter",
	#     "parametersSignature": "(s)",
	#     "description": "Get the specified parameter.",
	#     "parameters": [
	#         {
	#             "name": "paramName",
	#             "description": "\"LookStimulusSpeed\" : Speed of head moves when looking at a stimulus, as fraction of max speed\n \"LookBackSpeed\" : Speed of head moves when looking back to previous position, as fraction of max speed\n \"NobodyFoundTimeOut\" : timeout to send HumanLost event when no blob is found, in seconds\n \"MinTimeTracking\" : Minimum Time for the robot to be focused on someone, without listening to other stimuli, in seconds\n \"TimeSleepBeforeResumeMS\" : Slept time before automatically resuming BasicAwareness when an automatic pause has been made, in milliseconds\n \"TimeOutResetHead\" : Timeout to reset the head, in seconds\n \"AmplitudeYawTracking\" : max absolute value for head yaw in tracking, in degrees\n \"PeoplePerceptionPeriod\" : Period for people perception, in milliseconds\n \"SlowPeoplePerceptionPeriod\" : Period for people perception in FullyEngaged mode, in milliseconds\n \"HeadThreshold\" : Yaw threshold for tracking, in degrees\n \"BodyRotationThreshold\" : Angular threshold for BodyRotation tracking mode, in degrees\n \"BodyRotationThresholdNao\" : Angular threshold for BodyRotation tracking mode on Nao, in degrees\n \"MoveDistanceX\" : X Distance for the Move tracking mode, in meters\n \"MoveDistanceY\" : Y Distance for the Move tracking mode, in meters\n \"MoveAngleTheta\" : Angle for the Move tracking mode, in degrees\n \"MoveThresholdX\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdY\" : Threshold for the Move tracking mode, in meters\n \"MoveThresholdTheta\" : Theta Threshold for the Move tracking mode, in degrees\n \"MaxDistanceFullyEngaged\" : Maximum distance for someone to be tracked for FullyEngaged mode, in meters\n \"MaxDistanceNotFullyEngaged\" : Maximum distance for someone to be tracked for modes different from FullyEngaged, in meters\n \"MaxHumanSearchTime\" : Maximum time to find a human after observing stimulus, in seconds\n \"DeltaPitchComfortZone\" : Pitch width of the comfort zone, in degree\n \"CenterPitchComfortZone\" : Pitch center of the confort zone, in degree\n \"SoundHeight\" : Default Height for sound detection, in meters\n \"MoveSpeed\" : Speed of the robot moves\n \"MC_Interactive_MinTime\" : Minimum time between 2 contextual moves (when the robot is tracking somebody)\n \"MC_Interactive_MaxOffsetTime\" : Maximum time that we can add to MC_Interactive_MinTime (when the robot is tracking somebody)\n \"MC_Interactive_DistanceXY\" : Maximum offset distance in X and Y that the robot can apply when he tracks somebody\n \"MC_Interactive_MinTheta\" : Minimum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_MaxTheta\" : Maximum theta that the robot can apply when he tracks somebody\n \"MC_Interactive_DistanceHumanRobot\" : Distance between the human and the robot\n \"MC_Interactive_MaxDistanceHumanRobot\" : Maximum distance human robot to allow the robot to move (in MoveContextually mode)\n "
	#         }
	#     ],
	#     "returnDescription": "ALValue format for required parameter"
	# }
	return call_method("ALBasicAwareness", "getParameter", [paramName])

def setEngagementMode(modeName:str) -> None:
	"""
	Set engagement mode.
	
	Parameters
	----------
	modeName:str
		Name of the mode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "v",
	#     "name": "setEngagementMode",
	#     "parametersSignature": "(s)",
	#     "description": "Set engagement mode.",
	#     "parameters": [
	#         {
	#             "name": "modeName",
	#             "description": "Name of the mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "setEngagementMode", [modeName])

def getEngagementMode() -> str:
	"""
	Set engagement mode.
	
	Returns
	----------
	Name of current engagement mode as a string
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "s",
	#     "name": "getEngagementMode",
	#     "parametersSignature": "()",
	#     "description": "Set engagement mode.",
	#     "parameters": [],
	#     "returnDescription": "Name of current engagement mode as a string"
	# }
	return call_method("ALBasicAwareness", "getEngagementMode", [])

def _setCustomEngagementMode(checkStimWhenFocused:bool, stimuliWhenNotTracking:List[str], stimuliWhenTracking:List[str]) -> None:
	"""
	Set engagement mode.
	
	Parameters
	----------
	checkStimWhenFocused:bool
		when it is tracking someone, true makes the robot check a stimulus to see if it corresponds to a human, false makes it go back to the current track human just after watching in the stim direction (as in SemiEngaged mode)
	stimuliWhenNotTracking:List[str]
		stimuli enabled when the robot is tracking, as a stimuli names list
	stimuliWhenTracking:List[str]
		stimuli enabled when the robot is not tracking, as a stimuli names list
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "v",
	#     "name": "_setCustomEngagementMode",
	#     "parametersSignature": "(b[s][s])",
	#     "description": "Set engagement mode.",
	#     "parameters": [
	#         {
	#             "name": "checkStimWhenFocused",
	#             "description": "when it is tracking someone, true makes the robot check a stimulus to see if it corresponds to a human, false makes it go back to the current track human just after watching in the stim direction (as in SemiEngaged mode)"
	#         },
	#         {
	#             "name": "stimuliWhenNotTracking",
	#             "description": "stimuli enabled when the robot is tracking, as a stimuli names list"
	#         },
	#         {
	#             "name": "stimuliWhenTracking",
	#             "description": "stimuli enabled when the robot is not tracking, as a stimuli names list"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_setCustomEngagementMode", [checkStimWhenFocused, stimuliWhenNotTracking, stimuliWhenTracking])

def setTrackingMode(modeName:str) -> None:
	"""
	Set tracking mode.
	
	Parameters
	----------
	modeName:str
		Name of the mode
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "setTrackingMode",
	#     "parametersSignature": "(s)",
	#     "description": "Set tracking mode.",
	#     "parameters": [
	#         {
	#             "name": "modeName",
	#             "description": "Name of the mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "setTrackingMode", [modeName])

def getTrackingMode() -> str:
	"""
	Set tracking mode.
	
	Returns
	----------
	Name of current tracking mode as a string
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "s",
	#     "name": "getTrackingMode",
	#     "parametersSignature": "()",
	#     "description": "Set tracking mode.",
	#     "parameters": [],
	#     "returnDescription": "Name of current tracking mode as a string"
	# }
	return call_method("ALBasicAwareness", "getTrackingMode", [])

def engagePerson(engagePerson:int) -> bool:
	"""
	Force Engage Person.
	
	Parameters
	----------
	engagePerson:int
		ID of the person as found in PeoplePerception.
	
	Returns
	----------
	true if the robot succeeded to engage the person, else false.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "b",
	#     "name": "engagePerson",
	#     "parametersSignature": "(i)",
	#     "description": "Force Engage Person.",
	#     "parameters": [
	#         {
	#             "name": "engagePerson",
	#             "description": "ID of the person as found in PeoplePerception."
	#         }
	#     ],
	#     "returnDescription": "true if the robot succeeded to engage the person, else false."
	# }
	return call_method("ALBasicAwareness", "engagePerson", [engagePerson])

def _setContextualMoveType(contextualMove:str) -> None:
	"""
	Set a new contextual moves type.
	
	Parameters
	----------
	contextualMove:str
		The contextual move, can be 'forward', 'backward', 'sides' and 'random'.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "_setContextualMoveType",
	#     "parametersSignature": "(s)",
	#     "description": "Set a new contextual moves type.",
	#     "parameters": [
	#         {
	#             "name": "contextualMove",
	#             "description": "The contextual move, can be 'forward', 'backward', 'sides' and 'random'."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_setContextualMoveType", [contextualMove])

def triggerStimulus(stimulusPosition:List[float]) -> int:
	"""
	Trigger a custom stimulus.
	
	Parameters
	----------
	stimulusPosition:List[float]
		Position of the stimulus, in Frame World
	
	Returns
	----------
	If someone was found, return value is its ID, else it's -1
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "i",
	#     "name": "triggerStimulus",
	#     "parametersSignature": "([f])",
	#     "description": "Trigger a custom stimulus.",
	#     "parameters": [
	#         {
	#             "name": "stimulusPosition",
	#             "description": "Position of the stimulus, in Frame World"
	#         }
	#     ],
	#     "returnDescription": "If someone was found, return value is its ID, else it's -1"
	# }
	return call_method("ALBasicAwareness", "triggerStimulus", [stimulusPosition])

def _useLedDebug(useLeds:bool) -> None:
	"""
	Use leds for debug
	
	Parameters
	----------
	useLeds:bool
		Boolean value: true to use leds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "_useLedDebug",
	#     "parametersSignature": "(b)",
	#     "description": "Use leds for debug",
	#     "parameters": [
	#         {
	#             "name": "useLeds",
	#             "description": "Boolean value: true to use leds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_useLedDebug", [useLeds])

def _setLedGroup(ledGroupName:str) -> None:
	"""
	Set Led group
	
	Parameters
	----------
	ledGroupName:str
		Name of the led group.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "v",
	#     "name": "_setLedGroup",
	#     "parametersSignature": "(s)",
	#     "description": "Set Led group",
	#     "parameters": [
	#         {
	#             "name": "ledGroupName",
	#             "description": "Name of the led group."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_setLedGroup", [ledGroupName])

def _displayRobotViewDebug(useDisplay:bool) -> None:
	"""
	Use debug display in robot view
	
	Parameters
	----------
	useDisplay:bool
		Boolean value: true to use debug display in robot view.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "v",
	#     "name": "_displayRobotViewDebug",
	#     "parametersSignature": "(b)",
	#     "description": "Use debug display in robot view",
	#     "parameters": [
	#         {
	#             "name": "useDisplay",
	#             "description": "Boolean value: true to use debug display in robot view."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_displayRobotViewDebug", [useDisplay])

def _getParametersInfo() -> str:
	"""
	Get parameters documentation
	
	Returns
	----------
	Parameters info as string
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "s",
	#     "name": "_getParametersInfo",
	#     "parametersSignature": "()",
	#     "description": "Get parameters documentation",
	#     "parameters": [],
	#     "returnDescription": "Parameters info as string"
	# }
	return call_method("ALBasicAwareness", "_getParametersInfo", [])

def _setEnableStimuliFromBehind(enable:bool) -> None:
	"""
	Allow the robot to detect stimuli coming from behind and to turnthe base up to 180 degrees to watch them. If it's disabled, thestimuli from behind won't be taken into account.
	
	Parameters
	----------
	enable:bool
		true to enable, false to disable
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "_setEnableStimuliFromBehind",
	#     "parametersSignature": "(b)",
	#     "description": "Allow the robot to detect stimuli coming from behind and to turnthe base up to 180 degrees to watch them. If it's disabled, thestimuli from behind won't be taken into account.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "true to enable, false to disable"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_setEnableStimuliFromBehind", [enable])

def _getEnableStimuliFromBehind() -> bool:
	"""
	To know if the robot can detect stimuli from behind
	
	Returns
	----------
	Boolean value: true if stimuli from behind are enabled, else false.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "b",
	#     "name": "_getEnableStimuliFromBehind",
	#     "parametersSignature": "()",
	#     "description": "To know if the robot can detect stimuli from behind",
	#     "parameters": [],
	#     "returnDescription": "Boolean value: true if stimuli from behind are enabled, else false."
	# }
	return call_method("ALBasicAwareness", "_getEnableStimuliFromBehind", [])

def _setEnableCheckLowStimuli(enable:bool) -> None:
	"""
	Allow the robot to check downwards for low stimuli if nobody's found.
	
	Parameters
	----------
	enable:bool
		true to enable, false to disable
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "_setEnableCheckLowStimuli",
	#     "parametersSignature": "(b)",
	#     "description": "Allow the robot to check downwards for low stimuli if nobody's found.",
	#     "parameters": [
	#         {
	#             "name": "enable",
	#             "description": "true to enable, false to disable"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALBasicAwareness", "_setEnableCheckLowStimuli", [enable])

def _getEnableCheckLowStimuli() -> bool:
	"""
	To know if the robot can detect stimuli from behind
	
	Returns
	----------
	Boolean value: true if low stimuli are enabled, else false.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "b",
	#     "name": "_getEnableCheckLowStimuli",
	#     "parametersSignature": "()",
	#     "description": "To know if the robot can detect stimuli from behind",
	#     "parameters": [],
	#     "returnDescription": "Boolean value: true if low stimuli are enabled, else false."
	# }
	return call_method("ALBasicAwareness", "_getEnableCheckLowStimuli", [])

def _getHomeReferencePosition() -> List[float]:
	"""
	Get the position of home
	
	Returns
	----------
	Pose2D as vector: Pose2D of home.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "[f]",
	#     "name": "_getHomeReferencePosition",
	#     "parametersSignature": "()",
	#     "description": "Get the position of home",
	#     "parameters": [],
	#     "returnDescription": "Pose2D as vector: Pose2D of home."
	# }
	return call_method("ALBasicAwareness", "_getHomeReferencePosition", [])

def _onPreferenceUpdated(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceUpdated",
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
	return call_method("ALBasicAwareness", "_onPreferenceUpdated", [p1, p2, p3])

def _onPreferenceSynchronized(p1:str, p2:object, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p1:str
		
	p2:object
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceSynchronized",
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
	return call_method("ALBasicAwareness", "_onPreferenceSynchronized", [p1, p2, p3])

class _Signals:
	stimulusDetected: Signal[[str]] = Signal("ALBasicAwareness", "stimulusDetected")
	"""
	Bridge notes
	------------
	A signal sent by ALBasicAwareness on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	humanTracked: Signal[[int]] = Signal("ALBasicAwareness", "humanTracked")
	"""
	Bridge notes
	------------
	A signal sent by ALBasicAwareness on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	humanLost: Signal[[bool]] = Signal("ALBasicAwareness", "humanLost")
	"""
	Bridge notes
	------------
	A signal sent by ALBasicAwareness on the robot.
	
	subscribe(callback) calls callback(bool) each time the robot sends it.
	"""
signals = _Signals()

