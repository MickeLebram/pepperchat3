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
	return send_mfc("ALRALManagerModule", "registerEvent", [p0, p1, p2])

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
	return send_mfc("ALRALManagerModule", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("ALRALManagerModule", "metaObject", [p0])

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
	return send_mfc("ALRALManagerModule", "terminate", [p0])

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
	return send_mfc("ALRALManagerModule", "property", [p0])

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
	return send_mfc("ALRALManagerModule", "setProperty", [p0, p1])

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
	return send_mfc("ALRALManagerModule", "properties", [])

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
	return send_mfc("ALRALManagerModule", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("ALRALManagerModule", "isStatsEnabled", [])

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
	return send_mfc("ALRALManagerModule", "enableStats", [p0])

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
	return send_mfc("ALRALManagerModule", "stats", [])

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
	return send_mfc("ALRALManagerModule", "clearStats", [])

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
	return send_mfc("ALRALManagerModule", "isTraceEnabled", [])

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
	return send_mfc("ALRALManagerModule", "enableTrace", [p0])

def _finishApk() -> object:
	"""
	Finish activity.
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "m",
	    "name": "_finishApk",
	    "parametersSignature": "()",
	    "description": "Finish activity.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_finishApk", [])

def _getAbsoluteUrl(p0:object, p1:object) -> object:
	"""
	Returns the url of a file in the html directory.
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "m",
	    "name": "_getAbsoluteUrl",
	    "parametersSignature": "(mm)",
	    "description": "Returns the url of a file in the html directory.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_getAbsoluteUrl", [p0, p1])

def _onPreferenceAdded(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "m",
	    "name": "_onPreferenceAdded",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_onPreferenceAdded", [p0])

def _onPreferenceChanged(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "m",
	    "name": "_onPreferenceChanged",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_onPreferenceChanged", [p0])

def _onPreferenceDomainRemoved(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "m",
	    "name": "_onPreferenceDomainRemoved",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_onPreferenceDomainRemoved", [p0])

def _onPreferenceRemoved(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "m",
	    "name": "_onPreferenceRemoved",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_onPreferenceRemoved", [p0])

def _onPreferenceSynchronized() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "m",
	    "name": "_onPreferenceSynchronized",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_onPreferenceSynchronized", [])

def _parseXML(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "m",
	    "name": "_parseXML",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_parseXML", [p0])

def _setSubscribers() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "m",
	    "name": "_setSubscribers",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_setSubscribers", [])

def _showError(p0:object) -> object:
	"""
	Show error activity
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "m",
	    "name": "_showError",
	    "parametersSignature": "(m)",
	    "description": "Show error activity",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_showError", [p0])

def _startFade(p0:int) -> None:
	"""
	Start fade.
	
	Parameters
	----------
	p0:int
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "v",
	    "name": "_startFade",
	    "parametersSignature": "(i)",
	    "description": "Start fade.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_startFade", [p0])

def _strip_aldebaran_mail(p0:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "m",
	    "name": "_strip_aldebaran_mail",
	    "parametersSignature": "(m)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "_strip_aldebaran_mail", [p0])

def appLauncherClosed() -> object:
	"""
	Raise signal when application launcher has been closed
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "m",
	    "name": "appLauncherClosed",
	    "parametersSignature": "()",
	    "description": "Raise signal when application launcher has been closed",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "appLauncherClosed", [])

def defaultScreen() -> object:
	"""
	Show default application screen (i.e. when apps have no
	        tablet content of their own)
	        
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "m",
	    "name": "defaultScreen",
	    "parametersSignature": "()",
	    "description": "Show default application screen (i.e. when apps have no\n        tablet content of their own)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "defaultScreen", [])

def display() -> object:
	"""
	Display tablet app launcher.
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "m",
	    "name": "display",
	    "parametersSignature": "()",
	    "description": "Display tablet app launcher.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "display", [])

def emotion() -> object:
	"""
	Display emotional bubble.
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "m",
	    "name": "emotion",
	    "parametersSignature": "()",
	    "description": "Display emotional bubble.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "emotion", [])

def getAppNameByLocale(p0:object, p1:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "m",
	    "name": "getAppNameByLocale",
	    "parametersSignature": "(mm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "getAppNameByLocale", [p0, p1])

def getIgnoredApps() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "getIgnoredApps",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "getIgnoredApps", [])

def getUserOauthToken(p0:object, p1:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getUserOauthToken",
	    "parametersSignature": "(mm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "getUserOauthToken", [p0, p1])

def getUserRequestableViolations() -> object:
	"""
	Placeholder function until the permissions is updated.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "getUserRequestableViolations",
	    "parametersSignature": "()",
	    "description": "Placeholder function until the permissions is updated.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "getUserRequestableViolations", [])

def install() -> object:
	"""
	Install tablet apk.
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "m",
	    "name": "install",
	    "parametersSignature": "()",
	    "description": "Install tablet apk.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "install", [])

def isConnectedToChargingStation() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "isConnectedToChargingStation",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "isConnectedToChargingStation", [])

def onApkInstalled(p0:object) -> object:
	"""
	On apk installed on tablet.
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "onApkInstalled",
	    "parametersSignature": "(m)",
	    "description": "On apk installed on tablet.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "onApkInstalled", [p0])

def onTabletTouched(p0:object, p1:object) -> object:
	"""
	Translate the ALTabletService.onTouchDown signal into an ALMemory
	        event.
	        
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "onTabletTouched",
	    "parametersSignature": "(mm)",
	    "description": "Translate the ALTabletService.onTouchDown signal into an ALMemory\n        event.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "onTabletTouched", [p0, p1])

def removeApp(p0:object) -> object:
	"""
	Remove app by voice
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "m",
	    "name": "removeApp",
	    "parametersSignature": "(m)",
	    "description": "Remove app by voice",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "removeApp", [p0])

def restartTablet() -> object:
	"""
	"Sometimes the tablet stops working and needs a restart.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "m",
	    "name": "restartTablet",
	    "parametersSignature": "()",
	    "description": "\"Sometimes the tablet stops working and needs a restart.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "restartTablet", [])

def selectApp(p0:object, p1:object) -> object:
	"""
	Show application selection screen
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "m",
	    "name": "selectApp",
	    "parametersSignature": "(mm)",
	    "description": "Show application selection screen",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "selectApp", [p0, p1])

def startRobotApp(p0:object, p1:object, p2:object) -> object:
	"""
	
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	p2:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "m",
	    "name": "startRobotApp",
	    "parametersSignature": "(mmm)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "startRobotApp", [p0, p1, p2])

def startService() -> object:
	"""
	Start service
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "m",
	    "name": "startService",
	    "parametersSignature": "()",
	    "description": "Start service",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "startService", [])

def updateApplications_1() -> object:
	"""
	Note: This is one of the overloads of the original method (updateApplications)
	
	Update tablet application list.
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "m",
	    "name": "updateApplications",
	    "parametersSignature": "()",
	    "description": "Update tablet application list.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "updateApplications", [])

def updateApplications_2(p0:object) -> object:
	"""
	Note: This is one of the overloads of the original method (updateApplications)
	
	Update tablet application list, with specific intent.
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 131,
	    "returnSignature": "m",
	    "name": "updateApplications",
	    "parametersSignature": "(m)",
	    "description": "Update tablet application list, with specific intent.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "updateApplications", [p0])

def webview() -> object:
	"""
	Tbd.
	
	*Reference struct*
	'''
	{
	    "uid": 132,
	    "returnSignature": "m",
	    "name": "webview",
	    "parametersSignature": "()",
	    "description": "Tbd.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALRALManagerModule", "webview", [])

