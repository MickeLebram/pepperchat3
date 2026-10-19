"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def _getBitsNames() -> List[str]:
	"""
	 Get all ExpressiveBits' names
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "[s]",
	#     "name": "_getBitsNames",
	#     "parametersSignature": "()",
	#     "description": " Get all ExpressiveBits' names\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSignsAndFeedback", "_getBitsNames", [])

def _getStates() -> List[str]:
	"""
	 Get the last triggered Recipes
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "[s]",
	#     "name": "_getStates",
	#     "parametersSignature": "()",
	#     "description": " Get the last triggered Recipes\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSignsAndFeedback", "_getStates", [])

def _resetConfiguration() -> None:
	"""
	 Reset the configuration using default configuration file
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "_resetConfiguration",
	#     "parametersSignature": "()",
	#     "description": " Reset the configuration using default configuration file\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSignsAndFeedback", "_resetConfiguration", [])

def _setConfiguration(p0:str) -> None:
	"""
	 Set the path for the yaml configuration file and set the
	            signs and feedback behaviors and triggers accordingly
	        
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "_setConfiguration",
	#     "parametersSignature": "(s)",
	#     "description": " Set the path for the yaml configuration file and set the\n            signs and feedback behaviors and triggers accordingly\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSignsAndFeedback", "_setConfiguration", [p0])

def triggerBit(p0:str) -> None:
	"""
	 Trigger one of the expressive_bits specified in the configuration
	            the argument can be a bit name or a recipe name. This is a blocking
	            call.
	        
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "triggerBit",
	#     "parametersSignature": "(s)",
	#     "description": " Trigger one of the expressive_bits specified in the configuration\n            the argument can be a bit name or a recipe name. This is a blocking\n            call.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSignsAndFeedback", "triggerBit", [p0])

