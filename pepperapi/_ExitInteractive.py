"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def start() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ExitInteractive", "start", [])

def stop() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "stop",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ExitInteractive", "stop", [])

def isRunning() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "isRunning",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ExitInteractive", "isRunning", [])

class _Properties:
	timeout: Property[int] = Property("_ExitInteractive", "timeout")
	"""
	Bridge notes
	------------
	A property of _ExitInteractive on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

