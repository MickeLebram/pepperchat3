"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def addTagForAnimations(p0:Dict[str,List[str]]) -> None:
	"""
	
	
	Parameters
	----------
	p0:Dict[str,List[str]]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "addTagForAnimations",
	#     "parametersSignature": "({s[s]})",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "addTagForAnimations", [p0])

def declarePathForTags(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "declarePathForTags",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "declarePathForTags", [p0])

def _declarePathForTagsPermanently(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "_declarePathForTagsPermanently",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "_declarePathForTagsPermanently", [p0])

def reset() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "reset",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "reset", [])

def _getPathsForTags() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "[s]",
	#     "name": "_getPathsForTags",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "_getPathsForTags", [])

@overload
def _getTags() -> List[str]:
	"""
	
	
	Bridge notes
	------------
	_getTags has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[s]",
	#     "name": "_getTags",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _getTags(p0:str, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	_getTags has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "[s]",
	#     "name": "_getTags",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _getTags(*args, **kwargs):
	"""
	Bridge notes
	------------
	_getTags has 2 variants on the robot:
	- _getTags()
	- _getTags(p0:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAnimationPlayer._getTags has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAnimationPlayer", "_getTags", list(args))

@overload
def _getAnimations() -> List[str]:
	"""
	
	
	Bridge notes
	------------
	_getAnimations has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "[s]",
	#     "name": "_getAnimations",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _getAnimations(p0:str, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	_getAnimations has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "[s]",
	#     "name": "_getAnimations",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _getAnimations(*args, **kwargs):
	"""
	Bridge notes
	------------
	_getAnimations has 2 variants on the robot:
	- _getAnimations()
	- _getAnimations(p0:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAnimationPlayer._getAnimations has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAnimationPlayer", "_getAnimations", list(args))

@overload
def _getAnimationsForTag(p0:str, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	_getAnimationsForTag has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "[s]",
	#     "name": "_getAnimationsForTag",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _getAnimationsForTag(p0:str, p1:str, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	_getAnimationsForTag has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "[s]",
	#     "name": "_getAnimationsForTag",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _getAnimationsForTag(*args, **kwargs):
	"""
	Bridge notes
	------------
	_getAnimationsForTag has 2 variants on the robot:
	- _getAnimationsForTag(p0:str)
	- _getAnimationsForTag(p0:str, p1:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAnimationPlayer._getAnimationsForTag has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAnimationPlayer", "_getAnimationsForTag", list(args))

def run(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "run",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALAnimationPlayer", "run", [p0])

@overload
def runTag(p0:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	runTag has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "runTag",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def runTag(p0:str, p1:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	runTag has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "v",
	#     "name": "runTag",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def runTag(*args, **kwargs):
	"""
	Bridge notes
	------------
	runTag has 2 variants on the robot:
	- runTag(p0:str)
	- runTag(p0:str, p1:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALAnimationPlayer.runTag has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALAnimationPlayer", "runTag", list(args))

