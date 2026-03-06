import re

s = input()

n = re.findall(r"\d{2,}", s)

print(" ".join(n))