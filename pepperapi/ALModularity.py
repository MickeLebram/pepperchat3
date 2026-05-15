from .gentypes import *
from .robot_client import send_mfc
import json
"""
ALModularityis a filter management system based on a filter graph.The users of this module can add, modify, delete or use filters that are stored in a library.
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
	return send_mfc("ALModularity", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALModularity", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALModularity", "metaObject", [p0])

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
	return send_mfc("ALModularity", "terminate", [p0])

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
	return send_mfc("ALModularity", "property", [p0])

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
	return send_mfc("ALModularity", "setProperty", [p0, p1])

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
	return send_mfc("ALModularity", "properties", [])

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
	return send_mfc("ALModularity", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALModularity", "isStatsEnabled", [])

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
	return send_mfc("ALModularity", "enableStats", [p0])

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
	return send_mfc("ALModularity", "stats", [])

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
	return send_mfc("ALModularity", "clearStats", [])

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
	return send_mfc("ALModularity", "isTraceEnabled", [])

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
	return send_mfc("ALModularity", "enableTrace", [p0])

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
	return send_mfc("ALModularity", "version", [])

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
	return send_mfc("ALModularity", "ping", [])

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
	return send_mfc("ALModularity", "getMethodList", [])

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
	return send_mfc("ALModularity", "getMethodHelp", [methodName])

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
	return send_mfc("ALModularity", "getModuleHelp", [])

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
	return send_mfc("ALModularity", "wait", [id, timeoutPeriod])

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
	return send_mfc("ALModularity", "wait", [id])

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
	return send_mfc("ALModularity", "isRunning", [id])

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
	return send_mfc("ALModularity", "stop", [id])

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
	return send_mfc("ALModularity", "getBrokerName", [])

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
	return send_mfc("ALModularity", "getUsage", [name])

def getModularity() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "X",
	    "name": "getModularity",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getModularity", [])

def loadProgram(program:str) -> bool:
	"""
	
	
	Parameters
	----------
	program:str
		The code that will be used by Modularity to generate a part of the graph.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "b",
	    "name": "loadProgram",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "program",
	            "description": "The code that will be used by Modularity to generate a part of the graph."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "loadProgram", [program])

def loadProgramFromFile(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "loadProgramFromFile",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "loadProgramFromFile", [p0])

def getData(sink:str) -> object:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "m",
	    "name": "getData",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sink",
	            "description": "The name of the sink from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getData", [sink])

def getLastData(sink:str) -> object:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "getLastData",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sink",
	            "description": "The name of the sink from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getLastData", [sink])

def getImageLocal(sink:str) -> object:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "X",
	    "name": "getImageLocal",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sink",
	            "description": "The name of the sink from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getImageLocal", [sink])

def getImageRemote(sink:str) -> object:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "getImageRemote",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sink",
	            "description": "The name of the sink from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getImageRemote", [sink])

def getFilters() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "m",
	    "name": "getFilters",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getFilters", [])

def getFilterDescription(name:str) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "s",
	    "name": "getFilterDescription",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the filter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getFilterDescription", [name])

def getFilterInputs(name:str) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "getFilterInputs",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the filter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getFilterInputs", [name])

def getFilterOutputs(name:str) -> object:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "getFilterOutputs",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the filter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getFilterOutputs", [name])

def deleteFilter(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "b",
	    "name": "deleteFilter",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the filter."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "deleteFilter", [name])

def getSources() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "[s]",
	    "name": "getSources",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getSources", [])

def isSourceBinded(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "isSourceBinded",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the source."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "isSourceBinded", [name])

def getSourceFrequency(name:str) -> float:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "f",
	    "name": "getSourceFrequency",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the source."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getSourceFrequency", [name])

def getSourceData_1(source:str) -> object:
	"""
	Note: This is one of the overloads of the original method (getSourceData)
	
	
	
	Parameters
	----------
	source:str
		The name of the source from where data must be extracted.
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "m",
	    "name": "getSourceData",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "source",
	            "description": "The name of the source from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getSourceData", [source])

def getSourceData_2(source:str, p1:int) -> object:
	"""
	Note: This is one of the overloads of the original method (getSourceData)
	
	
	
	Parameters
	----------
	source:str
		The name of the source from where data must be extracted.
	p1:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "m",
	    "name": "getSourceData",
	    "parametersSignature": "(sl)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "source",
	            "description": "The name of the source from where data must be extracted."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getSourceData", [source, p1])

def setData(name:str, value:object) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	value:object
		The new value to set.
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "v",
	    "name": "setData",
	    "parametersSignature": "(sm)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the source."
	        },
	        {
	            "name": "value",
	            "description": "The new value to set."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "setData", [name, value])

def deleteSource(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "b",
	    "name": "deleteSource",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the source."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "deleteSource", [name])

def getRobotHeightOffset() -> float:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "f",
	    "name": "getRobotHeightOffset",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getRobotHeightOffset", [])

def setRobotHeightOffset(heightOffset:float) -> None:
	"""
	
	
	Parameters
	----------
	heightOffset:float
		Height Offset of the robot from the ground.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "v",
	    "name": "setRobotHeightOffset",
	    "parametersSignature": "(f)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "heightOffset",
	            "description": "Height Offset of the robot from the ground."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "setRobotHeightOffset", [heightOffset])

def getProcesses() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "[s]",
	    "name": "getProcesses",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcesses", [])

def isProcesses(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "isProcesses",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "isProcesses", [name])

def getProcessDescription(name:str) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "s",
	    "name": "getProcessDescription",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessDescription", [name])

def getProcessSources(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "[s]",
	    "name": "getProcessSources",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessSources", [name])

def getProcessSinks(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 139,
	    "returnSignature": "[s]",
	    "name": "getProcessSinks",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessSinks", [name])

def getProcessAggregatedSinks(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 140,
	    "returnSignature": "[s]",
	    "name": "getProcessAggregatedSinks",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessAggregatedSinks", [name])

def getProcessPriority(name:str) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 141,
	    "returnSignature": "i",
	    "name": "getProcessPriority",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessPriority", [name])

def getProcessFrequency(name:str) -> float:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 142,
	    "returnSignature": "f",
	    "name": "getProcessFrequency",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getProcessFrequency", [name])

def setProcessPriority(name:str, priority:int) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	priority:int
		The new priority of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 143,
	    "returnSignature": "v",
	    "name": "setProcessPriority",
	    "parametersSignature": "(sI)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        },
	        {
	            "name": "priority",
	            "description": "The new priority of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "setProcessPriority", [name, priority])

def setProcessFrequency(name:str, frequency:float) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	frequency:float
		The new frequency of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 144,
	    "returnSignature": "v",
	    "name": "setProcessFrequency",
	    "parametersSignature": "(sf)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        },
	        {
	            "name": "frequency",
	            "description": "The new frequency of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "setProcessFrequency", [name, frequency])

def setProcessTolerance(name:str, tolerance:int) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	tolerance:int
		The new tolerance of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 145,
	    "returnSignature": "v",
	    "name": "setProcessTolerance",
	    "parametersSignature": "(sl)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        },
	        {
	            "name": "tolerance",
	            "description": "The new tolerance of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "setProcessTolerance", [name, tolerance])

def resetProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process to reset.
	
	*Reference struct*
	'''
	{
	    "uid": 146,
	    "returnSignature": "b",
	    "name": "resetProcess",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process to reset."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "resetProcess", [name])

def isProcessEnable(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 147,
	    "returnSignature": "b",
	    "name": "isProcessEnable",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "isProcessEnable", [name])

def isProcessZombie(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 148,
	    "returnSignature": "b",
	    "name": "isProcessZombie",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "isProcessZombie", [name])

def enableProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 149,
	    "returnSignature": "b",
	    "name": "enableProcess",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "enableProcess", [name])

def disableProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 150,
	    "returnSignature": "b",
	    "name": "disableProcess",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "disableProcess", [name])

def deleteProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	
	*Reference struct*
	'''
	{
	    "uid": 151,
	    "returnSignature": "b",
	    "name": "deleteProcess",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "name",
	            "description": "The name of the process."
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "deleteProcess", [name])

def getScheduledJobs() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 152,
	    "returnSignature": "[s]",
	    "name": "getScheduledJobs",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getScheduledJobs", [])

def startScheduler() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 153,
	    "returnSignature": "b",
	    "name": "startScheduler",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "startScheduler", [])

def stopScheduler() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 154,
	    "returnSignature": "b",
	    "name": "stopScheduler",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "stopScheduler", [])

def getInstrumentationResult() -> str:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 155,
	    "returnSignature": "s",
	    "name": "getInstrumentationResult",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getInstrumentationResult", [])

def getDotGraph(filter:str, level:int) -> object:
	"""
	
	
	Parameters
	----------
	filter:str
		The name of the filter to dump.
	level:int
		Maximum depth (-1 for unlimited depth)
	
	*Reference struct*
	'''
	{
	    "uid": 156,
	    "returnSignature": "m",
	    "name": "getDotGraph",
	    "parametersSignature": "(si)",
	    "description": "",
	    "parameters": [
	        {
	            "name": "filter",
	            "description": "The name of the filter to dump."
	        },
	        {
	            "name": "level",
	            "description": "Maximum depth (-1 for unlimited depth)"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "getDotGraph", [filter, level])

def _startMotionWorker() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 157,
	    "returnSignature": "v",
	    "name": "_startMotionWorker",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "_startMotionWorker", [])

def _stopMotionWorker() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 158,
	    "returnSignature": "v",
	    "name": "_stopMotionWorker",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "_stopMotionWorker", [])

def _setMotionSource(sourceName:str, data:List[float]) -> None:
	"""
	
	
	Parameters
	----------
	sourceName:str
		Name of the source to update
	data:List[float]
		New value of the source
	
	*Reference struct*
	'''
	{
	    "uid": 159,
	    "returnSignature": "v",
	    "name": "_setMotionSource",
	    "parametersSignature": "(s[f])",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sourceName",
	            "description": "Name of the source to update"
	        },
	        {
	            "name": "data",
	            "description": "New value of the source"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "_setMotionSource", [sourceName, data])

def _setMotionSources(sourceNameList:List[str], dataList:List[List[float]]) -> None:
	"""
	
	
	Parameters
	----------
	sourceNameList:List[str]
		Name of the sources to update
	dataList:List[List[float]]
		New value of the sources
	
	*Reference struct*
	'''
	{
	    "uid": 160,
	    "returnSignature": "v",
	    "name": "_setMotionSources",
	    "parametersSignature": "([s][[f]])",
	    "description": "",
	    "parameters": [
	        {
	            "name": "sourceNameList",
	            "description": "Name of the sources to update"
	        },
	        {
	            "name": "dataList",
	            "description": "New value of the sources"
	        }
	    ],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALModularity", "_setMotionSources", [sourceNameList, dataList])

