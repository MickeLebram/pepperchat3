"""
ALModularityis a filter management system based on a filter graph.The users of this module can add, modify, delete or use filters that are stored in a library.
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
	return call_method("ALModularity", "version", [])

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
	return call_method("ALModularity", "ping", [])

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
	return call_method("ALModularity", "getMethodList", [])

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
	return call_method("ALModularity", "getMethodHelp", [methodName])

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
	return call_method("ALModularity", "getModuleHelp", [])

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
	return call_method("ALModularity", "getBrokerName", [])

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
	return call_method("ALModularity", "getUsage", [name])

def loadProgram(program:str) -> bool:
	"""
	
	
	Parameters
	----------
	program:str
		The code that will be used by Modularity to generate a part of the graph.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "loadProgram",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "program",
	#             "description": "The code that will be used by Modularity to generate a part of the graph."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "loadProgram", [program])

def loadProgramFromFile(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "loadProgramFromFile",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "loadProgramFromFile", [p0])

def getData(sink:str) -> Any:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "getData",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "sink",
	#             "description": "The name of the sink from where data must be extracted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getData", [sink])

def getLastData(sink:str) -> Any:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "getLastData",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "sink",
	#             "description": "The name of the sink from where data must be extracted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getLastData", [sink])

def getImageRemote(sink:str) -> Any:
	"""
	
	
	Parameters
	----------
	sink:str
		The name of the sink from where data must be extracted.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "m",
	#     "name": "getImageRemote",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "sink",
	#             "description": "The name of the sink from where data must be extracted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getImageRemote", [sink])

def getFilters() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "getFilters",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getFilters", [])

def getFilterDescription(name:str) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "s",
	#     "name": "getFilterDescription",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the filter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getFilterDescription", [name])

def getFilterInputs(name:str) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getFilterInputs",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the filter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getFilterInputs", [name])

def getFilterOutputs(name:str) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "getFilterOutputs",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the filter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getFilterOutputs", [name])

def deleteFilter(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the filter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "b",
	#     "name": "deleteFilter",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the filter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "deleteFilter", [name])

def getSources() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "getSources",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getSources", [])

def isSourceBinded(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "isSourceBinded",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the source."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "isSourceBinded", [name])

def getSourceFrequency(name:str) -> float:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "f",
	#     "name": "getSourceFrequency",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the source."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getSourceFrequency", [name])

@overload
def getSourceData(source:str, /) -> Any:
	"""
	
	
	Parameters
	----------
	source:str
		The name of the source from where data must be extracted.
	
	Bridge notes
	------------
	getSourceData has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "m",
	#     "name": "getSourceData",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "source",
	#             "description": "The name of the source from where data must be extracted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def getSourceData(source:str, p1:int, /) -> Any:
	"""
	
	
	Parameters
	----------
	source:str
		The name of the source from where data must be extracted.
	p1:int
		
	
	Bridge notes
	------------
	getSourceData has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "m",
	#     "name": "getSourceData",
	#     "parametersSignature": "(sl)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "source",
	#             "description": "The name of the source from where data must be extracted."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def getSourceData(*args, **kwargs):
	"""
	Bridge notes
	------------
	getSourceData has 2 variants on the robot:
	- getSourceData(source:str)
	- getSourceData(source:str, p1:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALModularity.getSourceData has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALModularity", "getSourceData", list(args))

def setData(name:str, value:Any) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	value:Any
		The new value to set.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "setData",
	#     "parametersSignature": "(sm)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the source."
	#         },
	#         {
	#             "name": "value",
	#             "description": "The new value to set."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "setData", [name, value])

def deleteSource(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the source.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "b",
	#     "name": "deleteSource",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the source."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "deleteSource", [name])

def getRobotHeightOffset() -> float:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "f",
	#     "name": "getRobotHeightOffset",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getRobotHeightOffset", [])

def setRobotHeightOffset(heightOffset:float) -> None:
	"""
	
	
	Parameters
	----------
	heightOffset:float
		Height Offset of the robot from the ground.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "setRobotHeightOffset",
	#     "parametersSignature": "(f)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "heightOffset",
	#             "description": "Height Offset of the robot from the ground."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "setRobotHeightOffset", [heightOffset])

def getProcesses() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "[s]",
	#     "name": "getProcesses",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcesses", [])

def isProcesses(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "isProcesses",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "isProcesses", [name])

def getProcessDescription(name:str) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "s",
	#     "name": "getProcessDescription",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessDescription", [name])

def getProcessSources(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "[s]",
	#     "name": "getProcessSources",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessSources", [name])

def getProcessSinks(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "[s]",
	#     "name": "getProcessSinks",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessSinks", [name])

def getProcessAggregatedSinks(name:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "[s]",
	#     "name": "getProcessAggregatedSinks",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessAggregatedSinks", [name])

def getProcessPriority(name:str) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "i",
	#     "name": "getProcessPriority",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessPriority", [name])

def getProcessFrequency(name:str) -> float:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "f",
	#     "name": "getProcessFrequency",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getProcessFrequency", [name])

def setProcessPriority(name:str, priority:int) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	priority:int
		The new priority of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "v",
	#     "name": "setProcessPriority",
	#     "parametersSignature": "(sI)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         },
	#         {
	#             "name": "priority",
	#             "description": "The new priority of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "setProcessPriority", [name, priority])

def setProcessFrequency(name:str, frequency:float) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	frequency:float
		The new frequency of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "setProcessFrequency",
	#     "parametersSignature": "(sf)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         },
	#         {
	#             "name": "frequency",
	#             "description": "The new frequency of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "setProcessFrequency", [name, frequency])

def setProcessTolerance(name:str, tolerance:int) -> None:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	tolerance:int
		The new tolerance of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "setProcessTolerance",
	#     "parametersSignature": "(sl)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         },
	#         {
	#             "name": "tolerance",
	#             "description": "The new tolerance of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "setProcessTolerance", [name, tolerance])

def resetProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process to reset.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "b",
	#     "name": "resetProcess",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process to reset."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "resetProcess", [name])

def isProcessEnable(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "b",
	#     "name": "isProcessEnable",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "isProcessEnable", [name])

def isProcessZombie(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "b",
	#     "name": "isProcessZombie",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "isProcessZombie", [name])

def enableProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "b",
	#     "name": "enableProcess",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "enableProcess", [name])

def disableProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "b",
	#     "name": "disableProcess",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "disableProcess", [name])

def deleteProcess(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		The name of the process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "b",
	#     "name": "deleteProcess",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the process."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "deleteProcess", [name])

def getScheduledJobs() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "[s]",
	#     "name": "getScheduledJobs",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getScheduledJobs", [])

def startScheduler() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "b",
	#     "name": "startScheduler",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "startScheduler", [])

def stopScheduler() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "b",
	#     "name": "stopScheduler",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "stopScheduler", [])

def getInstrumentationResult() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "s",
	#     "name": "getInstrumentationResult",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getInstrumentationResult", [])

def getDotGraph(filter:str, level:int) -> Any:
	"""
	
	
	Parameters
	----------
	filter:str
		The name of the filter to dump.
	level:int
		Maximum depth (-1 for unlimited depth)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "m",
	#     "name": "getDotGraph",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "filter",
	#             "description": "The name of the filter to dump."
	#         },
	#         {
	#             "name": "level",
	#             "description": "Maximum depth (-1 for unlimited depth)"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "getDotGraph", [filter, level])

def _startMotionWorker() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "v",
	#     "name": "_startMotionWorker",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "_startMotionWorker", [])

def _stopMotionWorker() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "_stopMotionWorker",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "_stopMotionWorker", [])

def _setMotionSource(sourceName:str, data:List[float]) -> None:
	"""
	
	
	Parameters
	----------
	sourceName:str
		Name of the source to update
	data:List[float]
		New value of the source
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "v",
	#     "name": "_setMotionSource",
	#     "parametersSignature": "(s[f])",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "sourceName",
	#             "description": "Name of the source to update"
	#         },
	#         {
	#             "name": "data",
	#             "description": "New value of the source"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "_setMotionSource", [sourceName, data])

def _setMotionSources(sourceNameList:List[str], dataList:List[List[float]]) -> None:
	"""
	
	
	Parameters
	----------
	sourceNameList:List[str]
		Name of the sources to update
	dataList:List[List[float]]
		New value of the sources
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "v",
	#     "name": "_setMotionSources",
	#     "parametersSignature": "([s][[f]])",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "sourceNameList",
	#             "description": "Name of the sources to update"
	#         },
	#         {
	#             "name": "dataList",
	#             "description": "New value of the sources"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALModularity", "_setMotionSources", [sourceNameList, dataList])

