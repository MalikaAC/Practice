n = int(input())

def evens(x):
    for i in range(0, x + 1):
        if i % 2 == 0:
            yield i

first = True
for num in evens(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False