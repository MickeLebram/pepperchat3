"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def decreaseVolume() -> bool:
	"""
	Decrease volume to next multiple of 20%.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "b",
	#     "name": "decreaseVolume",
	#     "parametersSignature": "()",
	#     "description": "Decrease volume to next multiple of 20%.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVolumeSlider", "decreaseVolume", [])

def hideTablet() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "hideTablet",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVolumeSlider", "hideTablet", [])

def increaseVolume() -> bool:
	"""
	Increase volume to next multiple of 20%.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "increaseVolume",
	#     "parametersSignature": "()",
	#     "description": "Increase volume to next multiple of 20%.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVolumeSlider", "increaseVolume", [])

def setVolume(p0:float) -> None:
	"""
	
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "setVolume",
	#     "parametersSignature": "(f)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVolumeSlider", "setVolume", [p0])

def showTablet(p0:int, p1:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "showTablet",
	#     "parametersSignature": "(ii)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVolumeSlider", "showTablet", [p0, p1])

