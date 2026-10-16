"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def getAccessToken() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "s",
	#     "name": "getAccessToken",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALCloudToken", "getAccessToken", [])

def refreshAccessToken() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "s",
	#     "name": "refreshAccessToken",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALCloudToken", "refreshAccessToken", [])

