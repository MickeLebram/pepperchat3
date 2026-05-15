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
	return send_mfc("ALUserInfo", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALUserInfo", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALUserInfo", "metaObject", [p0])

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
	return send_mfc("ALUserInfo", "terminate", [p0])

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
	return send_mfc("ALUserInfo", "property", [p0])

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
	return send_mfc("ALUserInfo", "setProperty", [p0, p1])

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
	return send_mfc("ALUserInfo", "properties", [])

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
	return send_mfc("ALUserInfo", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALUserInfo", "isStatsEnabled", [])

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
	return send_mfc("ALUserInfo", "enableStats", [p0])

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
	return send_mfc("ALUserInfo", "stats", [])

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
	return send_mfc("ALUserInfo", "clearStats", [])

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
	return send_mfc("ALUserInfo", "isTraceEnabled", [])

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
	return send_mfc("ALUserInfo", "enableTrace", [p0])

def get_1(p0:str) -> object:
	"""
	Note: This is one of the overloads of the original method (get)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "m",
	    "name": "get",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "get", [p0])

def get_2(p0:int, p1:str) -> object:
	"""
	Note: This is one of the overloads of the original method (get)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "m",
	    "name": "get",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "get", [p0, p1])

def get_3(p0:str, p1:str) -> object:
	"""
	Note: This is one of the overloads of the original method (get)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "m",
	    "name": "get",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "get", [p0, p1])

def get_4(p0:str, p1:int, p2:str) -> object:
	"""
	Note: This is one of the overloads of the original method (get)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "m",
	    "name": "get",
	    "parametersSignature": "(sis)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "get", [p0, p1, p2])

def _set_1(p0:str, p1:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (_set)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "b",
	    "name": "_set",
	    "parametersSignature": "(sm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_set", [p0, p1])

def _set_2(p0:int, p1:str, p2:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (_set)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "b",
	    "name": "_set",
	    "parametersSignature": "(ism)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_set", [p0, p1, p2])

def set_1(p0:str, p1:str, p2:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (set)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "b",
	    "name": "set",
	    "parametersSignature": "(ssm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "set", [p0, p1, p2])

def set_2(p0:str, p1:int, p2:str, p3:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (set)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	p3:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "b",
	    "name": "set",
	    "parametersSignature": "(sism)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "set", [p0, p1, p2, p3])

def has_1(p0:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (has)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "b",
	    "name": "has",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "has", [p0])

def has_2(p0:int, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (has)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "b",
	    "name": "has",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "has", [p0, p1])

def has_3(p0:str, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (has)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "b",
	    "name": "has",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "has", [p0, p1])

def has_4(p0:str, p1:int, p2:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (has)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "b",
	    "name": "has",
	    "parametersSignature": "(sis)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "has", [p0, p1, p2])

def _remove_1(p0:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_remove)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "b",
	    "name": "_remove",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_remove", [p0])

def _remove_2(p0:int, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_remove)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "b",
	    "name": "_remove",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_remove", [p0, p1])

def remove_1(p0:str, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (remove)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "remove",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "remove", [p0, p1])

def remove_2(p0:str, p1:int, p2:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (remove)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "remove",
	    "parametersSignature": "(sis)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "remove", [p0, p1, p2])

def removeUser_1(p0:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (removeUser)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "removeUser",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "removeUser", [p0])

def removeUser_2(p0:str, p1:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (removeUser)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "removeUser",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "removeUser", [p0, p1])

def _removeUser_1() -> bool:
	"""
	Note: This is one of the overloads of the original method (_removeUser)
	
	
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "_removeUser",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_removeUser", [])

def _removeUser_2(p0:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (_removeUser)
	
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "_removeUser",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "_removeUser", [p0])

def getType(p0:str, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "s",
	    "name": "getType",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserInfo", "getType", [p0, p1])

