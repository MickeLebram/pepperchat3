"""

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
	return call_method("ALWorldRepresentation", "version", [])

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
	return call_method("ALWorldRepresentation", "ping", [])

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
	return call_method("ALWorldRepresentation", "getMethodList", [])

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
	return call_method("ALWorldRepresentation", "getMethodHelp", [methodName])

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
	return call_method("ALWorldRepresentation", "getModuleHelp", [])

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
	return call_method("ALWorldRepresentation", "getBrokerName", [])

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
	return call_method("ALWorldRepresentation", "getUsage", [name])

def addAttributeToCategory(p0:str, p1:str, p2:Any) -> int:
	"""
	Add an attribute to a category.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "i",
	#     "name": "addAttributeToCategory",
	#     "parametersSignature": "(ssm)",
	#     "description": "Add an attribute to a category.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "addAttributeToCategory", [p0, p1, p2])

def clearObject(p0:str) -> int:
	"""
	Clear an object.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "i",
	#     "name": "clearObject",
	#     "parametersSignature": "(s)",
	#     "description": "Clear an object.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "clearObject", [p0])

def clearOldPositions(p0:str, p1:int) -> int:
	"""
	Clear recording of old positions.
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "i",
	#     "name": "clearOldPositions",
	#     "parametersSignature": "(si)",
	#     "description": "Clear recording of old positions.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "clearOldPositions", [p0, p1])

def createObjectCategory(p0:str, p1:bool) -> int:
	"""
	Create a new object category
	
	Parameters
	----------
	p0:str
		
	p1:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "i",
	#     "name": "createObjectCategory",
	#     "parametersSignature": "(sb)",
	#     "description": "Create a new object category",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "createObjectCategory", [p0, p1])

def removeObjectCategory(p0:str) -> int:
	"""
	Remove an object category
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "i",
	#     "name": "removeObjectCategory",
	#     "parametersSignature": "(s)",
	#     "description": "Remove an object category",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "removeObjectCategory", [p0])

def objectCategoryExists(p0:str) -> bool:
	"""
	Tells if an object category exists
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "objectCategoryExists",
	#     "parametersSignature": "(s)",
	#     "description": "Tells if an object category exists",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "objectCategoryExists", [p0])

def deleteObjectAttribute(p0:str, p1:str, p2:str) -> int:
	"""
	Delete an object attribute
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "deleteObjectAttribute",
	#     "parametersSignature": "(sss)",
	#     "description": "Delete an object attribute",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "deleteObjectAttribute", [p0, p1, p2])

def findObject(p0:str) -> bool:
	"""
	Check that an object is present.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "b",
	#     "name": "findObject",
	#     "parametersSignature": "(s)",
	#     "description": "Check that an object is present.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "findObject", [p0])

def load() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "load",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "load", [])

def getAttributesFromCategory(p0:str) -> Any:
	"""
	Get all attributes from a category if it exists.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "m",
	#     "name": "getAttributesFromCategory",
	#     "parametersSignature": "(s)",
	#     "description": "Get all attributes from a category if it exists.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getAttributesFromCategory", [p0])

def getChildrenNames(p0:str) -> List[str]:
	"""
	Get the direct children of an object.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "[s]",
	#     "name": "getChildrenNames",
	#     "parametersSignature": "(s)",
	#     "description": "Get the direct children of an object.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getChildrenNames", [p0])

def getObjectNames() -> List[str]:
	"""
	Get the name of the objects.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "[s]",
	#     "name": "getObjectNames",
	#     "parametersSignature": "()",
	#     "description": "Get the name of the objects.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectNames", [])

def getObjectAttributes(p0:str) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "m",
	#     "name": "getObjectAttributes",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectAttributes", [p0])

def getObjectAttributeValues(p0:str, p1:str, p2:int) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "m",
	#     "name": "getObjectAttributeValues",
	#     "parametersSignature": "(ssi)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectAttributeValues", [p0, p1, p2])

def getObjectLatestAttributes(p0:str, p1:int) -> Any:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "m",
	#     "name": "getObjectLatestAttributes",
	#     "parametersSignature": "(si)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectLatestAttributes", [p0, p1])

def getObjectParentName(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "s",
	#     "name": "getObjectParentName",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectParentName", [p0])

def getObjectsInCategory(p0:str) -> List[str]:
	"""
	Get the name of the objects stored in the database.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "[s]",
	#     "name": "getObjectsInCategory",
	#     "parametersSignature": "(s)",
	#     "description": "Get the name of the objects stored in the database.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectsInCategory", [p0])

def getObjectCategory(p0:str) -> str:
	"""
	Get the name of the database where the object is stored.
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "s",
	#     "name": "getObjectCategory",
	#     "parametersSignature": "(s)",
	#     "description": "Get the name of the database where the object is stored.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getObjectCategory", [p0])

def getPosition(p0:str, p1:str) -> Any:
	"""
	Get the position of an object with quaternion / translation.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 132,
	#     "returnSignature": "m",
	#     "name": "getPosition",
	#     "parametersSignature": "(ss)",
	#     "description": "Get the position of an object with quaternion / translation.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getPosition", [p0, p1])

def getPosition6D(p0:str, p1:str) -> List[float]:
	"""
	Get the position from one object to another.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 133,
	#     "returnSignature": "[f]",
	#     "name": "getPosition6D",
	#     "parametersSignature": "(ss)",
	#     "description": "Get the position from one object to another.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getPosition6D", [p0, p1])

def getPosition6DAtTime(p0:str, p1:str, p2:int, p3:int) -> List[float]:
	"""
	Get the interpolated position of an object
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:int
		
	p3:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 134,
	#     "returnSignature": "[f]",
	#     "name": "getPosition6DAtTime",
	#     "parametersSignature": "(ssii)",
	#     "description": "Get the interpolated position of an object",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getPosition6DAtTime", [p0, p1, p2, p3])

def getRootName() -> str:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 135,
	#     "returnSignature": "s",
	#     "name": "getRootName",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "getRootName", [])

def save() -> int:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 136,
	#     "returnSignature": "i",
	#     "name": "save",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "save", [])

def select(p0:str, p1:str, p2:str, p3:str) -> Any:
	"""
	Select information from a database.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 137,
	#     "returnSignature": "m",
	#     "name": "select",
	#     "parametersSignature": "(ssss)",
	#     "description": "Select information from a database.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "select", [p0, p1, p2, p3])

def selectWithOrder(p0:str, p1:str, p2:str, p3:str, p4:str) -> Any:
	"""
	Select ordered information from a database.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:str
		
	p4:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 138,
	#     "returnSignature": "m",
	#     "name": "selectWithOrder",
	#     "parametersSignature": "(sssss)",
	#     "description": "Select ordered information from a database.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "selectWithOrder", [p0, p1, p2, p3, p4])

def storeObject(p0:str, p1:str, p2:List[float], p3:str, p4:Any) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:List[float]
		
	p3:str
		
	p4:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 139,
	#     "returnSignature": "i",
	#     "name": "storeObject",
	#     "parametersSignature": "(ss[f]sm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "storeObject", [p0, p1, p2, p3, p4])

def storeObjectWithReference(p0:str, p1:str, p2:str, p3:List[float], p4:str, p5:Any) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:List[float]
		
	p4:str
		
	p5:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 140,
	#     "returnSignature": "i",
	#     "name": "storeObjectWithReference",
	#     "parametersSignature": "(sss[f]sm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "storeObjectWithReference", [p0, p1, p2, p3, p4, p5])

def storeObjectAttribute(p0:str, p1:str, p2:Any) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 141,
	#     "returnSignature": "i",
	#     "name": "storeObjectAttribute",
	#     "parametersSignature": "(ssm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "storeObjectAttribute", [p0, p1, p2])

def updatePosition(p0:str, p1:List[float], p2:bool) -> int:
	"""
	Update the position of an object.
	
	Parameters
	----------
	p0:str
		
	p1:List[float]
		
	p2:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 142,
	#     "returnSignature": "i",
	#     "name": "updatePosition",
	#     "parametersSignature": "(s[f]b)",
	#     "description": "Update the position of an object.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "updatePosition", [p0, p1, p2])

def updatePositionWithReference(p0:str, p1:str, p2:List[float], p3:bool) -> int:
	"""
	Update the position of an object relative to another.
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:List[float]
		
	p3:bool
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 143,
	#     "returnSignature": "i",
	#     "name": "updatePositionWithReference",
	#     "parametersSignature": "(ss[f]b)",
	#     "description": "Update the position of an object relative to another.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "updatePositionWithReference", [p0, p1, p2, p3])

def updateAttribute(p0:str, p1:str, p2:str, p3:Any) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:Any
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 144,
	#     "returnSignature": "i",
	#     "name": "updateAttribute",
	#     "parametersSignature": "(sssm)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "updateAttribute", [p0, p1, p2, p3])

def _startMemoryCheck(p0:int) -> None:
	"""
	
	
	Parameters
	----------
	p0:int
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 145,
	#     "returnSignature": "v",
	#     "name": "_startMemoryCheck",
	#     "parametersSignature": "(i)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "_startMemoryCheck", [p0])

def _stopMemoryCheck() -> None:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 146,
	#     "returnSignature": "v",
	#     "name": "_stopMemoryCheck",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "_stopMemoryCheck", [])

def _beginTransaction(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 147,
	#     "returnSignature": "i",
	#     "name": "_beginTransaction",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "_beginTransaction", [p0])

def _endTransaction(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 148,
	#     "returnSignature": "i",
	#     "name": "_endTransaction",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALWorldRepresentation", "_endTransaction", [p0])

