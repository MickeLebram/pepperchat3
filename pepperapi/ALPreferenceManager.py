"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def getDomainList() -> List[str]:
	"""
	
	        Return the list of all Preferences Domains.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "[s]",
	#     "name": "getDomainList",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the list of all Preferences Domains.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "getDomainList", [])

def getValues() -> List[List[object]]:
	"""
	
	        Return all Preferences for all Domains with their values.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "[[m]]",
	#     "name": "getValues",
	#     "parametersSignature": "()",
	#     "description": "\n        Return all Preferences for all Domains with their values.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "getValues", [])

def getValueList(domain:str) -> List[List[object]]:
	"""
	
	        Return all Preferences for a Domain with its values.
	
	Parameters
	----------
	domain:str
		Preference Domain
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "[[m]]",
	#     "name": "getValueList",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Return all Preferences for a Domain with its values.\n            :param domain: Preference Domain\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "getValueList", [domain])

def getValue(domain:str, setting:str) -> object:
	"""
	
	        Return the Preference Value for a Domain and Setting.
	        Warning! Return None / null if the Preference doesn't exist.
	
	Parameters
	----------
	domain:str
		Preference Domain
	setting:str
		Preference Setting
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "getValue",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Return the Preference Value for a Domain and Setting.\n        Warning! Return None / null if the Preference doesn't exist.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "getValue", [domain, setting])

def setValue(domain:str, setting:str, value:object) -> None:
	"""
	
	        Set a Preference Value for a Domain and Setting.
	        If successful, will try to synchronize it with the Cloud directly.
	        Warning! Only String values are processed, other types are ignored.
	
	Parameters
	----------
	domain:str
		Preference Domain
	setting:str
		Preference Setting
	value:object
		New Preference Value
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "v",
	#     "name": "setValue",
	#     "parametersSignature": "(ssm)",
	#     "description": "\n        Set a Preference Value for a Domain and Setting.\n        If successful, will try to synchronize it with the Cloud directly.\n        Warning! Only String values are processed, other types are ignored.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n            :param value: New Preference Value\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "setValue", [domain, setting, value])

def setValues(values:Dict[str,Dict[str,object]]) -> None:
	"""
	
	        Save a list of Preference Domain, Setting and Values.
	        If successful, will try to synchronize them with the Cloud directly.
	        Warning! Only String values are processed, other types are ignored.
	
	Parameters
	----------
	values:Dict[str,Dict[str,object]]
		New Preference Values (ex: {'PrefDomain': {'PrefSetting': 'StringValue'}})
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "v",
	#     "name": "setValues",
	#     "parametersSignature": "({s{sm}})",
	#     "description": "\n        Save a list of Preference Domain, Setting and Values.\n        If successful, will try to synchronize them with the Cloud directly.\n        Warning! Only String values are processed, other types are ignored.\n            :param values: New Preference Values (ex: {'PrefDomain': {'PrefSetting': 'StringValue'}})\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "setValues", [values])

def removeValue(domain:str, setting:str) -> None:
	"""
	
	        Remove a Preference.
	        If successful, will try to synchronize it with the Cloud directly.
	
	Parameters
	----------
	domain:str
		Preference Domain
	setting:str
		Preference Setting
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "removeValue",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Remove a Preference.\n        If successful, will try to synchronize it with the Cloud directly.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "removeValue", [domain, setting])

def removeDomainValues(domain:str) -> None:
	"""
	
	        Remove a Preference Domain and all its Settings / Values.
	        If successful, will try to synchronize them with the Cloud directly.
	
	Parameters
	----------
	domain:str
		Preference Domain
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "removeDomainValues",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Remove a Preference Domain and all its Settings / Values.\n        If successful, will try to synchronize them with the Cloud directly.\n            :param domain: Preference Domain\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "removeDomainValues", [domain])

def importPrefFile(domain:str, application:str, filename:str, override:bool) -> None:
	"""
	
	        Import an old ALPreferences File into ALPreferenceManager.
	        Warning! Only String values are processed, other types are ignored.
	        Ex: qicli call ALPreferenceManager.importPrefFile "motion" "naoqi" "ALMotion.xml" 1
	
	Parameters
	----------
	domain:str
		Domain for the new Preferences
	application:str
		Application name to search the file (ex: 'naoqi')
	filename:str
		ALPreference filename
	override:bool
		Override the values if already exists in ALPreferenceManager
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "v",
	#     "name": "importPrefFile",
	#     "parametersSignature": "(sssb)",
	#     "description": "\n        Import an old ALPreferences File into ALPreferenceManager.\n        Warning! Only String values are processed, other types are ignored.\n        Ex: qicli call ALPreferenceManager.importPrefFile \"motion\" \"naoqi\" \"ALMotion.xml\" 1\n            :param domain: Domain for the new Preferences\n            :param application: Application name to search the file (ex: 'naoqi')\n            :param filename: ALPreference filename\n            :param override: Override the values if already exists in ALPreferenceManager\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "importPrefFile", [domain, application, filename, override])

def update() -> None:
	"""
	
	        Synchronize Preferences with the Cloud.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "v",
	#     "name": "update",
	#     "parametersSignature": "()",
	#     "description": "\n        Synchronize Preferences with the Cloud.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "update", [])

def _factoryReset() -> None:
	"""
	
	        Reset all Robot Preferences on Cloud and locally.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "v",
	#     "name": "_factoryReset",
	#     "parametersSignature": "()",
	#     "description": "\n        Reset all Robot Preferences on Cloud and locally.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_factoryReset", [])

def _setFromCloud(p0:str, p1:str, p2:object) -> None:
	"""
	
	        Set a Preference in Database without Cloud Synchronization.
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "_setFromCloud",
	#     "parametersSignature": "(ssm)",
	#     "description": "\n        Set a Preference in Database without Cloud Synchronization.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_setFromCloud", [p0, p1, p2])

def _restart(p0:str, p1:str) -> None:
	"""
	
	        Reinitialize the Service with a different Cloud URL and Database Path.
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "_restart",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Reinitialize the Service with a different Cloud URL and Database Path.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_restart", [p0, p1])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "s",
	#     "name": "_package",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "_ping",
	#     "parametersSignature": "()",
	#     "description": "\n        Return True if the Service is Running.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "_unload",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop the Service.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "s",
	#     "name": "_version",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Version Number.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALPreferenceManager", "_version", [])

class _Signals:
	preferenceAdded: Signal[[str, str, object]] = Signal("ALPreferenceManager", "preferenceAdded")
	"""
	Bridge notes
	------------
	A signal sent by ALPreferenceManager on the robot.
	
	subscribe(callback) calls callback(str, str, object) each time the robot sends it.
	"""
	preferenceDomainRemoved: Signal[[str]] = Signal("ALPreferenceManager", "preferenceDomainRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALPreferenceManager on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	preferenceRemoved: Signal[[str, str]] = Signal("ALPreferenceManager", "preferenceRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALPreferenceManager on the robot.
	
	subscribe(callback) calls callback(str, str) each time the robot sends it.
	"""
	preferenceUpdated: Signal[[str, str, object]] = Signal("ALPreferenceManager", "preferenceUpdated")
	"""
	Bridge notes
	------------
	A signal sent by ALPreferenceManager on the robot.
	
	subscribe(callback) calls callback(str, str, object) each time the robot sends it.
	"""
	preferencesSynchronized: Signal[[]] = Signal("ALPreferenceManager", "preferencesSynchronized")
	"""
	Bridge notes
	------------
	A signal sent by ALPreferenceManager on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
signals = _Signals()

