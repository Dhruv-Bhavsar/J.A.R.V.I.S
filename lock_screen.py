# ctypes module to load windows library
import ctypes
# speech recognition module
import speech_recognition as sr
import sys
import os

if sys.argv[1] == "lock":
    ctypes.windll.user32.LockWorkStation()

elif sys.argv[1] == "sleep":
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")