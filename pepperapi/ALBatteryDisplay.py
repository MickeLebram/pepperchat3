from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def hide() -> None:
	"""
	Hides the tablet.
	
	*Reference struct*
	'''
	{
	    "uid": 100,
	    "returnSignature": "v",
	    "name": "hide",
	    "parametersSignature": "()",
	    "description": "Hides the tablet.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBatteryDisplay", "hide", [])

def show() -> None:
	"""
	Shows battery level on tablet, for 10 seconds.
	
	*Reference struct*
	'''
	{
	    "uid": 101,
	    "returnSignature": "v",
	    "name": "show",
	    "parametersSignature": "()",
	    "description": "Shows battery level on tablet, for 10 seconds.",
	    "parameters": [],
	    "returnDescription": ""
	}
	'''
	"""
	return send_mfc("ALBatteryDisplay", "show", [])

