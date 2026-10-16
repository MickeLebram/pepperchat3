"""
ALPreferences allows access to xml preference files. 
A preference is defined as follows : 
pParams[0] Name of the preference; 
pParams[1] Description of the preference; 
pParams[2] The value of the preference (can contain other preferences); 
pParams[3] (optional) The name of the data when inserted into memory.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
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
	return call_method("ALPreferences", "version", [])

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
	return call_method("ALPreferences", "ping", [])

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
	return call_method("ALPreferences", "getMethodList", [])

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
	return call_method("ALPreferences", "getMethodHelp", [methodName])

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
	return call_method("ALPreferences", "getModuleHelp", [])

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
	return call_method("ALPreferences", "getBrokerName", [])

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
	return call_method("ALPreferences", "getUsage", [name])

def readPrefFile(fileName:str, autoGenerateMemoryNames:bool) -> object:
	"""
	Reads all preferences from an xml files and stores them in an ALValue.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	autoGenerateMemoryNames:bool
		If true a memory name will be generated for each non-array preference.
	
	Returns
	----------
	array reprenting the whole file.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "m",
	#     "name": "readPrefFile",
	#     "parametersSignature": "(sb)",
	#     "description": "Reads all preferences from an xml files and stores them in an ALValue.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associated to the preference."
	#         },
	#         {
	#             "name": "autoGenerateMemoryNames",
	#             "description": "If true a memory name will be generated for each non-array preference."
	#         }
	#     ],
	#     "returnDescription": "array reprenting the whole file."
	# }
	return call_method("ALPreferences", "readPrefFile", [fileName, autoGenerateMemoryNames])

def writePrefFile(fileName:str, prefs:object, ignoreMemoryNames:bool) -> None:
	"""
	Writes all preferences from ALValue to an xml file.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	prefs:object
		array reprenting the whole file.
	ignoreMemoryNames:bool
		If true all memory names will be removed before saving.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "writePrefFile",
	#     "parametersSignature": "(smb)",
	#     "description": "Writes all preferences from ALValue to an xml file.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associated to the preference."
	#         },
	#         {
	#             "name": "prefs",
	#             "description": "array reprenting the whole file."
	#         },
	#         {
	#             "name": "ignoreMemoryNames",
	#             "description": "If true all memory names will be removed before saving."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferences", "writePrefFile", [fileName, prefs, ignoreMemoryNames])

def removePrefFile(fileName:str) -> None:
	"""
	Remove the xml file.
	
	Parameters
	----------
	fileName:str
		Name of the module associated to the preference.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "removePrefFile",
	#     "parametersSignature": "(s)",
	#     "description": "Remove the xml file.",
	#     "parameters": [
	#         {
	#             "name": "fileName",
	#             "description": "Name of the module associated to the preference."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferences", "removePrefFile", [fileName])

def saveToMemory(prefs:object) -> bool:
	"""
	Writes all preferences from ALValue to an xml file.
	
	Parameters
	----------
	prefs:object
		array representing the whole file.
	
	Returns
	----------
	True upon success.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "saveToMemory",
	#     "parametersSignature": "(m)",
	#     "description": "Writes all preferences from ALValue to an xml file.",
	#     "parameters": [
	#         {
	#             "name": "prefs",
	#             "description": "array representing the whole file."
	#         }
	#     ],
	#     "returnDescription": "True upon success."
	# }
	return call_method("ALPreferences", "saveToMemory", [prefs])

