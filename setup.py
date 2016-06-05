import sys
from cx_Freeze import setup, Executable

include_files = ['pythoncom', 'pyHook']
base = None

setup(name="Logger",
	version="1.0.0",
	description="pyHook demo",
	options={'build.exe':{'include_files':include_files}},
	executables=[Executable("logger.py", base=base)])

