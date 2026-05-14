from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def getDomainList() -> List[str]:
	"""
	
	        Return the list of all Preferences Domains.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "[s]",
	    "name": "getDomainList",
	    "parametersSignature": "()",
	    "description": "\n        Return the list of all Preferences Domains.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "getDomainList", [])

def getValues() -> List[List[object]]:
	"""
	
	        Return all Preferences for all Domains with their values.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "[[m]]",
	    "name": "getValues",
	    "parametersSignature": "()",
	    "description": "\n        Return all Preferences for all Domains with their values.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "getValues", [])

def getValueList(p0:str) -> List[List[object]]:
	"""
	
	        Return all Preferences for a Domain with its values.
	            :param domain: Preference Domain
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "[[m]]",
	    "name": "getValueList",
	    "parametersSignature": "(s)",
	    "description": "\n        Return all Preferences for a Domain with its values.\n            :param domain: Preference Domain\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "getValueList", [p0])

def getValue(p0:str, p1:str) -> object:
	"""
	
	        Return the Preference Value for a Domain and Setting.
	        Warning! Return None / null if the Preference doesn't exist.
	            :param domain: Preference Domain
	            :param setting: Preference Setting
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "m",
	    "name": "getValue",
	    "parametersSignature": "(ss)",
	    "description": "\n        Return the Preference Value for a Domain and Setting.\n        Warning! Return None / null if the Preference doesn't exist.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "getValue", [p0, p1])

def setValue(p0:str, p1:str, p2:object) -> None:
	"""
	
	        Set a Preference Value for a Domain and Setting.
	        If successful, will try to synchronize it with the Cloud directly.
	        Warning! Only String values are processed, other types are ignored.
	            :param domain: Preference Domain
	            :param setting: Preference Setting
	            :param value: New Preference Value
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "v",
	    "name": "setValue",
	    "parametersSignature": "(ssm)",
	    "description": "\n        Set a Preference Value for a Domain and Setting.\n        If successful, will try to synchronize it with the Cloud directly.\n        Warning! Only String values are processed, other types are ignored.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n            :param value: New Preference Value\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "setValue", [p0, p1, p2])

def setValues(p0:Dict[str,Dict[str,object]]) -> None:
	"""
	
	        Save a list of Preference Domain, Setting and Values.
	        If successful, will try to synchronize them with the Cloud directly.
	        Warning! Only String values are processed, other types are ignored.
	            :param values: New Preference Values (ex: {'PrefDomain': {'PrefSetting': 'StringValue'}})
	        
	
	Parameters
	----------
	p0:Dict[str,Dict[str,object]]
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "v",
	    "name": "setValues",
	    "parametersSignature": "({s{sm}})",
	    "description": "\n        Save a list of Preference Domain, Setting and Values.\n        If successful, will try to synchronize them with the Cloud directly.\n        Warning! Only String values are processed, other types are ignored.\n            :param values: New Preference Values (ex: {'PrefDomain': {'PrefSetting': 'StringValue'}})\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "setValues", [p0])

def removeValue(p0:str, p1:str) -> None:
	"""
	
	        Remove a Preference.
	        If successful, will try to synchronize it with the Cloud directly.
	            :param domain: Preference Domain
	            :param setting: Preference Setting
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "v",
	    "name": "removeValue",
	    "parametersSignature": "(ss)",
	    "description": "\n        Remove a Preference.\n        If successful, will try to synchronize it with the Cloud directly.\n            :param domain: Preference Domain\n            :param setting: Preference Setting\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "removeValue", [p0, p1])

def removeDomainValues(p0:str) -> None:
	"""
	
	        Remove a Preference Domain and all its Settings / Values.
	        If successful, will try to synchronize them with the Cloud directly.
	            :param domain: Preference Domain
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "v",
	    "name": "removeDomainValues",
	    "parametersSignature": "(s)",
	    "description": "\n        Remove a Preference Domain and all its Settings / Values.\n        If successful, will try to synchronize them with the Cloud directly.\n            :param domain: Preference Domain\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "removeDomainValues", [p0])

def importPrefFile(p0:str, p1:str, p2:str, p3:bool) -> None:
	"""
	
	        Import an old ALPreferences File into ALPreferenceManager.
	        Warning! Only String values are processed, other types are ignored.
	        Ex: qicli call ALPreferenceManager.importPrefFile "motion" "naoqi" "ALMotion.xml" 1
	            :param domain: Domain for the new Preferences
	            :param application: Application name to search the file (ex: 'naoqi')
	            :param filename: ALPreference filename
	            :param override: Override the values if already exists in ALPreferenceManager
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "v",
	    "name": "importPrefFile",
	    "parametersSignature": "(sssb)",
	    "description": "\n        Import an old ALPreferences File into ALPreferenceManager.\n        Warning! Only String values are processed, other types are ignored.\n        Ex: qicli call ALPreferenceManager.importPrefFile \"motion\" \"naoqi\" \"ALMotion.xml\" 1\n            :param domain: Domain for the new Preferences\n            :param application: Application name to search the file (ex: 'naoqi')\n            :param filename: ALPreference filename\n            :param override: Override the values if already exists in ALPreferenceManager\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "importPrefFile", [p0, p1, p2, p3])

def update() -> None:
	"""
	
	        Synchronize Preferences with the Cloud.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "v",
	    "name": "update",
	    "parametersSignature": "()",
	    "description": "\n        Synchronize Preferences with the Cloud.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "update", [])

def _factoryReset() -> None:
	"""
	
	        Reset all Robot Preferences on Cloud and locally.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "v",
	    "name": "_factoryReset",
	    "parametersSignature": "()",
	    "description": "\n        Reset all Robot Preferences on Cloud and locally.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_factoryReset", [])

def _setFromCloud(p0:str, p1:str, p2:object) -> None:
	"""
	
	        Set a Preference in Database without Cloud Synchronization.
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "_setFromCloud",
	    "parametersSignature": "(ssm)",
	    "description": "\n        Set a Preference in Database without Cloud Synchronization.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_setFromCloud", [p0, p1, p2])

def _restart(p0:str, p1:str) -> None:
	"""
	
	        Reinitialize the Service with a different Cloud URL and Database Path.
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "v",
	    "name": "_restart",
	    "parametersSignature": "(ss)",
	    "description": "\n        Reinitialize the Service with a different Cloud URL and Database Path.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_restart", [p0, p1])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "s",
	    "name": "_package",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "b",
	    "name": "_ping",
	    "parametersSignature": "()",
	    "description": "\n        Return True if the Service is Running.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "v",
	    "name": "_unload",
	    "parametersSignature": "()",
	    "description": "\n        Stop the Service.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "s",
	    "name": "_version",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Version Number.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALPreferenceManager", "_version", [])

