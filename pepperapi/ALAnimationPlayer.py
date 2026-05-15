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
	return send_mfc("ALAnimationPlayer", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALAnimationPlayer", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALAnimationPlayer", "metaObject", [p0])

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
	return send_mfc("ALAnimationPlayer", "terminate", [p0])

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
	return send_mfc("ALAnimationPlayer", "property", [p0])

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
	return send_mfc("ALAnimationPlayer", "setProperty", [p0, p1])

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
	return send_mfc("ALAnimationPlayer", "properties", [])

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
	return send_mfc("ALAnimationPlayer", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALAnimationPlayer", "isStatsEnabled", [])

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
	return send_mfc("ALAnimationPlayer", "enableStats", [p0])

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
	return send_mfc("ALAnimationPlayer", "stats", [])

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
	return send_mfc("ALAnimationPlayer", "clearStats", [])

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
	return send_mfc("ALAnimationPlayer", "isTraceEnabled", [])

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
	return send_mfc("ALAnimationPlayer", "enableTrace", [p0])

def addTagForAnimations(p0:Dict[str,List[str]]) -> None:
	"""
	
	
	Parameters
	----------
	p0:Dict[str,List[str]]
		
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "v",
	    "name": "addTagForAnimations",
	    "parametersSignature": "({s[s]})",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "addTagForAnimations", [p0])

def declarePathForTags(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "v",
	    "name": "declarePathForTags",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "declarePathForTags", [p0])

def _declarePathForTagsPermanently(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "v",
	    "name": "_declarePathForTagsPermanently",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_declarePathForTagsPermanently", [p0])

def reset() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "v",
	    "name": "reset",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "reset", [])

def _getPathsForTags() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "[s]",
	    "name": "_getPathsForTags",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getPathsForTags", [])

def _getTags_1() -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getTags)
	
	
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "[s]",
	    "name": "_getTags",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getTags", [])

def _getTags_2(p0:str) -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getTags)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "[s]",
	    "name": "_getTags",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getTags", [p0])

def _getAnimations_1() -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getAnimations)
	
	
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "[s]",
	    "name": "_getAnimations",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getAnimations", [])

def _getAnimations_2(p0:str) -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getAnimations)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "[s]",
	    "name": "_getAnimations",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getAnimations", [p0])

def _getAnimationsForTag_1(p0:str) -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getAnimationsForTag)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "[s]",
	    "name": "_getAnimationsForTag",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getAnimationsForTag", [p0])

def _getAnimationsForTag_2(p0:str, p1:str) -> List[str]:
	"""
	Note: This is one of the overloads of the original method (_getAnimationsForTag)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "[s]",
	    "name": "_getAnimationsForTag",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "_getAnimationsForTag", [p0, p1])

def run(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "run",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "run", [p0])

def runTag_1(p0:str) -> None:
	"""
	Note: This is one of the overloads of the original method (runTag)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "v",
	    "name": "runTag",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "runTag", [p0])

def runTag_2(p0:str, p1:str) -> None:
	"""
	Note: This is one of the overloads of the original method (runTag)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "v",
	    "name": "runTag",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALAnimationPlayer", "runTag", [p0, p1])

