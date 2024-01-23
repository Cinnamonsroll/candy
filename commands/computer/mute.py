import re
import pyautogui
def run(context):
    pyautogui.hotkey("ctrl", "m")
def name(input):
    return re.match(r"(?:computer)?(?:un|on)?mute", input)

def description():
    return "computer_mute"