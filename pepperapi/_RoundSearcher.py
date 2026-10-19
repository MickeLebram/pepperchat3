"""
Generic Searcher.
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
	return call_method("_RoundSearcher", "version", [])

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
	return call_method("_RoundSearcher", "ping", [])

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
	return call_method("_RoundSearcher", "getMethodList", [])

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
	return call_method("_RoundSearcher", "getMethodHelp", [methodName])

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
	return call_method("_RoundSearcher", "getModuleHelp", [])

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
	return call_method("_RoundSearcher", "getBrokerName", [])

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
	return call_method("_RoundSearcher", "getUsage", [name])

def startEvent() -> None:
	"""
	Start to work and raise the specified event.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startEvent",
	#     "parametersSignature": "()",
	#     "description": "Start to work and raise the specified event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "startEvent", [])

def stopSearcher() -> None:
	"""
	Stop working.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "stopSearcher",
	#     "parametersSignature": "()",
	#     "description": "Stop working.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "stopSearcher", [])

def search(p0:Any) -> None:
	"""
	Search.
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "search",
	#     "parametersSignature": "(m)",
	#     "description": "Search.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "search", [p0])

def searchEvent(p0:str, p1:Any) -> None:
	"""
	Search with event.
	
	Parameters
	----------
	p0:str
		
	p1:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "searchEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Search with event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "searchEvent", [p0, p1])

def _stopMove() -> None:
	"""
	Stop searching
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "_stopMove",
	#     "parametersSignature": "()",
	#     "description": "Stop searching",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "_stopMove", [])

def setUseWholeBodyLookAt(p0:bool) -> None:
	"""
	enable whole body look at for search
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "setUseWholeBodyLookAt",
	#     "parametersSignature": "(b)",
	#     "description": "enable whole body look at for search",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "setUseWholeBodyLookAt", [p0])

def setFractionMaxSpeed(p0:float) -> None:
	"""
	Set a fraction max speed for search.
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setFractionMaxSpeed",
	#     "parametersSignature": "(f)",
	#     "description": "Set a fraction max speed for search.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "setFractionMaxSpeed", [p0])

def getFractionMaxSpeed() -> float:
	"""
	Get the fraction max speed for search.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "f",
	#     "name": "getFractionMaxSpeed",
	#     "parametersSignature": "()",
	#     "description": "Get the fraction max speed for search.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "getFractionMaxSpeed", [])

def initialize() -> None:
	"""
	Initialize the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "initialize",
	#     "parametersSignature": "()",
	#     "description": "Initialize the module.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_RoundSearcher", "initialize", [])

