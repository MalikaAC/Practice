a = 606
b = 56

if a < b:
   print("a is greater than b")
else:
   print("b is greater than a")


print(bool(a == b))


if bool(()):
   print("Empty")
elif bool(0):
   print("It is zero.")
else:
   print("Normal number")


def myfunc():
   return True
if myfunc():
   print("Truth")
else:
   print("Lie")

x  = "lalalala"
print(isinstance(x, int))