import re
from utils.index import to_number

def run(context):
    direction, amount = context["args"][0].split(" ")
    amount = to_number(amount)
    if direction == "up":
        for i in range(amount):
            context["roku"].volume_up()
    elif direction == "down":
        for i in range(amount):
            context["roku"].volume_down()
    
def name(input):
    return re.match(r"(?:tv)?(?:volume) (.*)", input)

def description():
    return "tv_volume"