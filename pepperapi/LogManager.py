"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method

@dataclass
class LogMessage:
	"""NAOqi signature: (sisssILL)<LogMessage,source,level,category,location,message,id,date,systemDate>"""
	source: str
	level: int
	category: str
	location: str
	message: str
	id: int
	date: int
	systemDate: int


def log(p0:List[LogMessage]) -> None:
	"""
	
	
	Parameters
	----------
	p0:List[LogMessage]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "log",
	#     "parametersSignature": "([(sisssILL)<LogMessage,source,level,category,location,message,id,date,systemDate>])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("LogManager", "log", [p0])

def removeProvider(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "removeProvider",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("LogManager", "removeProvider", [p0])

