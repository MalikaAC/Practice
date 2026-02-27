import math
#1. Write a Python program to convert degree to radian.
n = int(input())
radi = (n * math.pi)/180
print(radi)

#2.Write a Python program to calculate the area of a trapezoid.
h, base1, base2 = map(int, input().split())
area = ((base1 + base2)/2)*h
print(area)

#3. Write a Python program to calculate the area of regular polygon.
n = int(input())
l = float(input())
print(math.ceil((n * l * l)/ 4 * math.tan(math.pi/n)))

#4. Write a Python program to calculate the area of a parallelogram.
length = int(input())
height = int(input())
print(length * height)