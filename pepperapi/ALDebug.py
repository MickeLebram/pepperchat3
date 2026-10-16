"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def _stopOneThread() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "_stopOneThread",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_stopOneThread", [])

def _dumpPythonTraces() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "s",
	#     "name": "_dumpPythonTraces",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_dumpPythonTraces", [])

def _makeMinidump() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "_makeMinidump",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_makeMinidump", [])

def _probesInit(p0:bool, p1:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "_probesInit",
	#     "parametersSignature": "(bi)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesInit", [p0, p1])

def _probesRecordSnapshot() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "_probesRecordSnapshot",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesRecordSnapshot", [])

def _probesSetTrigger(p0:str, p1:str, p2:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_probesSetTrigger",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesSetTrigger", [p0, p1, p2])

def _probesRemoveTrigger(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "_probesRemoveTrigger",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesRemoveTrigger", [p0])

def _probesStartTrigger() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "_probesStartTrigger",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesStartTrigger", [])

def _probesStopTrigger() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "v",
	#     "name": "_probesStopTrigger",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALDebug", "_probesStopTrigger", [])

