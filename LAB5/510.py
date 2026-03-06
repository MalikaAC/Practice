import re
s = input()
x = re.findall("cat|dog", s)
if x:
    print("Yes")
else:
    print("No")