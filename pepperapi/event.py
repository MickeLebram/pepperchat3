from typing import Any, Callable
from .robot_client import EventSubscription
class ALAnimatedSpeech_EndOfAnimatedSpeech:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALAnimatedSpeech/EndOfAnimatedSpeech', callback)
class ALAudioPlayer_currentSystemSoundSet:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALAudioPlayer/currentSystemSoundSet', callback)
class ALAudioSourceLocalization_SoundLocated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALAudioSourceLocalization/SoundLocated', callback)
class ALAudioSourceLocalization_SoundsLocated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALAudioSourceLocalization/SoundsLocated', callback)
class ALBasicAwareness_HumanLost:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBasicAwareness/HumanLost', callback)
class ALBasicAwareness_HumanTracked:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBasicAwareness/HumanTracked', callback)
class ALBasicAwareness_StimulusDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBasicAwareness/StimulusDetected', callback)
class ALBattery_BatteryLow:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBattery/BatteryLow', callback)
class ALBattery_ConnectedToChargingStation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBattery/ConnectedToChargingStation', callback)
class ALBehaviorManager_BehaviorAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorAdded', callback)
class ALBehaviorManager_BehaviorFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorFailed', callback)
class ALBehaviorManager_BehaviorRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorRemoved', callback)
class ALBehaviorManager_BehaviorUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorUpdated', callback)
class ALBehaviorManager_BehaviorsAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorsAdded', callback)
class ALBehaviorManager_BehaviorsLoaded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorsLoaded', callback)
class ALBehaviorManager_BehaviorsRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALBehaviorManager/BehaviorsRemoved', callback)
class ALChestButton_DoubleClickOccurred:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALChestButton/DoubleClickOccurred', callback)
class ALChestButton_SimpleClickOccurred:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALChestButton/SimpleClickOccurred', callback)
class ALChestButton_TripleClickOccurred:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALChestButton/TripleClickOccurred', callback)
class ALCloud_Enabled:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALCloud/Enabled', callback)
class ALCloud_User:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALCloud/User', callback)
class ALDiagnosis_ActiveDiagnosisFinished:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALDiagnosis/ActiveDiagnosisFinished', callback)
class ALDiagnosis_DiagnosisErrorChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALDiagnosis/DiagnosisErrorChanged', callback)
class ALDiagnosis_RobotIsReady:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALDiagnosis/RobotIsReady', callback)
class ALExpressiveness_StartNotificationBlink:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALExpressiveness/StartNotificationBlink', callback)
class ALExpressiveness_StopNotificationBlink:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALExpressiveness/StopNotificationBlink', callback)
class ALFastPersonTracking_TrackedPersonNotFound:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALFastPersonTracking/TrackedPersonNotFound', callback)
class ALFindPersonHead_HeadNotFound:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALFindPersonHead/HeadNotFound', callback)
class ALFindPersonHead_HeadReached:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALFindPersonHead/HeadReached', callback)
class ALLocalization_FullScanBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/FullScanBegin', callback)
class ALLocalization_FullScanInsufficient:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/FullScanInsufficient', callback)
class ALLocalization_FullScanSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/FullScanSuccess', callback)
class ALLocalization_GoToBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToBegin', callback)
class ALLocalization_GoToContinue:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToContinue', callback)
class ALLocalization_GoToFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToFailed', callback)
class ALLocalization_GoToLost:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToLost', callback)
class ALLocalization_GoToNextMove:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToNextMove', callback)
class ALLocalization_GoToSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/GoToSuccess', callback)
class ALLocalization_HalfScanBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/HalfScanBegin', callback)
class ALLocalization_HalfScanInsufficient:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/HalfScanInsufficient', callback)
class ALLocalization_HalfScanSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/HalfScanSuccess', callback)
class ALLocalization_LocalizeBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeBegin', callback)
class ALLocalization_LocalizeDirectionBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeDirectionBegin', callback)
class ALLocalization_LocalizeDirectionLost:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeDirectionLost', callback)
class ALLocalization_LocalizeDirectionSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeDirectionSuccess', callback)
class ALLocalization_LocalizeLost:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeLost', callback)
class ALLocalization_LocalizeSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/LocalizeSuccess', callback)
class ALLocalization_OdometryBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/OdometryBegin', callback)
class ALLocalization_OdometryInsufficient:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/OdometryInsufficient', callback)
class ALLocalization_StartShootOneFrame:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/StartShootOneFrame', callback)
class ALLocalization_StartingComputation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/StartingComputation', callback)
class ALLocalization_StopShootOneFrame:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/StopShootOneFrame', callback)
class ALLocalization_StoppingComputation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/StoppingComputation', callback)
class ALLocalization_UTurnEnd:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALLocalization/UTurnEnd', callback)
class ALMemory_KeyAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMemory/KeyAdded', callback)
class ALMemory_KeyRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMemory/KeyRemoved', callback)
class ALMemory_KeyTypeChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMemory/KeyTypeChanged', callback)
class ALMotion_MoveFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/MoveFailed', callback)
class ALMotion_Protection_DisabledDevicesChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Protection/DisabledDevicesChanged', callback)
class ALMotion_Protection_DisabledFeaturesChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Protection/DisabledFeaturesChanged', callback)
class ALMotion_RobotIsFalling:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/RobotIsFalling', callback)
class ALMotion_RobotIsStand:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/RobotIsStand', callback)
class ALMotion_RobotPushed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/RobotPushed', callback)
class ALMotion_Safety_ChainVelocityClipped:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Safety/ChainVelocityClipped', callback)
class ALMotion_Safety_PushRecovery:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Safety/PushRecovery', callback)
class ALMotion_Safety_RobotOnASlope:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Safety/RobotOnASlope', callback)
class ALMotion_Safety_RobotPushed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Safety/RobotPushed', callback)
class ALMotion_Stiffness_restFinished:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Stiffness/restFinished', callback)
class ALMotion_Stiffness_restStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Stiffness/restStarted', callback)
class ALMotion_Stiffness_wakeUpFinished:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Stiffness/wakeUpFinished', callback)
class ALMotion_Stiffness_wakeUpStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotion/Stiffness/wakeUpStarted', callback)
class ALMotionRecorder_CurrentFrame:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotionRecorder/CurrentFrame', callback)
class ALMotionRecorder_Recording:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotionRecorder/Recording', callback)
class ALMotionRecorder_StorePositionRequested:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALMotionRecorder/StorePositionRequested', callback)
class ALNotificationReader_SayingNotification:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALNotificationReader/SayingNotification', callback)
class ALPanoramaCompass_FullScanBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALPanoramaCompass/FullScanBegin', callback)
class ALPanoramaCompass_HalfScanBegin:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALPanoramaCompass/HalfScanBegin', callback)
class ALPanoramaCompass_HalfScanInsufficient:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALPanoramaCompass/HalfScanInsufficient', callback)
class ALRALManagerModule_onTouchDown:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRALManagerModule/onTouchDown', callback)
class ALRecharge_CloseToChargingStation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/CloseToChargingStation', callback)
class ALRecharge_ConnectedToChargingStation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/ConnectedToChargingStation', callback)
class ALRecharge_DockingBackwardStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/DockingBackwardStarted', callback)
class ALRecharge_DockingFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/DockingFailed', callback)
class ALRecharge_DockingRetry:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/DockingRetry', callback)
class ALRecharge_DockingSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/DockingSuccess', callback)
class ALRecharge_DockingUTurnStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/DockingUTurnStarted', callback)
class ALRecharge_LeaveFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LeaveFailed', callback)
class ALRecharge_LeaveSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LeaveSuccess', callback)
class ALRecharge_LookFalsePositive:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LookFalsePositive', callback)
class ALRecharge_LookForStationRetry:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LookForStationRetry', callback)
class ALRecharge_LookForStationSuccess:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LookForStationSuccess', callback)
class ALRecharge_LookPreviousHypothesis:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/LookPreviousHypothesis', callback)
class ALRecharge_MoveFailed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/MoveFailed', callback)
class ALRecharge_SearchStopped:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/SearchStopped', callback)
class ALRecharge_StationDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/StationDetected', callback)
class ALRecharge_StationNotFound:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/StationNotFound', callback)
class ALRecharge_StatusChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALRecharge/StatusChanged', callback)
class ALSentinel_BatteryLevel:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSentinel/BatteryLevel', callback)
class ALSentinel_DoubleClickOccured:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSentinel/DoubleClickOccured', callback)
class ALSentinel_SimpleClickOccured:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSentinel/SimpleClickOccured', callback)
class ALSentinel_TripleClickOccured:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSentinel/TripleClickOccured', callback)
class ALSignsAndFeedback_ASRStop:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/ASRStop', callback)
class ALSignsAndFeedback_DialogStart:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/DialogStart', callback)
class ALSignsAndFeedback_DialogStop:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/DialogStop', callback)
class ALSignsAndFeedback_Hearing:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Hearing', callback)
class ALSignsAndFeedback_HumanFound:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/HumanFound', callback)
class ALSignsAndFeedback_HumanFoundDirectly:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/HumanFoundDirectly', callback)
class ALSignsAndFeedback_Initialization:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Initialization', callback)
class ALSignsAndFeedback_Listening:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Listening', callback)
class ALSignsAndFeedback_ManualStopReleased:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/ManualStopReleased', callback)
class ALSignsAndFeedback_Processing:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Processing', callback)
class ALSignsAndFeedback_SoundDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/SoundDetected', callback)
class ALSignsAndFeedback_Speaking:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Speaking', callback)
class ALSignsAndFeedback_StartNotificationBlink_Error:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/StartNotificationBlink/Error', callback)
class ALSignsAndFeedback_StartNotificationBlink_Info:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/StartNotificationBlink/Info', callback)
class ALSignsAndFeedback_StartNotificationBlink_Warning:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/StartNotificationBlink/Warning', callback)
class ALSignsAndFeedback_StopNotificationBlink_Listening:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/StopNotificationBlink/Listening', callback)
class ALSignsAndFeedback_StopNotificationBlink_NotListening:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/StopNotificationBlink/NotListening', callback)
class ALSignsAndFeedback_Switched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSignsAndFeedback/Switched', callback)
class ALSoundLocalization_SoundLocated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSoundLocalization/SoundLocated', callback)
class ALSoundLocalization_SoundsLocated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSoundLocalization/SoundsLocated', callback)
class ALSpeechRecognition_ActiveListening:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/ActiveListening', callback)
class ALSpeechRecognition_IsConnected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/IsConnected', callback)
class ALSpeechRecognition_IsRunning:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/IsRunning', callback)
class ALSpeechRecognition_QueryError:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/QueryError', callback)
class ALSpeechRecognition_SignalTooLow:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/SignalTooLow', callback)
class ALSpeechRecognition_Status:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALSpeechRecognition/Status', callback)
class ALStore_SystemImageDownloaded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALStore/SystemImageDownloaded', callback)
class ALStore_Updated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALStore/Updated', callback)
class ALTactileGesture_Gesture:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTactileGesture/Gesture', callback)
class ALTactileGesture_Release:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTactileGesture/Release', callback)
class ALTextToSpeech_CurrentBookMark:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/CurrentBookMark', callback)
class ALTextToSpeech_CurrentSentence:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/CurrentSentence', callback)
class ALTextToSpeech_CurrentWord:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/CurrentWord', callback)
class ALTextToSpeech_PositionOfCurrentWord:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/PositionOfCurrentWord', callback)
class ALTextToSpeech_Status:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/Status', callback)
class ALTextToSpeech_TextDone:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/TextDone', callback)
class ALTextToSpeech_TextInterrupted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/TextInterrupted', callback)
class ALTextToSpeech_TextStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTextToSpeech/TextStarted', callback)
class ALTracker_ActiveTargetChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ActiveTargetChanged', callback)
class ALTracker_ArmTracking_Restarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ArmTracking/Restarted', callback)
class ALTracker_ArmTracking_Stopped:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ArmTracking/Stopped', callback)
class ALTracker_BaseTracking:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/BaseTracking', callback)
class ALTracker_BlobDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/BlobDetected', callback)
class ALTracker_CloseObjectDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/CloseObjectDetected', callback)
class ALTracker_ColorBlobDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ColorBlobDetected', callback)
class ALTracker_FastPersonTracking:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/FastPersonTracking', callback)
class ALTracker_FindPersonHead:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/FindPersonHead', callback)
class ALTracker_HeadTracking_Restarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/HeadTracking/Restarted', callback)
class ALTracker_HeadTracking_Stopped:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/HeadTracking/Stopped', callback)
class ALTracker_ObjectLookAt:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ObjectLookAt', callback)
class ALTracker_ObjectMoveTo:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/ObjectMoveTo', callback)
class ALTracker_PodDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/PodDetected', callback)
class ALTracker_SearchLoopOver:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/SearchLoopOver', callback)
class ALTracker_SearchRotation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/SearchRotation', callback)
class ALTracker_SearchScanStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/SearchScanStarted', callback)
class ALTracker_SecondTargetDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/SecondTargetDetected', callback)
class ALTracker_StopSearch:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/StopSearch', callback)
class ALTracker_TargetDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/TargetDetected', callback)
class ALTracker_TargetLost:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/TargetLost', callback)
class ALTracker_TargetReached:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALTracker/TargetReached', callback)
class ALVoiceEmotionAnalysis_EmotionRecognized:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALVoiceEmotionAnalysis/EmotionRecognized', callback)
class ALWorldRepresentation_AttributeChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALWorldRepresentation/AttributeChanged', callback)
class ALWorldRepresentation_DisplayRequired:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALWorldRepresentation/DisplayRequired', callback)
class ALWorldRepresentation_PositionChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ALWorldRepresentation/PositionChanged', callback)
class ActiveDiagnosisErrorChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ActiveDiagnosisErrorChanged', callback)
class AnimatedRecharge_WarningMode:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AnimatedRecharge/WarningMode', callback)
class AppLauncher_CustomLauncher:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AppLauncher/CustomLauncher', callback)
class AudioInputAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioInputAdded', callback)
class AudioInputChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioInputChanged', callback)
class AudioInputRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioInputRemoved', callback)
class AudioOutputAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioOutputAdded', callback)
class AudioOutputChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioOutputChanged', callback)
class AudioOutputRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AudioOutputRemoved', callback)
class AutonomousLife_Asleep:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/Asleep', callback)
class AutonomousLife_CompletedActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/CompletedActivity', callback)
class AutonomousLife_FocusedActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/FocusedActivity', callback)
class AutonomousLife_LaunchSuggestions:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/LaunchSuggestions', callback)
class AutonomousLife_NextActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/NextActivity', callback)
class AutonomousLife_Report:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/Report', callback)
class AutonomousLife_State:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('AutonomousLife/State', callback)
class BackBumperPressed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BackBumperPressed', callback)
class BacklightingDetection_BacklightingDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BacklightingDetection/BacklightingDetected', callback)
class BarcodeReader_BarcodeDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BarcodeReader/BarcodeDetected', callback)
class BatteryChargeCellVoltageMinChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryChargeCellVoltageMinChanged', callback)
class BatteryChargeChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryChargeChanged', callback)
class BatteryChargingFlagChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryChargingFlagChanged', callback)
class BatteryDisChargingFlagChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryDisChargingFlagChanged', callback)
class BatteryEmpty:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryEmpty', callback)
class BatteryFullChargedFlagChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryFullChargedFlagChanged', callback)
class BatteryLowDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryLowDetected', callback)
class BatteryNearlyEmpty:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryNearlyEmpty', callback)
class BatteryNotDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryNotDetected', callback)
class BatteryPowerPluggedChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryPowerPluggedChanged', callback)
class BatteryTrapIsOpen:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BatteryTrapIsOpen', callback)
class BehaviorsRun:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BehaviorsRun', callback)
class BootConfig_HasStartedAtBoot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('BootConfig/HasStartedAtBoot', callback)
class ChestButtonPressed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('ChestButtonPressed', callback)
class CloseObjectDetection_ObjectDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('CloseObjectDetection/ObjectDetected', callback)
class CloseObjectDetection_ObjectNotDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('CloseObjectDetection/ObjectNotDetected', callback)
class DarknessDetection_DarknessDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('DarknessDetection/DarknessDetected', callback)
class DeviceNoLongerHotDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('DeviceNoLongerHotDetected', callback)
class Dialog_Answered:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Answered', callback)
class Dialog_CannotMakeIt:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/CannotMakeIt', callback)
class Dialog_CurrentString:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/CurrentString', callback)
class Dialog_DateCode:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/DateCode', callback)
class Dialog_Default:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Default', callback)
class Dialog_Failure:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Failure', callback)
class Dialog_Fallback:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Fallback', callback)
class Dialog_Focus:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Focus', callback)
class Dialog_FocusDescription:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/FocusDescription', callback)
class Dialog_IsQuiet:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/IsQuiet', callback)
class Dialog_IsStarted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/IsStarted', callback)
class Dialog_Language_English:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Language/English', callback)
class Dialog_LastAnswer:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/LastAnswer', callback)
class Dialog_LastInput:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/LastInput', callback)
class Dialog_Listening:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Listening', callback)
class Dialog_MatchedApp:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/MatchedApp', callback)
class Dialog_MatchedInput:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/MatchedInput', callback)
class Dialog_MatchedLine:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/MatchedLine', callback)
class Dialog_MatchedTopic:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/MatchedTopic', callback)
class Dialog_Nao:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Nao', callback)
class Dialog_Network_BlueTooth:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Network/BlueTooth', callback)
class Dialog_Network_Ethernet:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Network/Ethernet', callback)
class Dialog_Network_NoNetwork:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Network/NoNetwork', callback)
class Dialog_Network_WiFi:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Network/WiFi', callback)
class Dialog_No:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/No', callback)
class Dialog_NoOneSpeak:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NoOneSpeak', callback)
class Dialog_NoOneSpeak10:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NoOneSpeak10', callback)
class Dialog_NoOneSpeak15:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NoOneSpeak15', callback)
class Dialog_NoOneSpeak20:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NoOneSpeak20', callback)
class Dialog_NoOneSpeak5:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NoOneSpeak5', callback)
class Dialog_NotPossible:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotPossible', callback)
class Dialog_NotSpeaking:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotSpeaking', callback)
class Dialog_NotSpeaking10:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotSpeaking10', callback)
class Dialog_NotSpeaking15:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotSpeaking15', callback)
class Dialog_NotSpeaking20:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotSpeaking20', callback)
class Dialog_NotSpeaking5:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotSpeaking5', callback)
class Dialog_NotUnderstood:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotUnderstood', callback)
class Dialog_NotUnderstood2:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotUnderstood2', callback)
class Dialog_NotUnderstood3:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotUnderstood3', callback)
class Dialog_NotUnderstoodEvent:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NotUnderstoodEvent', callback)
class Dialog_NothingToSay:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/NothingToSay', callback)
class Dialog_Obstacle:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Obstacle', callback)
class Dialog_OpenSession:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/OpenSession', callback)
class Dialog_PreSay:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/PreSay', callback)
class Dialog_RobotModel:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/RobotModel', callback)
class Dialog_RobotName:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/RobotName', callback)
class Dialog_SaidMisunderstood:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/SaidMisunderstood', callback)
class Dialog_SameRule:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/SameRule', callback)
class Dialog_SpeakFailure:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/SpeakFailure', callback)
class Dialog_SpeakLouder:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/SpeakLouder', callback)
class Dialog_Stop:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Stop', callback)
class Dialog_Tag:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Tag', callback)
class Dialog_TalkTime:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/TalkTime', callback)
class Dialog_User:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/User', callback)
class Dialog_UtteranceOutcome:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/UtteranceOutcome', callback)
class Dialog_Yes:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/Yes', callback)
class Dialog_noLangPack:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/noLangPack', callback)
class Dialog_sayIP:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Dialog/sayIP', callback)
class DialogReflex_UnengagedReaction:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('DialogReflex/UnengagedReaction', callback)
class DialogSpeechRecognitionGrammar:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('DialogSpeechRecognitionGrammar', callback)
class EnablePowerMonitoring:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EnablePowerMonitoring', callback)
class EngagementZones_FirstLimitDistanceUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/FirstLimitDistanceUpdated', callback)
class EngagementZones_LimitAngleUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/LimitAngleUpdated', callback)
class EngagementZones_MovementsInZonesUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/MovementsInZonesUpdated', callback)
class EngagementZones_PeopleInZonesUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PeopleInZonesUpdated', callback)
class EngagementZones_PersonApproached:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PersonApproached', callback)
class EngagementZones_PersonEnteredZone1:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PersonEnteredZone1', callback)
class EngagementZones_PersonEnteredZone2:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PersonEnteredZone2', callback)
class EngagementZones_PersonEnteredZone3:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PersonEnteredZone3', callback)
class EngagementZones_PersonMovedAway:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/PersonMovedAway', callback)
class EngagementZones_SecondLimitDistanceUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('EngagementZones/SecondLimitDistanceUpdated', callback)
class FaceCharacteristics_PersonSmiling:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('FaceCharacteristics/PersonSmiling', callback)
class FaceDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('FaceDetected', callback)
class FaceDetection_FaceDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('FaceDetection/FaceDetected', callback)
class FrontTactilTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('FrontTactilTouched', callback)
class GazeAnalysis_PeopleLookingAtRobot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('GazeAnalysis/PeopleLookingAtRobot', callback)
class GazeAnalysis_PersonStartsLookingAtRobot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('GazeAnalysis/PersonStartsLookingAtRobot', callback)
class GazeAnalysis_PersonStopsLookingAtRobot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('GazeAnalysis/PersonStopsLookingAtRobot', callback)
class HandLeftBackTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandLeftBackTouched', callback)
class HandLeftLeftTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandLeftLeftTouched', callback)
class HandLeftRightTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandLeftRightTouched', callback)
class HandRightBackTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandRightBackTouched', callback)
class HandRightLeftTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandRightLeftTouched', callback)
class HandRightRightTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HandRightRightTouched', callback)
class HeadProcessorIsCriticallyHot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HeadProcessorIsCriticallyHot', callback)
class HeadProcessorIsHot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HeadProcessorIsHot', callback)
class HotDeviceDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HotDeviceDetected', callback)
class HotJointDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HotJointDetected', callback)
class HumanLostAfterTracking:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('HumanLostAfterTracking', callback)
class LandmarkDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('LandmarkDetected', callback)
class LastWordRecognized:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('LastWordRecognized', callback)
class Launchpad_BatteryIsCharging:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/BatteryIsCharging', callback)
class Launchpad_BatteryLevel:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/BatteryLevel', callback)
class Launchpad_BatteryStatus:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/BatteryStatus', callback)
class Launchpad_Date:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Date', callback)
class Launchpad_Day:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Day', callback)
class Launchpad_DayName:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/DayName', callback)
class Launchpad_DistanceOfTrackedHuman:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/DistanceOfTrackedHuman', callback)
class Launchpad_FocusCount_run_dialog_dev__:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/FocusCount/run_dialog_dev/.', callback)
class Launchpad_FocusedActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/FocusedActivity', callback)
class Launchpad_HighestJoint:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/HighestJoint', callback)
class Launchpad_HighestTemperature:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/HighestTemperature', callback)
class Launchpad_Hour:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Hour', callback)
class Launchpad_LifeTime:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/LifeTime', callback)
class Launchpad_Lifted:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Lifted', callback)
class Launchpad_Minute:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Minute', callback)
class Launchpad_MinuteOfDay:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/MinuteOfDay', callback)
class Launchpad_Month:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Month', callback)
class Launchpad_MonthName:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/MonthName', callback)
class Launchpad_NoMotionInZones:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NoMotionInZones', callback)
class Launchpad_NoPeopleInZones:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NoPeopleInZones', callback)
class Launchpad_NumMotionZone1:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumMotionZone1', callback)
class Launchpad_NumMotionZone2:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumMotionZone2', callback)
class Launchpad_NumMotionZone3:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumMotionZone3', callback)
class Launchpad_NumPeopleZone1:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumPeopleZone1', callback)
class Launchpad_NumPeopleZone2:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumPeopleZone2', callback)
class Launchpad_NumPeopleZone3:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/NumPeopleZone3', callback)
class Launchpad_PeopleNotSeen:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/PeopleNotSeen', callback)
class Launchpad_Posture:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Posture', callback)
class Launchpad_PostureFamily:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/PostureFamily', callback)
class Launchpad_PreviousActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/PreviousActivity', callback)
class Launchpad_PreviousState:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/PreviousState', callback)
class Launchpad_RobotFellRecently:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/RobotFellRecently', callback)
class Launchpad_RobotPushedRecently:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/RobotPushedRecently', callback)
class Launchpad_RobotType:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/RobotType', callback)
class Launchpad_SameTrackedHuman:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/SameTrackedHuman', callback)
class Launchpad_State:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/State', callback)
class Launchpad_TemperatureStatus:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/TemperatureStatus', callback)
class Launchpad_TrackedHumanIsLookingAtRobot:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/TrackedHumanIsLookingAtRobot', callback)
class Launchpad_WavingDetection:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/WavingDetection', callback)
class Launchpad_Week:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Week', callback)
class Launchpad_Year:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/Year', callback)
class Launchpad_ZoneOfTrackedHuman:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Launchpad/ZoneOfTrackedHuman', callback)
class LeftBumperPressed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('LeftBumperPressed', callback)
class MiddleTactilTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('MiddleTactilTouched', callback)
class MoodAnalytics_LastActivityMoods:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('MoodAnalytics/LastActivityMoods', callback)
class MoodEvent_Mood:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('MoodEvent/Mood', callback)
class MovementDetection_MovementDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('MovementDetection/MovementDetected', callback)
class MovementDetection_NoMovement:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('MovementDetection/NoMovement', callback)
class NAOqiReady:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NAOqiReady', callback)
class Navigation_AvoidanceNavigator_AbsTargetModified:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/AbsTargetModified', callback)
class Navigation_AvoidanceNavigator_MovingToFreeZone:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/MovingToFreeZone', callback)
class Navigation_AvoidanceNavigator_ObstacleDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/ObstacleDetected', callback)
class Navigation_AvoidanceNavigator_Status:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/Status', callback)
class Navigation_AvoidanceNavigator_TargetOutOfMap:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/TargetOutOfMap', callback)
class Navigation_AvoidanceNavigator_TooManyPathRecomputation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/TooManyPathRecomputation', callback)
class Navigation_AvoidanceNavigator_TrajectoryProgress:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/AvoidanceNavigator/TrajectoryProgress', callback)
class Navigation_FreeZoneFinder_ConstraintZone:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/FreeZoneFinder/ConstraintZone', callback)
class Navigation_MotionDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Navigation/MotionDetected', callback)
class NetworkConnectStatus:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkConnectStatus', callback)
class NetworkDefaultTechnologyChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkDefaultTechnologyChanged', callback)
class NetworkServiceAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkServiceAdded', callback)
class NetworkServiceInputRequired:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkServiceInputRequired', callback)
class NetworkServiceRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkServiceRemoved', callback)
class NetworkServiceStateChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkServiceStateChanged', callback)
class NetworkStateChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkStateChanged', callback)
class NetworkTechnologyAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkTechnologyAdded', callback)
class NetworkTechnologyRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NetworkTechnologyRemoved', callback)
class NoHumanFoundAfterStimulus:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NoHumanFoundAfterStimulus', callback)
class NoiseRecognized:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('NoiseRecognized', callback)
class PassiveDiagnosisErrorChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PassiveDiagnosisErrorChanged', callback)
class PeoplePerception_JustArrived:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/JustArrived', callback)
class PeoplePerception_JustLeft:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/JustLeft', callback)
class PeoplePerception_MaximumDetectionRangeUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/MaximumDetectionRangeUpdated', callback)
class PeoplePerception_NonVisiblePeopleList:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/NonVisiblePeopleList', callback)
class PeoplePerception_PeopleDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/PeopleDetected', callback)
class PeoplePerception_PeopleList:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/PeopleList', callback)
class PeoplePerception_PopulationReset:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/PopulationReset', callback)
class PeoplePerception_PopulationUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/PopulationUpdated', callback)
class PeoplePerception_RemovedPersonFromMemory:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/RemovedPersonFromMemory', callback)
class PeoplePerception_VisiblePeopleList:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PeoplePerception/VisiblePeopleList', callback)
class PictureDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PictureDetected', callback)
class PodDetection_Detection:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PodDetection/Detection', callback)
class PostureChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PostureChanged', callback)
class PostureFamilyChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PostureFamilyChanged', callback)
class PosturePerturbated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('PosturePerturbated', callback)
class RearTactilTouched:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('RearTactilTouched', callback)
class RecoLatency:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('RecoLatency', callback)
class RightBumperPressed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('RightBumperPressed', callback)
class Segmentation3D_BlobTrackerUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Segmentation3D/BlobTrackerUpdated', callback)
class Segmentation3D_SegmentationUpdated:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Segmentation3D/SegmentationUpdated', callback)
class Segmentation3D_TopOfTrackedBlob:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Segmentation3D/TopOfTrackedBlob', callback)
class Segmentation3D_TrackedBlobNotFound:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('Segmentation3D/TrackedBlobNotFound', callback)
class SittingPeopleDetection_PersonSittingDown:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SittingPeopleDetection/PersonSittingDown', callback)
class SittingPeopleDetection_PersonStandingUp:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SittingPeopleDetection/PersonStandingUp', callback)
class SonarLateralLeftDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarLateralLeftDetected', callback)
class SonarLateralRightDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarLateralRightDetected', callback)
class SonarLeftDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarLeftDetected', callback)
class SonarLeftNothingDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarLeftNothingDetected', callback)
class SonarMiddleDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarMiddleDetected', callback)
class SonarNothingDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarNothingDetected', callback)
class SonarRightDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarRightDetected', callback)
class SonarRightNothingDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SonarRightNothingDetected', callback)
class SoundDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SoundDetected', callback)
class SpeechDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('SpeechDetected', callback)
class TemperatureDiagnosisErrorChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('TemperatureDiagnosisErrorChanged', callback)
class TemperatureStatusChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('TemperatureStatusChanged', callback)
class TouchChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('TouchChanged', callback)
class UserSession_CreatedUsers:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/CreatedUsers', callback)
class UserSession_DeletedUsers:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/DeletedUsers', callback)
class UserSession_FocusedUser:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/FocusedUser', callback)
class UserSession_Identification_Status:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/Identification/Status', callback)
class UserSession_NoOpenSessions:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/NoOpenSessions', callback)
class UserSession_SessionsClosed:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/SessionsClosed', callback)
class UserSession_SessionsOpened:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/SessionsOpened', callback)
class UserSession_ShouldExitInteractiveActivity:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('UserSession/ShouldExitInteractiveActivity', callback)
class VisualCompass_Deviation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/Deviation', callback)
class VisualCompass_FinalDeviation:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/FinalDeviation', callback)
class VisualCompass_InvalidReference:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/InvalidReference', callback)
class VisualCompass_Match:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/Match', callback)
class VisualCompass_MoveAbort:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/MoveAbort', callback)
class VisualCompass_NewReferenceImageSet:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('VisualCompass/NewReferenceImageSet', callback)
class WavingDetection_PersonWaving:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WavingDetection/PersonWaving', callback)
class WavingDetection_PersonWavingCenter:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WavingDetection/PersonWavingCenter', callback)
class WavingDetection_PersonWavingLeft:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WavingDetection/PersonWavingLeft', callback)
class WavingDetection_PersonWavingRight:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WavingDetection/PersonWavingRight', callback)
class WavingDetection_Waving:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WavingDetection/Waving', callback)
class WordRecognized:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WordRecognized', callback)
class WordRecognizedAndGrammar:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('WordRecognizedAndGrammar', callback)
class _ALBasicAwareness_EngagementModeChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/EngagementModeChanged', callback)
class _ALBasicAwareness_HumanLostDebug:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/HumanLostDebug', callback)
class _ALBasicAwareness_IsPaused:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/IsPaused', callback)
class _ALBasicAwareness_ServoingEvent:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/ServoingEvent', callback)
class _ALBasicAwareness_StimulusCandidate:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/StimulusCandidate', callback)
class _ALBasicAwareness_StimulusCheckResult:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBasicAwareness/StimulusCheckResult', callback)
class _ALBrightnessStatistics_Avg:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBrightnessStatistics/Avg', callback)
class _ALBrightnessStatistics_Max:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBrightnessStatistics/Max', callback)
class _ALBrightnessStatistics_Min:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBrightnessStatistics/Min', callback)
class _ALBrightnessStatistics_Std:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_ALBrightnessStatistics/Std', callback)
class _AutonomousLife_ForceState:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_AutonomousLife/ForceState', callback)
class _AutonomousLife__ForbidStopCommands:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('_AutonomousLife/_ForbidStopCommands', callback)
class blind_me_Solitary:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('blind-me/Solitary', callback)
class go_to_sleep:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('go_to_sleep', callback)
class go_to_sleep_now:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('go_to_sleep_now', callback)
class notificationAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('notificationAdded', callback)
class notificationRead:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('notificationRead', callback)
class notificationRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('notificationRemoved', callback)
class packageInstalled:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('packageInstalled', callback)
class packageRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('packageRemoved', callback)
class preferenceAdded:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('preferenceAdded', callback)
class preferenceChanged:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('preferenceChanged', callback)
class preferenceDomainRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('preferenceDomainRemoved', callback)
class preferenceRemoved:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('preferenceRemoved', callback)
class preferenceSynchronized:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('preferenceSynchronized', callback)
class redBallDetected:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('redBallDetected', callback)
class robotHasFallen:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('robotHasFallen', callback)
class robotIsWakeUp:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('robotIsWakeUp', callback)
class rundialogInstalled:
	@staticmethod
	def subscribe(callback:Callable[[Any], None]):
		return EventSubscription('rundialogInstalled', callback)
