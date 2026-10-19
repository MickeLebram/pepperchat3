"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class RecognitionMatch:
	"""NAOqi signature: (ifb)<RecognitionMatch,uid,confidence,isLongTerm>"""
	uid: int
	confidence: float
	isLongTerm: bool


@dataclass
class RecognitionResult:
	"""NAOqi signature: (i[RecognitionMatch])<RecognitionResult,status,matches>"""
	status: int
	matches: List[RecognitionMatch]


def startMonitoringUsers() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "startMonitoringUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserSessionManager", "startMonitoringUsers", [])

def stopMonitoringUsers() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "stopMonitoringUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserSessionManager", "stopMonitoringUsers", [])

def isMonitoringUsers() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "isMonitoringUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserSessionManager", "isMonitoringUsers", [])

def identify(p0:int) -> RecognitionResult:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "(i[(ifb)<RecognitionMatch,uid,confidence,isLongTerm>])<RecognitionResult,status,matches>",
	#     "name": "identify",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserSessionManager", "identify", [p0], returns=RecognitionResult)

def reidentifyFocusedUser() -> RecognitionResult:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "(i[(ifb)<RecognitionMatch,uid,confidence,isLongTerm>])<RecognitionResult,status,matches>",
	#     "name": "reidentifyFocusedUser",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserSessionManager", "reidentifyFocusedUser", [], returns=RecognitionResult)

class _Signals:
	onStart: Signal[[]] = Signal("_UserSessionManager", "onStart")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	onStop: Signal[[]] = Signal("_UserSessionManager", "onStop")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	identificationStarted: Signal[[int]] = Signal("_UserSessionManager", "identificationStarted")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	identificationResult: Signal[[RecognitionResult]] = Signal("_UserSessionManager", "identificationResult", (RecognitionResult,))
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback(RecognitionResult) each time the robot sends it.
	"""
	focusingUser: Signal[[]] = Signal("_UserSessionManager", "focusingUser")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	unFocusingUser: Signal[[]] = Signal("_UserSessionManager", "unFocusingUser")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	identificationStatus: Signal[[int]] = Signal("_UserSessionManager", "identificationStatus")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	compatOnPopulationUpdated: Signal[[]] = Signal("_UserSessionManager", "compatOnPopulationUpdated")
	"""
	Bridge notes
	------------
	A signal sent by _UserSessionManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
signals = _Signals()

class _Properties:
	retryIdentificationDelay: Property[int] = Property("_UserSessionManager", "retryIdentificationDelay")
	"""
	Bridge notes
	------------
	A property of _UserSessionManager on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	unfocusTimeout: Property[int] = Property("_UserSessionManager", "unfocusTimeout")
	"""
	Bridge notes
	------------
	A property of _UserSessionManager on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	forgetUserTimout: Property[int] = Property("_UserSessionManager", "forgetUserTimout")
	"""
	Bridge notes
	------------
	A property of _UserSessionManager on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

