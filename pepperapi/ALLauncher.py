"""
ALlauncher allows to link dynamicaly with library, run executable, unload library, check if module is loaded...
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
	return call_method("ALLauncher", "version", [])

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
	return call_method("ALLauncher", "ping", [])

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
	return call_method("ALLauncher", "getMethodList", [])

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
	return call_method("ALLauncher", "getMethodHelp", [methodName])

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
	return call_method("ALLauncher", "getModuleHelp", [])

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
	return call_method("ALLauncher", "getBrokerName", [])

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
	return call_method("ALLauncher", "getUsage", [name])

def launchLocal(moduleName:str) -> List[str]:
	"""
	Loads dynamicaly a module
	
	Parameters
	----------
	moduleName:str
		the name of the module to launch or the name of the python script to evaluate
	
	Returns
	----------
	list of modules loaded
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "[s]",
	#     "name": "launchLocal",
	#     "parametersSignature": "(s)",
	#     "description": "Loads dynamicaly a module",
	#     "parameters": [
	#         {
	#             "name": "moduleName",
	#             "description": "the name of the module to launch or the name of the python script to evaluate"
	#         }
	#     ],
	#     "returnDescription": "list of modules loaded"
	# }
	return call_method("ALLauncher", "launchLocal", [moduleName])

def launchExecutable(moduleName:str) -> bool:
	"""
	runs an executable and connect it to current broker (executable)
	
	Parameters
	----------
	moduleName:str
		the name of the module to launch or the name of the script file to execute
	
	Returns
	----------
	true if ok
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "launchExecutable",
	#     "parametersSignature": "(s)",
	#     "description": "runs an executable and connect it to current broker (executable)",
	#     "parameters": [
	#         {
	#             "name": "moduleName",
	#             "description": "the name of the module to launch or the name of the script file to execute"
	#         }
	#     ],
	#     "returnDescription": "true if ok"
	# }
	return call_method("ALLauncher", "launchExecutable", [moduleName])

def _launch(executablePath:str, arguments:List[str]) -> int:
	"""
	runs an executable and connect it to current broker (executable)
	
	Parameters
	----------
	executablePath:str
		the name of the module to launch or the name of the script file to execute
	arguments:List[str]
		any optional argument to be passed to the executable.
	
	Returns
	----------
	the pid of the process spawned
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "i",
	#     "name": "_launch",
	#     "parametersSignature": "(s[s])",
	#     "description": "runs an executable and connect it to current broker (executable)",
	#     "parameters": [
	#         {
	#             "name": "executablePath",
	#             "description": "the name of the module to launch or the name of the script file to execute"
	#         },
	#         {
	#             "name": "arguments",
	#             "description": "any optional argument to be passed to the executable."
	#         }
	#     ],
	#     "returnDescription": "the pid of the process spawned"
	# }
	return call_method("ALLauncher", "_launch", [executablePath, arguments])

def _launchWait(executablePath:str, arguments:List[str]) -> int:
	"""
	Runs an executable with custom arguments, and waits for it to end.
	
	Parameters
	----------
	executablePath:str
		the name of the module to launch or the name of the script file to execute
	arguments:List[str]
		any optional argument to be passed to the executable.
	
	Returns
	----------
	the exit code of the program launched
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "_launchWait",
	#     "parametersSignature": "(s[s])",
	#     "description": "Runs an executable with custom arguments, and waits for it to end.",
	#     "parameters": [
	#         {
	#             "name": "executablePath",
	#             "description": "the name of the module to launch or the name of the script file to execute"
	#         },
	#         {
	#             "name": "arguments",
	#             "description": "any optional argument to be passed to the executable."
	#         }
	#     ],
	#     "returnDescription": "the exit code of the program launched"
	# }
	return call_method("ALLauncher", "_launchWait", [executablePath, arguments])

def launchScript(moduleName:str) -> bool:
	"""
	runs a script connected the current broker
	
	Parameters
	----------
	moduleName:str
		the name of the script to launch (python)
	
	Returns
	----------
	true if ok
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "b",
	#     "name": "launchScript",
	#     "parametersSignature": "(s)",
	#     "description": "runs a script connected the current broker",
	#     "parameters": [
	#         {
	#             "name": "moduleName",
	#             "description": "the name of the script to launch (python)"
	#         }
	#     ],
	#     "returnDescription": "true if ok"
	# }
	return call_method("ALLauncher", "launchScript", [moduleName])

def launchPythonModule(moduleName:str) -> bool:
	"""
	Import a python module
	
	Parameters
	----------
	moduleName:str
		the name of the module to launch
	
	Returns
	----------
	true if ok
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "launchPythonModule",
	#     "parametersSignature": "(s)",
	#     "description": "Import a python module",
	#     "parameters": [
	#         {
	#             "name": "moduleName",
	#             "description": "the name of the module to launch"
	#         }
	#     ],
	#     "returnDescription": "true if ok"
	# }
	return call_method("ALLauncher", "launchPythonModule", [moduleName])

def isModulePresent(strPartOfModuleName:str) -> bool:
	"""
	Tests the existence of an active module in the global system (in same executable or in another executable of the distributed system)
	
	Parameters
	----------
	strPartOfModuleName:str
		a part of the name of the module to test existence
	
	Returns
	----------
	the returned value is true if this module is present
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "b",
	#     "name": "isModulePresent",
	#     "parametersSignature": "(s)",
	#     "description": "Tests the existence of an active module in the global system (in same executable or in another executable of the distributed system)",
	#     "parameters": [
	#         {
	#             "name": "strPartOfModuleName",
	#             "description": "a part of the name of the module to test existence"
	#         }
	#     ],
	#     "returnDescription": "the returned value is true if this module is present"
	# }
	return call_method("ALLauncher", "isModulePresent", [strPartOfModuleName])

def getGlobalModuleList() -> List[str]:
	"""
	get the list of modules loaded on the robot and connected on the robot
	
	Returns
	----------
	array of present modules
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "[s]",
	#     "name": "getGlobalModuleList",
	#     "parametersSignature": "()",
	#     "description": "get the list of modules loaded on the robot and connected on the robot",
	#     "parameters": [],
	#     "returnDescription": "array of present modules"
	# }
	return call_method("ALLauncher", "getGlobalModuleList", [])

