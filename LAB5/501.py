import re
txt = input()
x = (re.findall("\\AHello", txt))
if x:
    print("Yes")
else:
    print("No")