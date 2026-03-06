import re
s = input()
w = re.findall(r"\b\w{3}\b", s)
print(len(w))