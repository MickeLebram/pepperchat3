from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
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

