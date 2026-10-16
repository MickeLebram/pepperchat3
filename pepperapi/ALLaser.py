"""
Allow control over Hokuyo laser when available on Nao's head.
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
	return call_method("ALLaser", "version", [])

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
	return call_method("ALLaser", "ping", [])

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
	return call_method("ALLaser", "getMethodList", [])

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
	return call_method("ALLaser", "getMethodHelp", [methodName])

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
	return call_method("ALLaser", "getModuleHelp", [])

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
	return call_method("ALLaser", "getBrokerName", [])

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
	return call_method("ALLaser", "getUsage", [name])

def laserOFF() -> None:
	"""
	Disable laser light
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "laserOFF",
	#     "parametersSignature": "()",
	#     "description": "Disable laser light",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLaser", "laserOFF", [])

def laserON() -> None:
	"""
	Enable laser light and sampling
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "laserON",
	#     "parametersSignature": "()",
	#     "description": "Enable laser light and sampling",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALLaser", "laserON", [])

def setOpeningAngle(angle_min_f:float, angle_max_f:float) -> None:
	"""
	Set openning angle of the laser
	
	Parameters
	----------
	angle_min_f:float
		float containing the min value in rad, this value must be upper than -2.35619449 
	angle_max_f:float
		float containing the max value in rad, this value must be lower than 2.092349795 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "setOpeningAngle",
	#     "parametersSignature": "(ff)",
	#     "description": "Set openning angle of the laser",
	#     "parameters": [
	#         {
	#             "name": "angle_min_f",
	#             "description": "float containing the min value in rad, this value must be upper than -2.35619449 "
	#         },
	#         {
	#             "name": "angle_max_f",
	#             "description": "float containing the max value in rad, this value must be lower than 2.092349795 "
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLaser", "setOpeningAngle", [angle_min_f, angle_max_f])

def setDetectingLength(length_min_l:int, length_max_l:int) -> None:
	"""
	Set detection threshold of the laser
	
	Parameters
	----------
	length_min_l:int
		int containing the min length that the laser will detect(mm), this value must be upper than 20 mm
	length_max_l:int
		int containing the max length that the laser will detect(mm), this value must be lower than 5600 mm
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "setDetectingLength",
	#     "parametersSignature": "(ii)",
	#     "description": "Set detection threshold of the laser",
	#     "parameters": [
	#         {
	#             "name": "length_min_l",
	#             "description": "int containing the min length that the laser will detect(mm), this value must be upper than 20 mm"
	#         },
	#         {
	#             "name": "length_max_l",
	#             "description": "int containing the max length that the laser will detect(mm), this value must be lower than 5600 mm"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALLaser", "setDetectingLength", [length_min_l, length_max_l])

