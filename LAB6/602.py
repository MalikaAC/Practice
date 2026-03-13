n = int(input())
arr = list(map(int, input().split()))
yo = list(filter(lambda x: x%2==0, arr))
print(len(yo))