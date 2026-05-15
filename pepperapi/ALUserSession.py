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
	return send_mfc("ALUserSession", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALUserSession", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALUserSession", "metaObject", [p0])

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
	return send_mfc("ALUserSession", "terminate", [p0])

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
	return send_mfc("ALUserSession", "property", [p0])

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
	return send_mfc("ALUserSession", "setProperty", [p0, p1])

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
	return send_mfc("ALUserSession", "properties", [])

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
	return send_mfc("ALUserSession", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALUserSession", "isStatsEnabled", [])

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
	return send_mfc("ALUserSession", "enableStats", [p0])

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
	return send_mfc("ALUserSession", "stats", [])

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
	return send_mfc("ALUserSession", "clearStats", [])

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
	return send_mfc("ALUserSession", "isTraceEnabled", [])

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
	return send_mfc("ALUserSession", "enableTrace", [p0])

def doesUserExist(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "b",
	    "name": "doesUserExist",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "doesUserExist", [p0])

def doUsersExist(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "b",
	    "name": "doUsersExist",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "doUsersExist", [p0])

def getUserList() -> List[int]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "[i]",
	    "name": "getUserList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserList", [])

def getNumUsers() -> int:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "i",
	    "name": "getNumUsers",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getNumUsers", [])

def getFocusedUser() -> int:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "i",
	    "name": "getFocusedUser",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getFocusedUser", [])

def getOpenUserSessions() -> List[int]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "[i]",
	    "name": "getOpenUserSessions",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getOpenUserSessions", [])

def isUserSessionOpen(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "isUserSessionOpen",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "isUserSessionOpen", [p0])

def areUserSessionsOpen(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "areUserSessionsOpen",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "areUserSessionsOpen", [p0])

def isUserPermanent(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "isUserPermanent",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "isUserPermanent", [p0])

def areUsersPermanent(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "areUsersPermanent",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "areUsersPermanent", [p0])

def getPermanentUserList() -> List[int]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "[i]",
	    "name": "getPermanentUserList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getPermanentUserList", [])

def _rememberUserPermanently(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "_rememberUserPermanently",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_rememberUserPermanently", [p0])

def _forgetPermanentUser(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "_forgetPermanentUser",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_forgetPermanentUser", [p0])

def getBindingList() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "[s]",
	    "name": "getBindingList",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getBindingList", [])

def doesBindingExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "b",
	    "name": "doesBindingExist",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "doesBindingExist", [p0])

def getUserBinding(p0:int, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "s",
	    "name": "getUserBinding",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserBinding", [p0, p1])

def getUserBindings(p0:int) -> Dict[str,str]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "{ss}",
	    "name": "getUserBindings",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserBindings", [p0])

def findUsersWithBinding(p0:str, p1:str) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "[i]",
	    "name": "findUsersWithBinding",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "findUsersWithBinding", [p0, p1])

def getUsidFromPpid(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "i",
	    "name": "getUsidFromPpid",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUsidFromPpid", [p0])

def getPpidFromUsid(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "i",
	    "name": "getPpidFromUsid",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getPpidFromUsid", [p0])

def _checkPhotoForIdentification(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "i",
	    "name": "_checkPhotoForIdentification",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_checkPhotoForIdentification", [p0])

def _reinforceIdentificationFromPhoto(p0:int, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "b",
	    "name": "_reinforceIdentificationFromPhoto",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_reinforceIdentificationFromPhoto", [p0, p1])

def _createUserFromPhoto(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "i",
	    "name": "_createUserFromPhoto",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_createUserFromPhoto", [p0])

def _setFocusedUser(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "v",
	    "name": "_setFocusedUser",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_setFocusedUser", [p0])

def _createUsers(p0:int) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "[i]",
	    "name": "_createUsers",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_createUsers", [p0])

def _deleteUser(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "_deleteUser",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_deleteUser", [p0])

def _deleteUsers(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "_deleteUsers",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_deleteUsers", [p0])

def _openUserSessions(p0:List[int]) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "[i]",
	    "name": "_openUserSessions",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_openUserSessions", [p0])

def _closeUserSessions(p0:List[int]) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "[i]",
	    "name": "_closeUserSessions",
	    "parametersSignature": "([i])",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_closeUserSessions", [p0])

def _bindUser(p0:int, p1:str, p2:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "b",
	    "name": "_bindUser",
	    "parametersSignature": "(iss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_bindUser", [p0, p1, p2])

def _unbindUser(p0:int, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "b",
	    "name": "_unbindUser",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_unbindUser", [p0, p1])

def _getDatabaseVersion() -> int:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "i",
	    "name": "_getDatabaseVersion",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_getDatabaseVersion", [])

def _deleteAllUsers() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "b",
	    "name": "_deleteAllUsers",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_deleteAllUsers", [])

def getBindingSources() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "[s]",
	    "name": "getBindingSources",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getBindingSources", [])

def doesBindingSourceExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "b",
	    "name": "doesBindingSourceExist",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "doesBindingSourceExist", [p0])

def getUserDataSources() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "[s]",
	    "name": "getUserDataSources",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserDataSources", [])

def doesUserDataSourceExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "b",
	    "name": "doesUserDataSourceExist",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "doesUserDataSourceExist", [p0])

def _registerUserDataSource(p0:str, p1:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "v",
	    "name": "_registerUserDataSource",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_registerUserDataSource", [p0, p1])

def _unregisterUserDataSource(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "v",
	    "name": "_unregisterUserDataSource",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_unregisterUserDataSource", [p0])

def getUserData_1(p0:int, p1:str, p2:str) -> object:
	"""
	Note: This is one of the overloads of the original method (getUserData)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "m",
	    "name": "getUserData",
	    "parametersSignature": "(iss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserData", [p0, p1, p2])

def getUserData_2(p0:int, p1:str) -> Dict[str,object]:
	"""
	Note: This is one of the overloads of the original method (getUserData)
	
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "{sm}",
	    "name": "getUserData",
	    "parametersSignature": "(is)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserData", [p0, p1])

def setUserData(p0:int, p1:str, p2:str, p3:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	p3:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "v",
	    "name": "setUserData",
	    "parametersSignature": "(issm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "setUserData", [p0, p1, p2, p3])

def getUserCreationDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "s",
	    "name": "getUserCreationDate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getUserCreationDate", [p0])

def getFirstEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "s",
	    "name": "getFirstEncounterDate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getFirstEncounterDate", [p0])

def getCurrentEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "s",
	    "name": "getCurrentEncounterDate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getCurrentEncounterDate", [p0])

def getLastEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "s",
	    "name": "getLastEncounterDate",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getLastEncounterDate", [p0])

def getSecondsSinceLastEncounter(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "i",
	    "name": "getSecondsSinceLastEncounter",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "getSecondsSinceLastEncounter", [p0])

def _getSecondsSinceUserCreation(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "i",
	    "name": "_getSecondsSinceUserCreation",
	    "parametersSignature": "(i)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALUserSession", "_getSecondsSinceUserCreation", [p0])

