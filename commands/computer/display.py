from tkinter import *

import re

from utils.index import to_color
def run(context):
    color = to_color(context["args"][0])
    gui = Tk(className='Color')
    gui.geometry("200x200")
    gui.configure(bg=f'{color}')
    gui.mainloop() 
def name(input):
    return re.match(r"(?:computer)?(?:display) (.*)", input)

def description():
    return "computer_display"