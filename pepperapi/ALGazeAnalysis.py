"""
This module computes the direction of the look of a person from the orientation of his/her face. It is then possible to know if the person looks at the robot or not.
"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
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
	return call_method("ALGazeAnalysis", "version", [])

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
	return call_method("ALGazeAnalysis", "ping", [])

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
	return call_method("ALGazeAnalysis", "getMethodList", [])

def getMethodHelp(methodName:str) -> object:
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
	return call_method("ALGazeAnalysis", "getMethodHelp", [methodName])

def getModuleHelp() -> object:
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
	return call_method("ALGazeAnalysis", "getModuleHelp", [])

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
	return call_method("ALGazeAnalysis", "getBrokerName", [])

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
	return call_method("ALGazeAnalysis", "getUsage", [name])

@overload
def subscribe(name:str, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def subscribe(name:str, period:int, precision:float, /) -> None:
	"""
	Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.
	
	Parameters
	----------
	name:str
		Name of the module which subscribes.
	period:int
		Refresh period (in milliseconds) if relevant.
	precision:float
		Precision of the extractor if relevant.
	
	Bridge notes
	------------
	subscribe has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "subscribe",
	#     "parametersSignature": "(sif)",
	#     "description": "Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData(\"keyName\"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which subscribes."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds) if relevant."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor if relevant."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def subscribe(*args, **kwargs):
	"""
	Bridge notes
	------------
	subscribe has 2 variants on the robot:
	- subscribe(name:str)
	- subscribe(name:str, period:int, precision:float)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("ALGazeAnalysis.subscribe has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("ALGazeAnalysis", "subscribe", list(args))

def unsubscribe(name:str) -> None:
	"""
	Unsubscribes from the extractor.
	
	Parameters
	----------
	name:str
		Name of the module which had subscribed.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "unsubscribe",
	#     "parametersSignature": "(s)",
	#     "description": "Unsubscribes from the extractor.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which had subscribed."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "unsubscribe", [name])

def updatePeriod(name:str, period:int) -> None:
	"""
	Updates the period if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	period:int
		Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "updatePeriod",
	#     "parametersSignature": "(si)",
	#     "description": "Updates the period if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "period",
	#             "description": "Refresh period (in milliseconds)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "updatePeriod", [name, period])

def updatePrecision(name:str, precision:float) -> None:
	"""
	Updates the precision if relevant.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	precision:float
		Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "updatePrecision",
	#     "parametersSignature": "(sf)",
	#     "description": "Updates the precision if relevant.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         },
	#         {
	#             "name": "precision",
	#             "description": "Precision of the extractor."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "updatePrecision", [name, precision])

def getCurrentPeriod() -> int:
	"""
	Gets the current period.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "i",
	#     "name": "getCurrentPeriod",
	#     "parametersSignature": "()",
	#     "description": "Gets the current period.",
	#     "parameters": [],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALGazeAnalysis", "getCurrentPeriod", [])

def getCurrentPrecision() -> float:
	"""
	Gets the current precision.
	
	Returns
	----------
	Precision of the extractor.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "f",
	#     "name": "getCurrentPrecision",
	#     "parametersSignature": "()",
	#     "description": "Gets the current precision.",
	#     "parameters": [],
	#     "returnDescription": "Precision of the extractor."
	# }
	return call_method("ALGazeAnalysis", "getCurrentPrecision", [])

def getMyPeriod(name:str) -> int:
	"""
	Gets the period for a specific subscription.
	
	Parameters
	----------
	name:str
		Name of the module which has subscribed.
	
	Returns
	----------
	Refresh period (in milliseconds).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "getMyPeriod",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the period for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "Name of the module which has subscribed."
	#         }
	#     ],
	#     "returnDescription": "Refresh period (in milliseconds)."
	# }
	return call_method("ALGazeAnalysis", "getMyPeriod", [name])

def getMyPrecision(name:str) -> float:
	"""
	Gets the precision for a specific subscription.
	
	Parameters
	----------
	name:str
		name of the module which has subscribed
	
	Returns
	----------
	precision of the extractor
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "f",
	#     "name": "getMyPrecision",
	#     "parametersSignature": "(s)",
	#     "description": "Gets the precision for a specific subscription.",
	#     "parameters": [
	#         {
	#             "name": "name",
	#             "description": "name of the module which has subscribed"
	#         }
	#     ],
	#     "returnDescription": "precision of the extractor"
	# }
	return call_method("ALGazeAnalysis", "getMyPrecision", [name])

def getSubscribersInfo() -> object:
	"""
	Gets the parameters given by the module.
	
	Returns
	----------
	Array of names and parameters of all subscribers.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getSubscribersInfo",
	#     "parametersSignature": "()",
	#     "description": "Gets the parameters given by the module.",
	#     "parameters": [],
	#     "returnDescription": "Array of names and parameters of all subscribers."
	# }
	return call_method("ALGazeAnalysis", "getSubscribersInfo", [])

def getOutputNames() -> List[str]:
	"""
	Get the list of values updated in ALMemory.
	
	Returns
	----------
	Array of values updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getOutputNames",
	#     "parametersSignature": "()",
	#     "description": "Get the list of values updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of values updated by this extractor in ALMemory"
	# }
	return call_method("ALGazeAnalysis", "getOutputNames", [])

def getEventList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getEventList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALGazeAnalysis", "getEventList", [])

def getMemoryKeyList() -> List[str]:
	"""
	Get the list of events updated in ALMemory.
	
	Returns
	----------
	Array of events updated by this extractor in ALMemory
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "[s]",
	#     "name": "getMemoryKeyList",
	#     "parametersSignature": "()",
	#     "description": "Get the list of events updated in ALMemory.",
	#     "parameters": [],
	#     "returnDescription": "Array of events updated by this extractor in ALMemory"
	# }
	return call_method("ALGazeAnalysis", "getMemoryKeyList", [])

def isPaused() -> bool:
	"""
	Gets extractor pause status
	
	Returns
	----------
	True if the extractor is paused, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "b",
	#     "name": "isPaused",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor pause status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is paused, False if not"
	# }
	return call_method("ALGazeAnalysis", "isPaused", [])

def pause(status:bool) -> None:
	"""
	Changes the pause status of the extractor
	
	Parameters
	----------
	status:bool
		New pause satus
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "pause",
	#     "parametersSignature": "(b)",
	#     "description": "Changes the pause status of the extractor",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "New pause satus"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "pause", [status])

def isProcessing() -> bool:
	"""
	Gets extractor running status
	
	Returns
	----------
	True if the extractor is currently processing images, False if not
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "b",
	#     "name": "isProcessing",
	#     "parametersSignature": "()",
	#     "description": "Gets extractor running status",
	#     "parameters": [],
	#     "returnDescription": "True if the extractor is currently processing images, False if not"
	# }
	return call_method("ALGazeAnalysis", "isProcessing", [])

def setFaceAnalysisEnabled(status:bool) -> None:
	"""
	Turns face analysis on or off.
	
	Parameters
	----------
	status:bool
		True to turn it on, False to turn it off.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "setFaceAnalysisEnabled",
	#     "parametersSignature": "(b)",
	#     "description": "Turns face analysis on or off.",
	#     "parameters": [
	#         {
	#             "name": "status",
	#             "description": "True to turn it on, False to turn it off."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "setFaceAnalysisEnabled", [status])

def isFaceAnalysisEnabled() -> bool:
	"""
	Gets the current status of face analysis.
	
	Returns
	----------
	True if face analysis is enabled, False otherwise.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "b",
	#     "name": "isFaceAnalysisEnabled",
	#     "parametersSignature": "()",
	#     "description": "Gets the current status of face analysis.",
	#     "parameters": [],
	#     "returnDescription": "True if face analysis is enabled, False otherwise."
	# }
	return call_method("ALGazeAnalysis", "isFaceAnalysisEnabled", [])

def setTolerance(tolerance:float) -> None:
	"""
	Sets the tolerance (between 0 and 1) for deciding whether or not a person is looking at the robot after face analysis. This tolerance is used only when face analysis is enabled.
	
	Parameters
	----------
	tolerance:float
		New value of the tolerance (between 0 and 1).
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "setTolerance",
	#     "parametersSignature": "(f)",
	#     "description": "Sets the tolerance (between 0 and 1) for deciding whether or not a person is looking at the robot after face analysis. This tolerance is used only when face analysis is enabled.",
	#     "parameters": [
	#         {
	#             "name": "tolerance",
	#             "description": "New value of the tolerance (between 0 and 1)."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALGazeAnalysis", "setTolerance", [tolerance])

def getTolerance() -> float:
	"""
	Gets the tolerance used to decide whether or not a person is looking at the robot after face analysis.
	
	Returns
	----------
	Current value of the tolerance.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "f",
	#     "name": "getTolerance",
	#     "parametersSignature": "()",
	#     "description": "Gets the tolerance used to decide whether or not a person is looking at the robot after face analysis.",
	#     "parameters": [],
	#     "returnDescription": "Current value of the tolerance."
	# }
	return call_method("ALGazeAnalysis", "getTolerance", [])

