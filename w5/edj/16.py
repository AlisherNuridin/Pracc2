import re

s = input()

match = re.search(r"Name:\s*(.*),\s*Age:\s*(.*)", s)

if match:
    print(match.group(1), match.group(2))