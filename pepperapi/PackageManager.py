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
	return send_mfc("PackageManager", "registerEvent", [p0, p1, p2])

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
	return send_mfc("PackageManager", "unregisterEvent", [p0, p1, p2])

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
	return send_mfc("PackageManager", "metaObject", [p0])

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
	return send_mfc("PackageManager", "terminate", [p0])

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
	return send_mfc("PackageManager", "property", [p0])

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
	return send_mfc("PackageManager", "setProperty", [p0, p1])

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
	return send_mfc("PackageManager", "properties", [])

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
	return send_mfc("PackageManager", "registerEventWithSignature", [p0, p1, p2, p3])

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
	return send_mfc("PackageManager", "isStatsEnabled", [])

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
	return send_mfc("PackageManager", "enableStats", [p0])

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
	return send_mfc("PackageManager", "stats", [])

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
	return send_mfc("PackageManager", "clearStats", [])

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
	return send_mfc("PackageManager", "isTraceEnabled", [])

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
	return send_mfc("PackageManager", "enableTrace", [p0])

def install_1(p0:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (install)
	
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "b",
	    "name": "install",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "install", [p0])

def install_2(p0:object) -> bool:
	"""
	Note: This is one of the overloads of the original method (install)
	
	
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "b",
	    "name": "install",
	    "parametersSignature": "(o)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "install", [p0])

def installCheckMd5(p0:str, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "b",
	    "name": "installCheckMd5",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "installCheckMd5", [p0, p1])

def _install_1(p0:str, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_install)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "b",
	    "name": "_install",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "_install", [p0, p1])

def _install_2(p0:str, p1:str, p2:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_install)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "b",
	    "name": "_install",
	    "parametersSignature": "(sss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "_install", [p0, p1, p2])

def _install_3(p0:str, p1:str, p2:str, p3:bool) -> bool:
	"""
	Note: This is one of the overloads of the original method (_install)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:bool
		
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "b",
	    "name": "_install",
	    "parametersSignature": "(sssb)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "_install", [p0, p1, p2, p3])

def _install_4(p0:object, p1:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_install)
	
	
	
	Parameters
	----------
	p0:object
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "b",
	    "name": "_install",
	    "parametersSignature": "(os)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "_install", [p0, p1])

def _install_5(p0:object, p1:str, p2:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (_install)
	
	
	
	Parameters
	----------
	p0:object
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "b",
	    "name": "_install",
	    "parametersSignature": "(oss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "_install", [p0, p1, p2])

def hasPackage(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "b",
	    "name": "hasPackage",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "hasPackage", [p0])

def packages2() -> List[PackageInfo2]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "[(sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>]",
	    "name": "packages2",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "packages2", [])

def package2(p0:str) -> PackageInfo2:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "(sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>",
	    "name": "package2",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "package2", [p0])

def packageIcon(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "s",
	    "name": "packageIcon",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "packageIcon", [p0])

def removePkg(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "v",
	    "name": "removePkg",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "removePkg", [p0])

def getPackages() -> object:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 115,
	    "returnSignature": "m",
	    "name": "getPackages",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "getPackages", [])

def packages() -> List[PackageInfo]:
	"""
	
	
	*Reference struct*
	'''
	{
	    "uid": 116,
	    "returnSignature": "[(ssssssss{ss}{ss}[s][(ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>][(ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>]s[(sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>][(ss)<NaoqiRequirement,minVersion,maxVersion>][(ssb)<PackageService,execStart,name,autoRun>][s][(ss{ss})<DialogInfo,topicName,typeVersion,topics>][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>]",
	    "name": "packages",
	    "parametersSignature": "()",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "packages", [])

def package(p0:str) -> PackageInfo:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 117,
	    "returnSignature": "(ssssssss{ss}{ss}[s][(ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>][(ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>]s[(sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>][(ss)<NaoqiRequirement,minVersion,maxVersion>][(ssb)<PackageService,execStart,name,autoRun>][s][(ss{ss})<DialogInfo,topicName,typeVersion,topics>][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>",
	    "name": "package",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "package", [p0])

def getPackage(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "getPackage",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "getPackage", [p0])

def getPackageIcon(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "getPackageIcon",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "getPackageIcon", [p0])

def install_3(p0:str, p1:str) -> int:
	"""
	Note: This is one of the overloads of the original method (install)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "i",
	    "name": "install",
	    "parametersSignature": "(ss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "install", [p0, p1])

def install_4(p0:str, p1:str, p2:str) -> int:
	"""
	Note: This is one of the overloads of the original method (install)
	
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "i",
	    "name": "install",
	    "parametersSignature": "(sss)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "install", [p0, p1, p2])

def remove(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "i",
	    "name": "remove",
	    "parametersSignature": "(s)",
	    "description": "",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("PackageManager", "remove", [p0])

