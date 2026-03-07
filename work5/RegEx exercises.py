#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

s = input()

if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")


#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
s = input()
x = re.fullmatch(r"ab{2,3}", s)
if x:
    print("Yes")
else:
    print("No")

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
yxy = input()
x = re.fullmatch(r"^[a-z]+_[a-z]+$", yxy)
if x:
    print("Yes")
else:
    print("No")

#4.Write a Python program to find the sequences of one upper case letter followed by lower case letters.
uxu = input()
x = re.fullmatch(r"[A-Z][a-z]+", uxu)
if x:
    print("Yes")
else:
    print("No")


#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
ixi = input()
x = re.fullmatch(r"^a.*b$", ixi)
if x:
    print("Yes")
else:
    print("No")



#6.Write a Python program to replace all occurrences of space, comma, or dot with a colon.
oxo = input()
print(re.sub(r"[ .,]", ":", oxo))


#7.Write a python program to convert snake case string to camel case string.
pxp = input()
x = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), pxp)
print(x)


#8.Write a Python program to split a string at uppercase letters
axa = input()
x = re.split(r"?=[A-Z]", axa)
print(x)


#9. Write a Python program to insert spaces between words starting with capital letters.
sxs = input()
x = re.sub(r"(?=[A-Z])", " ", sxs)
print(x)



#10. Write a Python program to convert a given camel case string to snake case.
dxd = input()
x = re.sub(r"([A-Z])", r"_\1", s).lower()
print(x)