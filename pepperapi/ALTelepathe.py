"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def connectNetwork() -> None:
	"""
	
	        Connect the Robot to the Jabber Server.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "v",
	#     "name": "connectNetwork",
	#     "parametersSignature": "()",
	#     "description": "\n        Connect the Robot to the Jabber Server.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "connectNetwork", [])

def disconnectNetwork() -> None:
	"""
	
	        Disconnect the Robot from the Jabber Server.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "disconnectNetwork",
	#     "parametersSignature": "()",
	#     "description": "\n        Disconnect the Robot from the Jabber Server.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "disconnectNetwork", [])

def isConnected() -> bool:
	"""
	
	        Return the Jabber Connection Status.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "isConnected",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Jabber Connection Status.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "isConnected", [])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "s",
	#     "name": "_package",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "_ping",
	#     "parametersSignature": "()",
	#     "description": "\n        Return True if the Service is Running.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "_unload",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop the Service.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "s",
	#     "name": "_version",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Version Number.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTelepathe", "_version", [])

class _Signals:
	connected: Signal[[bool]] = Signal("ALTelepathe", "connected")
	"""
	Bridge notes
	------------
	A signal sent by ALTelepathe on the robot.
	
	subscribe(callback) calls callback(bool) each time the robot sends it.
	"""
	messageReceived: Signal[[str, str]] = Signal("ALTelepathe", "messageReceived")
	"""
	Bridge notes
	------------
	A signal sent by ALTelepathe on the robot.
	
	subscribe(callback) calls callback(str, str) each time the robot sends it.
	"""
signals = _Signals()

