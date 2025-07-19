import os
import sys

# Credit: Nautilius/Stack Overflow

def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS2
	except Exception:
		base_path = os.path.abspath(".")
	
	return os.path.join(base_path, relative_path)