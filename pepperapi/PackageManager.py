"""

"""
from __future__ import annotations
from typing import Dict, List, Tuple, overload
from dataclasses import dataclass, field
from .robot_client import call_method
from .robot_client import Signal, Property

@dataclass
class PackageInfo2:
	"""NAOqi signature: (sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>"""
	uuid: str
	version: str
	author: str
	channel: str
	organization: str
	date: str
	typeVersion: str
	installer: str
	path: str
	elems: Dict[str,object]


@dataclass
class BehaviorInfo:
	"""NAOqi signature: (ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>"""
	path: str
	nature: str
	langToName: Dict[str,str]
	langToDesc: Dict[str,str]
	categories: str
	langToTags: Dict[str,List[str]]
	langToTriggerSentences: Dict[str,List[str]]
	langToLoadingResponses: Dict[str,List[str]]
	purposeToCondition: Dict[str,List[str]]
	permissions: List[str]
	userRequestable: bool


@dataclass
class LanguageInfo:
	"""NAOqi signature: (ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>"""
	path: str
	engineName: str
	engineVersion: str
	locale: str
	langToName: Dict[str,str]


@dataclass
class RobotRequirement:
	"""NAOqi signature: (sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>"""
	model: str
	minHeadVersion: str
	maxHeadVersion: str
	minBodyVersion: str
	maxBodyVersion: str


@dataclass
class NaoqiRequirement:
	"""NAOqi signature: (ss)<NaoqiRequirement,minVersion,maxVersion>"""
	minVersion: str
	maxVersion: str


@dataclass
class PackageService:
	"""NAOqi signature: (ssb)<PackageService,execStart,name,autoRun>"""
	execStart: str
	name: str
	autoRun: bool


@dataclass
class DialogInfo:
	"""NAOqi signature: (ss{ss})<DialogInfo,topicName,typeVersion,topics>"""
	topicName: str
	typeVersion: str
	topics: Dict[str,str]


@dataclass
class PackageInfo:
	"""NAOqi signature: (ssssssss{ss}{ss}[s][BehaviorInfo][LanguageInfo]s[RobotRequirement][NaoqiRequirement][PackageService][s][DialogInfo][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>"""
	uuid: str
	path: str
	version: str
	channel: str
	author: str
	organization: str
	date: str
	typeVersion: str
	langToName: Dict[str,str]
	langToDesc: Dict[str,str]
	supportedLanguages: List[str]
	behaviors: List[BehaviorInfo]
	languages: List[LanguageInfo]
	installer: str
	robotRequirements: List[RobotRequirement]
	naoqiRequirements: List[NaoqiRequirement]
	services: List[PackageService]
	executableFiles: List[str]
	dialogs: List[DialogInfo]
	descriptionLanguages: List[str]


@overload
def install(p0:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	
	Bridge notes
	------------
	install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 100,
	#     "returnSignature": "b",
	#     "name": "install",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def install(p0:str, p1:str, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 120,
	#     "returnSignature": "i",
	#     "name": "install",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def install(p0:str, p1:str, p2:str, /) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	Bridge notes
	------------
	install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 121,
	#     "returnSignature": "i",
	#     "name": "install",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def install(*args, **kwargs):
	"""
	Bridge notes
	------------
	install has 3 variants on the robot:
	- install(p0:str)
	- install(p0:str, p1:str)
	- install(p0:str, p1:str, p2:str)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("PackageManager.install has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("PackageManager", "install", list(args))

def installCheckMd5(p0:str, p1:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 102,
	#     "returnSignature": "b",
	#     "name": "installCheckMd5",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "installCheckMd5", [p0, p1])

@overload
def _install(p0:str, p1:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	
	Bridge notes
	------------
	_install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 103,
	#     "returnSignature": "b",
	#     "name": "_install",
	#     "parametersSignature": "(ss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _install(p0:str, p1:str, p2:str, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	
	Bridge notes
	------------
	_install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 104,
	#     "returnSignature": "b",
	#     "name": "_install",
	#     "parametersSignature": "(sss)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

@overload
def _install(p0:str, p1:str, p2:str, p3:bool, /) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	p1:str
		
	p2:str
		
	p3:bool
		
	
	Bridge notes
	------------
	_install has 3 variants on the robot, chosen by the number of arguments.
	
	Pass arguments by position, not by keyword.
	"""
	# NAOqi metadata:
	# {
	#     "uid": 105,
	#     "returnSignature": "b",
	#     "name": "_install",
	#     "parametersSignature": "(sssb)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	...

def _install(*args, **kwargs):
	"""
	Bridge notes
	------------
	_install has 3 variants on the robot:
	- _install(p0:str, p1:str)
	- _install(p0:str, p1:str, p2:str)
	- _install(p0:str, p1:str, p2:str, p3:bool)
	
	Pass arguments by position, not by keyword.
	"""
	if kwargs:
		raise TypeError("PackageManager._install has several variants on the robot. Pass the arguments by position, without keywords.")
	return call_method("PackageManager", "_install", list(args))

def hasPackage(p0:str) -> bool:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 108,
	#     "returnSignature": "b",
	#     "name": "hasPackage",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "hasPackage", [p0])

def packages2() -> List[PackageInfo2]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 109,
	#     "returnSignature": "[(sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>]",
	#     "name": "packages2",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "packages2", [], returns=List[PackageInfo2])

def package2(p0:str) -> PackageInfo2:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 110,
	#     "returnSignature": "(sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>",
	#     "name": "package2",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "package2", [p0], returns=PackageInfo2)

def packageIcon(p0:str) -> str:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 111,
	#     "returnSignature": "s",
	#     "name": "packageIcon",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "packageIcon", [p0])

def removePkg(p0:str) -> None:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 112,
	#     "returnSignature": "v",
	#     "name": "removePkg",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "removePkg", [p0])

def getPackages() -> object:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 115,
	#     "returnSignature": "m",
	#     "name": "getPackages",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "getPackages", [])

def packages() -> List[PackageInfo]:
	"""
	
	"""
	# NAOqi metadata:
	# {
	#     "uid": 116,
	#     "returnSignature": "[(ssssssss{ss}{ss}[s][(ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>][(ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>]s[(sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>][(ss)<NaoqiRequirement,minVersion,maxVersion>][(ssb)<PackageService,execStart,name,autoRun>][s][(ss{ss})<DialogInfo,topicName,typeVersion,topics>][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>]",
	#     "name": "packages",
	#     "parametersSignature": "()",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "packages", [], returns=List[PackageInfo])

def package(p0:str) -> PackageInfo:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 117,
	#     "returnSignature": "(ssssssss{ss}{ss}[s][(ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>][(ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>]s[(sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>][(ss)<NaoqiRequirement,minVersion,maxVersion>][(ssb)<PackageService,execStart,name,autoRun>][s][(ss{ss})<DialogInfo,topicName,typeVersion,topics>][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>",
	#     "name": "package",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "package", [p0], returns=PackageInfo)

def getPackage(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 118,
	#     "returnSignature": "m",
	#     "name": "getPackage",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "getPackage", [p0])

def getPackageIcon(p0:str) -> object:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 119,
	#     "returnSignature": "m",
	#     "name": "getPackageIcon",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "getPackageIcon", [p0])

def remove(p0:str) -> int:
	"""
	
	
	Parameters
	----------
	p0:str
		
	"""
	# NAOqi metadata:
	# {
	#     "uid": 122,
	#     "returnSignature": "i",
	#     "name": "remove",
	#     "parametersSignature": "(s)",
	#     "description": "",
	#     "parameters": [],
	#     "returnDescription": ""
	# }
	return call_method("PackageManager", "remove", [p0])

class _Signals:
	onPackageInstalled2: Signal[[PackageInfo2]] = Signal("PackageManager", "onPackageInstalled2", (PackageInfo2,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo2) each time the robot sends it.
	"""
	onPackageRemoved2: Signal[[PackageInfo2]] = Signal("PackageManager", "onPackageRemoved2", (PackageInfo2,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo2) each time the robot sends it.
	"""
	_onPackageInstalled: Signal[[object]] = Signal("PackageManager", "_onPackageInstalled")
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(object) each time the robot sends it.
	"""
	_onPackageRemoved: Signal[[object]] = Signal("PackageManager", "_onPackageRemoved")
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(object) each time the robot sends it.
	"""
	packageInstalled: Signal[[PackageInfo]] = Signal("PackageManager", "packageInstalled", (PackageInfo,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo) each time the robot sends it.
	"""
	packageRemoved: Signal[[PackageInfo]] = Signal("PackageManager", "packageRemoved", (PackageInfo,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo) each time the robot sends it.
	"""
	onPackageInstalled: Signal[[PackageInfo]] = Signal("PackageManager", "onPackageInstalled", (PackageInfo,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo) each time the robot sends it.
	"""
	onPackageRemoved: Signal[[PackageInfo]] = Signal("PackageManager", "onPackageRemoved", (PackageInfo,))
	"""
	Bridge notes
	------------
	A signal sent by PackageManager on the robot.
	
	subscribe(callback) calls callback(PackageInfo) each time the robot sends it.
	"""
signals = _Signals()

