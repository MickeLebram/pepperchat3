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
	return send_mfc("ALConnectionManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALConnectionManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALConnectionManager", "metaObject", [p0])

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
	return send_mfc("ALConnectionManager", "terminate", [p0])

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
	return send_mfc("ALConnectionManager", "property", [p0])

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
	return send_mfc("ALConnectionManager", "setProperty", [p0, p1])

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
	return send_mfc("ALConnectionManager", "properties", [])

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
	return send_mfc("ALConnectionManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALConnectionManager", "isStatsEnabled", [])

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
	return send_mfc("ALConnectionManager", "enableStats", [p0])

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
	return send_mfc("ALConnectionManager", "stats", [])

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
	return send_mfc("ALConnectionManager", "clearStats", [])

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
	return send_mfc("ALConnectionManager", "isTraceEnabled", [])

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
	return send_mfc("ALConnectionManager", "enableTrace", [p0])

def services() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "m",
	    "name": "services",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "services", [])

def service(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "m",
	    "name": "service",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "service", [p0])

def scan_1(p0:str) -> None:
	"""
	Note: This is one of the overloads of the original method (scan)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "v",
	    "name": "scan",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "scan", [p0])

def scan_2() -> None:
	"""
	Note: This is one of the overloads of the original method (scan)
	
	
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "v",
	    "name": "scan",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "scan", [])

def setServiceConfiguration(p0:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "v",
	    "name": "setServiceConfiguration",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "setServiceConfiguration", [p0])

def setServiceInput(p0:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "v",
	    "name": "setServiceInput",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "setServiceInput", [p0])

def state() -> str:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "s",
	    "name": "state",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "state", [])

def forget(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "v",
	    "name": "forget",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "forget", [p0])

def connect(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "v",
	    "name": "connect",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "connect", [p0])

def disconnect(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "v",
	    "name": "disconnect",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "disconnect", [p0])

def technologies() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "m",
	    "name": "technologies",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "technologies", [])

def enableTethering_1(p0:str, p1:str, p2:str) -> None:
	"""
	Note: This is one of the overloads of the original method (enableTethering)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "enableTethering",
	    "parametersSignature": "(sss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "enableTethering", [p0, p1, p2])

def enableTethering_2(p0:str) -> None:
	"""
	Note: This is one of the overloads of the original method (enableTethering)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "v",
	    "name": "enableTethering",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "enableTethering", [p0])

def disableTethering(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "v",
	    "name": "disableTethering",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "disableTethering", [p0])

def getTetheringEnable(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "getTetheringEnable",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "getTetheringEnable", [p0])

def tetheringName(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "s",
	    "name": "tetheringName",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "tetheringName", [p0])

def tetheringPassphrase(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "s",
	    "name": "tetheringPassphrase",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "tetheringPassphrase", [p0])

def countries() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "[s]",
	    "name": "countries",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "countries", [])

def setCountry(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "setCountry",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "setCountry", [p0])

def country() -> str:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "s",
	    "name": "country",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "country", [])

def interfaces() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "interfaces",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "interfaces", [])

def provisionService(p0:Dict[str,str]) -> None:
	"""
	
	
	Parameters
	----------
	p0:Dict[str,str]
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "v",
	    "name": "provisionService",
	    "parametersSignature": "({ss})",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "provisionService", [p0])

def provisionedServices() -> List[Dict[str,str]]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "[{ss}]",
	    "name": "provisionedServices",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "provisionedServices", [])

def removeProvisionedService(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "removeProvisionedService",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALConnectionManager", "removeProvisionedService", [p0])

