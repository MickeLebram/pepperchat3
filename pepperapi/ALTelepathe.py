from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def connectNetwork() -> None:
	"""
	
	        Connect the Robot to the Jabber Server.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "v",
	    "name": "connectNetwork",
	    "parametersSignature": "()",
	    "description": "\n        Connect the Robot to the Jabber Server.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "connectNetwork", [])

def disconnectNetwork() -> None:
	"""
	
	        Disconnect the Robot from the Jabber Server.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "v",
	    "name": "disconnectNetwork",
	    "parametersSignature": "()",
	    "description": "\n        Disconnect the Robot from the Jabber Server.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "disconnectNetwork", [])

def isConnected() -> bool:
	"""
	
	        Return the Jabber Connection Status.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "b",
	    "name": "isConnected",
	    "parametersSignature": "()",
	    "description": "\n        Return the Jabber Connection Status.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "isConnected", [])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "s",
	    "name": "_package",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "b",
	    "name": "_ping",
	    "parametersSignature": "()",
	    "description": "\n        Return True if the Service is Running.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "v",
	    "name": "_unload",
	    "parametersSignature": "()",
	    "description": "\n        Stop the Service.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "s",
	    "name": "_version",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Version Number.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTelepathe", "_version", [])

