"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def getEnvironment() -> str:
	"""
	
	        Return the Current Environment (int, qa, ppd, or prod).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "s",
	#     "name": "getEnvironment",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Current Environment (int, qa, ppd, or prod).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "getEnvironment", [])

def setEnvironment(env:str) -> bool:
	"""
	
	        Set the Active Environment (int, qa, ppd, or prod).
	
	Parameters
	----------
	env:str
		Requested Environment (int, qa, ppd, or prod)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "b",
	#     "name": "setEnvironment",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Set the Active Environment (int, qa, ppd, or prod).\n            :param env: Requested Environment (int, qa, ppd, or prod)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "setEnvironment", [env])

def isCloudEnabled() -> bool:
	"""
	
	        Return True if the Cloud Services are Enabled for this Robot.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "isCloudEnabled",
	#     "parametersSignature": "()",
	#     "description": "\n        Return True if the Cloud Services are Enabled for this Robot.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "isCloudEnabled", [])

def enableCloud(enabled:bool) -> None:
	"""
	
	        Enable or disable Cloud Services for this Robot.
	
	Parameters
	----------
	enabled:bool
		True to enable Cloud Services
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "enableCloud",
	#     "parametersSignature": "(b)",
	#     "description": "\n        Enable or disable Cloud Services for this Robot.\n            :param enabled: True to enable Cloud Services\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "enableCloud", [enabled])

def associatedUser() -> str:
	"""
	
	        Return the email of the User associated to the Robot (the owner), empty if None.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "s",
	#     "name": "associatedUser",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the email of the User associated to the Robot (the owner), empty if None.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "associatedUser", [])

def dissociateUser() -> None:
	"""
	
	        Unassign / Dissociate / Unregister the Robot from its owner.
	        This will reset all applications installed for him on the Application Delivery Engine (ADE).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "dissociateUser",
	#     "parametersSignature": "()",
	#     "description": "\n        Unassign / Dissociate / Unregister the Robot from its owner.\n        This will reset all applications installed for him on the Application Delivery Engine (ADE).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "dissociateUser", [])

def associateUser(user:str, password:str) -> None:
	"""
	
	        Assign / Associate / Register the Robot to a User (owner).
	        This will reset all applications installed for him on the Application Delivery Engine (ADE).
	
	Parameters
	----------
	user:str
		New owner SoftBank Robotics Account Login
	password:str
		New owner SoftBank Robotics Account Password
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "associateUser",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Assign / Associate / Register the Robot to a User (owner).\n        This will reset all applications installed for him on the Application Delivery Engine (ADE).\n            :param user: New owner SoftBank Robotics Account Login\n            :param password: New owner SoftBank Robotics Account Password\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "associateUser", [user, password])

def associateToGUID(guid:str, token:str) -> None:
	"""
	
	        Assign / Associate / Register the Robot to a User (owner) (With a Google account ?).
	        This will reset all applications installed for him on the Application Delivery Engine (ADE).
	
	Parameters
	----------
	guid:str
		New owner SoftBank Robotics Account GUID
	token:str
		New owner (Google Account ?) OAuth Token
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "associateToGUID",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Assign / Associate / Register the Robot to a User (owner) (With a Google account ?).\n        This will reset all applications installed for him on the Application Delivery Engine (ADE).\n            :param guid: New owner SoftBank Robotics Account GUID\n            :param token: New owner (Google Account ?) OAuth Token\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "associateToGUID", [guid, token])

def _cloudHost() -> str:
	"""
	
	        Return the Current Cloud Domain for the Environment. (ex: https://cloud.aldebaran.com for prod).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "s",
	#     "name": "_cloudHost",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Current Cloud Domain for the Environment. (ex: https://cloud.aldebaran.com for prod).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_cloudHost", [])

def _report() -> None:
	"""
	
	        Send the Robot Cloud Service Report with the basic Robot Information.
	        Robot Name, BodyId, BuildId, TabletId, BatteryId and Language are sent.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "v",
	#     "name": "_report",
	#     "parametersSignature": "()",
	#     "description": "\n        Send the Robot Cloud Service Report with the basic Robot Information.\n        Robot Name, BodyId, BuildId, TabletId, BatteryId and Language are sent.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_report", [])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "s",
	#     "name": "_package",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "b",
	#     "name": "_ping",
	#     "parametersSignature": "()",
	#     "description": "\n        Return True if the Service is Running.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "_unload",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop the Service.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "s",
	#     "name": "_version",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Version Number.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_ALCloud", "_version", [])

class _Signals:
	onMessage: Signal[[str, str, object]] = Signal("_ALCloud", "onMessage")
	"""
	Bridge notes
	------------
	A signal sent by _ALCloud on the robot.
	
	subscribe(callback) calls callback(str, str, object) each time the robot sends it.
	"""
	onPreferenceMessage: Signal[[str, object]] = Signal("_ALCloud", "onPreferenceMessage")
	"""
	Bridge notes
	------------
	A signal sent by _ALCloud on the robot.
	
	subscribe(callback) calls callback(str, object) each time the robot sends it.
	"""
	onStoreMessage: Signal[[str, object]] = Signal("_ALCloud", "onStoreMessage")
	"""
	Bridge notes
	------------
	A signal sent by _ALCloud on the robot.
	
	subscribe(callback) calls callback(str, object) each time the robot sends it.
	"""
signals = _Signals()

