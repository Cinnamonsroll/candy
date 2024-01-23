import os
import importlib


ordinal = {
   "one": 1,
   "to": 2,
   "two": 2,
   "twice": 2,
   "three": 3,
   "for": 4,
   "fourth": 4,
   "four": 4,
   "five": 5,
   "six": 6,
   "seven": 7,
   "eight": 8,
   "nine": 9,
   "ten": 10
}

def to_number(string):
    return ordinal[string]
def to_color(s):
    s = s.split(" ")
    color = ""
    for p in s:
        if p in ordinal:
            color += f"{to_number(p)}"
        else:
            color += "#" if p == "hashtag" else p
    return color


def process_file(file):
    parents = [p.replace("./", "") for p in file.split(os.path.sep)]
    index = parents.index('commands')
    parents = [p for i, p in enumerate(parents) if i > index]
    command = "/".join(parents)
    try:
        module_name = ".".join(["commands"] + parents[:-1] + [os.path.splitext(parents[-1])[0]])
        module = importlib.import_module(module_name)
        run_function = getattr(module, "run")
        name_function = getattr(module, "name")
        name_description = getattr(module, "description")
        return (command, run_function, name_function, name_description)
    except (ImportError, AttributeError):
        return None


def load(dir, cb, first=True):
    joined = os.path.join(os.getcwd(), dir) if first else dir
    for entry in os.listdir(joined):
        joined_entry = os.path.join(joined, entry)
        if os.path.isdir(joined_entry):
            load(joined_entry, cb, False)
        else:
            cb(process_file(joined_entry))

def parse_statement(statement, validCommands = []):
    parts = statement.split()
    result = []
    i = 0
    while i < len(parts):
       curr = str(ordinal[parts[i]] if parts[i] in ordinal else parts[i])
       if curr.isdigit():
           result.append((parts[i-1], int(curr)))
           i += 1
       elif curr in validCommands:
           result.append((curr,))
       i += 1
    return result

def parse_command(textInput, prefix):
    textSplit = textInput.split(" ")
    for wordIndex in range(len(textSplit)):
        word = textSplit[wordIndex]
        if word == prefix:
            textInput = textInput[len(' '.join(textSplit[:wordIndex+1])):]
            textInput = textInput.strip()
            return textInput
    return None