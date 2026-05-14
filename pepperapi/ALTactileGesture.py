from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def _bit_distance(p0:object) -> object:
	"""
	
	        Computes 'Hamming distance' between the binary representations of
	        numbers in pair
	        
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "m",
	    "name": "_bit_distance",
	    "parametersSignature": "(m)",
	    "description": "\n        Computes 'Hamming distance' between the binary representations of\n        numbers in pair\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_bit_distance", [p0])

def _cancel_futures() -> object:
	"""
	Cancel all futures
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "m",
	    "name": "_cancel_futures",
	    "parametersSignature": "()",
	    "description": "Cancel all futures",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_cancel_futures", [])

def _check_sequence(p0:object, p1:object, p2:object, p3:object) -> object:
	"""
	
	        Given a gesture, check if the active sequence matches it.
	
	        Algorithm:
	        1. Create a list of overlapping pairs from each gesture's sequence
	        2. Loop through each pair (a,b):
	           3. If the active sequence matches 'a' in the pair:
	              4. Check if the active sequence contains the 'b' in the pair
	                 5a. If True, check if it is within n-1 positions from where 'a'
	                     was (Where 'n' is the number of bits changed between 'a'
	                     and 'b')
	                     6a. If True: goto Step 2 [if last pair; goto Step 7)
	                     6b. Else: break; fullfill promise as None
	                 5b. Else: break; fullfill promise as None
	        7. If all pairs check out and they used all of the active sequence
	           8. Fullfill promise with the gesture and the difference in length between the
	              inputted sequence and the matched sequence (i.e. the number of
	              excess frames)
	        
	
	Parameters
	----------
	p0:object
		
	p1:object
		
	p2:object
		
	p3:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "m",
	    "name": "_check_sequence",
	    "parametersSignature": "(mmmm)",
	    "description": "\n        Given a gesture, check if the active sequence matches it.\n\n        Algorithm:\n        1. Create a list of overlapping pairs from each gesture's sequence\n        2. Loop through each pair (a,b):\n           3. If the active sequence matches 'a' in the pair:\n              4. Check if the active sequence contains the 'b' in the pair\n                 5a. If True, check if it is within n-1 positions from where 'a'\n                     was (Where 'n' is the number of bits changed between 'a'\n                     and 'b')\n                     6a. If True: goto Step 2 [if last pair; goto Step 7)\n                     6b. Else: break; fullfill promise as None\n                 5b. Else: break; fullfill promise as None\n        7. If all pairs check out and they used all of the active sequence\n           8. Fullfill promise with the gesture and the difference in length between the\n              inputted sequence and the matched sequence (i.e. the number of\n              excess frames)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_check_sequence", [p0, p1, p2, p3])

def _clean_up() -> object:
	"""
	Clean up/reset after a sequence has been completed
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "m",
	    "name": "_clean_up",
	    "parametersSignature": "()",
	    "description": "Clean up/reset after a sequence has been completed",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_clean_up", [])

def _clean_up_hold() -> object:
	"""
	Clean up/reset after a hold sequence has been completed
	
	*Reference struct*
	'''
	{
	    "uid": 104,
	    "returnSignature": "m",
	    "name": "_clean_up_hold",
	    "parametersSignature": "()",
	    "description": "Clean up/reset after a hold sequence has been completed",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_clean_up_hold", [])

def _connect_services() -> object:
	"""
	Connect to all services required by ALTactileGesture
	
	*Reference struct*
	'''
	{
	    "uid": 105,
	    "returnSignature": "m",
	    "name": "_connect_services",
	    "parametersSignature": "()",
	    "description": "Connect to all services required by ALTactileGesture",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_connect_services", [])

def _connect_signals() -> object:
	"""
	Init qi.Signals and memory events (for compatibility)
	
	*Reference struct*
	'''
	{
	    "uid": 106,
	    "returnSignature": "m",
	    "name": "_connect_signals",
	    "parametersSignature": "()",
	    "description": "Init qi.Signals and memory events (for compatibility)",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_connect_signals", [])

def _create_gesture_name(p0:object) -> object:
	"""
	Create gesture name from sequence
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 107,
	    "returnSignature": "m",
	    "name": "_create_gesture_name",
	    "parametersSignature": "(m)",
	    "description": "Create gesture name from sequence",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_create_gesture_name", [p0])

def _eval_hold() -> object:
	"""
	
	        Once the hold time has expired:
	          - Evaluate if the current sequence is a valid hold gesture
	          - Fire gesture signal (if valid)
	          - Reset for next touch input
	        
	
	*Reference struct*
	'''
	{
	    "uid": 108,
	    "returnSignature": "m",
	    "name": "_eval_hold",
	    "parametersSignature": "()",
	    "description": "\n        Once the hold time has expired:\n          - Evaluate if the current sequence is a valid hold gesture\n          - Fire gesture signal (if valid)\n          - Reset for next touch input\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_eval_hold", [])

def _eval_sequence() -> object:
	"""
	
	        Once the sequence time has expired:
	          - Evaluate if the current sequence is a valid gesture
	          - Fire gesture signal (if valid)
	          - Reset for next touch input
	        
	
	*Reference struct*
	'''
	{
	    "uid": 109,
	    "returnSignature": "m",
	    "name": "_eval_sequence",
	    "parametersSignature": "()",
	    "description": "\n        Once the sequence time has expired:\n          - Evaluate if the current sequence is a valid gesture\n          - Fire gesture signal (if valid)\n          - Reset for next touch input\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_eval_sequence", [])

def _fire_gesture_signal(p0:object) -> object:
	"""
	Fire signal linked to gesture
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 110,
	    "returnSignature": "m",
	    "name": "_fire_gesture_signal",
	    "parametersSignature": "(m)",
	    "description": "Fire signal linked to gesture",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_fire_gesture_signal", [p0])

def _fire_release_signal() -> object:
	"""
	Fire signal linked to release of sensors
	
	*Reference struct*
	'''
	{
	    "uid": 111,
	    "returnSignature": "m",
	    "name": "_fire_release_signal",
	    "parametersSignature": "()",
	    "description": "Fire signal linked to release of sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_fire_release_signal", [])

def _on_sensor_change(p0:object) -> object:
	"""
	
	        On any head sensor change, acquire lock and starts e_sim (settling)
	        timer.
	        Note: Only the first signal starts the timer and all others are
	        debounced.
	        
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 112,
	    "returnSignature": "m",
	    "name": "_on_sensor_change",
	    "parametersSignature": "(m)",
	    "description": "\n        On any head sensor change, acquire lock and starts e_sim (settling)\n        timer.\n        Note: Only the first signal starts the timer and all others are\n        debounced.\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_on_sensor_change", [p0])

def _read_sensors() -> object:
	"""
	
	        Once the settling time (e_sim) is over:
	          - Read from head sensors.
	          - Store pattern
	          - Start hold and sequential timers
	        
	
	*Reference struct*
	'''
	{
	    "uid": 113,
	    "returnSignature": "m",
	    "name": "_read_sensors",
	    "parametersSignature": "()",
	    "description": "\n        Once the settling time (e_sim) is over:\n          - Read from head sensors.\n          - Store pattern\n          - Start hold and sequential timers\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_read_sensors", [])

def _search_gestures() -> object:
	"""
	
	        Compare inputted sequence to all gestures to find match
	
	        Algorithm:
	        1. async call _check_sequence on for all gestures
	           (i.e. gestures that match the current hold status and are not unset custom gestures)
	              -> _check_sequence() will fullfill promise with the gesture if matched; else None
	        2. Build list of all futures whose value is a matched sequence
	        3. Return the gesture whose match is the closest the sequence prototype
	           it matched (i.e. smallest difference)
	        
	
	*Reference struct*
	'''
	{
	    "uid": 114,
	    "returnSignature": "m",
	    "name": "_search_gestures",
	    "parametersSignature": "()",
	    "description": "\n        Compare inputted sequence to all gestures to find match\n\n        Algorithm:\n        1. async call _check_sequence on for all gestures\n           (i.e. gestures that match the current hold status and are not unset custom gestures)\n              -> _check_sequence() will fullfill promise with the gesture if matched; else None\n        2. Build list of all futures whose value is a matched sequence\n        3. Return the gesture whose match is the closest the sequence prototype\n           it matched (i.e. smallest difference)\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_search_gestures", [])

def _start() -> object:
	"""
	Start subscriptions to head sensors
	
	*Reference struct*
	'''
	{
	    "uid": 118,
	    "returnSignature": "m",
	    "name": "_start",
	    "parametersSignature": "()",
	    "description": "Start subscriptions to head sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_start", [])

def _start_d_hold_timer() -> object:
	"""
	Starts a timer that waits for the hold period to evaluate if there is a
	        valid hold sequence
	
	*Reference struct*
	'''
	{
	    "uid": 119,
	    "returnSignature": "m",
	    "name": "_start_d_hold_timer",
	    "parametersSignature": "()",
	    "description": "Starts a timer that waits for the hold period to evaluate if there is a\n        valid hold sequence",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_start_d_hold_timer", [])

def _start_e_seq_timer() -> object:
	"""
	Starts a timer that determines if events in a sequence happen soon
	        enough for them to be considered in teh current sequence.
	
	*Reference struct*
	'''
	{
	    "uid": 120,
	    "returnSignature": "m",
	    "name": "_start_e_seq_timer",
	    "parametersSignature": "()",
	    "description": "Starts a timer that determines if events in a sequence happen soon\n        enough for them to be considered in teh current sequence.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_start_e_seq_timer", [])

def _start_e_sim_timer() -> object:
	"""
	Starts timer that waits for a setteling time before reading the sensors
	
	*Reference struct*
	'''
	{
	    "uid": 121,
	    "returnSignature": "m",
	    "name": "_start_e_sim_timer",
	    "parametersSignature": "()",
	    "description": "Starts timer that waits for a setteling time before reading the sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_start_e_sim_timer", [])

def _stop() -> object:
	"""
	Unsubscribe from head sensors
	
	*Reference struct*
	'''
	{
	    "uid": 122,
	    "returnSignature": "m",
	    "name": "_stop",
	    "parametersSignature": "()",
	    "description": "Unsubscribe from head sensors",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_stop", [])

def _sync_preferences() -> object:
	"""
	Sync with preferences. This includes: Settle Time, Hold Time and Sequence Time
	
	*Reference struct*
	'''
	{
	    "uid": 123,
	    "returnSignature": "m",
	    "name": "_sync_preferences",
	    "parametersSignature": "()",
	    "description": "Sync with preferences. This includes: Settle Time, Hold Time and Sequence Time",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_sync_preferences", [])

def _validate_sequence(p0:object) -> object:
	"""
	Validate a requested gesture sequence
	
	Parameters
	----------
	p0:object
		
	
	*Reference struct*
	'''
	{
	    "uid": 124,
	    "returnSignature": "m",
	    "name": "_validate_sequence",
	    "parametersSignature": "(m)",
	    "description": "Validate a requested gesture sequence",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "_validate_sequence", [p0])

def createGesture_1(sensor_sequence:List[str]) -> str:
	"""
	Note: This is one of the overloads of the original method (createGesture)
	
	Define touch gesture.
	
	Parameters
	----------
	sensor_sequence:List[str]
		List of strings that represent the sequence of the desired gesture. For example, SingleFront would be the following: ['000', '100', '000']. NOTE: All sequences must start with '000' and all non-hold sequences must end with '000'. Hold gestures should end with the touch sequence you will be holding. For example, a SingleFrontHold would be the following: ['000', '100'].
	
	Returns
	----------
	If sequence is valid, the name of gesture to listen for, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 125,
	    "returnSignature": "s",
	    "name": "createGesture",
	    "parametersSignature": "([s])",
	    "description": "Define touch gesture.\n\n        :param sensor_sequence: List of strings that represent the\n        sequence of the desired gesture. For example, SingleFront\n        would be the following: ['000', '100', '000']. NOTE: All\n        sequences must start with '000' and all non-hold sequences\n        must end with '000'. Hold gestures should end with the touch\n        sequence you will be holding. For example, a SingleFrontHold\n        would be the following: ['000', '100'].\n\n        :returns: If sequence is valid, the name of gesture to listen\n        for, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "createGesture", [sensor_sequence])

def createGesture_2(sensor_sequence:str) -> str:
	"""
	Note: This is one of the overloads of the original method (createGesture)
	
	Define touch gesture.
	
	Parameters
	----------
	sensor_sequence:str
		Comma-separated string that represents the sequence of the desired gesture. For example, SingleFront would be the following: "000,100,000". NOTE: All sequences must start with '000' and all non-hold sequences must end with '000'. Hold gestures should end with the touch sequence you will be holding. For example, a SingleFrontHold would be the following: "000,100".
	
	Returns
	----------
	If sequence is valid, the name of gesture to listen for, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 126,
	    "returnSignature": "s",
	    "name": "createGesture",
	    "parametersSignature": "(s)",
	    "description": "Define touch gesture.\n\n        :param sensor_sequence: Comma-separated string that represents\n        the sequence of the desired gesture. For example, SingleFront\n        would be the following: \"000,100,000\". NOTE: All sequences\n        must start with '000' and all non-hold sequences must end with\n        '000'. Hold gestures should end with the touch sequence you\n        will be holding. For example, a SingleFrontHold would be the\n        following: \"000,100\".\n\n        :returns: If sequence is valid, the name of gesture to listen\n        for, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "createGesture", [sensor_sequence])

def getGesture_1(sequence:List[str]) -> object:
	"""
	Note: This is one of the overloads of the original method (getGesture)
	
	Get the sequence associated with a gesture name
	
	Parameters
	----------
	sequence:List[str]
		Sequence you want the gesture name of
	
	Returns
	----------
	Sequence (as list of strings) if it exists, None otherwise
	
	*Reference struct*
	'''
	{
	    "uid": 127,
	    "returnSignature": "m",
	    "name": "getGesture",
	    "parametersSignature": "([s])",
	    "description": "Get the sequence associated with a gesture name\n\n        :param sequence: Sequence you want the gesture name of\n\n        :returns: Sequence (as list of strings) if it exists, None otherwise",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "getGesture", [sequence])

def getGesture_2(sequence:str) -> object:
	"""
	Note: This is one of the overloads of the original method (getGesture)
	
	Get the sequence associated with a gesture name
	
	Parameters
	----------
	sequence:str
		Sequence you want the gesture name of
	
	Returns
	----------
	Sequence (as list of strings) if it exists, None otherwise
	
	*Reference struct*
	'''
	{
	    "uid": 128,
	    "returnSignature": "m",
	    "name": "getGesture",
	    "parametersSignature": "(s)",
	    "description": "Get the sequence associated with a gesture name\n\n        :param sequence: Sequence you want the gesture name of\n\n        :returns: Sequence (as list of strings) if it exists, None otherwise",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "getGesture", [sequence])

def getGestures() -> Dict[str,List[str]]:
	"""
	Get all gestures that have been defined in the system
	
	        :returns: Dictionary (Map<String, List<String>>) of all gestures
	
	*Reference struct*
	'''
	{
	    "uid": 129,
	    "returnSignature": "{s[s]}",
	    "name": "getGestures",
	    "parametersSignature": "()",
	    "description": "Get all gestures that have been defined in the system\n\n        :returns: Dictionary (Map<String, List<String>>) of all gestures",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "getGestures", [])

def getSequence(gesture_name:str) -> List[str]:
	"""
	Get the sequence associated with a gesture name
	
	Parameters
	----------
	gesture_name:str
		Name of gesture you want the sequence of
	
	Returns
	----------
	Sequence (as list of strings) if it exists, None otherwise 
	
	*Reference struct*
	'''
	{
	    "uid": 130,
	    "returnSignature": "[s]",
	    "name": "getSequence",
	    "parametersSignature": "(s)",
	    "description": "Get the sequence associated with a gesture name\n\n        :param gesture_name: Name of gesture you want the sequence of\n\n        :returns: Sequence (as list of strings) if it exists, None otherwise\n        ",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "getSequence", [gesture_name])

def setHoldTime_1(hold_time:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (setHoldTime)
	
	Set length of hold time.
	
	Parameters
	----------
	hold_time:float
		Desired hold time, in seconds (Default: 0.8s)
	
	Returns
	----------
	True if hold time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 133,
	    "returnSignature": "b",
	    "name": "setHoldTime",
	    "parametersSignature": "(f)",
	    "description": "Set length of hold time.\n\n        :param hold_time: Desired hold time, in seconds (Default: 0.8s)\n\n        :returns: True if hold time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setHoldTime", [hold_time])

def setHoldTime_2(hold_time:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (setHoldTime)
	
	Set length of hold time.
	
	Parameters
	----------
	hold_time:str
		Desired hold time, in seconds (Default: 0.8s)
	
	Returns
	----------
	True if hold time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 134,
	    "returnSignature": "b",
	    "name": "setHoldTime",
	    "parametersSignature": "(s)",
	    "description": "Set length of hold time.\n\n        :param hold_time: Desired hold time, in seconds (Default: 0.8s)\n\n        :returns: True if hold time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setHoldTime", [hold_time])

def setSequenceTime_1(sequence_time:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (setSequenceTime)
	
	Update length of sequence time.
	
	Parameters
	----------
	sequence_time:float
		Desired sequence time, in seconds (Default: 0.2s)
	
	Returns
	----------
	True if sequence time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 135,
	    "returnSignature": "b",
	    "name": "setSequenceTime",
	    "parametersSignature": "(f)",
	    "description": "Update length of sequence time.\n\n        :param sequence_time: Desired sequence time, in seconds (Default: 0.2s)\n\n        :returns: True if sequence time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setSequenceTime", [sequence_time])

def setSequenceTime_2(sequence_time:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (setSequenceTime)
	
	Set length of sequence time.
	
	Parameters
	----------
	sequence_time:str
		Desired sequence time, in seconds (Default: 0.2s)
	
	Returns
	----------
	True if sequence time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 136,
	    "returnSignature": "b",
	    "name": "setSequenceTime",
	    "parametersSignature": "(s)",
	    "description": "Set length of sequence time.\n\n        :param sequence_time: Desired sequence time, in seconds (Default: 0.2s)\n\n        :returns: True if sequence time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setSequenceTime", [sequence_time])

def setSettleTime_1(settle_time:float) -> bool:
	"""
	Note: This is one of the overloads of the original method (setSettleTime)
	
	Update length of settling time.
	
	Parameters
	----------
	settle_time:float
		Desired settling time, in seconds (Default: 0.04s)
	
	Returns
	----------
	True if settle time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 137,
	    "returnSignature": "b",
	    "name": "setSettleTime",
	    "parametersSignature": "(f)",
	    "description": "Update length of settling time.\n\n        :param settle_time: Desired settling time, in seconds (Default: 0.04s)\n\n        :returns: True if settle time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setSettleTime", [settle_time])

def setSettleTime_2(settle_time:str) -> bool:
	"""
	Note: This is one of the overloads of the original method (setSettleTime)
	
	Update length of settling time.
	
	Parameters
	----------
	settle_time:str
		Desired settling time, in seconds (Default: 0.04s)
	
	Returns
	----------
	True if settle time successfully updated, RuntimeError otherwise.
	
	*Reference struct*
	'''
	{
	    "uid": 138,
	    "returnSignature": "b",
	    "name": "setSettleTime",
	    "parametersSignature": "(s)",
	    "description": "Update length of settling time.\n\n        :param settle_time: Desired settling time, in seconds (Default: 0.04s)\n\n        :returns: True if settle time successfully updated, RuntimeError otherwise.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALTactileGesture", "setSettleTime", [settle_time])

