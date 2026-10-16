"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def update() -> bool:
	"""
	
	        Check System and Packages Updates, download and Install them.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "b",
	#     "name": "update",
	#     "parametersSignature": "()",
	#     "description": "\n        Check System and Packages Updates, download and Install them.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "update", [])

def updatePackages() -> None:
	"""
	
	        Check Packages Updates if not already done, download and install them.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "v",
	#     "name": "updatePackages",
	#     "parametersSignature": "()",
	#     "description": "\n        Check Packages Updates if not already done, download and install them.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "updatePackages", [])

def downloadPackagesInfo() -> List[Dict[str,object]]:
	"""
	
	        Check Packages Updates from the Application Delivery Engine (ADE) and return the list.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "[{sm}]",
	#     "name": "downloadPackagesInfo",
	#     "parametersSignature": "()",
	#     "description": "\n        Check Packages Updates from the Application Delivery Engine (ADE) and return the list.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadPackagesInfo", [])

def getPackagesInfo() -> List[Dict[str,object]]:
	"""
	
	        Check Packages Updates from the Application Delivery Engine (ADE) if not done and return the list.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "[{sm}]",
	#     "name": "getPackagesInfo",
	#     "parametersSignature": "()",
	#     "description": "\n        Check Packages Updates from the Application Delivery Engine (ADE) if not done and return the list.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getPackagesInfo", [])

def getPackagesToAdd() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Install on the Robot.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "[{sm}]",
	#     "name": "getPackagesToAdd",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the List of Packages to Install on the Robot.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getPackagesToAdd", [])

def getPackagesToUpdate() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Update in the Robot.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[{sm}]",
	#     "name": "getPackagesToUpdate",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the List of Packages to Update in the Robot.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getPackagesToUpdate", [])

def getPackagesToRemove() -> List[Dict[str,object]]:
	"""
	
	        Return the List of Packages to Delete from the Robot.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "[{sm}]",
	#     "name": "getPackagesToRemove",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the List of Packages to Delete from the Robot.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getPackagesToRemove", [])

def getPackageInfo(uuid:str) -> object:
	"""
	
	        Return the Information of a Package the Robot should have installed.
	
	Parameters
	----------
	uuid:str
		Package ID (uuid in the Manifest)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "m",
	#     "name": "getPackageInfo",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Return the Information of a Package the Robot should have installed.\n            :param uuid: Package ID (uuid in the Manifest)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getPackageInfo", [uuid])

def updatePackage(uuid:str) -> bool:
	"""
	
	        Check Packages Updates if needed, download if needed and install a Package.
	
	Parameters
	----------
	uuid:str
		Package ID (uuid in the Manifest)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "updatePackage",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Check Packages Updates if needed, download if needed and install a Package.\n            :param uuid: Package ID (uuid in the Manifest)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "updatePackage", [uuid])

def updateSystem() -> bool:
	"""
	
	        Check System Updates, download if needed and install the Sustem Update.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "b",
	#     "name": "updateSystem",
	#     "parametersSignature": "()",
	#     "description": "\n        Check System Updates, download if needed and install the Sustem Update.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "updateSystem", [])

def downloadNextSystemImageInfo() -> Dict[str,object]:
	"""
	
	        Check System Updates and return the System Update Info Map or {} if None.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "{sm}",
	#     "name": "downloadNextSystemImageInfo",
	#     "parametersSignature": "()",
	#     "description": "\n        Check System Updates and return the System Update Info Map or {} if None.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadNextSystemImageInfo", [])

def getNextSystemImageInfo() -> Dict[str,object]:
	"""
	
	        Check System Updates if needed and return the System Update Info Map or {} if None.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "{sm}",
	#     "name": "getNextSystemImageInfo",
	#     "parametersSignature": "()",
	#     "description": "\n        Check System Updates if needed and return the System Update Info Map or {} if None.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getNextSystemImageInfo", [])

def downloadNextSystemImage() -> bool:
	"""
	
	        Check System Updates and download it if present.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "b",
	#     "name": "downloadNextSystemImage",
	#     "parametersSignature": "()",
	#     "description": "\n        Check System Updates and download it if present.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadNextSystemImage", [])

def installNextSystemImage(freset:bool) -> bool:
	"""
	
	        Check System Updates if needed, download it if needed and install it if present.
	
	Parameters
	----------
	freset:bool
		True to perform a Factory Reset (delete all local files and configuration)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "b",
	#     "name": "installNextSystemImage",
	#     "parametersSignature": "(b)",
	#     "description": "\n        Check System Updates if needed, download it if needed and install it if present.\n            :param freset: True to perform a Factory Reset (delete all local files and configuration)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "installNextSystemImage", [freset])

@overload
def downloadCurrentSystemImageInfo(token:str, /) -> Dict[str,object]:
	"""
	
	        Get the Current System Image Info to allow a Factory Reset with an OAuth Token.
	        Once successful, download it with 'downloadCurrentSystemImage'.
	        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.
	
	Parameters
	----------
	token:str
		SoftBank Account OAuth Token of the user making the request
	
	Bridge notes
	------------
	downloadCurrentSystemImageInfo has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "{sm}",
	#     "name": "downloadCurrentSystemImageInfo",
	#     "parametersSignature": "(s)",
	#     "description": "\n        Get the Current System Image Info to allow a Factory Reset with an OAuth Token.\n        Once successful, download it with 'downloadCurrentSystemImage'.\n        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.\n            :param token: SoftBank Account OAuth Token of the user making the request\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def downloadCurrentSystemImageInfo(login:str, password:str, /) -> Dict[str,object]:
	"""
	
	        Get the Current System Image Info to allow a Factory Reset.
	        Once successful, download it with 'downloadCurrentSystemImage'.
	        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.
	
	Parameters
	----------
	login:str
		SoftBank Robotics Account Login of the user making the request
	password:str
		SoftBank Robotics Account Password of the user making the request
	
	Bridge notes
	------------
	downloadCurrentSystemImageInfo has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "{sm}",
	#     "name": "downloadCurrentSystemImageInfo",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Get the Current System Image Info to allow a Factory Reset.\n        Once successful, download it with 'downloadCurrentSystemImage'.\n        This operation can be performed by the Robot Owner, Admin or by a Fleet Manager.\n            :param login: SoftBank Robotics Account Login of the user making the request\n            :param password: SoftBank Robotics Account Password of the user making the request\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def downloadCurrentSystemImageInfo(*args, **kwargs):
	"""
	Bridge notes
	------------
	downloadCurrentSystemImageInfo has 2 variants on the robot:
	- downloadCurrentSystemImageInfo(token:str)
	- downloadCurrentSystemImageInfo(login:str, password:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALStore.downloadCurrentSystemImageInfo has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALStore", "downloadCurrentSystemImageInfo", list(args))

def downloadCurrentSystemImage() -> bool:
	"""
	
	        Download the Robot Current System Image to perform a Factory Reset.
	        Once downloaded, install it with 'installCurrentSystemImage'.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "downloadCurrentSystemImage",
	#     "parametersSignature": "()",
	#     "description": "\n        Download the Robot Current System Image to perform a Factory Reset.\n        Once downloaded, install it with 'installCurrentSystemImage'.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadCurrentSystemImage", [])

def installCurrentSystemImage(freset:bool) -> bool:
	"""
	
	        Re-install the current System Image downloaded through downloadCurrentSystemImage.
	
	Parameters
	----------
	freset:bool
		True to perform a Factory Reset (delete all local files and configuration)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "b",
	#     "name": "installCurrentSystemImage",
	#     "parametersSignature": "(b)",
	#     "description": "\n        Re-install the current System Image downloaded through downloadCurrentSystemImage.\n            :param freset: True to perform a Factory Reset (delete all local files and configuration)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "installCurrentSystemImage", [freset])

def abortSystemImageInstall() -> None:
	"""
	
	        Abort System Image Install and remove any downloaded System Image.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "abortSystemImageInstall",
	#     "parametersSignature": "()",
	#     "description": "\n        Abort System Image Install and remove any downloaded System Image.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "abortSystemImageInstall", [])

def downloadNextOTAImageInfo(fingerprint:str, product_model:str) -> Dict[str,object]:
	"""
	
	        Check the Android Tablet Update Info if available and Return it.
	        Returns a dict with the Android Image Info or {}
	
	Parameters
	----------
	fingerprint:str
		Fingerprint of the current Tablet Firmare
	product_model:str
		Android Tablet Model
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "{sm}",
	#     "name": "downloadNextOTAImageInfo",
	#     "parametersSignature": "(ss)",
	#     "description": "\n        Check the Android Tablet Update Info if available and Return it.\n        Returns a dict with the Android Image Info or {}\n            :param fingerprint: Fingerprint of the current Tablet Firmare\n            :param product_model: Android Tablet Model\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadNextOTAImageInfo", [fingerprint, product_model])

def getNextOTAImageInfo() -> Dict[str,object]:
	"""
	
	        Return info about the newest available Android Tablet Image if available.
	        Returns a dict with the Image Info or {}
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "{sm}",
	#     "name": "getNextOTAImageInfo",
	#     "parametersSignature": "()",
	#     "description": "\n        Return info about the newest available Android Tablet Image if available.\n        Returns a dict with the Image Info or {}\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "getNextOTAImageInfo", [])

def downloadNextOTAImage() -> bool:
	"""
	
	        Download the Android Tablet Update Image and its APK if available.
	        Once downloaded, install it using 'installNextOTAImage'.
	        Returns True if everything went fine, False overwise.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "downloadNextOTAImage",
	#     "parametersSignature": "()",
	#     "description": "\n        Download the Android Tablet Update Image and its APK if available.\n        Once downloaded, install it using 'installNextOTAImage'.\n        Returns True if everything went fine, False overwise.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "downloadNextOTAImage", [])

def installNextOTAImage() -> bool:
	"""
	
	        Install Android Tablet Update and APK downloaded with 'downloadNextOTAImage'.
	        Returns True if everything went fine, False overwise.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "installNextOTAImage",
	#     "parametersSignature": "()",
	#     "description": "\n        Install Android Tablet Update and APK downloaded with 'downloadNextOTAImage'.\n        Returns True if everything went fine, False overwise.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "installNextOTAImage", [])

def cleanOTAImageInstall() -> None:
	"""
	
	        Abort Android Tablet System Image and APK Installation.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "cleanOTAImageInstall",
	#     "parametersSignature": "()",
	#     "description": "\n        Abort Android Tablet System Image and APK Installation.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "cleanOTAImageInstall", [])

def abortAll() -> None:
	"""
	
	        Stop all current worker operations (downloads, etc.).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "abortAll",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop all current worker operations (downloads, etc.).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "abortAll", [])

def _reportStatusToADE() -> None:
	"""
	
	        Send the Robot Status to the Application Delivery Engine.
	        This report contains the HeadId, BodyId, Robot Name, Language, BuildId
	        Robot Model, System Version and Applications List.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_reportStatusToADE",
	#     "parametersSignature": "()",
	#     "description": "\n        Send the Robot Status to the Application Delivery Engine.\n        This report contains the HeadId, BodyId, Robot Name, Language, BuildId\n        Robot Model, System Version and Applications List.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "_reportStatusToADE", [])

def updateApps() -> bool:
	"""
	
	        Check and Update the Robot Packages.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "updateApps",
	#     "parametersSignature": "()",
	#     "description": "\n        Check and Update the Robot Packages.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "updateApps", [])

def checkUpdate(p0:bool, p1:bool) -> bool:
	"""
	
	        Check the System and Packages Updates.
	        
	
	Parameters
	----------
	p0:bool
		
	p1:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "checkUpdate",
	#     "parametersSignature": "(bb)",
	#     "description": "\n        Check the System and Packages Updates.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "checkUpdate", [p0, p1])

def status() -> List[Dict[str,object]]:
	"""
	
	        Return the Packages Information retrueved from the Application Delivery Engine.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "[{sm}]",
	#     "name": "status",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Packages Information retrueved from the Application Delivery Engine.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "status", [])

def stopUpdate() -> None:
	"""
	
	        Stop all current worker operations (downloads, etc.).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "stopUpdate",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop all current worker operations (downloads, etc.).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "stopUpdate", [])

def analyse() -> bool:
	"""
	
	        Was used to analyze the actions to do in previous ALStore versions. Does nothing now.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "b",
	#     "name": "analyse",
	#     "parametersSignature": "()",
	#     "description": "\n        Was used to analyze the actions to do in previous ALStore versions. Does nothing now.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "analyse", [])

def updateRunningApps() -> bool:
	"""
	
	        Was used to know if running applications would be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "updateRunningApps",
	#     "parametersSignature": "()",
	#     "description": "\n        Was used to know if running applications would be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "updateRunningApps", [])

def activateUpdateRunningApps() -> bool:
	"""
	
	        Was used to set that running applications would be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "b",
	#     "name": "activateUpdateRunningApps",
	#     "parametersSignature": "()",
	#     "description": "\n        Was used to set that running applications would be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "activateUpdateRunningApps", [])

def deactivateUpdateRunningApps() -> bool:
	"""
	
	        Was used to set that running applications would not be updated by ALStore.
	        This choice is not possible anymore, running applications are always updated.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "b",
	#     "name": "deactivateUpdateRunningApps",
	#     "parametersSignature": "()",
	#     "description": "\n        Was used to set that running applications would not be updated by ALStore.\n        This choice is not possible anymore, running applications are always updated.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "deactivateUpdateRunningApps", [])

def _package() -> str:
	"""
	
	        Return the Service Package ID of the Service (uuid in the Manifest).
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "s",
	#     "name": "_package",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Package ID of the Service (uuid in the Manifest).\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "_package", [])

def _ping() -> bool:
	"""
	
	        Return True if the Service is Running.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "_ping",
	#     "parametersSignature": "()",
	#     "description": "\n        Return True if the Service is Running.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "_ping", [])

def _unload() -> None:
	"""
	
	        Stop the Service.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "v",
	#     "name": "_unload",
	#     "parametersSignature": "()",
	#     "description": "\n        Stop the Service.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "_unload", [])

def _version() -> str:
	"""
	
	        Return the Service Version Number.
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "s",
	#     "name": "_version",
	#     "parametersSignature": "()",
	#     "description": "\n        Return the Service Version Number.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALStore", "_version", [])

class _Signals:
	downloadProgress: Signal[[str, int, int]] = Signal("ALStore", "downloadProgress")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str, int, int) each time the robot sends it.
	"""
	error: Signal[[]] = Signal("ALStore", "error")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	otaImageDownloaded: Signal[[str]] = Signal("ALStore", "otaImageDownloaded")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	pkgFailed: Signal[[str]] = Signal("ALStore", "pkgFailed")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	pkgInstalled: Signal[[str]] = Signal("ALStore", "pkgInstalled")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	pkgRemoved: Signal[[str]] = Signal("ALStore", "pkgRemoved")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	pkgUpdated: Signal[[str]] = Signal("ALStore", "pkgUpdated")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	progress: Signal[[str, int, int]] = Signal("ALStore", "progress")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str, int, int) each time the robot sends it.
	"""
	systemImageDownloaded: Signal[[str]] = Signal("ALStore", "systemImageDownloaded")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	updateAborted: Signal[[]] = Signal("ALStore", "updateAborted")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	updated: Signal[[]] = Signal("ALStore", "updated")
	"""
	Bridge notes
	------------
	A signal sent by ALStore on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
signals = _Signals()

class _Properties:
	lastPkgsInfoRefresh: Property[int] = Property("ALStore", "lastPkgsInfoRefresh")
	"""
	Bridge notes
	------------
	A property of ALStore on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	lastSysImgInfoRefresh: Property[int] = Property("ALStore", "lastSysImgInfoRefresh")
	"""
	Bridge notes
	------------
	A property of ALStore on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(int) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	workerPkgsState: Property[Tuple[str,str]] = Property("ALStore", "workerPkgsState")
	"""
	Bridge notes
	------------
	A property of ALStore on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(Tuple[str,str]) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
	workerSysImgState: Property[Tuple[str,str]] = Property("ALStore", "workerSysImgState")
	"""
	Bridge notes
	------------
	A property of ALStore on the robot.
	
	get() returns it, set(value) changes it, and subscribe(callback) calls callback(Tuple[str,str]) each time the robot sets it. Some properties are set regularly even when the value doesn't change.
	"""
properties = _Properties()

