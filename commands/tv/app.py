import re


applications = {
      "netflix": 12,
      "youtube": 837,
      "you": 837
}


def run(context):
    parsedApp = context["args"][0]
    if(parsedApp == "home"): return context["roku"].home()
    show = context["roku"][applications[parsedApp]]
    show.launch()

def name(input):
    return re.match(r"(?:tv)?(?:switch|go) (?:to )?(\w+)", input)

def description():
    return "app_switch"