"""

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
	return call_method("_Smoother", "version", [])

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
	return call_method("_Smoother", "ping", [])

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
	return call_method("_Smoother", "getMethodList", [])

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
	return call_method("_Smoother", "getMethodHelp", [methodName])

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
	return call_method("_Smoother", "getModuleHelp", [])

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
	return call_method("_Smoother", "getBrokerName", [])

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
	return call_method("_Smoother", "getUsage", [name])

@overload
def startEvent(pEventName:str, /) -> None:
	"""
	Start the smoother with Event.
	
	Parameters
	----------
	pEventName:str
		The detector event name with Position6D output.
	
	Bridge notes
	------------
	startEvent has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "startEvent",
	#     "parametersSignature": "(s)",
	#     "description": "Start the smoother with Event.",
	#     "parameters": [
	#         {
	#             "name": "pEventName",
	#             "description": "The detector event name with Position6D output."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def startEvent(first_event_name:str, second_event_name:str, /) -> None:
	"""
	Start the smoother with events.
	
	Parameters
	----------
	first_event_name:str
		The first detector event name with Position6D output.
	second_event_name:str
		The second detector event name with Position6D output.
	
	Bridge notes
	------------
	startEvent has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "startEvent",
	#     "parametersSignature": "(ss)",
	#     "description": "Start the smoother with events.",
	#     "parameters": [
	#         {
	#             "name": "first event name",
	#             "description": "The first detector event name with Position6D output."
	#         },
	#         {
	#             "name": "second event name",
	#             "description": "The second detector event name with Position6D output."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def startEvent(*args, **kwargs):
	"""
	Bridge notes
	------------
	startEvent has 2 variants on the robot:
	- startEvent(pEventName:str)
	- startEvent(first_event_name:str, second_event_name:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_Smoother.startEvent has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_Smoother", "startEvent", list(args))

@overload
def restart(pEventName:str, /) -> None:
	"""
	Restart the smoother with Event.
	
	Parameters
	----------
	pEventName:str
		The detector event name with Position6D output.
	
	Bridge notes
	------------
	restart has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "v",
	#     "name": "restart",
	#     "parametersSignature": "(s)",
	#     "description": "Restart the smoother with Event.",
	#     "parameters": [
	#         {
	#             "name": "pEventName",
	#             "description": "The detector event name with Position6D output."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

@overload
def restart(first_event_name:str, second_event_name:str, /) -> None:
	"""
	Restart the smoother with events.
	
	Parameters
	----------
	first_event_name:str
		The first detector event name with Position6D output.
	second_event_name:str
		The second detector event name with Position6D output.
	
	Bridge notes
	------------
	restart has 2 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "restart",
	#     "parametersSignature": "(ss)",
	#     "description": "Restart the smoother with events.",
	#     "parameters": [
	#         {
	#             "name": "first event name",
	#             "description": "The first detector event name with Position6D output."
	#         },
	#         {
	#             "name": "second event name",
	#             "description": "The second detector event name with Position6D output."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	...

def restart(*args, **kwargs):
	"""
	Bridge notes
	------------
	restart has 2 variants on the robot:
	- restart(pEventName:str)
	- restart(first_event_name:str, second_event_name:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("_Smoother.restart has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("_Smoother", "restart", list(args))

def setMap(p0:object) -> None:
	"""
	Set the Map of the world.
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "setMap",
	#     "parametersSignature": "(m)",
	#     "description": "Set the Map of the world.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "setMap", [p0])

def setTarget(p0:object) -> None:
	"""
	Set the target.
	
	Parameters
	----------
	p0:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "v",
	#     "name": "setTarget",
	#     "parametersSignature": "(m)",
	#     "description": "Set the target.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "setTarget", [p0])

def setTargetIds(p0:int, p1:int) -> None:
	"""
	Set the target ids.
	
	Parameters
	----------
	p0:int
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "setTargetIds",
	#     "parametersSignature": "(ii)",
	#     "description": "Set the target ids.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "setTargetIds", [p0, p1])

def getPosition() -> object:
	"""
	Allow to get the position of robot in the map Space.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "m",
	#     "name": "getPosition",
	#     "parametersSignature": "()",
	#     "description": "Allow to get the position of robot in the map Space.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "getPosition", [])

def stopSmoother() -> None:
	"""
	Stop the smoother.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "stopSmoother",
	#     "parametersSignature": "()",
	#     "description": "Stop the smoother.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "stopSmoother", [])

def _smoothEvent(p0:str, p1:object) -> None:
	"""
	Is the callback.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "v",
	#     "name": "_smoothEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Is the callback.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_smoothEvent", [p0, p1])

def _smoothFirstEvent(p0:str, p1:object) -> None:
	"""
	Is the callback for the first object.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "v",
	#     "name": "_smoothFirstEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Is the callback for the first object.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_smoothFirstEvent", [p0, p1])

def _smoothSecondEvent(p0:str, p1:object) -> None:
	"""
	Is the callback for the second object.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "v",
	#     "name": "_smoothSecondEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Is the callback for the second object.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_smoothSecondEvent", [p0, p1])

def _raiseSearchEvent() -> None:
	"""
	Restart search process.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "_raiseSearchEvent",
	#     "parametersSignature": "()",
	#     "description": "Restart search process.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_raiseSearchEvent", [])

def getTimeOut() -> int:
	"""
	get the time out parameter for target lost.
	
	Returns
	----------
	time in milliseconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "i",
	#     "name": "getTimeOut",
	#     "parametersSignature": "()",
	#     "description": "get the time out parameter for target lost.",
	#     "parameters": [],
	#     "returnDescription": "time in milliseconds."
	# }
	return call_method("_Smoother", "getTimeOut", [])

def setTimeOut(pTime:int) -> None:
	"""
	set the time out parameter for target lost.
	
	Parameters
	----------
	pTime:int
		time in milliseconds.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "v",
	#     "name": "setTimeOut",
	#     "parametersSignature": "(i)",
	#     "description": "set the time out parameter for target lost.",
	#     "parameters": [
	#         {
	#             "name": "pTime",
	#             "description": "time in milliseconds."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "setTimeOut", [pTime])

def getMaxDistance() -> float:
	"""
	get the maximum distance parameter for target lost.
	
	Returns
	----------
	Distance in meter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "f",
	#     "name": "getMaxDistance",
	#     "parametersSignature": "()",
	#     "description": "get the maximum distance parameter for target lost.",
	#     "parameters": [],
	#     "returnDescription": "Distance in meter."
	# }
	return call_method("_Smoother", "getMaxDistance", [])

def setMaxDistance(pDistance:float) -> None:
	"""
	set the maximum distance parameter for target lost.
	
	Parameters
	----------
	pDistance:float
		Distance in meter.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "v",
	#     "name": "setMaxDistance",
	#     "parametersSignature": "(f)",
	#     "description": "set the maximum distance parameter for target lost.",
	#     "parameters": [
	#         {
	#             "name": "pDistance",
	#             "description": "Distance in meter."
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "setMaxDistance", [pDistance])

def _setMoveEvent(p0:str) -> None:
	"""
	Set a specific event for move.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "v",
	#     "name": "_setMoveEvent",
	#     "parametersSignature": "(s)",
	#     "description": "Set a specific event for move.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_setMoveEvent", [p0])

def _smoothMoveEvent(p0:str, p1:object) -> None:
	"""
	Callback for move event.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "v",
	#     "name": "_smoothMoveEvent",
	#     "parametersSignature": "(sm)",
	#     "description": "Callback for move event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_smoothMoveEvent", [p0, p1])

def _disableFeaturesChanged(p0:str, p1:object) -> None:
	"""
	Is the callback for motion disabled features event.
	
	Parameters
	----------
	p0:str
		
	p1:object
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "v",
	#     "name": "_disableFeaturesChanged",
	#     "parametersSignature": "(sm)",
	#     "description": "Is the callback for motion disabled features event.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_disableFeaturesChanged", [p0, p1])

def _setMoveHysteresis(p0:List[float]) -> None:
	"""
	Set move hysteresis.
	
	Parameters
	----------
	p0:List[float]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "v",
	#     "name": "_setMoveHysteresis",
	#     "parametersSignature": "([f])",
	#     "description": "Set move hysteresis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_setMoveHysteresis", [p0])

def _getMoveHysteresis() -> List[float]:
	"""
	Set move hysteresis.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "[f]",
	#     "name": "_getMoveHysteresis",
	#     "parametersSignature": "()",
	#     "description": "Set move hysteresis.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("_Smoother", "_getMoveHysteresis", [])

