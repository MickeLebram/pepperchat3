from .gentypes import *
from .robot_client import send_mfc
import json
"""

"""
def add(expression:str, report_mode:int) -> object:
	"""
	Adds a condition expression to ALExpressionWatcher engine
	
	Parameters
	----------
	expression:str
		Condition expression in ConditionChecker language
	report_mode:int
		ALExpressionWatcher report mode, available modes: { REPORT_CHANGE = 0, REPORT_EDGE = 1, REPORT_EDGE_TRUE = 2 }
	
	Returns
	----------
	Corresponding ExpressionObject
	
	*Reference struct*
	'''
	{
	    "uid": 103,
	    "returnSignature": "o",
	    "name": "add",
	    "parametersSignature": "(si)",
	    "description": "Adds a condition expression to ALExpressionWatcher engine",
	    "parameters": [
	        {
	            "name": "expression",
	            "description": "Condition expression in ConditionChecker language"
	        },
	        {
	            "name": "report_mode",
	            "description": "ALExpressionWatcher report mode, available modes: { REPORT_CHANGE = 0, REPORT_EDGE = 1, REPORT_EDGE_TRUE = 2 }"
	        }
	    ],
	    "returnDescription": "Corresponding ExpressionObject"
	}
	'''
	"""
	return send_mfc("ALExpressionWatcher", "add", [expression, report_mode])

