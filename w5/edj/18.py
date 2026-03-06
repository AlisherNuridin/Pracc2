import re

s = input()
pattern = input()

literal_pattern = re.escape(pattern)

matches = re.findall(literal_pattern, s)

print(len(matches))