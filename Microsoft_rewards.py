import pyautogui
import time
from random_word import RandomWords
import os

r = RandomWords()
url = "https://rewards.bing.com/?ref=WSB&redref=amc"
command = f"start microsoft-edge:{url}"
time.sleep(1)
count, x = 0, 0
os.system(command)
time.sleep(3)

while count < 34 and x <= 1:
    pyautogui.hotkey("ctrl", "t")
    pyautogui.typewrite(r.get_random_word())
    pyautogui.press("enter")
    time.sleep(1 - x)
    pyautogui.hotkey("ctrl", "w")
    x += 1 / 33
    count = count + 1
