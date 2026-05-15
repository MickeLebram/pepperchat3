from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALlauncher allows to link dynamicaly with library, run executable, unload library, check if module is loaded...
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
	return send_mfc("ALLauncher", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALLauncher", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALLauncher", "metaObject", [p0])

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
	return send_mfc("ALLauncher", "terminate", [p0])

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
	return send_mfc("ALLauncher", "property", [p0])

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
	return send_mfc("ALLauncher", "setProperty", [p0, p1])

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
	return send_mfc("ALLauncher", "properties", [])

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
	return send_mfc("ALLauncher", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALLauncher", "isStatsEnabled", [])

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
	return send_mfc("ALLauncher", "enableStats", [p0])

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
	return send_mfc("ALLauncher", "stats", [])

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
	return send_mfc("ALLauncher", "clearStats", [])

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
	return send_mfc("ALLauncher", "isTraceEnabled", [])

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
	return send_mfc("ALLauncher", "enableTrace", [p0])

def version() -> str:
	"""
	Returns the version of the module.
	
	Returns
	----------
	A string containing the version of the module.
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "s",
	    "name": "version",
	    "parametersSignature": "()",
	    "description": "Returns the version of the module.",
	    "parameters": [],
	    "returnDescription": "A string containing the version of the module."
	}
	'''
	"""
	return send_mfc("ALLauncher", "version", [])

def ping() -> bool:
	"""
	Just a ping. Always returns true
	
	Returns
	----------
	returns true
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "b",
	    "name": "ping",
	    "parametersSignature": "()",
	    "description": "Just a ping. Always returns true",
	    "parameters": [],
	    "returnDescription": "returns true"
	}
	'''
	"""
	return send_mfc("ALLauncher", "ping", [])

def getMethodList() -> List[str]:
	"""
	Retrieves the module's method list.
	
	Returns
	----------
	An array of method names.
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "[s]",
	    "name": "getMethodList",
	    "parametersSignature": "()",
	    "description": "Retrieves the module's method list.",
	    "parameters": [],
	    "returnDescription": "An array of method names."
	}
	'''
	"""
	return send_mfc("ALLauncher", "getMethodList", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "m",
	    "name": "getMethodHelp",
	    "parametersSignature": "(s)",
	    "description": "Retrieves a method's description.",
	    "parameters": [
	        {
	            "name": "methodName",
	            "description": "The name of the method."
	        }
	    ],
	    "returnDescription": "A structure containing the method's description."
	}
	'''
	"""
	return send_mfc("ALLauncher", "getMethodHelp", [methodName])

def getModuleHelp() -> object:
	"""
	Retrieves the module's description.
	
	Returns
	----------
	A structure describing the module.
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "m",
	    "name": "getModuleHelp",
	    "parametersSignature": "()",
	    "description": "Retrieves the module's description.",
	    "parameters": [],
	    "returnDescription": "A structure describing the module."
	}
	'''
	"""
	return send_mfc("ALLauncher", "getModuleHelp", [])

def wait_1(id:int, timeoutPeriod:int) -> bool:
	"""
	Note: This is one of the overloads of the original method (wait)
	
	Wait for the end of a long running method that was called using 'post'
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	timeoutPeriod:int
		The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
	
	Returns
	----------
	True if the timeout period terminated. False if the method returned.
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "b",
	    "name": "wait",
	    "parametersSignature": "(ii)",
	    "description": "Wait for the end of a long running method that was called using 'post'",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        },
	        {
	            "name": "timeoutPeriod",
	            "description": "The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero."
	        }
	    ],
	    "returnDescription": "True if the timeout period terminated. False if the method returned."
	}
	'''
	"""
	return send_mfc("ALLauncher", "wait", [id, timeoutPeriod])

def wait_2(id:int) -> None:
	"""
	Note: This is one of the overloads of the original method (wait)
	
	Wait for the end of a long running method that was called using 'post', returns a cancelable future
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "v",
	    "name": "wait",
	    "parametersSignature": "(i)",
	    "description": "Wait for the end of a long running method that was called using 'post', returns a cancelable future",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLauncher", "wait", [id])

def isRunning(id:int) -> bool:
	"""
	Returns true if the method is currently running.
	
	Parameters
	----------
	id:int
		The ID of the method that was returned when calling the method using 'post'
	
	Returns
	----------
	True if the method is currently running
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "b",
	    "name": "isRunning",
	    "parametersSignature": "(i)",
	    "description": "Returns true if the method is currently running.",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "The ID of the method that was returned when calling the method using 'post'"
	        }
	    ],
	    "returnDescription": "True if the method is currently running"
	}
	'''
	"""
	return send_mfc("ALLauncher", "isRunning", [id])

def stop(id:int) -> None:
	"""
	returns true if the method is currently running
	
	Parameters
	----------
	id:int
		the ID of the method to wait for
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "stop",
	    "parametersSignature": "(i)",
	    "description": "returns true if the method is currently running",
	    "parameters": [
	        {
	            "name": "id",
	            "description": "the ID of the method to wait for"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALLauncher", "stop", [id])

def getBrokerName() -> str:
	"""
	Gets the name of the parent broker.
	
	Returns
	----------
	The name of the parent broker.
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "s",
	    "name": "getBrokerName",
	    "parametersSignature": "()",
	    "description": "Gets the name of the parent broker.",
	    "parameters": [],
	    "returnDescription": "The name of the parent broker."
	}
	'''
	"""
	return send_mfc("ALLauncher", "getBrokerName", [])

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
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "s",
	    "name": "getUsage",
	    "parametersSignature": "(s)",
	    "description": "Gets the method usage string. This summarises how to use the method.",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the method."
	        }
	    ],
	    "returnDescription": "A string that summarises the usage of the method."
	}
	'''
	"""
	return send_mfc("ALLauncher", "getUsage", [name])

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
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "[s]",
	    "name": "launchLocal",
	    "parametersSignature": "(s)",
	    "description": "Loads dynamicaly a module",
	    "parameters": [
	        {
	            "name": "moduleName",
	            "description": "the name of the module to launch or the name of the python script to evaluate"
	        }
	    ],
	    "returnDescription": "list of modules loaded"
	}
	'''
	"""
	return send_mfc("ALLauncher", "launchLocal", [moduleName])

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
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "launchExecutable",
	    "parametersSignature": "(s)",
	    "description": "runs an executable and connect it to current broker (executable)",
	    "parameters": [
	        {
	            "name": "moduleName",
	            "description": "the name of the module to launch or the name of the script file to execute"
	        }
	    ],
	    "returnDescription": "true if ok"
	}
	'''
	"""
	return send_mfc("ALLauncher", "launchExecutable", [moduleName])

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
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "i",
	    "name": "_launch",
	    "parametersSignature": "(s[s])",
	    "description": "runs an executable and connect it to current broker (executable)",
	    "parameters": [
	        {
	            "name": "executablePath",
	            "description": "the name of the module to launch or the name of the script file to execute"
	        },
	        {
	            "name": "arguments",
	            "description": "any optional argument to be passed to the executable."
	        }
	    ],
	    "returnDescription": "the pid of the process spawned"
	}
	'''
	"""
	return send_mfc("ALLauncher", "_launch", [executablePath, arguments])

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
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "i",
	    "name": "_launchWait",
	    "parametersSignature": "(s[s])",
	    "description": "Runs an executable with custom arguments, and waits for it to end.",
	    "parameters": [
	        {
	            "name": "executablePath",
	            "description": "the name of the module to launch or the name of the script file to execute"
	        },
	        {
	            "name": "arguments",
	            "description": "any optional argument to be passed to the executable."
	        }
	    ],
	    "returnDescription": "the exit code of the program launched"
	}
	'''
	"""
	return send_mfc("ALLauncher", "_launchWait", [executablePath, arguments])

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
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "b",
	    "name": "launchScript",
	    "parametersSignature": "(s)",
	    "description": "runs a script connected the current broker",
	    "parameters": [
	        {
	            "name": "moduleName",
	            "description": "the name of the script to launch (python)"
	        }
	    ],
	    "returnDescription": "true if ok"
	}
	'''
	"""
	return send_mfc("ALLauncher", "launchScript", [moduleName])

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
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "b",
	    "name": "launchPythonModule",
	    "parametersSignature": "(s)",
	    "description": "Import a python module",
	    "parameters": [
	        {
	            "name": "moduleName",
	            "description": "the name of the module to launch"
	        }
	    ],
	    "returnDescription": "true if ok"
	}
	'''
	"""
	return send_mfc("ALLauncher", "launchPythonModule", [moduleName])

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
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "b",
	    "name": "isModulePresent",
	    "parametersSignature": "(s)",
	    "description": "Tests the existence of an active module in the global system (in same executable or in another executable of the distributed system)",
	    "parameters": [
	        {
	            "name": "strPartOfModuleName",
	            "description": "a part of the name of the module to test existence"
	        }
	    ],
	    "returnDescription": "the returned value is true if this module is present"
	}
	'''
	"""
	return send_mfc("ALLauncher", "isModulePresent", [strPartOfModuleName])

def getGlobalModuleList() -> List[str]:
	"""
	get the list of modules loaded on the robot and connected on the robot
	
	Returns
	----------
	array of present modules
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "[s]",
	    "name": "getGlobalModuleList",
	    "parametersSignature": "()",
	    "description": "get the list of modules loaded on the robot and connected on the robot",
	    "parameters": [],
	    "returnDescription": "array of present modules"
	}
	'''
	"""
	return send_mfc("ALLauncher", "getGlobalModuleList", [])

