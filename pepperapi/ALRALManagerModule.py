"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

def _finishApk() -> object:
	"""
	Finish activity.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "m",
	#     "name": "_finishApk",
	#     "parametersSignature": "()",
	#     "description": "Finish activity.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_finishApk", [])

def _getAbsoluteUrl(p0:object, p1:object) -> object:
	"""
	Returns the url of a file in the html directory.
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "m",
	#     "name": "_getAbsoluteUrl",
	#     "parametersSignature": "(mm)",
	#     "description": "Returns the url of a file in the html directory.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_getAbsoluteUrl", [p0, p1])

def _onPreferenceAdded(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "m",
	#     "name": "_onPreferenceAdded",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_onPreferenceAdded", [p0])

def _onPreferenceChanged(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "m",
	#     "name": "_onPreferenceChanged",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_onPreferenceChanged", [p0])

def _onPreferenceDomainRemoved(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "m",
	#     "name": "_onPreferenceDomainRemoved",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_onPreferenceDomainRemoved", [p0])

def _onPreferenceRemoved(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "m",
	#     "name": "_onPreferenceRemoved",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_onPreferenceRemoved", [p0])

def _onPreferenceSynchronized() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "m",
	#     "name": "_onPreferenceSynchronized",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_onPreferenceSynchronized", [])

def _parseXML(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "m",
	#     "name": "_parseXML",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_parseXML", [p0])

def _setSubscribers() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "m",
	#     "name": "_setSubscribers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_setSubscribers", [])

def _showError(p0:object) -> object:
	"""
	Show error activity
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "m",
	#     "name": "_showError",
	#     "parametersSignature": "(m)",
	#     "description": "Show error activity",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_showError", [p0])

def _startFade(p0:int) -> None:
	"""
	Start fade.
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "_startFade",
	#     "parametersSignature": "(i)",
	#     "description": "Start fade.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_startFade", [p0])

def _strip_aldebaran_mail(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "m",
	#     "name": "_strip_aldebaran_mail",
	#     "parametersSignature": "(m)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "_strip_aldebaran_mail", [p0])

def appLauncherClosed() -> object:
	"""
	Raise signal when application launcher has been closed
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "m",
	#     "name": "appLauncherClosed",
	#     "parametersSignature": "()",
	#     "description": "Raise signal when application launcher has been closed",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "appLauncherClosed", [])

def defaultScreen() -> object:
	"""
	Show default application screen (i.e. when apps have no
	        tablet content of their own)
	        
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "m",
	#     "name": "defaultScreen",
	#     "parametersSignature": "()",
	#     "description": "Show default application screen (i.e. when apps have no\n        tablet content of their own)\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "defaultScreen", [])

def display() -> object:
	"""
	Display tablet app launcher.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "m",
	#     "name": "display",
	#     "parametersSignature": "()",
	#     "description": "Display tablet app launcher.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "display", [])

def emotion() -> object:
	"""
	Display emotional bubble.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "m",
	#     "name": "emotion",
	#     "parametersSignature": "()",
	#     "description": "Display emotional bubble.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "emotion", [])

def getAppNameByLocale(p0:object, p1:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "getAppNameByLocale",
	#     "parametersSignature": "(mm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "getAppNameByLocale", [p0, p1])

def getIgnoredApps() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "getIgnoredApps",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "getIgnoredApps", [])

def getUserOauthToken(p0:object, p1:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "getUserOauthToken",
	#     "parametersSignature": "(mm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "getUserOauthToken", [p0, p1])

def getUserRequestableViolations() -> object:
	"""
	Placeholder function until the permissions is updated.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "m",
	#     "name": "getUserRequestableViolations",
	#     "parametersSignature": "()",
	#     "description": "Placeholder function until the permissions is updated.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "getUserRequestableViolations", [])

def install() -> object:
	"""
	Install tablet apk.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "install",
	#     "parametersSignature": "()",
	#     "description": "Install tablet apk.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "install", [])

def isConnectedToChargingStation() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "m",
	#     "name": "isConnectedToChargingStation",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "isConnectedToChargingStation", [])

def onApkInstalled(p0:object) -> object:
	"""
	On apk installed on tablet.
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "onApkInstalled",
	#     "parametersSignature": "(m)",
	#     "description": "On apk installed on tablet.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "onApkInstalled", [p0])

def onTabletTouched(p0:object, p1:object) -> object:
	"""
	Translate the ALTabletService.onTouchDown signal into an ALMemory
	        event.
	        
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "m",
	#     "name": "onTabletTouched",
	#     "parametersSignature": "(mm)",
	#     "description": "Translate the ALTabletService.onTouchDown signal into an ALMemory\n        event.\n        ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "onTabletTouched", [p0, p1])

def removeApp(p0:object) -> object:
	"""
	Remove app by voice
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "m",
	#     "name": "removeApp",
	#     "parametersSignature": "(m)",
	#     "description": "Remove app by voice",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "removeApp", [p0])

def restartTablet() -> object:
	"""
	"Sometimes the tablet stops working and needs a restart.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "m",
	#     "name": "restartTablet",
	#     "parametersSignature": "()",
	#     "description": "\"Sometimes the tablet stops working and needs a restart.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "restartTablet", [])

def selectApp(p0:object, p1:object) -> object:
	"""
	Show application selection screen
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "m",
	#     "name": "selectApp",
	#     "parametersSignature": "(mm)",
	#     "description": "Show application selection screen",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "selectApp", [p0, p1])

def startRobotApp(p0:object, p1:object, p2:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	p2:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "m",
	#     "name": "startRobotApp",
	#     "parametersSignature": "(mmm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "startRobotApp", [p0, p1, p2])

def startService() -> object:
	"""
	Start service
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "m",
	#     "name": "startService",
	#     "parametersSignature": "()",
	#     "description": "Start service",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "startService", [])

@overload
def updateApplications() -> object:
	"""
	Update tablet application list.
	
	Bridge notes
	------------
	updateApplications has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "m",
	#     "name": "updateApplications",
	#     "parametersSignature": "()",
	#     "description": "Update tablet application list.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def updateApplications(p0:object, /) -> object:
	"""
	Update tablet application list, with specific intent.
	
	Parameters
	----------
	p0:object
		
	
	Bridge notes
	------------
	updateApplications has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "m",
	#     "name": "updateApplications",
	#     "parametersSignature": "(m)",
	#     "description": "Update tablet application list, with specific intent.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def updateApplications(*args, **kwargs):
	"""
	Bridge notes
	------------
	updateApplications has 2 variants on the robot:
	- updateApplications()
	- updateApplications(p0:object)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALRALManagerModule.updateApplications has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALRALManagerModule", "updateApplications", list(args))

def webview() -> object:
	"""
	Tbd.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "m",
	#     "name": "webview",
	#     "parametersSignature": "()",
	#     "description": "Tbd.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALRALManagerModule", "webview", [])

class _Signals:
	_activityRequestedByUser: Signal[[str]] = Signal("ALRALManagerModule", "_activityRequestedByUser")
	"""
	Bridge notes
	------------
	A signal sent by ALRALManagerModule on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
signals = _Signals()

