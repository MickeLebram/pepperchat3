"""
Manage robot resources: Synchronize movement, led, sound. Run specific actions when another behavior wants your resources
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
	return call_method("ALResourceManager", "version", [])

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
	return call_method("ALResourceManager", "ping", [])

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
	return call_method("ALResourceManager", "getMethodList", [])

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
	return call_method("ALResourceManager", "getMethodHelp", [methodName])

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
	return call_method("ALResourceManager", "getModuleHelp", [])

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
	return call_method("ALResourceManager", "getBrokerName", [])

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
	return call_method("ALResourceManager", "getUsage", [name])

def waitForResource(resourceName:str, ownerName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	ownerName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 114,
	#     "returnSignature": "v",
	#     "name": "waitForResource",
	#     "parametersSignature": "(sssi)",
	#     "description": "Wait resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "ownerName",
	#             "description": "Module name"
	#         },
	#         {
	#             "name": "callbackName",
	#             "description": "callback name"
	#         },
	#         {
	#             "name": "timeoutSeconds",
	#             "description": "Timeout in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "waitForResource", [resourceName, ownerName, callbackName, timeoutSeconds])

def acquireResource(resourceName:str, moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait and acquire a resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "v",
	#     "name": "acquireResource",
	#     "parametersSignature": "(sssi)",
	#     "description": "Wait and acquire a resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "moduleName",
	#             "description": "Module name"
	#         },
	#         {
	#             "name": "callbackName",
	#             "description": "callback name"
	#         },
	#         {
	#             "name": "timeoutSeconds",
	#             "description": "Timeout in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "acquireResource", [resourceName, moduleName, callbackName, timeoutSeconds])

def waitForOptionalResourcesTree(p0:List[str], p1:str, p2:str, p3:int, p4:List[str]) -> List[str]:
	"""
	Wait resource
	
	Parameters
	----------
	p0:List[str]
		
	p1:str
		
	p2:str
		
	p3:int
		
	p4:List[str]
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "[s]",
	#     "name": "waitForOptionalResourcesTree",
	#     "parametersSignature": "([s]ssi[s])",
	#     "description": "Wait resource",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "waitForOptionalResourcesTree", [p0, p1, p2, p3, p4])

def waitForResourcesTree(resourceName:List[str], moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait for resource tree. Parent and children are not in conflict. Local function
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "v",
	#     "name": "waitForResourcesTree",
	#     "parametersSignature": "([s]ssi)",
	#     "description": "Wait for resource tree. Parent and children are not in conflict. Local function",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "moduleName",
	#             "description": "Module name"
	#         },
	#         {
	#             "name": "callbackName",
	#             "description": "callback name"
	#         },
	#         {
	#             "name": "timeoutSeconds",
	#             "description": "Timeout in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "waitForResourcesTree", [resourceName, moduleName, callbackName, timeoutSeconds])

def acquireResourcesTree(resourceName:List[str], moduleName:str, callbackName:str, timeoutSeconds:int) -> None:
	"""
	Wait for resource tree. Parent and children are not in conflict. Local function
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	moduleName:str
		Module name
	callbackName:str
		callback name
	timeoutSeconds:int
		Timeout in seconds
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "v",
	#     "name": "acquireResourcesTree",
	#     "parametersSignature": "([s]ssi)",
	#     "description": "Wait for resource tree. Parent and children are not in conflict. Local function",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "moduleName",
	#             "description": "Module name"
	#         },
	#         {
	#             "name": "callbackName",
	#             "description": "callback name"
	#         },
	#         {
	#             "name": "timeoutSeconds",
	#             "description": "Timeout in seconds"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "acquireResourcesTree", [resourceName, moduleName, callbackName, timeoutSeconds])

def areResourcesOwnedBy(resourceNameList:List[str], ownerName:str) -> bool:
	"""
	True if all the specified resources are owned by the owner
	
	Parameters
	----------
	resourceNameList:List[str]
		Resource name
	ownerName:str
		Owner pointer with hierarchy
	
	Returns
	----------
	True if all the specify resources are owned by the owner
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "b",
	#     "name": "areResourcesOwnedBy",
	#     "parametersSignature": "([s]s)",
	#     "description": "True if all the specified resources are owned by the owner",
	#     "parameters": [
	#         {
	#             "name": "resourceNameList",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "ownerName",
	#             "description": "Owner pointer with hierarchy"
	#         }
	#     ],
	#     "returnDescription": "True if all the specify resources are owned by the owner"
	# }
	return call_method("ALResourceManager", "areResourcesOwnedBy", [resourceNameList, ownerName])

def releaseResource(resourceName:str, ownerName:str) -> None:
	"""
	Release resource
	
	Parameters
	----------
	resourceName:str
		Resource name
	ownerName:str
		Existing owner name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "v",
	#     "name": "releaseResource",
	#     "parametersSignature": "(ss)",
	#     "description": "Release resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         },
	#         {
	#             "name": "ownerName",
	#             "description": "Existing owner name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "releaseResource", [resourceName, ownerName])

def releaseResources(resourceNames:List[str], ownerName:str) -> None:
	"""
	Release  resources list
	
	Parameters
	----------
	resourceNames:List[str]
		Resource names
	ownerName:str
		Owner name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "v",
	#     "name": "releaseResources",
	#     "parametersSignature": "([s]s)",
	#     "description": "Release  resources list",
	#     "parameters": [
	#         {
	#             "name": "resourceNames",
	#             "description": "Resource names"
	#         },
	#         {
	#             "name": "ownerName",
	#             "description": "Owner name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "releaseResources", [resourceNames, ownerName])

def enableStateResource(resourceName:str, enabled:bool) -> None:
	"""
	Enable or disable a state resource
	
	Parameters
	----------
	resourceName:str
		The name of the resource that you wish enable of disable. e.g. Standing
	enabled:bool
		True to enable, false to disable
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "v",
	#     "name": "enableStateResource",
	#     "parametersSignature": "(sb)",
	#     "description": "Enable or disable a state resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "The name of the resource that you wish enable of disable. e.g. Standing"
	#         },
	#         {
	#             "name": "enabled",
	#             "description": "True to enable, false to disable"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "enableStateResource", [resourceName, enabled])

def checkStateResourceFree(resourceName:List[str]) -> bool:
	"""
	check if all the state resource in the list are free
	
	Parameters
	----------
	resourceName:List[str]
		Resource name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 123,
	#     "returnSignature": "b",
	#     "name": "checkStateResourceFree",
	#     "parametersSignature": "([s])",
	#     "description": "check if all the state resource in the list are free",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "checkStateResourceFree", [resourceName])

def areResourcesFree(resourceNames:List[str]) -> bool:
	"""
	True if all resources are free
	
	Parameters
	----------
	resourceNames:List[str]
		Resource names
	
	Returns
	----------
	True if all the specify resources are free
	"""
	# NAOqi metadata:
	# {
	#     "uid": 124,
	#     "returnSignature": "b",
	#     "name": "areResourcesFree",
	#     "parametersSignature": "([s])",
	#     "description": "True if all resources are free",
	#     "parameters": [
	#         {
	#             "name": "resourceNames",
	#             "description": "Resource names"
	#         }
	#     ],
	#     "returnDescription": "True if all the specify resources are free"
	# }
	return call_method("ALResourceManager", "areResourcesFree", [resourceNames])

def isResourceFree(resourceNames:str) -> bool:
	"""
	True if the resource is free
	
	Parameters
	----------
	resourceNames:str
		Resource name
	
	Returns
	----------
	True if the specify resources is free
	"""
	# NAOqi metadata:
	# {
	#     "uid": 125,
	#     "returnSignature": "b",
	#     "name": "isResourceFree",
	#     "parametersSignature": "(s)",
	#     "description": "True if the resource is free",
	#     "parameters": [
	#         {
	#             "name": "resourceNames",
	#             "description": "Resource name"
	#         }
	#     ],
	#     "returnDescription": "True if the specify resources is free"
	# }
	return call_method("ALResourceManager", "isResourceFree", [resourceNames])

def createResource(resourceName:str, parentResourceName:str) -> None:
	"""
	Create a resource
	
	Parameters
	----------
	resourceName:str
		Resource name to create
	parentResourceName:str
		Parent resource name or empty string for root resource
	"""
	# NAOqi metadata:
	# {
	#     "uid": 126,
	#     "returnSignature": "v",
	#     "name": "createResource",
	#     "parametersSignature": "(ss)",
	#     "description": "Create a resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name to create"
	#         },
	#         {
	#             "name": "parentResourceName",
	#             "description": "Parent resource name or empty string for root resource"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "createResource", [resourceName, parentResourceName])

def deleteResource(resourceName:str, deleteChildResources:bool) -> None:
	"""
	Delete a root resource
	
	Parameters
	----------
	resourceName:str
		Resource name to delete
	deleteChildResources:bool
		DEPRECATED: Delete child resources if true
	"""
	# NAOqi metadata:
	# {
	#     "uid": 127,
	#     "returnSignature": "v",
	#     "name": "deleteResource",
	#     "parametersSignature": "(sb)",
	#     "description": "Delete a root resource",
	#     "parameters": [
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name to delete"
	#         },
	#         {
	#             "name": "deleteChildResources",
	#             "description": "DEPRECATED: Delete child resources if true"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "deleteResource", [resourceName, deleteChildResources])

def isInGroup(resourceGroupName:str, resourceName:str) -> bool:
	"""
	True if a resource is in another parent resource
	
	Parameters
	----------
	resourceGroupName:str
		Group name. Ex: Arm
	resourceName:str
		Resource name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 128,
	#     "returnSignature": "b",
	#     "name": "isInGroup",
	#     "parametersSignature": "(ss)",
	#     "description": "True if a resource is in another parent resource",
	#     "parameters": [
	#         {
	#             "name": "resourceGroupName",
	#             "description": "Group name. Ex: Arm"
	#         },
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "isInGroup", [resourceGroupName, resourceName])

def createResourcesList(resourceGroupName:List[str], resourceName:str) -> None:
	"""
	True if a resource is in another parent resource
	
	Parameters
	----------
	resourceGroupName:List[str]
		Group name. Ex: Arm
	resourceName:str
		Resource name
	"""
	# NAOqi metadata:
	# {
	#     "uid": 129,
	#     "returnSignature": "v",
	#     "name": "createResourcesList",
	#     "parametersSignature": "([s]s)",
	#     "description": "True if a resource is in another parent resource",
	#     "parameters": [
	#         {
	#             "name": "resourceGroupName",
	#             "description": "Group name. Ex: Arm"
	#         },
	#         {
	#             "name": "resourceName",
	#             "description": "Resource name"
	#         }
	#     ],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "createResourcesList", [resourceGroupName, resourceName])

def getResources() -> object:
	"""
	Get tree of resources
	"""
	# NAOqi metadata:
	# {
	#     "uid": 130,
	#     "returnSignature": "m",
	#     "name": "getResources",
	#     "parametersSignature": "()",
	#     "description": "Get tree of resources",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "getResources", [])

def ownersGet() -> object:
	"""
	The tree of the resources owners.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 131,
	#     "returnSignature": "m",
	#     "name": "ownersGet",
	#     "parametersSignature": "()",
	#     "description": "The tree of the resources owners.",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("ALResourceManager", "ownersGet", [])

