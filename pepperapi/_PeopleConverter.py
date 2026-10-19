"""
Generic Converter.
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
	return call_method("_PeopleConverter", "version", [])

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
	return call_method("_PeopleConverter", "ping", [])

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
	return call_method("_PeopleConverter", "getMethodList", [])

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
	return call_method("_PeopleConverter", "getMethodHelp", [methodName])

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
	return call_method("_PeopleConverter", "getModuleHelp", [])

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
	return call_method("_PeopleConverter", "getBrokerName", [])

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
	return call_method("_PeopleConverter", "getUsage", [name])

def setImplParam(p0:Any) -> None:
	"""
	Set the parameters to the converter.
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "setImplParam",
	#     "parametersSignature": "(m)",
	#     "description": "Set the parameters to the converter.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "setImplParam", [p0])

def start(p0:int) -> None:
	"""
	Start to work and raise the specified event.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "(i)",
	#     "description": "Start to work and raise the specified event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "start", [p0])

def stopConverter() -> None:
	"""
	Stop working.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "stopConverter",
	#     "parametersSignature": "()",
	#     "description": "Stop working.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "stopConverter", [])

def convert(p0:Any) -> Any:
	"""
	Convert.
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "convert",
	#     "parametersSignature": "(m)",
	#     "description": "Convert.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "convert", [p0])

def convertEvent(p0:str, p1:Any) -> None:
	"""
	Convert with event.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "convertEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Convert with event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "convertEvent", [p0, p1])

def updateDetectorPeriod(p0:int) -> None:
	"""
	update detector period
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "updateDetectorPeriod",
	#     "parametersSignature": "(i)",
	#     "description": "update detector period",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "updateDetectorPeriod", [p0])

def getDetectorPeriod() -> int:
	"""
	get detector period
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "getDetectorPeriod",
	#     "parametersSignature": "()",
	#     "description": "get detector period",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_PeopleConverter", "getDetectorPeriod", [])

