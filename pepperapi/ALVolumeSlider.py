from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def decreaseVolume() -> bool:
	"""
	Decrease volume to next multiple of 20%.
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "b",
	    "name": "decreaseVolume",
	    "parametersSignature": "()",
	    "description": "Decrease volume to next multiple of 20%.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVolumeSlider", "decreaseVolume", [])

def increaseVolume() -> bool:
	"""
	Increase volume to next multiple of 20%.
	
	*Reference struct*
	'''
	{
	    "uid": 102,
	    "returnSignature": "b",
	    "name": "increaseVolume",
	    "parametersSignature": "()",
	    "description": "Increase volume to next multiple of 20%.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALVolumeSlider", "increaseVolume", [])

