from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def registerEvent(p0:int, p1:int, p2:int) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 0,
	    "returnSignature": "L",
	    "name": "registerEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "registerEvent", [p0, p1, p2])

def unregisterEvent(p0:int, p1:int, p2:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 1,
	    "returnSignature": "v",
	    "name": "unregisterEvent",
	    "parametersSignature": "(IIL)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "unregisterEvent", [p0, p1, p2])

def metaObject(p0:int) -> MetaObject:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 2,
	    "returnSignature": "({I(Issss[(ss)<MetaMethodParameter,name,description>]s)<MetaMethod,uid,returnSignature,name,parametersSignature,description,parameters,returnDescription>}{I(Iss)<MetaSignal,uid,name,signature>}{I(Iss)<MetaProperty,uid,name,signature>}s)<MetaObject,methods,signals,properties,description>",
	    "name": "metaObject",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "metaObject", [p0])

def terminate(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 3,
	    "returnSignature": "v",
	    "name": "terminate",
	    "parametersSignature": "(I)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "terminate", [p0])

def property(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 5,
	    "returnSignature": "m",
	    "name": "property",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "property", [p0])

def setProperty(p0:object, p1:object) -> None:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 6,
	    "returnSignature": "v",
	    "name": "setProperty",
	    "parametersSignature": "(mm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "setProperty", [p0, p1])

def properties() -> List[str]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 7,
	    "returnSignature": "[s]",
	    "name": "properties",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "properties", [])

def registerEventWithSignature(p0:int, p1:int, p2:int, p3:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	p2:int
		
	p3:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 8,
	    "returnSignature": "L",
	    "name": "registerEventWithSignature",
	    "parametersSignature": "(IILs)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "registerEventWithSignature", [p0, p1, p2, p3])

def isStatsEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 80,
	    "returnSignature": "b",
	    "name": "isStatsEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "isStatsEnabled", [])

def enableStats(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 81,
	    "returnSignature": "v",
	    "name": "enableStats",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "enableStats", [p0])

def stats() -> Dict[int,MethodStatistics]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 82,
	    "returnSignature": "{I(I(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>)<MethodStatistics,count,wall,user,system>}",
	    "name": "stats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "stats", [])

def clearStats() -> None:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 83,
	    "returnSignature": "v",
	    "name": "clearStats",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "clearStats", [])

def isTraceEnabled() -> bool:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 84,
	    "returnSignature": "b",
	    "name": "isTraceEnabled",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "isTraceEnabled", [])

def enableTrace(p0:bool) -> None:
	"""
	
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 85,
	    "returnSignature": "v",
	    "name": "enableTrace",
	    "parametersSignature": "(b)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "enableTrace", [p0])

def update() -> bool:
	"""
	
	        Check System and Packages Updates, download and Install them.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "b",
	    "name": "update",
	    "parametersSignature": "()",
	    "description": "\n        Check System and Packages Updates, download and Install them.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "update", [])

def updatePackages() -> None:
	"""
	
	        Check Packages Updates if not already done, download and install them.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "v",
	    "name": "updatePackages",
	    "parametersSignature": "()",
	    "description": "\n        Check Packages Updates if not already done, download and install them.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "updatePackages", [])

def downloadPackagesInfo() -> List[Dict[str,object]]:
	"""
	
	        Check Packages Updates from the Application Delivery Engine (ADE) and return the list.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "[{sm}]",
	    "name": "downloadPackagesInfo",
	    "parametersSignature": "()",
	    "description": "\n        Check Packages Updates from the Application Delivery Engine (ADE) and return the list.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadPackagesInfo", [])

def getPackagesInfo() -> List[Dict[str,object]]:
	"""
	
	        Check Packages Updates from the Application Delivery Engine (ADE) if not done and return the list.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "[{sm}]",
	    "name": "getPackagesInfo",
	    "parametersSignature": "()",
	    "description": "\n        Check Packages Updates from the Application Delivery Engine (ADE) if not done and return the list.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getPackagesInfo", [])

def getPackagesToAdd() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Install on the Robot.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "[{sm}]",
	    "name": "getPackagesToAdd",
	    "parametersSignature": "()",
	    "description": "\n        Return the List of Packages to Install on the Robot.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getPackagesToAdd", [])

def getPackagesToUpdate() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Update in the Robot.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "[{sm}]",
	    "name": "getPackagesToUpdate",
	    "parametersSignature": "()",
	    "description": "\n        Return the List of Packages to Update in the Robot.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getPackagesToUpdate", [])

def getPackagesToRemove() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Delete from the Robot.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "[{sm}]",
	    "name": "getPackagesToRemove",
	    "parametersSignature": "()",
	    "description": "\n        Return the List of Packages to Delete from the Robot.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getPackagesToRemove", [])

def getPackageInfo(p0:str) -> object:
	"""
	
	        Return the Information of a Package the Robot should have installed.
	            :param uuid: Package ID (uuid in the Manifest)
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "m",
	    "name": "getPackageInfo",
	    "parametersSignature": "(s)",
	    "description": "\n        Return the Information of a Package the Robot should have installed.\n            :param uuid: Package ID (uuid in the Manifest)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getPackageInfo", [p0])

def updatePackage(p0:str) -> bool:
	"""
	
	        Check Packages Updates if needed, download if needed and install a Package.
	            :param uuid: Package ID (uuid in the Manifest)
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "b",
	    "name": "updatePackage",
	    "parametersSignature": "(s)",
	    "description": "\n        Check Packages Updates if needed, download if needed and install a Package.\n            :param uuid: Package ID (uuid in the Manifest)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "updatePackage", [p0])

def updateSystem() -> bool:
	"""
	
	        Check System Updates, download if needed and install the Sustem Update.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "b",
	    "name": "updateSystem",
	    "parametersSignature": "()",
	    "description": "\n        Check System Updates, download if needed and install the Sustem Update.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "updateSystem", [])

def downloadNextSystemImageInfo() -> Dict[str,object]:
	"""
	
	        Check System Updates and return the System Update Info Map or {} if None.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "{sm}",
	    "name": "downloadNextSystemImageInfo",
	    "parametersSignature": "()",
	    "description": "\n        Check System Updates and return the System Update Info Map or {} if None.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadNextSystemImageInfo", [])

def getNextSystemImageInfo() -> Dict[str,object]:
	"""
	
	        Check System Updates if needed and return the System Update Info Map or {} if None.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "{sm}",
	    "name": "getNextSystemImageInfo",
	    "parametersSignature": "()",
	    "description": "\n        Check System Updates if needed and return the System Update Info Map or {} if None.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getNextSystemImageInfo", [])

def downloadNextSystemImage() -> bool:
	"""
	
	        Check System Updates and download it if present.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "b",
	    "name": "downloadNextSystemImage",
	    "parametersSignature": "()",
	    "description": "\n        Check System Updates and download it if present.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadNextSystemImage", [])

def installNextSystemImage(p0:bool) -> bool:
	"""
	
	        Check System Updates if needed, download it if needed and install it if present.
	            :param freset: True to perform a Factory Reset (delete all local files and configuration)
	        
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "b",
	    "name": "installNextSystemImage",
	    "parametersSignature": "(b)",
	    "description": "\n        Check System Updates if needed, download it if needed and install it if present.\n            :param freset: True to perform a Factory Reset (delete all local files and configuration)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "installNextSystemImage", [p0])

def downloadCurrentSystemImageInfo_1(p0:str, p1:str) -> Dict[str,object]:
	"""
	Note: This is one of the overloads of the original method (downloadCurrentSystemImageInfo)
	
	
	        Get the Current System Image Info to allow a Factory Reset.
	        Once successful, download it with 'downloadCurrentSystemImage'.
	        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.
	            :param login: SoftBank Robotics Account Login of the user making the request
	            :param password: SoftBank Robotics Account Password of the user making the request
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "{sm}",
	    "name": "downloadCurrentSystemImageInfo",
	    "parametersSignature": "(ss)",
	    "description": "\n        Get the Current System Image Info to allow a Factory Reset.\n        Once successful, download it with 'downloadCurrentSystemImage'.\n        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.\n            :param login: SoftBank Robotics Account Login of the user making the request\n            :param password: SoftBank Robotics Account Password of the user making the request\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadCurrentSystemImageInfo", [p0, p1])

def downloadCurrentSystemImageInfo_2(p0:str) -> Dict[str,object]:
	"""
	Note: This is one of the overloads of the original method (downloadCurrentSystemImageInfo)
	
	
	        Get the Current System Image Info to allow a Factory Reset with an OAuth Token.
	        Once successful, download it with 'downloadCurrentSystemImage'.
	        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.
	            :param token: SoftBank Account OAuth Token of the user making the request
	        
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "{sm}",
	    "name": "downloadCurrentSystemImageInfo",
	    "parametersSignature": "(s)",
	    "description": "\n        Get the Current System Image Info to allow a Factory Reset with an OAuth Token.\n        Once successful, download it with 'downloadCurrentSystemImage'.\n        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.\n            :param token: SoftBank Account OAuth Token of the user making the request\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadCurrentSystemImageInfo", [p0])

def downloadCurrentSystemImage() -> bool:
	"""
	
	        Download the Robot Current System Image to perform a Factory Reset.
	        Once downloaded, install it with 'installCurrentSystemImage'.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "b",
	    "name": "downloadCurrentSystemImage",
	    "parametersSignature": "()",
	    "description": "\n        Download the Robot Current System Image to perform a Factory Reset.\n        Once downloaded, install it with 'installCurrentSystemImage'.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadCurrentSystemImage", [])

def installCurrentSystemImage(p0:bool) -> bool:
	"""
	
	        Re-install the current System Image downloaded through downloadCurrentSystemImage.
	            :param freset: True to perform a Factory Reset (delete all local files and configuration)
	        
	
	Parameters
	----------
	p0:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "b",
	    "name": "installCurrentSystemImage",
	    "parametersSignature": "(b)",
	    "description": "\n        Re-install the current System Image downloaded through downloadCurrentSystemImage.\n            :param freset: True to perform a Factory Reset (delete all local files and configuration)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "installCurrentSystemImage", [p0])

def abortSystemImageInstall() -> None:
	"""
	
	        Abort System Image Install and remove any downloaded System Image.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "v",
	    "name": "abortSystemImageInstall",
	    "parametersSignature": "()",
	    "description": "\n        Abort System Image Install and remove any downloaded System Image.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "abortSystemImageInstall", [])

def downloadNextOTAImageInfo(p0:str, p1:str) -> Dict[str,object]:
	"""
	
	        Check the Android Tablet Update Info if available and Return it.
	        Returns a dict with the Android Image Info or {}
	            :param fingerprint: Fingerprint of the current Tablet Firmare
	            :param product_model: Android Tablet Model
	        
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "{sm}",
	    "name": "downloadNextOTAImageInfo",
	    "parametersSignature": "(ss)",
	    "description": "\n        Check the Android Tablet Update Info if available and Return it.\n        Returns a dict with the Android Image Info or {}\n            :param fingerprint: Fingerprint of the current Tablet Firmare\n            :param product_model: Android Tablet Model\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadNextOTAImageInfo", [p0, p1])

def getNextOTAImageInfo() -> Dict[str,object]:
	"""
	
	        Return info about the newest available Android Tablet Image if available.
	        Returns a dict with the Image Info or {}
	        
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "{sm}",
	    "name": "getNextOTAImageInfo",
	    "parametersSignature": "()",
	    "description": "\n        Return info about the newest available Android Tablet Image if available.\n        Returns a dict with the Image Info or {}\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "getNextOTAImageInfo", [])

def downloadNextOTAImage() -> bool:
	"""
	
	        Download the Android Tablet Update Image and its APK if available.
	        Once downloaded, install it using 'installNextOTAImage'.
	        Returns True if everything went fine, False overwise.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "b",
	    "name": "downloadNextOTAImage",
	    "parametersSignature": "()",
	    "description": "\n        Download the Android Tablet Update Image and its APK if available.\n        Once downloaded, install it using 'installNextOTAImage'.\n        Returns True if everything went fine, False overwise.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "downloadNextOTAImage", [])

def installNextOTAImage() -> bool:
	"""
	
	        Install Android Tablet Update and APK downloaded with 'downloadNextOTAImage'.
	        Returns True if everything went fine, False overwise.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "b",
	    "name": "installNextOTAImage",
	    "parametersSignature": "()",
	    "description": "\n        Install Android Tablet Update and APK downloaded with 'downloadNextOTAImage'.\n        Returns True if everything went fine, False overwise.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "installNextOTAImage", [])

def cleanOTAImageInstall() -> None:
	"""
	
	        Abort Android Tablet System Image and APK Installation.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "v",
	    "name": "cleanOTAImageInstall",
	    "parametersSignature": "()",
	    "description": "\n        Abort Android Tablet System Image and APK Installation.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "cleanOTAImageInstall", [])

def abortAll() -> None:
	"""
	
	        Stop all current worker operations (downloads, etc.).
	        
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "v",
	    "name": "abortAll",
	    "parametersSignature": "()",
	    "description": "\n        Stop all current worker operations (downloads, etc.).\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "abortAll", [])

def _reportStatusToADE() -> None:
	"""
	
	        Send the Robot Status to the Application Delivery Engine.
	        This report contains the HeadId, BodyId, Robot Name, Language, BuildId
	        Robot Model, System Version and Applications List.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "v",
	    "name": "_reportStatusToADE",
	    "parametersSignature": "()",
	    "description": "\n        Send the Robot Status to the Application Delivery Engine.\n        This report contains the HeadId, BodyId, Robot Name, Language, BuildId\n        Robot Model, System Version and Applications List.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "_reportStatusToADE", [])

def updateApps() -> bool:
	"""
	
	        Check and Update the Robot Packages.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "b",
	    "name": "updateApps",
	    "parametersSignature": "()",
	    "description": "\n        Check and Update the Robot Packages.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "updateApps", [])

def checkUpdate(p0:bool, p1:bool) -> bool:
	"""
	
	        Check the System and Packages Updates.
	        
	
	Parameters
	----------
	p0:bool
		
	p1:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "b",
	    "name": "checkUpdate",
	    "parametersSignature": "(bb)",
	    "description": "\n        Check the System and Packages Updates.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "checkUpdate", [p0, p1])

def status() -> List[Dict[str,object]]:
	"""
	
	        Return the Packages Information retrueved from the Application Delivery Engine.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "[{sm}]",
	    "name": "status",
	    "parametersSignature": "()",
	    "description": "\n        Return the Packages Information retrueved from the Application Delivery Engine.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "status", [])

def stopUpdate() -> None:
	"""
	
	        Stop all current worker operations (downloads, etc.).
	        
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "v",
	    "name": "stopUpdate",
	    "parametersSignature": "()",
	    "description": "\n        Stop all current worker operations (downloads, etc.).\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "stopUpdate", [])

def analyse() -> bool:
	"""
	
	        Was used to analyze the actions to do in previous ALStore versions. Does nothing now.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "b",
	    "name": "analyse",
	    "parametersSignature": "()",
	    "description": "\n        Was used to analyze the actions to do in previous ALStore versions. Does nothing now.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "analyse", [])

def updateRunningApps() -> bool:
	"""
	
	        Was used to know if running applications would be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "b",
	    "name": "updateRunningApps",
	    "parametersSignature": "()",
	    "description": "\n        Was used to know if running applications would be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "updateRunningApps", [])

def activateUpdateRunningApps() -> bool:
	"""
	
	        Was used to set that running applications would be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "b",
	    "name": "activateUpdateRunningApps",
	    "parametersSignature": "()",
	    "description": "\n        Was used to set that running applications would be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "activateUpdateRunningApps", [])

def deactivateUpdateRunningApps() -> bool:
	"""
	
	        Was used to set that running applications would not be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "b",
	    "name": "deactivateUpdateRunningApps",
	    "parametersSignature": "()",
	    "description": "\n        Was used to set that running applications would not be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "deactivateUpdateRunningApps", [])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "s",
	    "name": "_package",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "_ping",
	    "parametersSignature": "()",
	    "description": "\n        Return True if the Service is Running.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "v",
	    "name": "_unload",
	    "parametersSignature": "()",
	    "description": "\n        Stop the Service.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "s",
	    "name": "_version",
	    "parametersSignature": "()",
	    "description": "\n        Return the Service Version Number.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALStore", "_version", [])

