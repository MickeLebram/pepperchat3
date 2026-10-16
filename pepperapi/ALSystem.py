"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class AppBackupInfo:
	"""NAOqi signature: (sss[s][s])<AppBackupInfo,applicationName,userDataPath,userConfPath,dataBackupPaths,confBackupPaths>"""
	applicationName: str
	userDataPath: str
	userConfPath: str
	dataBackupPaths: List[str]
	confBackupPaths: List[str]


@dataclass
class PartitionInfo:
	"""NAOqi signature: (ssLL)<PartitionInfo,filesystem,path,size,free>"""
	filesystem: str
	path: str
	size: int
	free: int


@dataclass
class SystemInfo:
	"""NAOqi signature: (ssss)<SystemInfo,systemVersion,buildDate,buildID,buildTag>"""
	systemVersion: str
	buildDate: str
	buildID: str
	buildTag: str


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
	return call_method("ALSystem", "version", [])

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
	return call_method("ALSystem", "ping", [])

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
	return call_method("ALSystem", "getMethodList", [])

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
	return call_method("ALSystem", "getMethodHelp", [methodName])

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
	return call_method("ALSystem", "getModuleHelp", [])

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
	return call_method("ALSystem", "getBrokerName", [])

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
	return call_method("ALSystem", "getUsage", [name])

def appBackupInfo() -> List[AppBackupInfo]:
	"""
	Get the backup information of applications
	
	Returns
	----------
	A vector with all application backup infos
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "[(sss[s][s])<AppBackupInfo,applicationName,userDataPath,userConfPath,dataBackupPaths,confBackupPaths>]",
	#     "name": "appBackupInfo",
	#     "parametersSignature": "()",
	#     "description": "Get the backup information of applications",
	#     "parameters": [],
	#     "returnDescription": "A vector with all application backup infos"
	# }
	return call_method("ALSystem", "appBackupInfo", [], returns=List[AppBackupInfo])

def diskFree(all:bool) -> List[PartitionInfo]:
	"""
	Display free disk space
	
	Parameters
	----------
	all:bool
		Show all mount partions.
	
	Returns
	----------
	A vector with all partions' infos
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "[(ssLL)<PartitionInfo,filesystem,path,size,free>]",
	#     "name": "diskFree",
	#     "parametersSignature": "(b)",
	#     "description": "Display free disk space",
	#     "parameters": [
	#         {
	#             "name": "all",
	#             "description": "Show all mount partions."
	#         }
	#     ],
	#     "returnDescription": "A vector with all partions' infos"
	# }
	return call_method("ALSystem", "diskFree", [all], returns=List[PartitionInfo])

def robotName() -> str:
	"""
	System hostname
	
	Returns
	----------
	name of the robot
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "s",
	#     "name": "robotName",
	#     "parametersSignature": "()",
	#     "description": "System hostname",
	#     "parameters": [],
	#     "returnDescription": "name of the robot"
	# }
	return call_method("ALSystem", "robotName", [])

def setRobotName(name:str) -> bool:
	"""
	Set system hostname
	
	Parameters
	----------
	name:str
		name to use
	
	Returns
	----------
	whether the operation was successful
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "setRobotName",
	#     "parametersSignature": "(s)",
	#     "description": "Set system hostname",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name to use"
	#         }
	#     ],
	#     "returnDescription": "whether the operation was successful"
	# }
	return call_method("ALSystem", "setRobotName", [name])

def robotIcon() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "robotIcon",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "robotIcon", [])

def shutdown() -> None:
	"""
	Shutdown robot
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "shutdown",
	#     "parametersSignature": "()",
	#     "description": "Shutdown robot",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "shutdown", [])

def reboot() -> None:
	"""
	Reboot robot
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "reboot",
	#     "parametersSignature": "()",
	#     "description": "Reboot robot",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "reboot", [])

def systemVersion() -> str:
	"""
	Running system version
	
	Returns
	----------
	running system version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "s",
	#     "name": "systemVersion",
	#     "parametersSignature": "()",
	#     "description": "Running system version",
	#     "parameters": [],
	#     "returnDescription": "running system version"
	# }
	return call_method("ALSystem", "systemVersion", [])

def systemInfo() -> SystemInfo:
	"""
	Running system version
	
	Returns
	----------
	information about the system version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "(ssss)<SystemInfo,systemVersion,buildDate,buildID,buildTag>",
	#     "name": "systemInfo",
	#     "parametersSignature": "()",
	#     "description": "Running system version",
	#     "parameters": [],
	#     "returnDescription": "information about the system version"
	# }
	return call_method("ALSystem", "systemInfo", [], returns=SystemInfo)

def freeMemory() -> int:
	"""
	Amount of available memory in heap
	
	Returns
	----------
	amount of available memory in heap
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "freeMemory",
	#     "parametersSignature": "()",
	#     "description": "Amount of available memory in heap",
	#     "parameters": [],
	#     "returnDescription": "amount of available memory in heap"
	# }
	return call_method("ALSystem", "freeMemory", [])

def totalMemory() -> int:
	"""
	Amount of total memory in heap
	
	Returns
	----------
	amount of total memory in heap
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "totalMemory",
	#     "parametersSignature": "()",
	#     "description": "Amount of total memory in heap",
	#     "parameters": [],
	#     "returnDescription": "amount of total memory in heap"
	# }
	return call_method("ALSystem", "totalMemory", [])

def timezone() -> str:
	"""
	Current timezone
	
	Returns
	----------
	current timezone
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "s",
	#     "name": "timezone",
	#     "parametersSignature": "()",
	#     "description": "Current timezone",
	#     "parameters": [],
	#     "returnDescription": "current timezone"
	# }
	return call_method("ALSystem", "timezone", [])

def setTimezone(timezone:str) -> bool:
	"""
	Set current timezone
	
	Parameters
	----------
	timezone:str
		timezone to use
	
	Returns
	----------
	whether the operation was successful
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "setTimezone",
	#     "parametersSignature": "(s)",
	#     "description": "Set current timezone",
	#     "parameters": [
	#         {
	#             "name": "timezone",
	#             "description": "timezone to use"
	#         }
	#     ],
	#     "returnDescription": "whether the operation was successful"
	# }
	return call_method("ALSystem", "setTimezone", [timezone])

def previousSystemVersion() -> str:
	"""
	Previous system version before software update (empty if this is not the 1st boot after a software update)
	
	Returns
	----------
	Previous system version before software update.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "s",
	#     "name": "previousSystemVersion",
	#     "parametersSignature": "()",
	#     "description": "Previous system version before software update (empty if this is not the 1st boot after a software update)",
	#     "parameters": [],
	#     "returnDescription": "Previous system version before software update."
	# }
	return call_method("ALSystem", "previousSystemVersion", [])

def changePassword(old_password:str, new_password:str) -> None:
	"""
	Change the user password.
	
	Parameters
	----------
	old_password:str
		The current password of the user.
	new_password:str
		The new user password.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "changePassword",
	#     "parametersSignature": "(ss)",
	#     "description": "Change the user password.",
	#     "parameters": [
	#         {
	#             "name": "old password",
	#             "description": "The current password of the user."
	#         },
	#         {
	#             "name": "new password",
	#             "description": "The new user password."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "changePassword", [old_password, new_password])

def upgrade(image:str, checksum:str) -> None:
	"""
	Flash the system image.
	
	Parameters
	----------
	image:str
		Local path to a valid image.
	checksum:str
		Local path to a md5 checksum file, or empty string for no verification
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "upgrade",
	#     "parametersSignature": "(ss)",
	#     "description": "Flash the system image.",
	#     "parameters": [
	#         {
	#             "name": "image",
	#             "description": "Local path to a valid image."
	#         },
	#         {
	#             "name": "checksum",
	#             "description": "Local path to a md5 checksum file, or empty string for no verification"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "upgrade", [image, checksum])

def factoryReset(image:str, checksum:str) -> None:
	"""
	Flash the system image and erase the user data
	
	Parameters
	----------
	image:str
		Local path to a valid image.
	checksum:str
		Local path to a md5 checksum file, or empty string for no verification
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "factoryReset",
	#     "parametersSignature": "(ss)",
	#     "description": "Flash the system image and erase the user data",
	#     "parameters": [
	#         {
	#             "name": "image",
	#             "description": "Local path to a valid image."
	#         },
	#         {
	#             "name": "checksum",
	#             "description": "Local path to a md5 checksum file, or empty string for no verification"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "factoryReset", [image, checksum])

def _setStatusLed(state:int) -> None:
	"""
	Set the robot status LED
	
	Parameters
	----------
	state:int
		state to set
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_setStatusLed",
	#     "parametersSignature": "(i)",
	#     "description": "Set the robot status LED",
	#     "parameters": [
	#         {
	#             "name": "state",
	#             "description": "state to set"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "_setStatusLed", [state])

def _initializeSystemNotification() -> None:
	"""
	Load system notification and data
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "_initializeSystemNotification",
	#     "parametersSignature": "()",
	#     "description": "Load system notification and data",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "_initializeSystemNotification", [])

def _boardFirmwareUpdateError() -> List[str]:
	"""
	List of the faulty boards
	
	Returns
	----------
	A vector with the name of the faulty boards
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "[s]",
	#     "name": "_boardFirmwareUpdateError",
	#     "parametersSignature": "()",
	#     "description": "List of the faulty boards",
	#     "parameters": [],
	#     "returnDescription": "A vector with the name of the faulty boards"
	# }
	return call_method("ALSystem", "_boardFirmwareUpdateError", [])

def _prepareNaoqiStop() -> None:
	"""
	Execute operations for safe naoqi stop
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "_prepareNaoqiStop",
	#     "parametersSignature": "()",
	#     "description": "Execute operations for safe naoqi stop",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSystem", "_prepareNaoqiStop", [])

class _Signals:
	rebootRequested: Signal[[str]] = Signal("ALSystem", "rebootRequested")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	_rebootCompat: Signal[[]] = Signal("ALSystem", "_rebootCompat")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	shutdownRequested: Signal[[]] = Signal("ALSystem", "shutdownRequested")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	userDiskSpaceNearlyFull: Signal[[int]] = Signal("ALSystem", "userDiskSpaceNearlyFull")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	userDiskSpaceFull: Signal[[int]] = Signal("ALSystem", "userDiskSpaceFull")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(int) each time the robot sends it.
	"""
	userDiskError: Signal[[str]] = Signal("ALSystem", "userDiskError")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	systemUpdateSucceeded: Signal[[str]] = Signal("ALSystem", "systemUpdateSucceeded")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	systemUpdateFailed: Signal[[str]] = Signal("ALSystem", "systemUpdateFailed")
	"""
	Bridge notes
	------------
	A signal sent by ALSystem on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
signals = _Signals()

