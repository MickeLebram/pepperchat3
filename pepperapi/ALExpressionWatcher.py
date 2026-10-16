"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def _start() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "_start",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALExpressionWatcher", "_start", [])

def _stop() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "_stop",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALExpressionWatcher", "_stop", [])

def _isStarted() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "_isStarted",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALExpressionWatcher", "_isStarted", [])

def _listReactor() -> Dict[int,str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "{Is}",
	#     "name": "_listReactor",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALExpressionWatcher", "_listReactor", [])

def _purgeAll() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "_purgeAll",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALExpressionWatcher", "_purgeAll", [])

