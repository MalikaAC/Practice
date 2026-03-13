s = input()
if any(word in "aeiouAEIOU" for word in s):
    print("Yes")
else:
    print("No")