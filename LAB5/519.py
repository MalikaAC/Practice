import re

pattern = re.compile(r"\b\w+\b")

s = input()

words = pattern.findall(s)

print(len(words))