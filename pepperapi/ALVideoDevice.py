"""
ALVideoDevice, formerly called Video Input systemis architectured in order to provide every client related to vision, a direct access to raw images from video source, or an access to images transformed in the requested format.
  Extension name of the methods providing images depends on wether clients are local (dynamic library) or remote (executable).
"""
from __future__ import annotations
from typing import Any, Dict, List, Tuple, overload
from .robot_client import call_method

def version() -> str:
	"""
	Returns the version of the module.
	
	Returns
	----------
	A string containing the version of the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "s",
	#     "name": "version",
	#     "parametersSignature": "()",
	#     "description": "Returns the version of the module.",
	#     "parameters": [],
	#     "returnDescription": "A string containing the version of the module."
	# }
	return call_method("ALVideoDevice", "version", [])

def ping() -> bool:
	"""
	Just a ping. Always returns true
	
	Returns
	----------
	returns true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "ping",
	#     "parametersSignature": "()",
	#     "description": "Just a ping. Always returns true",
	#     "parameters": [],
	#     "returnDescription": "returns true"
	# }
	return call_method("ALVideoDevice", "ping", [])

def getMethodList() -> List[str]:
	"""
	Retrieves the module's method list.
	
	Returns
	----------
	An array of method names.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "[s]",
	#     "name": "getMethodList",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's method list.",
	#     "parameters": [],
	#     "returnDescription": "An array of method names."
	# }
	return call_method("ALVideoDevice", "getMethodList", [])

def getMethodHelp(methodName:str) -> Any:
	"""
	Retrieves a method's description.
	
	Parameters
	----------
	methodName:str
		The name of the method.
	
	Returns
	----------
	A structure containing the method's description.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 106,
	#     "returnSignature": "m",
	#     "name": "getMethodHelp",
	#     "parametersSignature": "(s)",
	#     "description": "Retrieves a method's description.",
	#     "parameters": [
	#         {
	#             "name": "methodName",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A structure containing the method's description."
	# }
	return call_method("ALVideoDevice", "getMethodHelp", [methodName])

def getModuleHelp() -> Any:
	"""
	Retrieves the module's description.
	
	Returns
	----------
	A structure describing the module.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 107,
	#     "returnSignature": "m",
	#     "name": "getModuleHelp",
	#     "parametersSignature": "()",
	#     "description": "Retrieves the module's description.",
	#     "parameters": [],
	#     "returnDescription": "A structure describing the module."
	# }
	return call_method("ALVideoDevice", "getModuleHelp", [])

def getBrokerName() -> str:
	"""
	Gets the name of the parent broker.
	
	Returns
	----------
	The name of the parent broker.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "s",
	#     "name": "getBrokerName",
	#     "parametersSignature": "()",
	#     "description": "Gets the name of the parent broker.",
	#     "parameters": [],
	#     "returnDescription": "The name of the parent broker."
	# }
	return call_method("ALVideoDevice", "getBrokerName", [])

def getUsage(name:str) -> str:
	"""
	Gets the method usage string. This summarises how to use the method.
	
	Parameters
	----------
	name:str
		The name of the method.
	
	Returns
	----------
	A string that summarises the usage of the method.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 113,
	#     "returnSignature": "s",
	#     "name": "getUsage",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the method usage string. This summarises how to use the method.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "The name of the method."
	#         }
	#     ],
	#     "returnDescription": "A string that summarises the usage of the method."
	# }
	return call_method("ALVideoDevice", "getUsage", [name])

def subscribeCamera(name:str, cameraIndex:int, resolution:int, colorSpace:int, fps:int) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndex:int
		Camera requested.
	resolution:int
		Resolution requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
	colorSpace:int
		Colorspace requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
	fps:int
		Fps (frames per second) requested.{5, 10, 15, 30}
	
	Returns
	----------
	Name under which the vision module is known from ALVideoDevice
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "s",
	#     "name": "subscribeCamera",
	#     "parametersSignature": "(siiii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "resolution",
	#             "description": "Resolution requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}"
	#         },
	#         {
	#             "name": "colorSpace",
	#             "description": "Colorspace requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}"
	#         },
	#         {
	#             "name": "fps",
	#             "description": "Fps (frames per second) requested.{5, 10, 15, 30}"
	#         }
	#     ],
	#     "returnDescription": "Name under which the vision module is known from ALVideoDevice"
	# }
	return call_method("ALVideoDevice", "subscribeCamera", [name, cameraIndex, resolution, colorSpace, fps])

def subscribeCameras(name:str, cameraIndexes:Any, resolutions:Any, colorSpaces:Any, fps:int) -> str:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndexes:Any
		Cameras requested.
	resolutions:Any
		Resolutions requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
	colorSpaces:Any
		Colorspaces requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
	fps:int
		Fps (frames per second) requested.{5, 10, 15, 30}
	
	Returns
	----------
	Name under which the vision module is known from ALVideoDevice
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "s",
	#     "name": "subscribeCameras",
	#     "parametersSignature": "(smmmi)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "cameraIndexes",
	#             "description": "Cameras requested."
	#         },
	#         {
	#             "name": "resolutions",
	#             "description": "Resolutions requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}"
	#         },
	#         {
	#             "name": "colorSpaces",
	#             "description": "Colorspaces requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}"
	#         },
	#         {
	#             "name": "fps",
	#             "description": "Fps (frames per second) requested.{5, 10, 15, 30}"
	#         }
	#     ],
	#     "returnDescription": "Name under which the vision module is known from ALVideoDevice"
	# }
	return call_method("ALVideoDevice", "subscribeCameras", [name, cameraIndexes, resolutions, colorSpaces, fps])

def unsubscribe(nameId:str) -> bool:
	"""
	
	
	Parameters
	----------
	nameId:str
		Name under which the vision module is known from ALVideoDevice.
	
	Returns
	----------
	True if success, false otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "b",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "nameId",
	#             "description": "Name under which the vision module is known from ALVideoDevice."
	#         }
	#     ],
	#     "returnDescription": "True if success, false otherwise"
	# }
	return call_method("ALVideoDevice", "unsubscribe", [nameId])

def getSubscribers() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "m",
	#     "name": "getSubscribers",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getSubscribers", [])

def getCameraIndexes() -> Any:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "getCameraIndexes",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCameraIndexes", [])

@overload
def getActiveCamera() -> int:
	"""
	Tells which camera is the default one
	
	Returns
	----------
	 0: top camera - 1: bottom camera
	
	Bridge notes
	------------
	getActiveCamera has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "i",
	#     "name": "getActiveCamera",
	#     "parametersSignature": "()",
	#     "description": "Tells which camera is the default one",
	#     "parameters": [],
	#     "returnDescription": " 0: top camera - 1: bottom camera"
	# }
	...

@overload
def getActiveCamera(name:str, /) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	getActiveCamera has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 150,
	#     "returnSignature": "i",
	#     "name": "getActiveCamera",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def getActiveCamera(*args, **kwargs):
	"""
	Bridge notes
	------------
	getActiveCamera has 2 variants on the robot:
	- getActiveCamera()
	- getActiveCamera(name:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.getActiveCamera has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "getActiveCamera", list(args))

@overload
def setActiveCamera(activeCamera:int, /) -> bool:
	"""
	Set the active camera
	
	Parameters
	----------
	activeCamera:int
		 0: top camera - 1: bottom camera
	
	Bridge notes
	------------
	setActiveCamera has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "b",
	#     "name": "setActiveCamera",
	#     "parametersSignature": "(i)",
	#     "description": "Set the active camera",
	#     "parameters": [
	#         {
	#             "name": "activeCamera",
	#             "description": " 0: top camera - 1: bottom camera"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setActiveCamera(name:str, cameraIndex:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	setActiveCamera has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 151,
	#     "returnSignature": "b",
	#     "name": "setActiveCamera",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setActiveCamera(*args, **kwargs):
	"""
	Bridge notes
	------------
	setActiveCamera has 2 variants on the robot:
	- setActiveCamera(activeCamera:int)
	- setActiveCamera(name:str, cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.setActiveCamera has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "setActiveCamera", list(args))

def getCameraModel(cameraIndex:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	 1(kOV7670): VGA camera - 2(kMT9M114): HD camera
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "getCameraModel",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": " 1(kOV7670): VGA camera - 2(kMT9M114): HD camera"
	# }
	return call_method("ALVideoDevice", "getCameraModel", [cameraIndex])

def isCameraSimulated(cameraIndex:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	 True: Camera is simulated - False: Camera is real
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "b",
	#     "name": "isCameraSimulated",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": " True: Camera is simulated - False: Camera is real"
	# }
	return call_method("ALVideoDevice", "isCameraSimulated", [cameraIndex])

def getCameraName(cameraIndex:int) -> str:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	CameraTop - CameraBottom - CameraDepth
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "s",
	#     "name": "getCameraName",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": "CameraTop - CameraBottom - CameraDepth"
	# }
	return call_method("ALVideoDevice", "getCameraName", [cameraIndex])

@overload
def getFrameRate(cameraIndex:int, /) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	getFrameRate has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getFrameRate_int(int)
	- getFrameRate_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def getFrameRate(name:str, /) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	getFrameRate has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getFrameRate_int(int)
	- getFrameRate_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def getFrameRate(*args, **kwargs):
	"""
	Bridge notes
	------------
	getFrameRate has 2 variants on the robot:
	- getFrameRate(cameraIndex:int), explicitly getFrameRate_int
	- getFrameRate(name:str), explicitly getFrameRate_str
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.getFrameRate has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "getFrameRate", list(args))

def getFrameRate_int(cameraIndex:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	Explicit variant of getFrameRate(int). Calling getFrameRate instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getFrameRate", [cameraIndex])

def getFrameRate_str(name:str) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	Explicit variant of getFrameRate(str). Calling getFrameRate instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "i",
	#     "name": "getFrameRate",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getFrameRate", [name])

@overload
def getResolution(cameraIndex:int, /) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	getResolution has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getResolution_int(int)
	- getResolution_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def getResolution(name:str, /) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	getResolution has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getResolution_int(int)
	- getResolution_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def getResolution(*args, **kwargs):
	"""
	Bridge notes
	------------
	getResolution has 2 variants on the robot:
	- getResolution(cameraIndex:int), explicitly getResolution_int
	- getResolution(name:str), explicitly getResolution_str
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.getResolution has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "getResolution", list(args))

def getResolution_int(cameraIndex:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	Explicit variant of getResolution(int). Calling getResolution instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getResolution", [cameraIndex])

def getResolution_str(name:str) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	Explicit variant of getResolution(str). Calling getResolution instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 152,
	#     "returnSignature": "i",
	#     "name": "getResolution",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getResolution", [name])

@overload
def getColorSpace(cameraIndex:int, /) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	getColorSpace has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getColorSpace_int(int)
	- getColorSpace_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def getColorSpace(name:str, /) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	getColorSpace has 2 variants, and some differ only by argument type. The robot picks one from the types you pass, so e.g. 5 and 5.0 can reach different variants.
	
	To choose explicitly, use:
	- getColorSpace_int(int)
	- getColorSpace_str(str)
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def getColorSpace(*args, **kwargs):
	"""
	Bridge notes
	------------
	getColorSpace has 2 variants on the robot:
	- getColorSpace(cameraIndex:int), explicitly getColorSpace_int
	- getColorSpace(name:str), explicitly getColorSpace_str
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.getColorSpace has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "getColorSpace", list(args))

def getColorSpace_int(cameraIndex:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	Explicit variant of getColorSpace(int). Calling getColorSpace instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getColorSpace", [cameraIndex])

def getColorSpace_str(name:str) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Bridge notes
	------------
	Explicit variant of getColorSpace(str). Calling getColorSpace instead lets the robot choose the variant from the argument types.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 154,
	#     "returnSignature": "i",
	#     "name": "getColorSpace",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getColorSpace", [name])

def getHorizontalFOV(cameraIndex:int) -> float:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "f",
	#     "name": "getHorizontalFOV",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getHorizontalFOV", [cameraIndex])

def getVerticalFOV(cameraIndex:int) -> float:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "f",
	#     "name": "getVerticalFOV",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getVerticalFOV", [cameraIndex])

def getParameterList(cameraIndex:int) -> List[int]:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "[i]",
	#     "name": "getParameterList",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getParameterList", [cameraIndex])

def getParameter(cameraIndex:int, parameterId:int) -> int:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "i",
	#     "name": "getParameter",
	#     "parametersSignature": "(ii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getParameter", [cameraIndex, parameterId])

def getParameterRange(cameraIndex:int, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "m",
	#     "name": "getParameterRange",
	#     "parametersSignature": "(ii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getParameterRange", [cameraIndex, parameterId])

def getParameterInfo(cameraIndex:int, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "m",
	#     "name": "getParameterInfo",
	#     "parametersSignature": "(ii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getParameterInfo", [cameraIndex, parameterId])

def setParameter(cameraIndex:int, parameterId:int, value:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	value:int
		value requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "b",
	#     "name": "setParameter",
	#     "parametersSignature": "(iii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         },
	#         {
	#             "name": "value",
	#             "description": "value requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setParameter", [cameraIndex, parameterId, value])

def setParameterToDefault(cameraIndex:int, parameterId:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "b",
	#     "name": "setParameterToDefault",
	#     "parametersSignature": "(ii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setParameterToDefault", [cameraIndex, parameterId])

def setCameraCalibration(cameraIndex:int, filenames:List[str]) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	filenames:List[str]
		Vector of files to retrieve in /media/internal/share/naoqi/vision or ~/.local/share/naoqi/vision
	
	Returns
	----------
	true if succeeded, false otherwise
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "b",
	#     "name": "setCameraCalibration",
	#     "parametersSignature": "(i[s])",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "filenames",
	#             "description": "Vector of files to retrieve in /media/internal/share/naoqi/vision or ~/.local/share/naoqi/vision"
	#         }
	#     ],
	#     "returnDescription": "true if succeeded, false otherwise"
	# }
	return call_method("ALVideoDevice", "setCameraCalibration", [cameraIndex, filenames])

def setAllParametersToDefault(cameraIndex:int) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "b",
	#     "name": "setAllParametersToDefault",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setAllParametersToDefault", [cameraIndex])

def openCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "b",
	#     "name": "openCamera",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "openCamera", [p0])

def closeCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "b",
	#     "name": "closeCamera",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "closeCamera", [p0])

def isCameraOpen(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "b",
	#     "name": "isCameraOpen",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "isCameraOpen", [p0])

def startCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "b",
	#     "name": "startCamera",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "startCamera", [p0])

def stopCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "b",
	#     "name": "stopCamera",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "stopCamera", [p0])

def isCameraStarted(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "b",
	#     "name": "isCameraStarted",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "isCameraStarted", [p0])

def resetCamera(p0:int) -> bool:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "b",
	#     "name": "resetCamera",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "resetCamera", [p0])

@overload
def startFrameGrabber() -> bool:
	"""
	Advanced method that opens and initialize video source device if it was not before.
	Note that the first client subscribing to ALVideoDevice will launch it automatically.
	
	Returns
	----------
	true if success
	
	Bridge notes
	------------
	startFrameGrabber has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 222,
	#     "returnSignature": "b",
	#     "name": "startFrameGrabber",
	#     "parametersSignature": "()",
	#     "description": "Advanced method that opens and initialize video source device if it was not before.\nNote that the first client subscribing to ALVideoDevice will launch it automatically.",
	#     "parameters": [],
	#     "returnDescription": "true if success"
	# }
	...

@overload
def startFrameGrabber(cameraIndex:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	startFrameGrabber has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "b",
	#     "name": "startFrameGrabber",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def startFrameGrabber(*args, **kwargs):
	"""
	Bridge notes
	------------
	startFrameGrabber has 2 variants on the robot:
	- startFrameGrabber()
	- startFrameGrabber(cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.startFrameGrabber has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "startFrameGrabber", list(args))

@overload
def stopFrameGrabber() -> bool:
	"""
	Advanced method that close video source device.
	Note that the last client unsubscribing to ALVideoDevice will launch it automatically.
	
	Returns
	----------
	true if success
	
	Bridge notes
	------------
	stopFrameGrabber has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 223,
	#     "returnSignature": "b",
	#     "name": "stopFrameGrabber",
	#     "parametersSignature": "()",
	#     "description": "Advanced method that close video source device.\nNote that the last client unsubscribing to ALVideoDevice will launch it automatically.",
	#     "parameters": [],
	#     "returnDescription": "true if success"
	# }
	...

@overload
def stopFrameGrabber(cameraIndex:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	stopFrameGrabber has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "b",
	#     "name": "stopFrameGrabber",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def stopFrameGrabber(*args, **kwargs):
	"""
	Bridge notes
	------------
	stopFrameGrabber has 2 variants on the robot:
	- stopFrameGrabber()
	- stopFrameGrabber(cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.stopFrameGrabber has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "stopFrameGrabber", list(args))

@overload
def isFrameGrabberOff() -> int:
	"""
	Advanced method that asks if the framegrabber is off.
	
	Returns
	----------
	true if off
	
	Bridge notes
	------------
	isFrameGrabberOff has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 224,
	#     "returnSignature": "i",
	#     "name": "isFrameGrabberOff",
	#     "parametersSignature": "()",
	#     "description": "Advanced method that asks if the framegrabber is off.",
	#     "parameters": [],
	#     "returnDescription": "true if off"
	# }
	...

@overload
def isFrameGrabberOff(cameraIndex:int, /) -> bool:
	"""
	
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	isFrameGrabberOff has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "b",
	#     "name": "isFrameGrabberOff",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def isFrameGrabberOff(*args, **kwargs):
	"""
	Bridge notes
	------------
	isFrameGrabberOff has 2 variants on the robot:
	- isFrameGrabberOff()
	- isFrameGrabberOff(cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.isFrameGrabberOff has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "isFrameGrabberOff", list(args))

def hasDepthCamera() -> bool:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "b",
	#     "name": "hasDepthCamera",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "hasDepthCamera", [])

def setFrameRate(name:str, frameRate:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	frameRate:int
		Frame Rate requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 149,
	#     "returnSignature": "b",
	#     "name": "setFrameRate",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "frameRate",
	#             "description": "Frame Rate requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setFrameRate", [name, frameRate])

def setResolution(name:str, resolution:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	resolution:int
		Resolution requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 153,
	#     "returnSignature": "b",
	#     "name": "setResolution",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "resolution",
	#             "description": "Resolution requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setResolution", [name, resolution])

def setColorSpace(name:str, colorSpace:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	colorSpace:int
		Color Space requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 155,
	#     "returnSignature": "b",
	#     "name": "setColorSpace",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "colorSpace",
	#             "description": "Color Space requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setColorSpace", [name, colorSpace])

def getCameraParameterList(name:str) -> List[int]:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 156,
	#     "returnSignature": "[i]",
	#     "name": "getCameraParameterList",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCameraParameterList", [name])

def getCameraParameter(name:str, parameterId:int) -> int:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 157,
	#     "returnSignature": "i",
	#     "name": "getCameraParameter",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCameraParameter", [name, parameterId])

def getCameraParameterRange(name:str, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 158,
	#     "returnSignature": "m",
	#     "name": "getCameraParameterRange",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCameraParameterRange", [name, parameterId])

def getCameraParameterInfo(name:str, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 159,
	#     "returnSignature": "m",
	#     "name": "getCameraParameterInfo",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCameraParameterInfo", [name, parameterId])

def setCameraParameter(name:str, parameterId:int, value:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	value:int
		value requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 160,
	#     "returnSignature": "b",
	#     "name": "setCameraParameter",
	#     "parametersSignature": "(sii)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         },
	#         {
	#             "name": "value",
	#             "description": "value requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setCameraParameter", [name, parameterId, value])

def setCameraParameterToDefault(name:str, parameterId:int) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 161,
	#     "returnSignature": "b",
	#     "name": "setCameraParameterToDefault",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setCameraParameterToDefault", [name, parameterId])

def setAllCameraParametersToDefault(name:str) -> bool:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 162,
	#     "returnSignature": "b",
	#     "name": "setAllCameraParametersToDefault",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setAllCameraParametersToDefault", [name])

def getDirectRawImageRemote(name:str) -> Any:
	"""
	Fills an ALValue with data coming directly from raw buffer (no format conversion).
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 164,
	#     "returnSignature": "m",
	#     "name": "getDirectRawImageRemote",
	#     "parametersSignature": "(s)",
	#     "description": "Fills an ALValue with data coming directly from raw buffer (no format conversion).\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	# }
	return call_method("ALVideoDevice", "getDirectRawImageRemote", [name])

def releaseDirectRawImage(name:str) -> bool:
	"""
	Release image buffer locked by getDirectRawImageLocal().
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 165,
	#     "returnSignature": "b",
	#     "name": "releaseDirectRawImage",
	#     "parametersSignature": "(s)",
	#     "description": "Release image buffer locked by getDirectRawImageLocal().\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "releaseDirectRawImage", [name])

def getImageRemote(name:str) -> Any:
	"""
	Applies transformations to the last image from video source and fills pFrameOut.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 167,
	#     "returnSignature": "m",
	#     "name": "getImageRemote",
	#     "parametersSignature": "(s)",
	#     "description": "Applies transformations to the last image from video source and fills pFrameOut.\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	# }
	return call_method("ALVideoDevice", "getImageRemote", [name])

def releaseImage(name:str) -> bool:
	"""
	Release image buffer locked by getImageLocal().
	If G.V.M. had no locked image buffer, does nothing.
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 168,
	#     "returnSignature": "b",
	#     "name": "releaseImage",
	#     "parametersSignature": "(s)",
	#     "description": "Release image buffer locked by getImageLocal().\nIf G.V.M. had no locked image buffer, does nothing.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "releaseImage", [name])

def getActiveCameras(name:str) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 169,
	#     "returnSignature": "m",
	#     "name": "getActiveCameras",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getActiveCameras", [name])

def setActiveCameras(name:str, cameraIndexes:Any) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	cameraIndexes:Any
		Cameras requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 170,
	#     "returnSignature": "m",
	#     "name": "setActiveCameras",
	#     "parametersSignature": "(sm)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "cameraIndexes",
	#             "description": "Cameras requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setActiveCameras", [name, cameraIndexes])

def getResolutions(name:str) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 171,
	#     "returnSignature": "m",
	#     "name": "getResolutions",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getResolutions", [name])

def setResolutions(name:str, resolutions:Any) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	resolutions:Any
		Resolutions requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 172,
	#     "returnSignature": "m",
	#     "name": "setResolutions",
	#     "parametersSignature": "(sm)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "resolutions",
	#             "description": "Resolutions requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setResolutions", [name, resolutions])

def getColorSpaces(name:str) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	"""
	# NAOqi metadata:
	# {
	#     "uid": 173,
	#     "returnSignature": "m",
	#     "name": "getColorSpaces",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getColorSpaces", [name])

def setColorSpaces(name:str, colorSpaces:Any) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	colorSpaces:Any
		Color Spaces requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 174,
	#     "returnSignature": "m",
	#     "name": "setColorSpaces",
	#     "parametersSignature": "(sm)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "colorSpaces",
	#             "description": "Color Spaces requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setColorSpaces", [name, colorSpaces])

def getCamerasParameter(name:str, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 175,
	#     "returnSignature": "m",
	#     "name": "getCamerasParameter",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getCamerasParameter", [name, parameterId])

def setCamerasParameter(name:str, parameterId:int, values:Any) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	values:Any
		values requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 176,
	#     "returnSignature": "m",
	#     "name": "setCamerasParameter",
	#     "parametersSignature": "(sim)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         },
	#         {
	#             "name": "values",
	#             "description": "values requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setCamerasParameter", [name, parameterId, values])

def setCamerasParameterToDefault(name:str, parameterId:int) -> Any:
	"""
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	parameterId:int
		Camera parameter requested.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 177,
	#     "returnSignature": "m",
	#     "name": "setCamerasParameterToDefault",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         },
	#         {
	#             "name": "parameterId",
	#             "description": "Camera parameter requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "setCamerasParameterToDefault", [name, parameterId])

def getDirectRawImagesLocal(name:str) -> Any:
	"""
	Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.
	Warning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.
	Warning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!
	Warning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array of pointer to the locked image buffer, NULL if error.
	Warning, image pointer is valid only for C++ dynamic library.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 178,
	#     "returnSignature": "m",
	#     "name": "getDirectRawImagesLocal",
	#     "parametersSignature": "(s)",
	#     "description": "Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer.\nWarning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested.\nWarning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!!\nWarning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array of pointer to the locked image buffer, NULL if error.\nWarning, image pointer is valid only for C++ dynamic library."
	# }
	return call_method("ALVideoDevice", "getDirectRawImagesLocal", [name])

def getDirectRawImagesRemote(name:str) -> Any:
	"""
	Fills an ALValue with data coming directly from raw buffer (no format conversion).
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 179,
	#     "returnSignature": "m",
	#     "name": "getDirectRawImagesRemote",
	#     "parametersSignature": "(s)",
	#     "description": "Fills an ALValue with data coming directly from raw buffer (no format conversion).\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	# }
	return call_method("ALVideoDevice", "getDirectRawImagesRemote", [name])

def releaseDirectRawImages(name:str) -> Any:
	"""
	Release image buffer locked by getDirectRawImagesLocal().
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 180,
	#     "returnSignature": "m",
	#     "name": "releaseDirectRawImages",
	#     "parametersSignature": "(s)",
	#     "description": "Release image buffer locked by getDirectRawImagesLocal().\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "releaseDirectRawImages", [name])

def getImagesLocal(name:str) -> Any:
	"""
	Applies transformations to the last image from video source and returns a pointer to a locked ALImage.
	When image is not necessary anymore, a call to releaseImage() is requested.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array of pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 181,
	#     "returnSignature": "m",
	#     "name": "getImagesLocal",
	#     "parametersSignature": "(s)",
	#     "description": "Applies transformations to the last image from video source and returns a pointer to a locked ALImage.\nWhen image is not necessary anymore, a call to releaseImage() is requested.\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array of pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library."
	# }
	return call_method("ALVideoDevice", "getImagesLocal", [name])

def getImagesRemote(name:str) -> Any:
	"""
	Applies transformations to the last image from video source and fills pFrameOut.
	
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	Array containing image informations : 
	    [0] : width;
	    [1] : height;
	    [2] : number of layers;
	    [3] : ColorSpace;
	    [4] : time stamp (highest 32 bits);
	    [5] : time stamp (lowest 32 bits);
	    [6] : array of size height * width * nblayers containing image data;
	    [7] : cameraID;
	    [8] : left angle;
	    [9] : top angle;
	    [10] : right angle;
	    [11] : bottom angle;
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 182,
	#     "returnSignature": "m",
	#     "name": "getImagesRemote",
	#     "parametersSignature": "(s)",
	#     "description": "Applies transformations to the last image from video source and fills pFrameOut.\n",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "Array containing image informations : \n    [0] : width;\n    [1] : height;\n    [2] : number of layers;\n    [3] : ColorSpace;\n    [4] : time stamp (highest 32 bits);\n    [5] : time stamp (lowest 32 bits);\n    [6] : array of size height * width * nblayers containing image data;\n    [7] : cameraID;\n    [8] : left angle;\n    [9] : top angle;\n    [10] : right angle;\n    [11] : bottom angle;\n"
	# }
	return call_method("ALVideoDevice", "getImagesRemote", [name])

def releaseImages(name:str) -> Any:
	"""
	Release image buffer locked by getImageLocal().
	If G.V.M. had no locked image buffer, does nothing.
	
	Parameters
	----------
	name:str
		Name of the subscribing vision module
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 183,
	#     "returnSignature": "m",
	#     "name": "releaseImages",
	#     "parametersSignature": "(s)",
	#     "description": "Release image buffer locked by getImageLocal().\nIf G.V.M. had no locked image buffer, does nothing.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the subscribing vision module"
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "releaseImages", [name])

def recordVideo(id:str, path:str, totalNumber:int, period:int) -> bool:
	"""
	Background record of an .arv raw format video from the images processed by a vision module
	Actualy it take picture each time the vision module call getDirectRawImageRemote().
	
	Parameters
	----------
	id:str
		Name under which the G.V.M. is known from the V.I.M.
	path:str
		path/name of the video to be recorded
	totalNumber:int
		number of images to be recorded. 0xFFFFFFFF for "unlimited"
	period:int
		one image recorded every pPeriod images
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 184,
	#     "returnSignature": "b",
	#     "name": "recordVideo",
	#     "parametersSignature": "(ssii)",
	#     "description": "Background record of an .arv raw format video from the images processed by a vision module\nActualy it take picture each time the vision module call getDirectRawImageRemote().",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Name under which the G.V.M. is known from the V.I.M."
	#         },
	#         {
	#             "name": "path",
	#             "description": "path/name of the video to be recorded"
	#         },
	#         {
	#             "name": "totalNumber",
	#             "description": "number of images to be recorded. 0xFFFFFFFF for \"unlimited\""
	#         },
	#         {
	#             "name": "period",
	#             "description": "one image recorded every pPeriod images"
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "recordVideo", [id, path, totalNumber, period])

def stopVideo(id:str) -> bool:
	"""
	Stop writing the video sequence
	
	Parameters
	----------
	id:str
		Name under which the G.V.M. is known from ALVideoDevice.
	
	Returns
	----------
	true if success
	"""
	# NAOqi metadata:
	# {
	#     "uid": 185,
	#     "returnSignature": "b",
	#     "name": "stopVideo",
	#     "parametersSignature": "(s)",
	#     "description": "Stop writing the video sequence",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Name under which the G.V.M. is known from ALVideoDevice."
	#         }
	#     ],
	#     "returnDescription": "true if success"
	# }
	return call_method("ALVideoDevice", "stopVideo", [id])

def getAngularPositionFromImagePosition(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 186,
	#     "returnSignature": "[f]",
	#     "name": "getAngularPositionFromImagePosition",
	#     "parametersSignature": "(i[f])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getAngularPositionFromImagePosition", [p0, p1])

def getImagePositionFromAngularPosition(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 187,
	#     "returnSignature": "[f]",
	#     "name": "getImagePositionFromAngularPosition",
	#     "parametersSignature": "(i[f])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getImagePositionFromAngularPosition", [p0, p1])

def getAngularSizeFromImageSize(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 188,
	#     "returnSignature": "[f]",
	#     "name": "getAngularSizeFromImageSize",
	#     "parametersSignature": "(i[f])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getAngularSizeFromImageSize", [p0, p1])

def getImageSizeFromAngularSize(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 189,
	#     "returnSignature": "[f]",
	#     "name": "getImageSizeFromAngularSize",
	#     "parametersSignature": "(i[f])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getImageSizeFromAngularSize", [p0, p1])

def getImageInfoFromAngularInfo(p0:int, p1:List[float]) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 190,
	#     "returnSignature": "[f]",
	#     "name": "getImageInfoFromAngularInfo",
	#     "parametersSignature": "(i[f])",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getImageInfoFromAngularInfo", [p0, p1])

def getImageInfoFromAngularInfoWithResolution(p0:int, p1:List[float], p2:int) -> List[float]:
	"""
	
	
	Parameters
	----------
	p0:int
		
	p1:List[float]
		
	p2:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 191,
	#     "returnSignature": "[f]",
	#     "name": "getImageInfoFromAngularInfoWithResolution",
	#     "parametersSignature": "(i[f]i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "getImageInfoFromAngularInfoWithResolution", [p0, p1, p2])

@overload
def putImage(imageBuffer:Any, /) -> bool:
	"""
	Allow image buffer pushing
	
	Parameters
	----------
	imageBuffer:Any
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	Bridge notes
	------------
	putImage has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 220,
	#     "returnSignature": "b",
	#     "name": "putImage",
	#     "parametersSignature": "(m)",
	#     "description": "Allow image buffer pushing",
	#     "parameters": [
	#         {
	#             "name": "imageBuffer",
	#             "description": "Image buffer in bitmap form"
	#         }
	#     ],
	#     "returnDescription": "true if the put succeeded"
	# }
	...

@overload
def putImage(cameraIndex:int, width:int, height:int, imageBuffer:Any, /) -> bool:
	"""
	Allow image buffer pushing
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	width:int
		int width of image among 1280*960, 640*480, 320*240, 240*160
	height:int
		int height of image
	imageBuffer:Any
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	Bridge notes
	------------
	putImage has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 221,
	#     "returnSignature": "b",
	#     "name": "putImage",
	#     "parametersSignature": "(iiim)",
	#     "description": "Allow image buffer pushing",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "width",
	#             "description": "int width of image among 1280*960, 640*480, 320*240, 240*160"
	#         },
	#         {
	#             "name": "height",
	#             "description": "int height of image"
	#         },
	#         {
	#             "name": "imageBuffer",
	#             "description": "Image buffer in bitmap form"
	#         }
	#     ],
	#     "returnDescription": "true if the put succeeded"
	# }
	...

@overload
def putImage(cameraIndex:int, timeStamp:Any, width:int, height:int, colorSpace:int, imageBuffer:Any, /) -> bool:
	"""
	Allow image buffer pushing
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	timeStamp:Any
		time stamp of the image. If empty, use current time.
	width:int
		int width of image among 1280*960, 640*480, 320*240, 240*160
	height:int
		int height of image
	colorSpace:int
		colorSpace of image.
	imageBuffer:Any
		Image buffer in bitmap form
	
	Returns
	----------
	true if the put succeeded
	
	Bridge notes
	------------
	putImage has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 192,
	#     "returnSignature": "b",
	#     "name": "putImage",
	#     "parametersSignature": "(imiiim)",
	#     "description": "Allow image buffer pushing",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         },
	#         {
	#             "name": "timeStamp",
	#             "description": "time stamp of the image. If empty, use current time."
	#         },
	#         {
	#             "name": "width",
	#             "description": "int width of image among 1280*960, 640*480, 320*240, 240*160"
	#         },
	#         {
	#             "name": "height",
	#             "description": "int height of image"
	#         },
	#         {
	#             "name": "colorSpace",
	#             "description": "colorSpace of image."
	#         },
	#         {
	#             "name": "imageBuffer",
	#             "description": "Image buffer in bitmap form"
	#         }
	#     ],
	#     "returnDescription": "true if the put succeeded"
	# }
	...

def putImage(*args, **kwargs):
	"""
	Bridge notes
	------------
	putImage has 3 variants on the robot:
	- putImage(imageBuffer:Any)
	- putImage(cameraIndex:int, width:int, height:int, imageBuffer:Any)
	- putImage(cameraIndex:int, timeStamp:Any, width:int, height:int, colorSpace:int, imageBuffer:Any)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.putImage has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "putImage", list(args))

@overload
def getExpectedImageParameters() -> Any:
	"""
	called by the simulator to know expected image parameters
	
	Returns
	----------
	ALValue of expected parameters, [int resolution, int framerate]
	
	Bridge notes
	------------
	getExpectedImageParameters has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 218,
	#     "returnSignature": "m",
	#     "name": "getExpectedImageParameters",
	#     "parametersSignature": "()",
	#     "description": "called by the simulator to know expected image parameters",
	#     "parameters": [],
	#     "returnDescription": "ALValue of expected parameters, [int resolution, int framerate]"
	# }
	...

@overload
def getExpectedImageParameters(cameraIndex:int, /) -> Any:
	"""
	called by the simulator to know expected image parameters
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	ALValue of expected parameters, [int resolution, int framerate]
	
	Bridge notes
	------------
	getExpectedImageParameters has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 193,
	#     "returnSignature": "m",
	#     "name": "getExpectedImageParameters",
	#     "parametersSignature": "(i)",
	#     "description": "called by the simulator to know expected image parameters",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": "ALValue of expected parameters, [int resolution, int framerate]"
	# }
	...

def getExpectedImageParameters(*args, **kwargs):
	"""
	Bridge notes
	------------
	getExpectedImageParameters has 2 variants on the robot:
	- getExpectedImageParameters()
	- getExpectedImageParameters(cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.getExpectedImageParameters has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "getExpectedImageParameters", list(args))

def _getExternalBrightness(cameraIndex:int) -> int:
	"""
	Get average environment luminance.
	
	Parameters
	----------
	cameraIndex:int
		Camera requested.
	
	Returns
	----------
	The average brightness luminance == (15680-Texposure)*256+AverageLuminance
	"""
	# NAOqi metadata:
	# {
	#     "uid": 194,
	#     "returnSignature": "i",
	#     "name": "_getExternalBrightness",
	#     "parametersSignature": "(i)",
	#     "description": "Get average environment luminance.",
	#     "parameters": [
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": "The average brightness luminance == (15680-Texposure)*256+AverageLuminance"
	# }
	return call_method("ALVideoDevice", "_getExternalBrightness", [cameraIndex])

def onClientDisconnected(eventName:str, eventContents:Any, message:str) -> None:
	"""
	Callback when client is disconnected
	
	Parameters
	----------
	eventName:str
		The echoed event name
	eventContents:Any
		The name of the client that has disconnected
	message:str
		The message give when subscribing.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 195,
	#     "returnSignature": "v",
	#     "name": "onClientDisconnected",
	#     "parametersSignature": "(sms)",
	#     "description": "Callback when client is disconnected",
	#     "parameters": [
	#         {
	#             "name": "eventName",
	#             "description": "The echoed event name"
	#         },
	#         {
	#             "name": "eventContents",
	#             "description": "The name of the client that has disconnected"
	#         },
	#         {
	#             "name": "message",
	#             "description": "The message give when subscribing."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "onClientDisconnected", [eventName, eventContents, message])

def subscribe(gvmName:str, resolution:int, colorSpace:int, fps:int) -> str:
	"""
	Register to ALVideoDevice (formerly Video Input Module/V.I.M.). When a General Video Module(G.V.M.) registers to ALVideoDevice, a buffer of the requested image format is added to the buffers list.
	Returns the name under which the G.V.M. is registered to ALVideoDevice (useful when two G.V.M. try to register using the same name
	
	Parameters
	----------
	gvmName:str
		Name of the subscribing G.V.M.
	resolution:int
		Resolution requested. {0: kQQVGA, 1: kQVGA, 2: kVGA}
	colorSpace:int
		Colorspace requested. {0: kYuv, 9: kYUV422, 10: kYUV, 11: kRGB, 12: kHSY, 13: kBGR}
	fps:int
		Fps (frames per second) requested. {5, 10, 15, 30}
	
	Returns
	----------
	Name under which the G.V.M. is known from ALVideoDevice, 0 if failed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 196,
	#     "returnSignature": "s",
	#     "name": "subscribe",
	#     "parametersSignature": "(siii)",
	#     "description": "Register to ALVideoDevice (formerly Video Input Module/V.I.M.). When a General Video Module(G.V.M.) registers to ALVideoDevice, a buffer of the requested image format is added to the buffers list.\nReturns the name under which the G.V.M. is registered to ALVideoDevice (useful when two G.V.M. try to register using the same name",
	#     "parameters": [
	#         {
	#             "name": "gvmName",
	#             "description": "Name of the subscribing G.V.M."
	#         },
	#         {
	#             "name": "resolution",
	#             "description": "Resolution requested. {0: kQQVGA, 1: kQVGA, 2: kVGA}"
	#         },
	#         {
	#             "name": "colorSpace",
	#             "description": "Colorspace requested. {0: kYuv, 9: kYUV422, 10: kYUV, 11: kRGB, 12: kHSY, 13: kBGR}"
	#         },
	#         {
	#             "name": "fps",
	#             "description": "Fps (frames per second) requested. {5, 10, 15, 30}"
	#         }
	#     ],
	#     "returnDescription": "Name under which the G.V.M. is known from ALVideoDevice, 0 if failed."
	# }
	return call_method("ALVideoDevice", "subscribe", [gvmName, resolution, colorSpace, fps])

def unsubscribeAllInstances(id:str) -> None:
	"""
	Used to unsubscribe all instances for a given G.V.M. (e.g. VisionModule and VisionModule_5) from ALVideoDevice.
	
	Parameters
	----------
	id:str
		Root name of the G.V.M. (e.g. with the example above this will be VisionModule).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 197,
	#     "returnSignature": "v",
	#     "name": "unsubscribeAllInstances",
	#     "parametersSignature": "(s)",
	#     "description": "Used to unsubscribe all instances for a given G.V.M. (e.g. VisionModule and VisionModule_5) from ALVideoDevice.",
	#     "parameters": [
	#         {
	#             "name": "id",
	#             "description": "Root name of the G.V.M. (e.g. with the example above this will be VisionModule)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALVideoDevice", "unsubscribeAllInstances", [id])

@overload
def setParam(param:int, newValue:int, /) -> None:
	"""
	Sets the value of a specific parameter for the video source.
	
	Parameters
	----------
	param:int
		Camera parameter requested.
	newValue:int
		value requested.
	
	Bridge notes
	------------
	setParam has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 205,
	#     "returnSignature": "v",
	#     "name": "setParam",
	#     "parametersSignature": "(ii)",
	#     "description": "Sets the value of a specific parameter for the video source.",
	#     "parameters": [
	#         {
	#             "name": "param",
	#             "description": "Camera parameter requested."
	#         },
	#         {
	#             "name": "newValue",
	#             "description": "value requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def setParam(param:int, newValue:int, cameraIndex:int, /) -> None:
	"""
	Sets the value of a specific parameter for the video source.
	
	Parameters
	----------
	param:int
		Camera parameter requested.
	newValue:int
		value requested.
	cameraIndex:int
		Camera requested.
	
	Bridge notes
	------------
	setParam has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 206,
	#     "returnSignature": "v",
	#     "name": "setParam",
	#     "parametersSignature": "(iii)",
	#     "description": "Sets the value of a specific parameter for the video source.",
	#     "parameters": [
	#         {
	#             "name": "param",
	#             "description": "Camera parameter requested."
	#         },
	#         {
	#             "name": "newValue",
	#             "description": "value requested."
	#         },
	#         {
	#             "name": "cameraIndex",
	#             "description": "Camera requested."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def setParam(*args, **kwargs):
	"""
	Bridge notes
	------------
	setParam has 2 variants on the robot:
	- setParam(param:int, newValue:int)
	- setParam(param:int, newValue:int, cameraIndex:int)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALVideoDevice.setParam has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALVideoDevice", "setParam", list(args))

def setSimCamInputSize(width:int, height:int) -> bool:
	"""
	called by the simulator to know expected image parameters
	
	Parameters
	----------
	width:int
		int width of image among 1280, 640, 320, 240, 120, 60
	height:int
		int height of image among 960, 480, 240, 160, 80, 40
	
	Returns
	----------
	true if setSize worked
	"""
	# NAOqi metadata:
	# {
	#     "uid": 219,
	#     "returnSignature": "b",
	#     "name": "setSimCamInputSize",
	#     "parametersSignature": "(ii)",
	#     "description": "called by the simulator to know expected image parameters",
	#     "parameters": [
	#         {
	#             "name": "width",
	#             "description": "int width of image among 1280, 640, 320, 240, 120, 60"
	#         },
	#         {
	#             "name": "height",
	#             "description": "int height of image among 960, 480, 240, 160, 80, 40"
	#         }
	#     ],
	#     "returnDescription": "true if setSize worked"
	# }
	return call_method("ALVideoDevice", "setSimCamInputSize", [width, height])

