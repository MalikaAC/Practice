import re

s = input()
ss = input()

x = len(re.findall(ss, s))

print(x)