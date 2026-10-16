"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method

def services() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "m",
	#     "name": "services",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "services", [])

def service(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "service",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "service", [p0])

@overload
def scan() -> None:
	"""
	
	
	Bridge notes
	------------
	scan has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "scan",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def scan(p0:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	scan has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "v",
	#     "name": "scan",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def scan(*args, **kwargs):
	"""
	Bridge notes
	------------
	scan has 2 variants on the robot:
	- scan()
	- scan(p0:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALConnectionManager.scan has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALConnectionManager", "scan", list(args))

def setServiceConfiguration(p0:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "setServiceConfiguration",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "setServiceConfiguration", [p0])

def setServiceInput(p0:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "setServiceInput",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "setServiceInput", [p0])

def state() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "s",
	#     "name": "state",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "state", [])

def forget(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "forget",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "forget", [p0])

def connect(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "v",
	#     "name": "connect",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "connect", [p0])

def disconnect(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "v",
	#     "name": "disconnect",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "disconnect", [p0])

def technologies() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "m",
	#     "name": "technologies",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "technologies", [])

@overload
def enableTethering(p0:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	enableTethering has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "enableTethering",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def enableTethering(p0:str, p1:str, p2:str, /) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	Bridge notes
	------------
	enableTethering has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "enableTethering",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def enableTethering(*args, **kwargs):
	"""
	Bridge notes
	------------
	enableTethering has 2 variants on the robot:
	- enableTethering(p0:str)
	- enableTethering(p0:str, p1:str, p2:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALConnectionManager.enableTethering has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALConnectionManager", "enableTethering", list(args))

def disableTethering(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "v",
	#     "name": "disableTethering",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "disableTethering", [p0])

def getTetheringEnable(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "getTetheringEnable",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "getTetheringEnable", [p0])

def tetheringName(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "s",
	#     "name": "tetheringName",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "tetheringName", [p0])

def tetheringPassphrase(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "s",
	#     "name": "tetheringPassphrase",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "tetheringPassphrase", [p0])

def countries() -> List[str]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "[s]",
	#     "name": "countries",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "countries", [])

def setCountry(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "setCountry",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "setCountry", [p0])

def country() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "s",
	#     "name": "country",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "country", [])

def interfaces() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "m",
	#     "name": "interfaces",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "interfaces", [])

def provisionService(p0:Dict[str,str]) -> None:
	"""
	
	
	Parameters
	----------
	p0:Dict[str,str]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "provisionService",
	#     "parametersSignature": "({ss})",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "provisionService", [p0])

def provisionedServices() -> List[Dict[str,str]]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "[{ss}]",
	#     "name": "provisionedServices",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "provisionedServices", [])

def removeProvisionedService(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "removeProvisionedService",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALConnectionManager", "removeProvisionedService", [p0])

