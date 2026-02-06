n = int(input())

pow = 1
while n  > pow:
    pow *= 2

if pow == n:
    print("YES")
else:
    print("NO")