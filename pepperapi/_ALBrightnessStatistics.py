"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def _start() -> None:
	"""
	Start ALBrightnessStatistics extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "_start",
	#     "parametersSignature": "()",
	#     "description": "Start ALBrightnessStatistics extractor",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALBrightnessStatistics", "_start", [])

def _stop() -> None:
	"""
	Stop ALBrightnessStatistics extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "_stop",
	#     "parametersSignature": "()",
	#     "description": "Stop ALBrightnessStatistics extractor",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALBrightnessStatistics", "_stop", [])

def _isStarted() -> bool:
	"""
	Check if ALBrightnessStatistics extractor is running
	
	Returns
	----------
	True if extractor is running
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "_isStarted",
	#     "parametersSignature": "()",
	#     "description": "Check if ALBrightnessStatistics extractor is running",
	#     "parameters": [],
	#     "returnDescription": "True if extractor is running"
	# }
	return call_method("_ALBrightnessStatistics", "_isStarted", [])

class _Signals:
	_statistics: Signal[[Dict[str,float]]] = Signal("_ALBrightnessStatistics", "_statistics")
	"""
	Bridge notes
	------------
	A signal sent by _ALBrightnessStatistics on the robot.
	
	subscribe(callback) calls callback(Dict[str,float]) each time the robot sends it.
	"""
signals = _Signals()

