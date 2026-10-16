"""

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
	return call_method("ALPanoramaCompass", "version", [])

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
	return call_method("ALPanoramaCompass", "ping", [])

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
	return call_method("ALPanoramaCompass", "getMethodList", [])

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
	return call_method("ALPanoramaCompass", "getMethodHelp", [methodName])

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
	return call_method("ALPanoramaCompass", "getModuleHelp", [])

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
	return call_method("ALPanoramaCompass", "getBrokerName", [])

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
	return call_method("ALPanoramaCompass", "getUsage", [name])

def setupPanorama() -> int:
	"""
	Shoot a panorama at the current position.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "i",
	#     "name": "setupPanorama",
	#     "parametersSignature": "()",
	#     "description": "Shoot a panorama at the current position.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "setupPanorama", [])

def isDataAvailable() -> bool:
	"""
	Returns true if there is some panorama data
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "isDataAvailable",
	#     "parametersSignature": "()",
	#     "description": "Returns true if there is some panorama data",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "isDataAvailable", [])

def getCurrentPosition() -> object:
	"""
	Return the current orientation of the robot in the current panorama.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "getCurrentPosition",
	#     "parametersSignature": "()",
	#     "description": "Return the current orientation of the robot in the current panorama.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "getCurrentPosition", [])

def localizeNoHint() -> List[float]:
	"""
	Localize the robot using the scan,without hint.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "[f]",
	#     "name": "localizeNoHint",
	#     "parametersSignature": "()",
	#     "description": "Localize the robot using the scan,without hint.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "localizeNoHint", [])

@overload
def localize() -> List[float]:
	"""
	Localize the robot using the scan.
	
	Bridge notes
	------------
	localize has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- localize_1()
	- localize_2(bool)
	- localize_3(int)
	- localize_4(int, bool)
	
	Pass arguments by position, not by keyword.
	
	NAOqi's documentation lists a parameter (pMode) that the method's signature doesn't have. This function follows the signature and takes no arguments.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "()",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def localize(pMode:bool, /) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:bool
		Localization mode
	
	Bridge notes
	------------
	localize has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- localize_1()
	- localize_2(bool)
	- localize_3(int)
	- localize_4(int, bool)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(b)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def localize(pMode:int, /) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	
	Bridge notes
	------------
	localize has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- localize_1()
	- localize_2(bool)
	- localize_3(int)
	- localize_4(int, bool)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(i)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def localize(pMode:int, p1:bool, /) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	p1:bool
		
	
	Bridge notes
	------------
	localize has 4 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- localize_1()
	- localize_2(bool)
	- localize_3(int)
	- localize_4(int, bool)
	
	Pass arguments by position, not by keyword.
	
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(ib)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def localize(*args, **kwargs):
	"""
	Bridge notes
	------------
	localize has 4 variants on the robot:
	- localize(), explicitly localize_1
	- localize(pMode:bool), explicitly localize_2
	- localize(pMode:int), explicitly localize_3
	- localize(pMode:int, p1:bool), explicitly localize_4
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPanoramaCompass.localize has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPanoramaCompass", "localize", list(args))

def localize_1() -> List[float]:
	"""
	Localize the robot using the scan.
	
	Bridge notes
	------------
	Explicit variant of localize(). Calling localize instead lets the robot choose the variant from the argument types.
	
	NAOqi's documentation lists a parameter (pMode) that the method's signature doesn't have. This function follows the signature and takes no arguments.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "()",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "localize", [])

def localize_2(pMode:bool) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:bool
		Localization mode
	
	Bridge notes
	------------
	Explicit variant of localize(bool). Calling localize instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(b)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "localize", [pMode])

def localize_3(pMode:int) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	
	Bridge notes
	------------
	Explicit variant of localize(int). Calling localize instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(i)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "localize", [pMode])

def localize_4(pMode:int, p1:bool) -> List[float]:
	"""
	Localize the robot using the scan.
	
	Parameters
	----------
	pMode:int
		Localization mode
	p1:bool
		
	
	Bridge notes
	------------
	Explicit variant of localize(int, bool). Calling localize instead lets the robot choose the variant from the argument types.
	
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "[f]",
	#     "name": "localize",
	#     "parametersSignature": "(ib)",
	#     "description": "Localize the robot using the scan.",
	#     "parameters": [
	#         {
	#             "name": "pMode",
	#             "description": "Localization mode"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "localize", [pMode, p1])

@overload
def isInPanorama() -> int:
	"""
	Check if the robot is in the current Panorama.
	
	Returns
	----------
	Error status.
	
	Bridge notes
	------------
	isInPanorama has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "isInPanorama",
	#     "parametersSignature": "()",
	#     "description": "Check if the robot is in the current Panorama.",
	#     "parameters": [],
	#     "returnDescription": "Error status."
	# }
	...

@overload
def isInPanorama(p0:int, /) -> int:
	"""
	Check if the robot is in the current Panorama.
	
	Parameters
	----------
	p0:int
		
	
	Returns
	----------
	Error status.
	
	Bridge notes
	------------
	isInPanorama has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "i",
	#     "name": "isInPanorama",
	#     "parametersSignature": "(i)",
	#     "description": "Check if the robot is in the current Panorama.",
	#     "parameters": [],
	#     "returnDescription": "Error status."
	# }
	...

def isInPanorama(*args, **kwargs):
	"""
	Bridge notes
	------------
	isInPanorama has 2 variants on the robot:
	- isInPanorama()
	- isInPanorama(p0:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPanoramaCompass.isInPanorama has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPanoramaCompass", "isInPanorama", list(args))

def isRelocalizationRequired() -> bool:
	"""
	Is a relocalization movement required.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "b",
	#     "name": "isRelocalizationRequired",
	#     "parametersSignature": "()",
	#     "description": "Is a relocalization movement required.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "isRelocalizationRequired", [])

def loadPanorama(id:int) -> int:
	"""
	Load the panorama corresponding to the input identity from the hard drive. It has to exist.
	
	Parameters
	----------
	id:int
		Identity of the requested Panorama.
	
	Returns
	----------
	Error status.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "loadPanorama",
	#     "parametersSignature": "(i)",
	#     "description": "Load the panorama corresponding to the input identity from the hard drive. It has to exist.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Identity of the requested Panorama."
	#         }
	#     ],
	#     "returnDescription": "Error status."
	# }
	return call_method("ALPanoramaCompass", "loadPanorama", [id])

def getCurrentPanoramaDescriptor() -> object:
	"""
	
	
	Returns
	----------
	Return an ALValue containing Panorama identity and contained Frames identity.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "m",
	#     "name": "getCurrentPanoramaDescriptor",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": "Return an ALValue containing Panorama identity and contained Frames identity."
	# }
	return call_method("ALPanoramaCompass", "getCurrentPanoramaDescriptor", [])

def getFrame(id:int, p1:str) -> object:
	"""
	Return the Frame corresponding to the input identity. It have to be in the current Panorama
	
	Parameters
	----------
	id:int
		Identity of the resquested Frame.
	p1:str
		
	
	Returns
	----------
	ALValue containing the Frame image part.
	
	Bridge notes
	------------
	NAOqi's documentation only names 1 of 2 parameters. The others are called p1 here.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "m",
	#     "name": "getFrame",
	#     "parametersSignature": "(is)",
	#     "description": "Return the Frame corresponding to the input identity. It have to be in the current Panorama",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Identity of the resquested Frame."
	#         }
	#     ],
	#     "returnDescription": "ALValue containing the Frame image part."
	# }
	return call_method("ALPanoramaCompass", "getFrame", [id, p1])

@overload
def clearAllPanoramas() -> int:
	"""
	Delete all panorama files in the current working directory
	
	Bridge notes
	------------
	clearAllPanoramas has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "i",
	#     "name": "clearAllPanoramas",
	#     "parametersSignature": "()",
	#     "description": "Delete all panorama files in the current working directory",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def clearAllPanoramas(p0:bool, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	Bridge notes
	------------
	clearAllPanoramas has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "i",
	#     "name": "clearAllPanoramas",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def clearAllPanoramas(*args, **kwargs):
	"""
	Bridge notes
	------------
	clearAllPanoramas has 2 variants on the robot:
	- clearAllPanoramas()
	- clearAllPanoramas(p0:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALPanoramaCompass.clearAllPanoramas has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALPanoramaCompass", "clearAllPanoramas", list(args))

def clearPanorama(pIdentity:int) -> int:
	"""
	Delete all files related to a given panorama in the current working directory
	
	Parameters
	----------
	pIdentity:int
		Panorama identity
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "i",
	#     "name": "clearPanorama",
	#     "parametersSignature": "(i)",
	#     "description": "Delete all files related to a given panorama in the current working directory",
	#     "parameters": [
	#         {
	#             "name": "pIdentity",
	#             "description": "Panorama identity"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "clearPanorama", [pIdentity])

def _launchLocalization() -> List[float]:
	"""
	Forces the robot to localize using the scan.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "[f]",
	#     "name": "_launchLocalization",
	#     "parametersSignature": "()",
	#     "description": "Forces the robot to localize using the scan.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPanoramaCompass", "_launchLocalization", [])

