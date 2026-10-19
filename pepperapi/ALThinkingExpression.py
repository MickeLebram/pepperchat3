"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def _startActivity(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "_startActivity",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "_startActivity", [p0])

def start() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "start", [])

def stop() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "stop",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "stop", [])

def isRunning() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "b",
	#     "name": "isRunning",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "isRunning", [])

def _getLoadingResponseToSay(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "s",
	#     "name": "_getLoadingResponseToSay",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "_getLoadingResponseToSay", [p0])

def _onPreferenceUpdated(p0:Any) -> None:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceUpdated",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "_onPreferenceUpdated", [p0])

def _onPreferenceSynchronized(p0:Any) -> None:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "_onPreferenceSynchronized",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "_onPreferenceSynchronized", [p0])

def _refCount() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "i",
	#     "name": "_refCount",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALThinkingExpression", "_refCount", [])

