from typing import List, Dict, Tuple
class AutonomousAbilityStatus:
	def __init__(self):
		'''
		(sbb)<AutonomousAbilityStatus,name,enabled,running>
		'''
		name:str = None
		enabled:bool = None
		running:bool = None
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
