import re

def run(context):
    query = context["args"][0]
    context["roku"].literal(query)
def name(input):
    return re.match(r"(?:tv)?(?:search) (.*)", input)

def description():
    return "tv_search"