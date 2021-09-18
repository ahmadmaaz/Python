import pywhatkit
import pyautogui
import time
toto= "+96176046064"
panda="+96181726783"
kitllers= "+966509558092"
zeinab="+96181710750"
sarah= "+96176819583"
number= input("please insert the : ")
message= input("insert the message: ")
time= input("insert the time(hour): ")
minutes= input("insert the time(minutes): ")

number= number.lower()
if number=="toto":
    number=toto
if number=="panda":
    number= panda
if number=="kitllers":
    number=kitllers
if number=="zeinab":
    number=zeinab
if number=="sarah":
    number=sarah

pywhatkit.sendwhatmsg(number, message, int(time), int(minutes))
time.sleep(25)
pyautogui.press("enter")
