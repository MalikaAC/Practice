n = int(input())
num = list(map(int, input().split()))
result = sorted(set(num))
print(*result)