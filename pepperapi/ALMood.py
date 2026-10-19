"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class ValueConfidence:
	"""NAOqi signature: (ff)<ValueConfidence,value,confidence>"""
	value: float
	confidence: float


@dataclass
class BodyLanguageEase:
	"""NAOqi signature: (ff)<BodyLanguageEase,level,confidence>"""
	level: float
	confidence: float


@dataclass
class Smile:
	"""NAOqi signature: (ff)<Smile,value,confidence>"""
	value: float
	confidence: float


@dataclass
class BodyLanguageState:
	"""NAOqi signature: (BodyLanguageEase)<BodyLanguageState,ease>"""
	ease: BodyLanguageEase


@dataclass
class Expressions:
	"""NAOqi signature: (ValueConfidence ValueConfidence ValueConfidence ValueConfidence ValueConfidence ValueConfidence ValueConfidence)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>"""
	calm: ValueConfidence
	anger: ValueConfidence
	joy: ValueConfidence
	sorrow: ValueConfidence
	laughter: ValueConfidence
	excitement: ValueConfidence
	surprise: ValueConfidence


@dataclass
class PersonState:
	"""NAOqi signature: (ValueConfidence ValueConfidence BodyLanguageState Smile Expressions)<PersonState,valence,attention,bodyLanguageState,smile,expressions>"""
	valence: ValueConfidence
	attention: ValueConfidence
	bodyLanguageState: BodyLanguageState
	smile: Smile
	expressions: Expressions


@dataclass
class Person:
	"""NAOqi signature: (i PersonState)<Person,userSessionID,personState>"""
	userSessionID: int
	personState: PersonState


@dataclass
class AmbianceState:
	"""NAOqi signature: (ff)<AmbianceState,agitationLevel,calmLevel>"""
	agitationLevel: float
	calmLevel: float


def subscribe(p0:str, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "b",
	#     "name": "subscribe",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "subscribe", [p0, p1])

def unsubscribe(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "b",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "unsubscribe", [p0])

def getSubscribersInfo() -> Dict[str,str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "{ss}",
	#     "name": "getSubscribersInfo",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "getSubscribersInfo", [])

def currentPersonState() -> PersonState:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	#     "name": "currentPersonState",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "currentPersonState", [], returns=PersonState)

def personStateFromPeoplePerception(p0:int) -> PersonState:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	#     "name": "personStateFromPeoplePerception",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "personStateFromPeoplePerception", [p0], returns=PersonState)

def personStateFromUserSession(p0:int) -> PersonState:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	#     "name": "personStateFromUserSession",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "personStateFromUserSession", [p0], returns=PersonState)

def persons() -> List[Person]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "[(i((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>)<Person,userSessionID,personState>]",
	#     "name": "persons",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "persons", [], returns=List[Person])

def _pushValence(p0:str, p1:float) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "b",
	#     "name": "_pushValence",
	#     "parametersSignature": "(sf)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "_pushValence", [p0, p1])

def ambianceState() -> AmbianceState:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "(ff)<AmbianceState,agitationLevel,calmLevel>",
	#     "name": "ambianceState",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "ambianceState", [], returns=AmbianceState)

def getEmotionalReaction() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "s",
	#     "name": "getEmotionalReaction",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALMood", "getEmotionalReaction", [])

class _Signals:
	currentFocusedUserMood: Signal[[str]] = Signal("ALMood", "currentFocusedUserMood")
	"""
	Bridge notes
	------------
	A signal sent by ALMood on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	valenceChanged: Signal[[str]] = Signal("ALMood", "valenceChanged")
	"""
	Bridge notes
	------------
	A signal sent by ALMood on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	
	Sent when properties.valence changes, not each time the robot sets it. Not necessarily for every change, though: on NAOqi 2.5 and 2.8, ALMood.valenceChanged and attentionChanged were seen to skip changes to 'unknown'. To catch every change, subscribe to properties.valence and compare the values.
	"""
	attentionChanged: Signal[[str]] = Signal("ALMood", "attentionChanged")
	"""
	Bridge notes
	------------
	A signal sent by ALMood on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	
	Sent when properties.attention changes, not each time the robot sets it. Not necessarily for every change, though: on NAOqi 2.5 and 2.8, ALMood.valenceChanged and attentionChanged were seen to skip changes to 'unknown'. To catch every change, subscribe to properties.attention and compare the values.
	"""
	ambianceChanged: Signal[[str]] = Signal("ALMood", "ambianceChanged")
	"""
	Bridge notes
	------------
	A signal sent by ALMood on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	
	Sent when properties.ambiance changes, not each time the robot sets it. Not necessarily for every change, though: on NAOqi 2.5 and 2.8, ALMood.valenceChanged and attentionChanged were seen to skip changes to 'unknown'. To catch every change, subscribe to properties.ambiance and compare the values.
	"""
signals = _Signals()

class _Properties:
	valence: Property[str] = Property("ALMood", "valence")
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(str) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	
	There is also signals.valenceChanged.
	"""
	valenceLevel: Property[ValueConfidence] = Property("ALMood", "valenceLevel", ValueConfidence)
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(ValueConfidence) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	attention: Property[str] = Property("ALMood", "attention")
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(str) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	
	There is also signals.attentionChanged.
	"""
	attentionLevel: Property[ValueConfidence] = Property("ALMood", "attentionLevel", ValueConfidence)
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(ValueConfidence) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	ambiance: Property[str] = Property("ALMood", "ambiance")
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(str) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	
	There is also signals.ambianceChanged.
	"""
	ambianceLevel: Property[float] = Property("ALMood", "ambianceLevel")
	"""
	Bridge notes
	------------
	A property of ALMood on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

