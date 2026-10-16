"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class ServiceProcessInfo:
	"""NAOqi signature: (bssb)<ServiceProcessInfo,running,name,execStart,autorun>"""
	running: bool
	name: str
	execStart: str
	autorun: bool


def start(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "start",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "start", [p0])

def restart(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "restart",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "restart", [p0])

def stop(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "stop",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "stop", [p0])

def stopAllServices() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "stopAllServices",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "stopAllServices", [])

def isServiceRunning(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "isServiceRunning",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "isServiceRunning", [p0])

def serviceMemoryUsage(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "I",
	#     "name": "serviceMemoryUsage",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "serviceMemoryUsage", [p0])

def services() -> List[ServiceProcessInfo]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "[(bssb)<ServiceProcessInfo,running,name,execStart,autorun>]",
	#     "name": "services",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "services", [], returns=List[ServiceProcessInfo])

def service(p0:str) -> ServiceProcessInfo:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "(bssb)<ServiceProcessInfo,running,name,execStart,autorun>",
	#     "name": "service",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "service", [p0], returns=ServiceProcessInfo)

def startService(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "b",
	#     "name": "startService",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "startService", [p0])

def restartService(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "b",
	#     "name": "restartService",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "restartService", [p0])

def stopService(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "b",
	#     "name": "stopService",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALServiceManager", "stopService", [p0])

class _Signals:
	serviceStarted: Signal[[str, int]] = Signal("ALServiceManager", "serviceStarted")
	"""
	Bridge notes
	------------
	A signal sent by ALServiceManager on the robot.
	
	subscribe(callback) calls callback(str, int) each time the robot sends it.
	"""
	serviceStopped: Signal[[str, int]] = Signal("ALServiceManager", "serviceStopped")
	"""
	Bridge notes
	------------
	A signal sent by ALServiceManager on the robot.
	
	subscribe(callback) calls callback(str, int) each time the robot sends it.
	"""
signals = _Signals()

