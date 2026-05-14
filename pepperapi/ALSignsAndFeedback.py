from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def _getBitsNames() -> List[str]:
	"""
	 Get all ExpressiveBits' names
	        
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "[s]",
	    "name": "_getBitsNames",
	    "parametersSignature": "()",
	    "description": " Get all ExpressiveBits' names\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSignsAndFeedback", "_getBitsNames", [])

def _getStates() -> List[str]:
	"""
	 Get the last triggered Recipes
	        
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "[s]",
	    "name": "_getStates",
	    "parametersSignature": "()",
	    "description": " Get the last triggered Recipes\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSignsAndFeedback", "_getStates", [])

def _resetConfiguration() -> None:
	"""
	 Reset the configuration using default configuration file
	        
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "v",
	    "name": "_resetConfiguration",
	    "parametersSignature": "()",
	    "description": " Reset the configuration using default configuration file\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSignsAndFeedback", "_resetConfiguration", [])

def _setConfiguration(p0:str) -> None:
	"""
	 Set the path for the yaml configuration file and set the
	            signs and feedback behaviors and triggers accordingly
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "v",
	    "name": "_setConfiguration",
	    "parametersSignature": "(s)",
	    "description": " Set the path for the yaml configuration file and set the\n            signs and feedback behaviors and triggers accordingly\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSignsAndFeedback", "_setConfiguration", [p0])

def triggerBit(p0:str) -> None:
	"""
	 Trigger one of the expressive_bits specified in the configuration
	            the argument can be a bit name or a recipe name. This is a blocking
	            call.
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "v",
	    "name": "triggerBit",
	    "parametersSignature": "(s)",
	    "description": " Trigger one of the expressive_bits specified in the configuration\n            the argument can be a bit name or a recipe name. This is a blocking\n            call.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALSignsAndFeedback", "triggerBit", [p0])

