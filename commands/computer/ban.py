import pyautogui
import time
from AppOpener import open
import re


def run(context):
    user = context["args"][0]
    open("Discord")
    time.sleep(1.2)
    pyautogui.hotkey("ctrl", "k")
    time.sleep(0.5)
    pyautogui.write("testing-1", interval=0.1)
    pyautogui.press("enter", interval=0.1)
    time.sleep(1)
    pyautogui.click(462, 930)
    time.sleep(1.5)
    pyautogui.write(f"/ban {user}", interval=0.1)
    pyautogui.press("enter", interval=0.1)
    time.sleep(0.5)
    pyautogui.press("enter", interval=0.1)
    time.sleep(1.5)
    pyautogui.press("enter", interval=0.1)

def name(input):
    return re.match(r"(?:computer)?(?:ban) (.*)", input)


def description():
    return "computer_ban"
