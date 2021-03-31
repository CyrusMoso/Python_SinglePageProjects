import pyautogui
import time

pyautogui.FAILSAFE = False

while True:
    time.sleep(50)
    for i in range(0,25):
        pyautogui.moveTo(0, i*5)
    for i in range(0,3):
        pyautogui.press("shift")
        # pyautogui.middleClick(0,10)