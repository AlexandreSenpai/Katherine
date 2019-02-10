import sys
from cx_Freeze import setup, Executable
#Vanilla Python Modules~
import os
import webbrowser
import smtplib
import win32com
#Not Python Vanilla Modules~
import speech_recognition as sr
from playsound import playsound
import ctypes
import comtypes
import pyttsx3
import gtts
from pycaw.pycaw import AudioUtilities
from audio_control import *
from shiro import *
from comandos import *
from user_check import *

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["comandos","audio_control","user_check","shiro","gtts","os", "pyttsx3", "win32com", "webbrowser", "smtplib", "speech_recognition", "playsound", "ctypes", "comtypes", "pycaw.pycaw"], "includes": ["playsound"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Shiro",
        version = "0.1",
        description = "Shiro",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base, icon="icon.ico")])
