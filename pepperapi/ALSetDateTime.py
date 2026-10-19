"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def askDateTime(p0:Any, p1:Any, p2:Any) -> Any:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	p1:Any
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "m",
	#     "name": "askDateTime",
	#     "parametersSignature": "(mmm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSetDateTime", "askDateTime", [p0, p1, p2])

def getData(p0:Any) -> Any:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "getData",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSetDateTime", "getData", [p0])

def removeData(p0:Any) -> Any:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "removeData",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSetDateTime", "removeData", [p0])

def removeValues() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "removeValues",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSetDateTime", "removeValues", [])

def setDateTime() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "m",
	#     "name": "setDateTime",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALSetDateTime", "setDateTime", [])

