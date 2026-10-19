"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class SentimentInfo:
	"""NAOqi signature: (ssiss)<SentimentInfo,author,sentiment,sentimentStrengh,recever,from>"""
	author: str
	sentiment: str
	sentimentStrengh: int
	recever: str
	from_: str = field(metadata={"key": "from"})


def _getLemma(p0:str, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "s",
	#     "name": "_getLemma",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_getLemma", [p0, p1])

def _analyze(p0:Any, p1:str, p2:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:Any
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "_analyze",
	#     "parametersSignature": "(mss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_analyze", [p0, p1, p2])

def _reformulate(p0:str, p1:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "s",
	#     "name": "_reformulate",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_reformulate", [p0, p1])

def _getLanguage(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "s",
	#     "name": "_getLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_getLanguage", [p0])

def _diagnosis() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "s",
	#     "name": "_diagnosis",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_diagnosis", [])

def _setMemoryConfiguration(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_setMemoryConfiguration",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALNaturalLanguageExtractor", "_setMemoryConfiguration", [p0])

class _Signals:
	_onReactionProposal: Signal[[str]] = Signal("_ALNaturalLanguageExtractor", "_onReactionProposal")
	"""
	Bridge notes
	------------
	A signal sent by _ALNaturalLanguageExtractor on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	onSentimentDetected: Signal[[SentimentInfo]] = Signal("_ALNaturalLanguageExtractor", "onSentimentDetected", (SentimentInfo,))
	"""
	Bridge notes
	------------
	A signal sent by _ALNaturalLanguageExtractor on the robot.
	
	subscribe(callback) calls callback(SentimentInfo) each time the robot sends it.
	"""
signals = _Signals()

