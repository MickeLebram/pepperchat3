"""
ALFileManager manages the user files stored in a shared folder.
Note that FileManager starts to look in the shared folder, and if it does not find anything,
then it looks in the data folder.
Shared folder can be changed on the fly, and module will then be able to say which
files are available in this folder, as well as return their complete path.
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

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
	return call_method("ALFileManager", "version", [])

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
	return call_method("ALFileManager", "ping", [])

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
	return call_method("ALFileManager", "getMethodList", [])

def getMethodHelp(methodName:str) -> Any:
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
	return call_method("ALFileManager", "getMethodHelp", [methodName])

def getModuleHelp() -> Any:
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
	return call_method("ALFileManager", "getModuleHelp", [])

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
	return call_method("ALFileManager", "getBrokerName", [])

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
	return call_method("ALFileManager", "getUsage", [name])

def setUserSharedFolderPath(fileName:str) -> None:
	"""
	Set a new value of the user shared folder path.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "setUserSharedFolderPath",
	#     "parametersSignature": "(s)",
	#     "description": "Set a new value of the user shared folder path.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associate to the preference."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALFileManager", "setUserSharedFolderPath", [fileName])

def getUserSharedFolderPath() -> str:
	"""
	Get the current user shared folder path.
	
	Returns
	----------
	User shared folder path string.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "s",
	#     "name": "getUserSharedFolderPath",
	#     "parametersSignature": "()",
	#     "description": "Get the current user shared folder path.",
	#     "parameters": [],
	#     "returnDescription": "User shared folder path string."
	# }
	return call_method("ALFileManager", "getUserSharedFolderPath", [])

def getSystemSharedFolderPath() -> str:
	"""
	Get the current system shared folder path.
	
	Returns
	----------
	System shared folder path string.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "s",
	#     "name": "getSystemSharedFolderPath",
	#     "parametersSignature": "()",
	#     "description": "Get the current system shared folder path.",
	#     "parameters": [],
	#     "returnDescription": "System shared folder path string."
	# }
	return call_method("ALFileManager", "getSystemSharedFolderPath", [])

def fileExists(fileName:str) -> bool:
	"""
	Try to find if this file does exist on robot or not.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	
	Returns
	----------
	True upon success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "fileExists",
	#     "parametersSignature": "(s)",
	#     "description": "Try to find if this file does exist on robot or not.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associate to the preference."
	#         }
	#     ],
	#     "returnDescription": "True upon success"
	# }
	return call_method("ALFileManager", "fileExists", [fileName])

def dataFileExists(fileName:str) -> bool:
	"""
	Try to find if this file does exist on robot or not.
	
	Parameters
	----------
	fileName:str
		Name of the module associate to the preference.
	
	Returns
	----------
	True upon success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "dataFileExists",
	#     "parametersSignature": "(s)",
	#     "description": "Try to find if this file does exist on robot or not.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associate to the preference."
	#         }
	#     ],
	#     "returnDescription": "True upon success"
	# }
	return call_method("ALFileManager", "dataFileExists", [fileName])

def getFileCompletePath(prefs:str) -> str:
	"""
	Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.
	
	Parameters
	----------
	prefs:str
		array reprenting the whole file.
	
	Returns
	----------
	True upon success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "s",
	#     "name": "getFileCompletePath",
	#     "parametersSignature": "(s)",
	#     "description": "Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.",
	#     "parameters": [
	#         {
	#             "name": "prefs",
	#             "description": "array reprenting the whole file."
	#         }
	#     ],
	#     "returnDescription": "True upon success"
	# }
	return call_method("ALFileManager", "getFileCompletePath", [prefs])

def getFileContents(prefs:str) -> Any:
	"""
	Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.
	
	Parameters
	----------
	prefs:str
		array reprenting the whole file.
	
	Returns
	----------
	True upon success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "m",
	#     "name": "getFileContents",
	#     "parametersSignature": "(s)",
	#     "description": "Returns the complete path of the file if it does exist. Starts by looking in user's shared folder, then in system folder.",
	#     "parameters": [
	#         {
	#             "name": "prefs",
	#             "description": "array reprenting the whole file."
	#         }
	#     ],
	#     "returnDescription": "True upon success"
	# }
	return call_method("ALFileManager", "getFileContents", [prefs])

def _getBehaviorsPath() -> str:
	"""
	Returns the path to the directory where behaviors are stored on the robot.
	
	Returns
	----------
	The behaviors path, as an UTF-8 encoded string.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "s",
	#     "name": "_getBehaviorsPath",
	#     "parametersSignature": "()",
	#     "description": "Returns the path to the directory where behaviors are stored on the robot.",
	#     "parameters": [],
	#     "returnDescription": "The behaviors path, as an UTF-8 encoded string."
	# }
	return call_method("ALFileManager", "_getBehaviorsPath", [])

def _getBoxLibrariesPath() -> str:
	"""
	Returns the path to the directory where box libraries are stored on the robot.
	
	Returns
	----------
	The box libraries path, as an UTF-8 encoded string.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "s",
	#     "name": "_getBoxLibrariesPath",
	#     "parametersSignature": "()",
	#     "description": "Returns the path to the directory where box libraries are stored on the robot.",
	#     "parameters": [],
	#     "returnDescription": "The box libraries path, as an UTF-8 encoded string."
	# }
	return call_method("ALFileManager", "_getBoxLibrariesPath", [])

