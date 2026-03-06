import re
s = input()
x = re.findall("\\d", s)
print(" ".join(x))