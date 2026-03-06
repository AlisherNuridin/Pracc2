import re

text = "My phone number is 12345 and my age is 20"

# re.search() - find first match
result = re.search(r"\d+", text)
print("search:", result.group())

# re.findall() - find all matches
numbers = re.findall(r"\d+", text)
print("findall:", numbers)

# re.split() - split string
fruits = "apple,banana,orange"
split_result = re.split(r",", fruits)
print("split:", split_result)

# re.sub() - replace text
sentence = "I like cats"
new_sentence = re.sub(r"cats", "dogs", sentence)
print("sub:", new_sentence)

# re.match() - match at beginning
start = "Hello world"
match_result = re.match(r"Hello", start)
if match_result:
    print("match: Found at beginning")

# special sequences
digits = re.findall(r"\d", text)
print("digits:", digits)

# word count example
words = re.findall(r"\b\w+\b", "Hello world from Python")
print("words:", words)