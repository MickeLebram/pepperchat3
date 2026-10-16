"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class RecognitionMatch:
	"""NAOqi signature: (Lfi)<RecognitionMatch,value,confidence,storage>"""
	value: int
	confidence: float
	storage: int


@dataclass
class RecognitionResult:
	"""NAOqi signature: (i[RecognitionMatch])<RecognitionResult,status,matches>"""
	status: int
	matches: List[RecognitionMatch]


@overload
def match(p0:int, /) -> RecognitionResult:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	match has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- match_int(int)
	- match_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "(i[(Lfi)<RecognitionMatch,value,confidence,storage>])<RecognitionResult,status,matches>",
	#     "name": "match",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def match(p0:str, /) -> RecognitionResult:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	match has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- match_int(int)
	- match_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "(i[(Lfi)<RecognitionMatch,value,confidence,storage>])<RecognitionResult,status,matches>",
	#     "name": "match",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def match(*args, **kwargs):
	"""
	Bridge notes
	------------
	match has 2 variants on the robot:
	- match(p0:int), explicitly match_int
	- match(p0:str), explicitly match_str
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_UserIdentification.match has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_UserIdentification", "match", list(args), returns=RecognitionResult)

def match_int(p0:int) -> RecognitionResult:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	Bridge notes
	------------
	Explicit variant of match(int). Calling match instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "(i[(Lfi)<RecognitionMatch,value,confidence,storage>])<RecognitionResult,status,matches>",
	#     "name": "match",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "match", [p0], returns=RecognitionResult)

def match_str(p0:str) -> RecognitionResult:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	Explicit variant of match(str). Calling match instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "(i[(Lfi)<RecognitionMatch,value,confidence,storage>])<RecognitionResult,status,matches>",
	#     "name": "match",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "match", [p0], returns=RecognitionResult)

@overload
def store(p0:int, p1:int, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	
	Bridge notes
	------------
	store has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- store_int(int, int)
	- store_str(str, int)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "i",
	#     "name": "store",
	#     "parametersSignature": "(iL)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def store(p0:str, p1:int, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	Bridge notes
	------------
	store has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- store_int(int, int)
	- store_str(str, int)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "i",
	#     "name": "store",
	#     "parametersSignature": "(sL)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def store(*args, **kwargs):
	"""
	Bridge notes
	------------
	store has 2 variants on the robot:
	- store(p0:int, p1:int), explicitly store_int
	- store(p0:str, p1:int), explicitly store_str
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_UserIdentification.store has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_UserIdentification", "store", list(args))

def store_int(p0:int, p1:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	
	Bridge notes
	------------
	Explicit variant of store(int, int). Calling store instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "i",
	#     "name": "store",
	#     "parametersSignature": "(iL)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "store", [p0, p1])

def store_str(p0:str, p1:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	Bridge notes
	------------
	Explicit variant of store(str, int). Calling store instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "i",
	#     "name": "store",
	#     "parametersSignature": "(sL)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "store", [p0, p1])

def makePermanent(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "makePermanent",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "makePermanent", [p0])

def makeTemporary(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "b",
	#     "name": "makeTemporary",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "makeTemporary", [p0])

def remove(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "b",
	#     "name": "remove",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "remove", [p0])

def clear() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "b",
	#     "name": "clear",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "clear", [])

def isPermanent(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "isPermanent",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "isPermanent", [p0])

def isTemporary(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "b",
	#     "name": "isTemporary",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "isTemporary", [p0])

def getStoredUsers() -> List[int]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "[L]",
	#     "name": "getStoredUsers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "getStoredUsers", [])

def checkPhotoForIdentification(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "i",
	#     "name": "checkPhotoForIdentification",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "checkPhotoForIdentification", [p0])

def _getImageMTM(p0:int) -> str:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "s",
	#     "name": "_getImageMTM",
	#     "parametersSignature": "(L)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "_getImageMTM", [p0])

def _printDatabase() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "v",
	#     "name": "_printDatabase",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_UserIdentification", "_printDatabase", [])

class _Properties:
	faceRecognitionThreshold: Property[float] = Property("_UserIdentification", "faceRecognitionThreshold")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	maxRetryRecognition: Property[int] = Property("_UserIdentification", "maxRetryRecognition")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	retryRecognitionDelay: Property[int] = Property("_UserIdentification", "retryRecognitionDelay")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	enableImageFiltering: Property[bool] = Property("_UserIdentification", "enableImageFiltering")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(bool) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	maximumHeadYawDegree: Property[float] = Property("_UserIdentification", "maximumHeadYawDegree")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	maximumHeadPitchDegree: Property[float] = Property("_UserIdentification", "maximumHeadPitchDegree")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	maximumHeadRollDegree: Property[float] = Property("_UserIdentification", "maximumHeadRollDegree")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	filterNonFrontalFaces: Property[bool] = Property("_UserIdentification", "filterNonFrontalFaces")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(bool) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	minimumHeadSizePixel: Property[int] = Property("_UserIdentification", "minimumHeadSizePixel")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	minimumFacialPartsAvgConfidence: Property[float] = Property("_UserIdentification", "minimumFacialPartsAvgConfidence")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(float) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	filterCameraMovements: Property[bool] = Property("_UserIdentification", "filterCameraMovements")
	"""
	Bridge notes
	------------
	A property of _UserIdentification on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(bool) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

