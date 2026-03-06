import re
s = input()
ss = input()

x = (re.search(ss, s))
if x:
    print("Yes")
else:
    print("No")