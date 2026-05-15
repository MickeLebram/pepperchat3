from .gentypes import *
from .robot_client import send_mfc
import json
"""

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
	return send_mfc("ALMood", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALMood", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALMood", "metaObject", [p0])

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
	return send_mfc("ALMood", "terminate", [p0])

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
	return send_mfc("ALMood", "property", [p0])

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
	return send_mfc("ALMood", "setProperty", [p0, p1])

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
	return send_mfc("ALMood", "properties", [])

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
	return send_mfc("ALMood", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALMood", "isStatsEnabled", [])

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
	return send_mfc("ALMood", "enableStats", [p0])

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
	return send_mfc("ALMood", "stats", [])

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
	return send_mfc("ALMood", "clearStats", [])

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
	return send_mfc("ALMood", "isTraceEnabled", [])

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
	return send_mfc("ALMood", "enableTrace", [p0])

def subscribe(p0:str, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "b",
	    "name": "subscribe",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "subscribe", [p0, p1])

def unsubscribe(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "b",
	    "name": "unsubscribe",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "unsubscribe", [p0])

def getSubscribersInfo() -> Dict[str,str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "{ss}",
	    "name": "getSubscribersInfo",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "getSubscribersInfo", [])

def currentPersonState() -> PersonState:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	    "name": "currentPersonState",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "currentPersonState", [])

def personStateFromPeoplePerception(p0:int) -> PersonState:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	    "name": "personStateFromPeoplePerception",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "personStateFromPeoplePerception", [p0])

def personStateFromUserSession(p0:int) -> PersonState:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>",
	    "name": "personStateFromUserSession",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "personStateFromUserSession", [p0])

def persons() -> List[Person]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "[(i((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>((ff)<BodyLanguageEase,level,confidence>)<BodyLanguageState,ease>(ff)<Smile,value,confidence>((ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>(ff)<ValueConfidence<float>,value,confidence>)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>)<PersonState,valence,attention,bodyLanguageState,smile,expressions>)<Person,userSessionID,personState>]",
	    "name": "persons",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "persons", [])

def _pushValence(p0:str, p1:float) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:float
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "b",
	    "name": "_pushValence",
	    "parametersSignature": "(sf)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "_pushValence", [p0, p1])

def ambianceState() -> AmbianceState:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "(ff)<AmbianceState,agitationLevel,calmLevel>",
	    "name": "ambianceState",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "ambianceState", [])

def getEmotionalReaction() -> str:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "s",
	    "name": "getEmotionalReaction",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALMood", "getEmotionalReaction", [])

