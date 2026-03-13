n = int(input())
num = list(map(int, input().split()))
squares = map(lambda x: x**2, num)
print(sum(squares))