"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class ServiceInfo:
	"""NAOqi signature: (sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>"""
	name: str
	serviceId: int
	machineId: str
	processId: int
	endpoints: List[str]
	sessionId: str


def service(p0:str) -> ServiceInfo:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "(sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>",
	#     "name": "service",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "service", [p0], returns=ServiceInfo)

def services() -> List[ServiceInfo]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "[(sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>]",
	#     "name": "services",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "services", [], returns=List[ServiceInfo])

def registerService(p0:ServiceInfo) -> int:
	"""
	
	
	Parameters
	----------
	p0:ServiceInfo
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "I",
	#     "name": "registerService",
	#     "parametersSignature": "((sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "registerService", [p0])

def unregisterService(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "unregisterService",
	#     "parametersSignature": "(I)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "unregisterService", [p0])

def serviceReady(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "serviceReady",
	#     "parametersSignature": "(I)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "serviceReady", [p0])

def updateServiceInfo(p0:ServiceInfo) -> None:
	"""
	
	
	Parameters
	----------
	p0:ServiceInfo
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "updateServiceInfo",
	#     "parametersSignature": "((sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "updateServiceInfo", [p0])

def machineId() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "s",
	#     "name": "machineId",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ServiceDirectory", "machineId", [])

class _Signals:
	serviceAdded: Signal[[int, str]] = Signal("ServiceDirectory", "serviceAdded")
	"""
	Bridge notes
	------------
	A signal sent by ServiceDirectory on the robot.
	
	subscribe(callback) calls callback(int, str) each time the robot sends it.
	"""
	serviceRemoved: Signal[[int, str]] = Signal("ServiceDirectory", "serviceRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ServiceDirectory on the robot.
	
	subscribe(callback) calls callback(int, str) each time the robot sends it.
	"""
signals = _Signals()

