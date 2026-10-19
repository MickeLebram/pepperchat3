"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method

@dataclass
class TaskInfo:
	"""NAOqi signature: (sibbb)<TaskInfo,priorityName,priorityValue,isContinuous,isEnabled,isRunning>"""
	priorityName: str
	priorityValue: int
	isContinuous: bool
	isEnabled: bool
	isRunning: bool


def printTasks() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "s",
	#     "name": "printTasks",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "printTasks", [])

def getTasks() -> List[TaskInfo]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "[(sibbb)<TaskInfo,priorityName,priorityValue,isContinuous,isEnabled,isRunning>]",
	#     "name": "getTasks",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "getTasks", [], returns=List[TaskInfo])

def reset() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "reset",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "reset", [])

def _inhibitAutonomousTasks(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "_inhibitAutonomousTasks",
	#     "parametersSignature": "(b)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "_inhibitAutonomousTasks", [p0])

def _subscribeToAutonomousTasksInhibitor() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "i",
	#     "name": "_subscribeToAutonomousTasksInhibitor",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "_subscribeToAutonomousTasksInhibitor", [])

def _unsubscribeToAutonomousTasksInhibitor(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_unsubscribeToAutonomousTasksInhibitor",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALMovementScheduler", "_unsubscribeToAutonomousTasksInhibitor", [p0])

