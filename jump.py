import pyHook
import pythoncom
import win32api
import math
from PIL import Image
import os
import time

def onMouseEvent(event):
    global n, all
    if event.MessageName == "mouse left down":
        n += 1
        print "MessageName:", event.MessageName
        #print "Message:", event.Message
        #print "Time:", event.Time
        #print "Window:", event.Window
        #print "WindowName:", event.WindowName
        print "Position:", event.Position
        #print "Wheel:", event.Wheel
        #print "Injected:", event.Injected
        print"---"
        all.append(str(event.Position))
    if n == 4:
        win32api.PostQuitMessage()
    return True

def onKeyboardEvent(event):
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    print "ScanCode:", event.ScanCode
    print "Extended:", event.Extended
    print "Injected:", event.Injected
    print "Alt", event.Alt
    print "Transition", event.Transition
    print "---"
    return True

def main():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()
    distance = (math.sqrt((int(str(all[0][1:-1]).split(",")[0]) - int(str(all[1][1:-1]).split(",")[0]))**2 +
           (int(str(all[0][1:-1]).split(",")[1]) - int(str(all[1][1:-1]).split(",")[1]))**2))
    print distance
    return distance

if __name__ == "__main__":
    while True:
        n = 0
        all = []
        #os.system('dir')
        os.system('ADB\\adb.exe shell screencap -p /sdcard/1.png')
        os.system('ADB\\adb.exe pull /sdcard/1.png .')
        im = Image.open("1.png")
        box = (0, 300, 700, 700)
        region = im.crop(box)
        region.show()
        distance = main()
        press_time = distance * 2.467
        press_time = int(press_time)
        cmd = 'ADB\\adb shell input swipe 320 410 320 410 ' + str(press_time)
        print(cmd)
        os.system(cmd)

        print ("end")
        time.sleep(0.8)