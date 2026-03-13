n = int(input())
num = list(map(int, input().split()))
if all(a >= 0 for a in num):
    print("Yes")
else:
    print("No")