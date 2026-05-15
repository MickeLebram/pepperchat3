from typing import List, Dict, Tuple
class MetaMethodParameter:
	def __init__(self):
		'''
		(ss)<MetaMethodParameter,name,description>
		'''
		name:str = None
		description:str = None
class MetaSignal:
	def __init__(self):
		'''
		(Iss)<MetaSignal,uid,name,signature>
		'''
		uid:int = None
		name:str = None
		signature:str = None
class MetaProperty:
	def __init__(self):
		'''
		(Iss)<MetaProperty,uid,name,signature>
		'''
		uid:int = None
		name:str = None
		signature:str = None
class MetaMethod:
	def __init__(self):
		'''
		(Issss[`MetaMethodParameter´]s)<MetaMethod,uid,returnSignature,name,parametersSignature,description,parameters,returnDescription>
		'''
		uid:int = None
		returnSignature:str = None
		name:str = None
		parametersSignature:str = None
		description:str = None
		parameters:List[MetaMethodParameter] = None
		returnDescription:str = None
class MetaObject:
	def __init__(self):
		'''
		({I`MetaMethod´}{I`MetaSignal´}{I`MetaProperty´}s)<MetaObject,methods,signals,properties,description>
		'''
		methods:Dict[int,MetaMethod] = None
		signals:Dict[int,MetaSignal] = None
		properties:Dict[int,MetaProperty] = None
		description:str = None
class MinMaxSum:
	def __init__(self):
		'''
		(fff)<MinMaxSum,minValue,maxValue,cumulatedValue>
		'''
		minValue:float = None
		maxValue:float = None
		cumulatedValue:float = None
class MethodStatistics:
	def __init__(self):
		'''
		(I`MinMaxSum´`MinMaxSum´`MinMaxSum´)<MethodStatistics,count,wall,user,system>
		'''
		count:int = None
		wall:MinMaxSum = None
		user:MinMaxSum = None
		system:MinMaxSum = None
class AutonomousAbilityStatus:
	def __init__(self):
		'''
		(sbb)<AutonomousAbilityStatus,name,enabled,running>
		'''
		name:str = None
		enabled:bool = None
		running:bool = None
class IdleDefinition:
	def __init__(self):
		'''
		([s][s])<IdleDefinition,idleBases,idleBreaks>
		'''
		idleBases:List[str] = None
		idleBreaks:List[str] = None
class ValueConfidence:
	def __init__(self):
		'''
		(ff)<ValueConfidence,value,confidence>
		'''
		value:float = None
		confidence:float = None
class BodyLanguageEase:
	def __init__(self):
		'''
		(ff)<BodyLanguageEase,level,confidence>
		'''
		level:float = None
		confidence:float = None
class Smile:
	def __init__(self):
		'''
		(ff)<Smile,value,confidence>
		'''
		value:float = None
		confidence:float = None
class BodyLanguageState:
	def __init__(self):
		'''
		(`BodyLanguageEase´)<BodyLanguageState,ease>
		'''
		ease:BodyLanguageEase = None
class Expressions:
	def __init__(self):
		'''
		(`ValueConfidence´`ValueConfidence´`ValueConfidence´`ValueConfidence´`ValueConfidence´`ValueConfidence´`ValueConfidence´)<Expressions,calm,anger,joy,sorrow,laughter,excitement,surprise>
		'''
		calm:ValueConfidence = None
		anger:ValueConfidence = None
		joy:ValueConfidence = None
		sorrow:ValueConfidence = None
		laughter:ValueConfidence = None
		excitement:ValueConfidence = None
		surprise:ValueConfidence = None
class PersonState:
	def __init__(self):
		'''
		(`ValueConfidence´`ValueConfidence´`BodyLanguageState´`Smile´`Expressions´)<PersonState,valence,attention,bodyLanguageState,smile,expressions>
		'''
		valence:ValueConfidence = None
		attention:ValueConfidence = None
		bodyLanguageState:BodyLanguageState = None
		smile:Smile = None
		expressions:Expressions = None
class Person:
	def __init__(self):
		'''
		(i`PersonState´)<Person,userSessionID,personState>
		'''
		userSessionID:int = None
		personState:PersonState = None
class AmbianceState:
	def __init__(self):
		'''
		(ff)<AmbianceState,agitationLevel,calmLevel>
		'''
		agitationLevel:float = None
		calmLevel:float = None
class MotionToDCM:
	def __init__(self):
		'''
		(iXXXXXXXXb)<MotionToDCM,whenToSendToDcm,anglesJoint,anglesActuator,stiffnessesJoint,stiffnessesActuator,stiffnessesWheel,velocitiesJoint,velocitiesWheel,torquesJoint,enableFuseProtection>
		'''
		whenToSendToDcm:int = None
		anglesJoint:object = None
		anglesActuator:object = None
		stiffnessesJoint:object = None
		stiffnessesActuator:object = None
		stiffnessesWheel:object = None
		velocitiesJoint:object = None
		velocitiesWheel:object = None
		torquesJoint:object = None
		enableFuseProtection:bool = None
class ServiceProcessInfo:
	def __init__(self):
		'''
		(bssb)<ServiceProcessInfo,running,name,execStart,autorun>
		'''
		running:bool = None
		name:str = None
		execStart:str = None
		autorun:bool = None
class SpeakingMovementConfig:
	def __init__(self):
		'''
		(bi{s[s]}b)<SpeakingMovementConfig,enabled,speakingMovementMode,wordsToTags,inputMode2>
		'''
		enabled:bool = None
		speakingMovementMode:int = None
		wordsToTags:Dict[str,List[str]] = None
		inputMode2:bool = None
class AppBackupInfo:
	def __init__(self):
		'''
		(sss[s][s])<AppBackupInfo,applicationName,userDataPath,userConfPath,dataBackupPaths,confBackupPaths>
		'''
		applicationName:str = None
		userDataPath:str = None
		userConfPath:str = None
		dataBackupPaths:List[str] = None
		confBackupPaths:List[str] = None
class PartitionInfo:
	def __init__(self):
		'''
		(ssLL)<PartitionInfo,filesystem,path,size,free>
		'''
		filesystem:str = None
		path:str = None
		size:int = None
		free:int = None
class SystemInfo:
	def __init__(self):
		'''
		(ssss)<SystemInfo,systemVersion,buildDate,buildID,buildTag>
		'''
		systemVersion:str = None
		buildDate:str = None
		buildID:str = None
		buildTag:str = None
class LogMessage:
	def __init__(self):
		'''
		(sisssILL)<LogMessage,source,level,category,location,message,id,date,systemDate>
		'''
		source:str = None
		level:int = None
		category:str = None
		location:str = None
		message:str = None
		id:int = None
		date:int = None
		systemDate:int = None
class PackageInfo2:
	def __init__(self):
		'''
		(sssssssss{sm})<PackageInfo2,uuid,version,author,channel,organization,date,typeVersion,installer,path,elems>
		'''
		uuid:str = None
		version:str = None
		author:str = None
		channel:str = None
		organization:str = None
		date:str = None
		typeVersion:str = None
		installer:str = None
		path:str = None
		elems:Dict[str,object] = None
class BehaviorInfo:
	def __init__(self):
		'''
		(ss{ss}{ss}s{s[s]}{s[s]}{s[s]}{s[s]}[s]b)<BehaviorInfo,path,nature,langToName,langToDesc,categories,langToTags,langToTriggerSentences,langToLoadingResponses,purposeToCondition,permissions,userRequestable>
		'''
		path:str = None
		nature:str = None
		langToName:Dict[str,str] = None
		langToDesc:Dict[str,str] = None
		categories:str = None
		langToTags:Dict[str,List[str]] = None
		langToTriggerSentences:Dict[str,List[str]] = None
		langToLoadingResponses:Dict[str,List[str]] = None
		purposeToCondition:Dict[str,List[str]] = None
		permissions:List[str] = None
		userRequestable:bool = None
class LanguageInfo:
	def __init__(self):
		'''
		(ssss{ss})<LanguageInfo,path,engineName,engineVersion,locale,langToName>
		'''
		path:str = None
		engineName:str = None
		engineVersion:str = None
		locale:str = None
		langToName:Dict[str,str] = None
class RobotRequirement:
	def __init__(self):
		'''
		(sssss)<RobotRequirement,model,minHeadVersion,maxHeadVersion,minBodyVersion,maxBodyVersion>
		'''
		model:str = None
		minHeadVersion:str = None
		maxHeadVersion:str = None
		minBodyVersion:str = None
		maxBodyVersion:str = None
class NaoqiRequirement:
	def __init__(self):
		'''
		(ss)<NaoqiRequirement,minVersion,maxVersion>
		'''
		minVersion:str = None
		maxVersion:str = None
class PackageService:
	def __init__(self):
		'''
		(ssb)<PackageService,execStart,name,autoRun>
		'''
		execStart:str = None
		name:str = None
		autoRun:bool = None
class DialogInfo:
	def __init__(self):
		'''
		(ss{ss})<DialogInfo,topicName,typeVersion,topics>
		'''
		topicName:str = None
		typeVersion:str = None
		topics:Dict[str,str] = None
class PackageInfo:
	def __init__(self):
		'''
		(ssssssss{ss}{ss}[s][`BehaviorInfo´][`LanguageInfo´]s[`RobotRequirement´][`NaoqiRequirement´][`PackageService´][s][`DialogInfo´][s])<PackageInfo,uuid,path,version,channel,author,organization,date,typeVersion,langToName,langToDesc,supportedLanguages,behaviors,languages,installer,robotRequirements,naoqiRequirements,services,executableFiles,dialogs,descriptionLanguages>
		'''
		uuid:str = None
		path:str = None
		version:str = None
		channel:str = None
		author:str = None
		organization:str = None
		date:str = None
		typeVersion:str = None
		langToName:Dict[str,str] = None
		langToDesc:Dict[str,str] = None
		supportedLanguages:List[str] = None
		behaviors:List[BehaviorInfo] = None
		languages:List[LanguageInfo] = None
		installer:str = None
		robotRequirements:List[RobotRequirement] = None
		naoqiRequirements:List[NaoqiRequirement] = None
		services:List[PackageService] = None
		executableFiles:List[str] = None
		dialogs:List[DialogInfo] = None
		descriptionLanguages:List[str] = None
class ServiceInfo:
	def __init__(self):
		'''
		(sIsI[s]s)<ServiceInfo,name,serviceId,machineId,processId,endpoints,sessionId>
		'''
		name:str = None
		serviceId:int = None
		machineId:str = None
		processId:int = None
		endpoints:List[str] = None
		sessionId:str = None
