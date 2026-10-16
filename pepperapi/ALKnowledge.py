"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def add(p0:str, p1:str, p2:str, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "add",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "add", [p0, p1, p2, p3])

def getSubject(p0:str, p1:str, p2:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "[s]",
	#     "name": "getSubject",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "getSubject", [p0, p1, p2])

def getPredicate(p0:str, p1:str, p2:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "[s]",
	#     "name": "getPredicate",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "getPredicate", [p0, p1, p2])

def getObject(p0:str, p1:str, p2:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "[s]",
	#     "name": "getObject",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "getObject", [p0, p1, p2])

def update(p0:str, p1:str, p2:str, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "update",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "update", [p0, p1, p2, p3])

def query(p0:str, p1:str, p2:str, p3:str) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[s]",
	#     "name": "query",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "query", [p0, p1, p2, p3])

def queryTriplet(p0:str, p1:str, p2:str, p3:str) -> List[List[str]]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "[[s]]",
	#     "name": "queryTriplet",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "queryTriplet", [p0, p1, p2, p3])

def remove(p0:str, p1:str, p2:str, p3:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "remove",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "remove", [p0, p1, p2, p3])

def contains(p0:str, p1:str, p2:str, p3:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "contains",
	#     "parametersSignature": "(ssss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "contains", [p0, p1, p2, p3])

def addRule(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "b",
	#     "name": "addRule",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "addRule", [p0])

def clearRules() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "v",
	#     "name": "clearRules",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "clearRules", [])

def resetKnowledge(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "resetKnowledge",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "resetKnowledge", [p0])

def exportModel(p0:str, p1:str, p2:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "exportModel",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "exportModel", [p0, p1, p2])

def importModel(p0:str, p1:str, p2:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "v",
	#     "name": "importModel",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALKnowledge", "importModel", [p0, p1, p2])

@overload
def sparqlQuery(p0:str, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	sparqlQuery has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "[s]",
	#     "name": "sparqlQuery",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def sparqlQuery(p0:str, p1:bool, /) -> List[str]:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:bool
		
	
	Bridge notes
	------------
	sparqlQuery has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "[s]",
	#     "name": "sparqlQuery",
	#     "parametersSignature": "(sb)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def sparqlQuery(*args, **kwargs):
	"""
	Bridge notes
	------------
	sparqlQuery has 2 variants on the robot:
	- sparqlQuery(p0:str)
	- sparqlQuery(p0:str, p1:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALKnowledge.sparqlQuery has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALKnowledge", "sparqlQuery", list(args))

class _Signals:
	knowledgeAdded: Signal[[str, str, str, str]] = Signal("ALKnowledge", "knowledgeAdded")
	"""
	Bridge notes
	------------
	A signal sent by ALKnowledge on the robot.
	
	subscribe(callback) calls callback(str, str, str, str) each time the robot sends it.
	"""
	knowledgeRemoved: Signal[[str, str, str, str]] = Signal("ALKnowledge", "knowledgeRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALKnowledge on the robot.
	
	subscribe(callback) calls callback(str, str, str, str) each time the robot sends it.
	"""
signals = _Signals()

