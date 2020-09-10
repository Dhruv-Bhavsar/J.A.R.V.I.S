import os
import time
import datetime
import pyttsx3
import sys
import subprocess

def offline_speak1(jarvis_speech):
    engine = pyttsx3.init('sapi5')
    engine.say(jarvis_speech)
    engine.runAndWait()    


if sys.argv[1] == "sublime":
    codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
    os.startfile(codepath)

elif sys.argv[1] == "eclipse":
    codePath = "E:\\aj-java_with_jsf[2017]\\eclipse-standard-kepler-SR2-win32\\eclipse\\eclipse.exe"
    os.startfile(codePath)

elif sys.argv[1] == "pycharm":
    codePath = "C:\\Users\\abc\\New folder\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
    os.startfile(codePath)

elif sys.argv[1] == "brackets":
    codepath = "C:\\Program Files (x86)\\Brackets\\Brackets.exe"
    os.startfile(codepath)

elif sys.argv[1] == "vs":
    codePath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif sys.argv[1] =="codeblocks":
    codepath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
    os.startfile(codepath)

elif sys.argv[1] == "time":
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    offline_speak1(f'The time is : {strTime}')

elif sys.argv[1] == "atom":
    codepath = "C:\\Users\\abc\\AppData\\Local\\atom\\atom.exe"
    os.startfile(codepath)

elif sys.argv[1] == "netbeans":
    codepath = "C:\\Program Files\\NetBeans 8.0.1\\bin\\netbeans64.exe"
    os.startfile(codepath)

elif sys.argv[1] == "android":
    codepath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
    os.startfile(codepath)

elif sys.argv[1] == "calc":
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')

elif sys.argv[1] == "vlc":
    subprocess.Popen('C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe')

elif sys.argv[1] == "firefox":
    subprocess.Popen('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')

elif sys.argv[1] == "chrome":
    subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
   
elif sys.argv[1] == "closeEclipse":
    os.system("taskkill /f /im eclipse.exe")

elif sys.argv[1] == "closePycharm":
    os.system("taskkill /f /im pycharm64.exe")

elif sys.argv[1] == "closeAndroid":
    os.system("taskkill /f /im studio64.exe")

elif sys.argv[1] == "closeNetbeans":
    os.system("taskkill /f /im netbeans64.exe")

elif sys.argv[1] == "closeAtom":
    os.system("taskkill /f /im atom.exe")

elif sys.argv[1] == "closeEclipse":
    os.system("taskkill /f /im eclipse.exe")

elif sys.argv[1] == "closeCodeblocks":
    os.system("taskkill /f /im codeblocks.exe")

elif sys.argv[1] == "closeCode":
    os.system("taskkill /f /im code.exe")

elif sys.argv[1] == "closeBrackets":
    os.system("taskkill /f /im Brackets.exe")

elif sys.argv[1] == "closeSublime":
    os.system("taskkill /f /im sublime_text.exe")

elif sys.argv[1] == "systemStatus":
    import psutil
    import wmi
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    f = wmi.WMI()
    i = 0 
    for process in f.Win32_Process():
        i += 1
    offline_speak1("All systems are at 100 percent. Battery : " + str(percent)+'% | Battery State : ' + plugged + ' and total ' + str(i) + ' processes are currently running.')

elif sys.argv[1] == "feel":
    import psutil
    import wmi
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    f = wmi.WMI()
    i = 0 
    for process in f.Win32_Process():
        i += 1
    offline_speak1(" I am Fine sir, Thanks for asking.All systems are at 100 percent. Battery : " + str(percent)+'% | Battery State : ' + plugged + ' and total ' + str(i) + ' processes are currently running.')




elif sys.argv[1] == "home":
    #!/usr/bin/env python
    import pygetwindow as gw
    windows = gw.getAllWindows()
    for i in range(len(windows)):
        windows[i].minimize()

    time.sleep(5)

elif sys.argv[1] == "s":
    import wmi

    brightness = int(sys.argv[2]) # percentage [0-100]
    c = wmi.WMI(namespace='wmi')

    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)