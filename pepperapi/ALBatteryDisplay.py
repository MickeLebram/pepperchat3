"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def hide() -> None:
	"""
	Hides the tablet.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "hide",
	#     "parametersSignature": "()",
	#     "description": "Hides the tablet.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBatteryDisplay", "hide", [])

def show() -> None:
	"""
	Shows battery level on tablet, for 10 seconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "show",
	#     "parametersSignature": "()",
	#     "description": "Shows battery level on tablet, for 10 seconds.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALBatteryDisplay", "show", [])

