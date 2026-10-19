"""

"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method
from .robot_client import Signal, Property

@overload
def showWebview() -> bool:
	"""
	Show Webview (with app-specific content)
	
	Bridge notes
	------------
	showWebview has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "b",
	#     "name": "showWebview",
	#     "parametersSignature": "()",
	#     "description": "Show Webview (with app-specific content)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def showWebview(p0:str, /) -> bool:
	"""
	Show Webview and load the url
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	showWebview has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 101,
	#     "returnSignature": "b",
	#     "name": "showWebview",
	#     "parametersSignature": "(s)",
	#     "description": "Show Webview and load the url",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def showWebview(*args, **kwargs):
	"""
	Bridge notes
	------------
	showWebview has 2 variants on the robot:
	- showWebview()
	- showWebview(p0:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALTabletService.showWebview has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALTabletService", "showWebview", list(args))

def loadUrl(p0:str) -> bool:
	"""
	Load URL on tablet
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "loadUrl",
	#     "parametersSignature": "(s)",
	#     "description": "Load URL on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "loadUrl", [p0])

def reloadPage(p0:bool) -> None:
	"""
	Reload current displayed web page
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "v",
	#     "name": "reloadPage",
	#     "parametersSignature": "(b)",
	#     "description": "Reload current displayed web page",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "reloadPage", [p0])

def loadApplication(p0:str) -> bool:
	"""
	Start application on tablet
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "loadApplication",
	#     "parametersSignature": "(s)",
	#     "description": "Start application on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "loadApplication", [p0])

def hideWebview() -> bool:
	"""
	Hide Webview 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "b",
	#     "name": "hideWebview",
	#     "parametersSignature": "()",
	#     "description": "Hide Webview ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "hideWebview", [])

def cleanWebview() -> None:
	"""
	Clean Webview 
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "v",
	#     "name": "cleanWebview",
	#     "parametersSignature": "()",
	#     "description": "Clean Webview ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "cleanWebview", [])

def _clearWebviewCache(p0:bool) -> None:
	"""
	Clear the cache of the webview, false : just RAM, true DISK FILES also
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "v",
	#     "name": "_clearWebviewCache",
	#     "parametersSignature": "(b)",
	#     "description": "Clear the cache of the webview, false : just RAM, true DISK FILES also",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_clearWebviewCache", [p0])

def executeJS(p0:str) -> None:
	"""
	Execute javascript 
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "v",
	#     "name": "executeJS",
	#     "parametersSignature": "(s)",
	#     "description": "Execute javascript ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "executeJS", [p0])

def _setAnimatedCrossWalkView(p0:bool) -> None:
	"""
	CrossWalk animated render mode (can make the webview crash)
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "v",
	#     "name": "_setAnimatedCrossWalkView",
	#     "parametersSignature": "(b)",
	#     "description": "CrossWalk animated render mode (can make the webview crash)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setAnimatedCrossWalkView", [p0])

def _setDebugCrossWalkViewEnable(p0:bool) -> None:
	"""
	CrossWalk animated render mode (can make the webview crash)
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "v",
	#     "name": "_setDebugCrossWalkViewEnable",
	#     "parametersSignature": "(b)",
	#     "description": "CrossWalk animated render mode (can make the webview crash)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setDebugCrossWalkViewEnable", [p0])

def setOnTouchWebviewScaleFactor(p0:float) -> None:
	"""
	Change the onTouch webview scale factor. Default is 1.34 so the viewport is 1707 × 1067
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "v",
	#     "name": "setOnTouchWebviewScaleFactor",
	#     "parametersSignature": "(f)",
	#     "description": "Change the onTouch webview scale factor. Default is 1.34 so the viewport is 1707 \u00d7 1067",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setOnTouchWebviewScaleFactor", [p0])

def getOnTouchScaleFactor() -> float:
	"""
	get the onTouch scale factor for current view, by default 1.34 for the webview and 1 for the other views
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "f",
	#     "name": "getOnTouchScaleFactor",
	#     "parametersSignature": "()",
	#     "description": "get the onTouch scale factor for current view, by default 1.34 for the webview and 1 for the other views",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getOnTouchScaleFactor", [])

def playVideo(p0:str) -> bool:
	"""
	Play video on tablet
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "b",
	#     "name": "playVideo",
	#     "parametersSignature": "(s)",
	#     "description": "Play video on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "playVideo", [p0])

def resumeVideo() -> bool:
	"""
	Resume video on tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "b",
	#     "name": "resumeVideo",
	#     "parametersSignature": "()",
	#     "description": "Resume video on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "resumeVideo", [])

def pauseVideo() -> bool:
	"""
	Pause video activity on tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "b",
	#     "name": "pauseVideo",
	#     "parametersSignature": "()",
	#     "description": "Pause video activity on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "pauseVideo", [])

def stopVideo() -> bool:
	"""
	Stop video activity on tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "stopVideo",
	#     "parametersSignature": "()",
	#     "description": "Stop video activity on tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "stopVideo", [])

def getVideoPosition() -> int:
	"""
	Get video position (in ms from beginning)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "getVideoPosition",
	#     "parametersSignature": "()",
	#     "description": "Get video position (in ms from beginning)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getVideoPosition", [])

def getVideoLength() -> int:
	"""
	Get video length (in ms)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "i",
	#     "name": "getVideoLength",
	#     "parametersSignature": "()",
	#     "description": "Get video length (in ms)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getVideoLength", [])

def preLoadImage(p0:str) -> bool:
	"""
	preload an image
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "preLoadImage",
	#     "parametersSignature": "(s)",
	#     "description": "preload an image",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "preLoadImage", [p0])

def showImage(p0:str) -> bool:
	"""
	show an image
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "b",
	#     "name": "showImage",
	#     "parametersSignature": "(s)",
	#     "description": "show an image",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "showImage", [p0])

def showImageNoCache(p0:str) -> bool:
	"""
	show an image, disable tablet cache
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "showImageNoCache",
	#     "parametersSignature": "(s)",
	#     "description": "show an image, disable tablet cache",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "showImageNoCache", [p0])

def hideImage() -> None:
	"""
	Hide an image
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "hideImage",
	#     "parametersSignature": "()",
	#     "description": "Hide an image",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "hideImage", [])

def resumeGif() -> None:
	"""
	resume the gif
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "resumeGif",
	#     "parametersSignature": "()",
	#     "description": "resume the gif",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "resumeGif", [])

def pauseGif() -> None:
	"""
	pause the gif
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "pauseGif",
	#     "parametersSignature": "()",
	#     "description": "pause the gif",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "pauseGif", [])

def setBackgroundColor(p0:str) -> bool:
	"""
	Set the background color for image
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "b",
	#     "name": "setBackgroundColor",
	#     "parametersSignature": "(s)",
	#     "description": "Set the background color for image",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setBackgroundColor", [p0])

def _startAnimation(p0:str) -> bool:
	"""
	Show a flash animation
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "b",
	#     "name": "_startAnimation",
	#     "parametersSignature": "(s)",
	#     "description": "Show a flash animation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_startAnimation", [p0])

def _stopAnimation() -> None:
	"""
	Hide a flash animation
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "_stopAnimation",
	#     "parametersSignature": "()",
	#     "description": "Hide a flash animation",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_stopAnimation", [])

def hide() -> None:
	"""
	hide the top view
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "hide",
	#     "parametersSignature": "()",
	#     "description": "hide the top view",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "hide", [])

def setBrightness(p0:float) -> bool:
	"""
	Change screen brightness
	
	Parameters
	----------
	p0:float
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "b",
	#     "name": "setBrightness",
	#     "parametersSignature": "(f)",
	#     "description": "Change screen brightness",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setBrightness", [p0])

def getBrightness() -> float:
	"""
	Change screen brightness
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "f",
	#     "name": "getBrightness",
	#     "parametersSignature": "()",
	#     "description": "Change screen brightness",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getBrightness", [])

def turnScreenOn(p0:bool) -> None:
	"""
	Turn on (true) / off (false)  the screen
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "turnScreenOn",
	#     "parametersSignature": "(b)",
	#     "description": "Turn on (true) / off (false)  the screen",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "turnScreenOn", [p0])

def goToSleep() -> None:
	"""
	Put the tablet in sleep mode (standby mode)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "goToSleep",
	#     "parametersSignature": "()",
	#     "description": "Put the tablet in sleep mode (standby mode)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "goToSleep", [])

def wakeUp() -> None:
	"""
	Put the tablet in wake mode (standby mode)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "wakeUp",
	#     "parametersSignature": "()",
	#     "description": "Put the tablet in wake mode (standby mode)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "wakeUp", [])

@overload
def _displayToast(p0:str, p1:int, /) -> None:
	"""
	Display an android Toast: 1) Text to display 2) Duration 1 long, 0 short
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	
	Bridge notes
	------------
	_displayToast has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "_displayToast",
	#     "parametersSignature": "(si)",
	#     "description": "Display an android Toast: 1) Text to display 2) Duration 1 long, 0 short",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _displayToast(p0:str, p1:int, p2:int, /) -> None:
	"""
	Display an android Toast: 1) Text to display 2) Duration 1 long, 0 short 3) Text size
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	p2:int
		
	
	Bridge notes
	------------
	_displayToast has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "v",
	#     "name": "_displayToast",
	#     "parametersSignature": "(sii)",
	#     "description": "Display an android Toast: 1) Text to display 2) Duration 1 long, 0 short 3) Text size",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _displayToast(*args, **kwargs):
	"""
	Bridge notes
	------------
	_displayToast has 2 variants on the robot:
	- _displayToast(p0:str, p1:int)
	- _displayToast(p0:str, p1:int, p2:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALTabletService._displayToast has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALTabletService", "_displayToast", list(args))

def getWifiStatus() -> str:
	"""
	Check the WIFI on the tablet : IDLE, SCANNING, DISCONNECTED, CONNECTED
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "s",
	#     "name": "getWifiStatus",
	#     "parametersSignature": "()",
	#     "description": "Check the WIFI on the tablet : IDLE, SCANNING, DISCONNECTED, CONNECTED",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getWifiStatus", [])

def enableWifi() -> None:
	"""
	Enable the wifi on the tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "v",
	#     "name": "enableWifi",
	#     "parametersSignature": "()",
	#     "description": "Enable the wifi on the tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "enableWifi", [])

def disableWifi() -> None:
	"""
	Disable the wifi on the tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "v",
	#     "name": "disableWifi",
	#     "parametersSignature": "()",
	#     "description": "Disable the wifi on the tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "disableWifi", [])

def forgetWifi(p0:str) -> bool:
	"""
	Forget the wifi : 1) SSID
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "forgetWifi",
	#     "parametersSignature": "(s)",
	#     "description": "Forget the wifi : 1) SSID",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "forgetWifi", [p0])

def connectWifi(p0:str) -> bool:
	"""
	Try to connect to the wifi by is SSID
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "connectWifi",
	#     "parametersSignature": "(s)",
	#     "description": "Try to connect to the wifi by is SSID",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "connectWifi", [p0])

def disconnectWifi() -> bool:
	"""
	Disconnect current wifi
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "b",
	#     "name": "disconnectWifi",
	#     "parametersSignature": "()",
	#     "description": "Disconnect current wifi",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "disconnectWifi", [])

def configureWifi(p0:str, p1:str, p2:str) -> bool:
	"""
	Configure the WIFI, arguments: 
	       1) is type among (wep, wpa, open) 
	       2) is the wifi SSID 
	       3) is wep or wap passphrase 
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "b",
	#     "name": "configureWifi",
	#     "parametersSignature": "(sss)",
	#     "description": "Configure the WIFI, arguments: \n       1) is type among (wep, wpa, open) \n       2) is the wifi SSID \n       3) is wep or wap passphrase \n",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "configureWifi", [p0, p1, p2])

def getWifiMacAddress() -> str:
	"""
	Get the wifi mac address
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "s",
	#     "name": "getWifiMacAddress",
	#     "parametersSignature": "()",
	#     "description": "Get the wifi mac address",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getWifiMacAddress", [])

@overload
def showInputTextDialog(p0:str, p1:str, p2:str, /) -> None:
	"""
	Show a input text dialog, arguments 
	       1) the title 
	       2) is the ok text  
	       3) the cancel text 
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	Bridge notes
	------------
	showInputTextDialog has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "v",
	#     "name": "showInputTextDialog",
	#     "parametersSignature": "(sss)",
	#     "description": "Show a input text dialog, arguments \n       1) the title \n       2) is the ok text  \n       3) the cancel text ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def showInputTextDialog(p0:str, p1:str, p2:str, p3:str, p4:int, /) -> None:
	"""
	Show a input text dialog, arguments 
	       1) the title 
	       2) is the ok text  
	       3) the cancel text 
	       4) the pre-filled text of the input field 
	       5) input characters limit
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	p4:int
		
	
	Bridge notes
	------------
	showInputTextDialog has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "showInputTextDialog",
	#     "parametersSignature": "(ssssi)",
	#     "description": "Show a input text dialog, arguments \n       1) the title \n       2) is the ok text  \n       3) the cancel text \n       4) the pre-filled text of the input field \n       5) input characters limit",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def showInputTextDialog(*args, **kwargs):
	"""
	Bridge notes
	------------
	showInputTextDialog has 2 variants on the robot:
	- showInputTextDialog(p0:str, p1:str, p2:str)
	- showInputTextDialog(p0:str, p1:str, p2:str, p3:str, p4:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALTabletService.showInputTextDialog has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALTabletService", "showInputTextDialog", list(args))

@overload
def showInputDialog(p0:str, p1:str, p2:str, p3:str, /) -> None:
	"""
	Show a input text dialog, arguments : 
	       1) is type among text, password, email, url, number 
	       2) the title 
	       3) is the ok text 
	       4) the cancel text
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	
	Bridge notes
	------------
	showInputDialog has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "showInputDialog",
	#     "parametersSignature": "(ssss)",
	#     "description": "Show a input text dialog, arguments : \n       1) is type among text, password, email, url, number \n       2) the title \n       3) is the ok text \n       4) the cancel text",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def showInputDialog(p0:str, p1:str, p2:str, p3:str, p4:str, p5:int, /) -> None:
	"""
	Show a input text dialog, arguments 
	       1) is type among text, password, email, url, number 
	       2) the title 
	       3) is the ok text 
	       4) the cancel text 
	       5) the pre-filled text of the input field, use '' if you don't want any 
	       6) input characters limit, use -1 if you don't want a limit
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	p4:str
		
	p5:int
		
	
	Bridge notes
	------------
	showInputDialog has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "v",
	#     "name": "showInputDialog",
	#     "parametersSignature": "(sssssi)",
	#     "description": "Show a input text dialog, arguments \n       1) is type among text, password, email, url, number \n       2) the title \n       3) is the ok text \n       4) the cancel text \n       5) the pre-filled text of the input field, use '' if you don't want any \n       6) input characters limit, use -1 if you don't want a limit",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def showInputDialog(*args, **kwargs):
	"""
	Bridge notes
	------------
	showInputDialog has 2 variants on the robot:
	- showInputDialog(p0:str, p1:str, p2:str, p3:str)
	- showInputDialog(p0:str, p1:str, p2:str, p3:str, p4:str, p5:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALTabletService.showInputDialog has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALTabletService", "showInputDialog", list(args))

def showAlertView(p0:float, p1:str, p2:int) -> None:
	"""
	Test debug function
	
	Parameters
	----------
	p0:float
		
	p1:str
		
	p2:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "v",
	#     "name": "showAlertView",
	#     "parametersSignature": "(fsi)",
	#     "description": "Test debug function",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "showAlertView", [p0, p1, p2])

def hideDialog() -> None:
	"""
	Hide the dialog view
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "v",
	#     "name": "hideDialog",
	#     "parametersSignature": "()",
	#     "description": "Hide the dialog view",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "hideDialog", [])

def setKeyboard(p0:str) -> bool:
	"""
	Set keyboard using is keyboard id from getAvailableKeyboards
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "b",
	#     "name": "setKeyboard",
	#     "parametersSignature": "(s)",
	#     "description": "Set keyboard using is keyboard id from getAvailableKeyboards",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setKeyboard", [p0])

def getAvailableKeyboards() -> List[str]:
	"""
	get available keyboards
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "[s]",
	#     "name": "getAvailableKeyboards",
	#     "parametersSignature": "()",
	#     "description": "get available keyboards",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getAvailableKeyboards", [])

def setTabletLanguage(p0:str) -> bool:
	"""
	Change the tablet language: fr, fr_FR, en, us, it, ja ... 
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "b",
	#     "name": "setTabletLanguage",
	#     "parametersSignature": "(s)",
	#     "description": "Change the tablet language: fr, fr_FR, en, us, it, ja ... ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setTabletLanguage", [p0])

def _openSettings() -> None:
	"""
	Open android settings
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "v",
	#     "name": "_openSettings",
	#     "parametersSignature": "()",
	#     "description": "Open android settings",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_openSettings", [])

def setVolume(p0:int) -> bool:
	"""
	Set the volume of the tablet between 0 and 15
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "b",
	#     "name": "setVolume",
	#     "parametersSignature": "(i)",
	#     "description": "Set the volume of the tablet between 0 and 15",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "setVolume", [p0])

def _setDebugEnabled(p0:bool) -> None:
	"""
	Enable debug menu.
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "v",
	#     "name": "_setDebugEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Enable debug menu.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setDebugEnabled", [p0])

def _setTimeZone(p0:str) -> None:
	"""
	Set the system time zone (Ex: Europe/Paris)
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "v",
	#     "name": "_setTimeZone",
	#     "parametersSignature": "(s)",
	#     "description": "Set the system time zone (Ex: Europe/Paris)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setTimeZone", [p0])

def _getAutoDateTimeEnabled() -> bool:
	"""
	Get the value of the "Automatic Date/Time" setting
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "b",
	#     "name": "_getAutoDateTimeEnabled",
	#     "parametersSignature": "()",
	#     "description": "Get the value of the \"Automatic Date/Time\" setting",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_getAutoDateTimeEnabled", [])

def _setAutoDateTimeEnabled(p0:bool) -> None:
	"""
	Set the "Automatic Date/Time" setting
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "v",
	#     "name": "_setAutoDateTimeEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Set the \"Automatic Date/Time\" setting",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setAutoDateTimeEnabled", [p0])

def _setStackTraceDepth(p0:int) -> bool:
	"""
	Number of lines that will be send for java stacktrace, current is 
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "b",
	#     "name": "_setStackTraceDepth",
	#     "parametersSignature": "(i)",
	#     "description": "Number of lines that will be send for java stacktrace, current is ",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setStackTraceDepth", [p0])

def _ping() -> str:
	"""
	Simple ping/pong method. Return 'pong'
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "s",
	#     "name": "_ping",
	#     "parametersSignature": "()",
	#     "description": "Simple ping/pong method. Return 'pong'",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_ping", [])

def robotIp() -> str:
	"""
	Get IP of connected robot
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "s",
	#     "name": "robotIp",
	#     "parametersSignature": "()",
	#     "description": "Get IP of connected robot",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "robotIp", [])

def getCurrentLifeActivity() -> str:
	"""
	Return the current life activity running
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "s",
	#     "name": "getCurrentLifeActivity",
	#     "parametersSignature": "()",
	#     "description": "Return the current life activity running",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "getCurrentLifeActivity", [])

def version() -> str:
	"""
	Return service version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 163,
	#     "returnSignature": "s",
	#     "name": "version",
	#     "parametersSignature": "()",
	#     "description": "Return service version",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "version", [])

def _firmwareVersion() -> str:
	"""
	Return android firmware version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "s",
	#     "name": "_firmwareVersion",
	#     "parametersSignature": "()",
	#     "description": "Return android firmware version",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_firmwareVersion", [])

def _launcherVersion() -> str:
	"""
	Return launcher version
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "s",
	#     "name": "_launcherVersion",
	#     "parametersSignature": "()",
	#     "description": "Return launcher version",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_launcherVersion", [])

def resetTablet() -> None:
	"""
	reset the tablet (get back to the bubble views and clear everything)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 166,
	#     "returnSignature": "v",
	#     "name": "resetTablet",
	#     "parametersSignature": "()",
	#     "description": "reset the tablet (get back to the bubble views and clear everything)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "resetTablet", [])

def _enableResetTablet(p0:bool) -> None:
	"""
	enable reset tablet command (true by default)
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "v",
	#     "name": "_enableResetTablet",
	#     "parametersSignature": "(b)",
	#     "description": "enable reset tablet command (true by default)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_enableResetTablet", [p0])

def _cancelReset() -> None:
	"""
	Cancel reset tablet (standby mode)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "v",
	#     "name": "_cancelReset",
	#     "parametersSignature": "()",
	#     "description": "Cancel reset tablet (standby mode)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_cancelReset", [])

def _setPreventCommandScreenOff(p0:bool) -> None:
	"""
	Prevent to run command if screen is turn off, default is true
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "v",
	#     "name": "_setPreventCommandScreenOff",
	#     "parametersSignature": "(b)",
	#     "description": "Prevent to run command if screen is turn off, default is true",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setPreventCommandScreenOff", [p0])

def _setOpenGLState(p0:int) -> None:
	"""
	Set custom Open GL state
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "v",
	#     "name": "_setOpenGLState",
	#     "parametersSignature": "(i)",
	#     "description": "Set custom Open GL state",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setOpenGLState", [p0])

def _setBlackScreenMode(p0:bool) -> None:
	"""
	Set if we use a black screen to turn off the screen
	
	Parameters
	----------
	p0:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "v",
	#     "name": "_setBlackScreenMode",
	#     "parametersSignature": "(b)",
	#     "description": "Set if we use a black screen to turn off the screen",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_setBlackScreenMode", [p0])

def _update() -> bool:
	"""
	Update browser service
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "b",
	#     "name": "_update",
	#     "parametersSignature": "()",
	#     "description": "Update browser service",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_update", [])

def _updateFirmware(p0:str) -> bool:
	"""
	Update the android firmware from robot url
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "b",
	#     "name": "_updateFirmware",
	#     "parametersSignature": "(s)",
	#     "description": "Update the android firmware from robot url",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_updateFirmware", [p0])

def _uninstallApps() -> None:
	"""
	Uninstall both the launcher and the browser
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "v",
	#     "name": "_uninstallApps",
	#     "parametersSignature": "()",
	#     "description": "Uninstall both the launcher and the browser",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_uninstallApps", [])

def _uninstallLauncher() -> None:
	"""
	Uninstall the launcher
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "v",
	#     "name": "_uninstallLauncher",
	#     "parametersSignature": "()",
	#     "description": "Uninstall the launcher",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_uninstallLauncher", [])

def _uninstallBrowser() -> None:
	"""
	Uninstall the browser
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "v",
	#     "name": "_uninstallBrowser",
	#     "parametersSignature": "()",
	#     "description": "Uninstall the browser",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_uninstallBrowser", [])

def _wipeData() -> None:
	"""
	Wipe all the data
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "v",
	#     "name": "_wipeData",
	#     "parametersSignature": "()",
	#     "description": "Wipe all the data",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_wipeData", [])

def _restart() -> None:
	"""
	Restart the browser application
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "v",
	#     "name": "_restart",
	#     "parametersSignature": "()",
	#     "description": "Restart the browser application",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_restart", [])

def _powerOff() -> None:
	"""
	Turn off the tablet
	"""
	# NAOqi metadata:
	# {
	#     "uid": 179,
	#     "returnSignature": "v",
	#     "name": "_powerOff",
	#     "parametersSignature": "()",
	#     "description": "Turn off the tablet",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_powerOff", [])

def _installApk(p0:str) -> bool:
	"""
	Install an android APK using an url
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "b",
	#     "name": "_installApk",
	#     "parametersSignature": "(s)",
	#     "description": "Install an android APK using an url",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_installApk", [p0])

def _installSystemApk(p0:str) -> bool:
	"""
	Install an android APK with system right using an url
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "b",
	#     "name": "_installSystemApk",
	#     "parametersSignature": "(s)",
	#     "description": "Install an android APK with system right using an url",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_installSystemApk", [p0])

def _launchApk(p0:str) -> bool:
	"""
	Launch an android APK using his package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "b",
	#     "name": "_launchApk",
	#     "parametersSignature": "(s)",
	#     "description": "Launch an android APK using his package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_launchApk", [p0])

def _removeApk(p0:str) -> None:
	"""
	Remove an android APK using his package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "v",
	#     "name": "_removeApk",
	#     "parametersSignature": "(s)",
	#     "description": "Remove an android APK using his package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_removeApk", [p0])

def _listApks() -> str:
	"""
	List all apks on the tablet (return package names)
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "s",
	#     "name": "_listApks",
	#     "parametersSignature": "()",
	#     "description": "List all apks on the tablet (return package names)",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_listApks", [])

def _stopApk(p0:str) -> None:
	"""
	Stop APK given is package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 185,
	#     "returnSignature": "v",
	#     "name": "_stopApk",
	#     "parametersSignature": "(s)",
	#     "description": "Stop APK given is package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_stopApk", [p0])

def _isApkExist(p0:str) -> bool:
	"""
	Test is apk installed using his package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 186,
	#     "returnSignature": "b",
	#     "name": "_isApkExist",
	#     "parametersSignature": "(s)",
	#     "description": "Test is apk installed using his package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_isApkExist", [p0])

def _getApkVersion(p0:str) -> str:
	"""
	Get apk version using his package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 187,
	#     "returnSignature": "s",
	#     "name": "_getApkVersion",
	#     "parametersSignature": "(s)",
	#     "description": "Get apk version using his package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_getApkVersion", [p0])

def _purgeInstallTabletUpdater() -> bool:
	"""
	Fetches apk from URL, installs it and start update procedure
	"""
	# NAOqi metadata:
	# {
	#     "uid": 188,
	#     "returnSignature": "b",
	#     "name": "_purgeInstallTabletUpdater",
	#     "parametersSignature": "()",
	#     "description": "Fetches apk from URL, installs it and start update procedure",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_purgeInstallTabletUpdater", [])

def _test() -> str:
	"""
	test function
	"""
	# NAOqi metadata:
	# {
	#     "uid": 189,
	#     "returnSignature": "s",
	#     "name": "_test",
	#     "parametersSignature": "()",
	#     "description": "test function",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_test", [])

def _crash() -> None:
	"""
	Crash the browser
	"""
	# NAOqi metadata:
	# {
	#     "uid": 190,
	#     "returnSignature": "v",
	#     "name": "_crash",
	#     "parametersSignature": "()",
	#     "description": "Crash the browser",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_crash", [])

def _getApkVersionCode(p0:str) -> str:
	"""
	Get apk version code using his package name
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 197,
	#     "returnSignature": "s",
	#     "name": "_getApkVersionCode",
	#     "parametersSignature": "(s)",
	#     "description": "Get apk version code using his package name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_getApkVersionCode", [p0])

def _isTopActivity(p0:str, p1:str) -> bool:
	"""
	is top activity
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 198,
	#     "returnSignature": "b",
	#     "name": "_isTopActivity",
	#     "parametersSignature": "(ss)",
	#     "description": "is top activity",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_isTopActivity", [p0, p1])

def _getTabletSerialno() -> str:
	"""
	get Tablet Serial-No
	"""
	# NAOqi metadata:
	# {
	#     "uid": 199,
	#     "returnSignature": "s",
	#     "name": "_getTabletSerialno",
	#     "parametersSignature": "()",
	#     "description": "get Tablet Serial-No",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_getTabletSerialno", [])

def _getTabletModelName() -> str:
	"""
	get Tablet Model Name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 200,
	#     "returnSignature": "s",
	#     "name": "_getTabletModelName",
	#     "parametersSignature": "()",
	#     "description": "get Tablet Model Name",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_getTabletModelName", [])

def _isTopApp(p0:str) -> bool:
	"""
	is top application
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 201,
	#     "returnSignature": "b",
	#     "name": "_isTopApp",
	#     "parametersSignature": "(s)",
	#     "description": "is top application",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_isTopApp", [p0])

def _startExtendedTabletService() -> bool:
	"""
	start ExtendedTabletService
	"""
	# NAOqi metadata:
	# {
	#     "uid": 202,
	#     "returnSignature": "b",
	#     "name": "_startExtendedTabletService",
	#     "parametersSignature": "()",
	#     "description": "start ExtendedTabletService",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALTabletService", "_startExtendedTabletService", [])

class _Signals:
	onTouch: Signal[[float, float]] = Signal("ALTabletService", "onTouch")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(float, float) each time the robot sends it.
	"""
	onTouchDown: Signal[[float, float]] = Signal("ALTabletService", "onTouchDown")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(float, float) each time the robot sends it.
	"""
	onTouchDownRatio: Signal[[float, float, str]] = Signal("ALTabletService", "onTouchDownRatio")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(float, float, str) each time the robot sends it.
	"""
	onTouchUp: Signal[[float, float]] = Signal("ALTabletService", "onTouchUp")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(float, float) each time the robot sends it.
	"""
	onTouchMove: Signal[[float, float]] = Signal("ALTabletService", "onTouchMove")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(float, float) each time the robot sends it.
	"""
	videoFinished: Signal[[]] = Signal("ALTabletService", "videoFinished")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	videoStarted: Signal[[]] = Signal("ALTabletService", "videoStarted")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	onPageStarted: Signal[[]] = Signal("ALTabletService", "onPageStarted")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	onPageFinished: Signal[[]] = Signal("ALTabletService", "onPageFinished")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	onLoadPageError: Signal[[int, str, str]] = Signal("ALTabletService", "onLoadPageError")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(int, str, str) each time the robot sends it.
	"""
	onWifiStatusChange: Signal[[str]] = Signal("ALTabletService", "onWifiStatusChange")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	onConsoleMessage: Signal[[str]] = Signal("ALTabletService", "onConsoleMessage")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	onInputText: Signal[[int, str]] = Signal("ALTabletService", "onInputText")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(int, str) each time the robot sends it.
	"""
	onApkInstalled: Signal[[str]] = Signal("ALTabletService", "onApkInstalled")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
	onImageLoaded: Signal[[]] = Signal("ALTabletService", "onImageLoaded")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback() each time the robot sends it.
	"""
	onJSEvent: Signal[[str]] = Signal("ALTabletService", "onJSEvent")
	"""
	Bridge notes
	------------
	A signal sent by ALTabletService on the robot.
	
	subscribe(callback) calls callback(str) each time the robot sends it.
	"""
signals = _Signals()

