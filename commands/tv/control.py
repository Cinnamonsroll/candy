import re
import time
from utils.index import parse_statement
def run(context):
    parsed_input = context["args"][0]
    commands = parse_statement(parsed_input, context["roku"].commands)
    lastCommand = None
    for command in commands:
       if len(command) == 1 and command[0] != "select": continue
       if lastCommand == command[0]: continue
       cmd, times = (command[0], command[1] if len(command) > 1 else 1)
       lastCommand = cmd
       for i in range(times):
          command_to_run = getattr(context["roku"], cmd)
          command_to_run()
          time.sleep(0.5)

def name(input):
    return re.match(r"(?:tv)?(?:control) (.*)", input)

def description():
    return "tv_control"