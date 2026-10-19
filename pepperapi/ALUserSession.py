"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def doesUserExist(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "b",
	#     "name": "doesUserExist",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "doesUserExist", [p0])

def doUsersExist(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "b",
	#     "name": "doUsersExist",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "doUsersExist", [p0])

def getUserList() -> List[int]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "[i]",
	#     "name": "getUserList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUserList", [])

def getNumUsers() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "i",
	#     "name": "getNumUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getNumUsers", [])

def getFocusedUser() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "i",
	#     "name": "getFocusedUser",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getFocusedUser", [])

def getOpenUserSessions() -> List[int]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "[i]",
	#     "name": "getOpenUserSessions",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getOpenUserSessions", [])

def isUserSessionOpen(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "isUserSessionOpen",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "isUserSessionOpen", [p0])

def areUserSessionsOpen(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "areUserSessionsOpen",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "areUserSessionsOpen", [p0])

def isUserPermanent(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "isUserPermanent",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "isUserPermanent", [p0])

def areUsersPermanent(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "areUsersPermanent",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "areUsersPermanent", [p0])

def getPermanentUserList() -> List[int]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "[i]",
	#     "name": "getPermanentUserList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getPermanentUserList", [])

def _rememberUserPermanently(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "_rememberUserPermanently",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_rememberUserPermanently", [p0])

def _forgetPermanentUser(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "_forgetPermanentUser",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_forgetPermanentUser", [p0])

def getBindingList() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "[s]",
	#     "name": "getBindingList",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getBindingList", [])

def doesBindingExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "b",
	#     "name": "doesBindingExist",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "doesBindingExist", [p0])

def getUserBinding(p0:int, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "s",
	#     "name": "getUserBinding",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUserBinding", [p0, p1])

def getUserBindings(p0:int) -> Dict[str,str]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "{ss}",
	#     "name": "getUserBindings",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUserBindings", [p0])

def findUsersWithBinding(p0:str, p1:str) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "[i]",
	#     "name": "findUsersWithBinding",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "findUsersWithBinding", [p0, p1])

def getUsidFromPpid(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "i",
	#     "name": "getUsidFromPpid",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUsidFromPpid", [p0])

def getPpidFromUsid(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "i",
	#     "name": "getPpidFromUsid",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getPpidFromUsid", [p0])

def _checkPhotoForIdentification(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "i",
	#     "name": "_checkPhotoForIdentification",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_checkPhotoForIdentification", [p0])

def _reinforceIdentificationFromPhoto(p0:int, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "_reinforceIdentificationFromPhoto",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_reinforceIdentificationFromPhoto", [p0, p1])

def _createUserFromPhoto(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "i",
	#     "name": "_createUserFromPhoto",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_createUserFromPhoto", [p0])

def _setFocusedUser(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_setFocusedUser",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_setFocusedUser", [p0])

def _createUsers(p0:int) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "[i]",
	#     "name": "_createUsers",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_createUsers", [p0])

def _deleteUser(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "_deleteUser",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_deleteUser", [p0])

def _deleteUsers(p0:List[int]) -> bool:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "_deleteUsers",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_deleteUsers", [p0])

def _openUserSessions(p0:List[int]) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "[i]",
	#     "name": "_openUserSessions",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_openUserSessions", [p0])

def _closeUserSessions(p0:List[int]) -> List[int]:
	"""
	
	
	Parameters
	----------
	p0:List[int]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "[i]",
	#     "name": "_closeUserSessions",
	#     "parametersSignature": "([i])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_closeUserSessions", [p0])

def _bindUser(p0:int, p1:str, p2:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "_bindUser",
	#     "parametersSignature": "(iss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_bindUser", [p0, p1, p2])

def _unbindUser(p0:int, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "_unbindUser",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_unbindUser", [p0, p1])

def _getDatabaseVersion() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "i",
	#     "name": "_getDatabaseVersion",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_getDatabaseVersion", [])

def _deleteAllUsers() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "b",
	#     "name": "_deleteAllUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_deleteAllUsers", [])

def getBindingSources() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "[s]",
	#     "name": "getBindingSources",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getBindingSources", [])

def doesBindingSourceExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "b",
	#     "name": "doesBindingSourceExist",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "doesBindingSourceExist", [p0])

def getUserDataSources() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "[s]",
	#     "name": "getUserDataSources",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUserDataSources", [])

def doesUserDataSourceExist(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "b",
	#     "name": "doesUserDataSourceExist",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "doesUserDataSourceExist", [p0])

def _registerUserDataSource(p0:str, p1:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "_registerUserDataSource",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_registerUserDataSource", [p0, p1])

def _unregisterUserDataSource(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "_unregisterUserDataSource",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_unregisterUserDataSource", [p0])

@overload
def getUserData(p0:int, p1:str, /) -> Dict[str,Any]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	
	Bridge notes
	------------
	getUserData has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "{sm}",
	#     "name": "getUserData",
	#     "parametersSignature": "(is)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def getUserData(p0:int, p1:str, p2:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	
	Bridge notes
	------------
	getUserData has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "m",
	#     "name": "getUserData",
	#     "parametersSignature": "(iss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def getUserData(*args, **kwargs):
	"""
	Bridge notes
	------------
	getUserData has 2 variants on the robot:
	- getUserData(p0:int, p1:str)
	- getUserData(p0:int, p1:str, p2:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALUserSession.getUserData has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALUserSession", "getUserData", list(args))

def setUserData(p0:int, p1:str, p2:str, p3:Any) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:str
		
	p2:str
		
	p3:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "v",
	#     "name": "setUserData",
	#     "parametersSignature": "(issm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "setUserData", [p0, p1, p2, p3])

def getUserCreationDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "s",
	#     "name": "getUserCreationDate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getUserCreationDate", [p0])

def getFirstEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "s",
	#     "name": "getFirstEncounterDate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getFirstEncounterDate", [p0])

def getCurrentEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "s",
	#     "name": "getCurrentEncounterDate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getCurrentEncounterDate", [p0])

def getLastEncounterDate(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "s",
	#     "name": "getLastEncounterDate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getLastEncounterDate", [p0])

def getSecondsSinceLastEncounter(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "i",
	#     "name": "getSecondsSinceLastEncounter",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "getSecondsSinceLastEncounter", [p0])

def _getSecondsSinceUserCreation(p0:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "i",
	#     "name": "_getSecondsSinceUserCreation",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALUserSession", "_getSecondsSinceUserCreation", [p0])

class _Signals:
	createdUsers: Signal[[List[int]]] = Signal("ALUserSession", "createdUsers")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	deletedUsers: Signal[[List[int]]] = Signal("ALUserSession", "deletedUsers")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	openedSessions: Signal[[List[int]]] = Signal("ALUserSession", "openedSessions")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	closedSessions: Signal[[List[int]]] = Signal("ALUserSession", "closedSessions")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	focusedUser: Signal[[int]] = Signal("ALUserSession", "focusedUser")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	noOpenSession: Signal[[bool]] = Signal("ALUserSession", "noOpenSession")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(bool) each time the robot sends it.
	"""
	addedPermanentUsers: Signal[[List[int]]] = Signal("ALUserSession", "addedPermanentUsers")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	removedPermanentUsers: Signal[[List[int]]] = Signal("ALUserSession", "removedPermanentUsers")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(List[int]) each time the robot sends it.
	"""
	bindedUser: Signal[[int, str, str]] = Signal("ALUserSession", "bindedUser")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(int, str, str) each time the robot sends it.
	"""
	unbindedUser: Signal[[int, str]] = Signal("ALUserSession", "unbindedUser")
	"""
	Bridge notes
	------------
	A signal sent by ALUserSession on the robot.
	
	subscribe(callback) calls callback(int, str) each time the robot sends it.
	"""
signals = _Signals()

