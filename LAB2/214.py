n = int(input())
a = list(map(int, input().split()))

best_number = a[0]
best_count = 0

for x in a:
    count = 0
    for y in a:
        if y == x:
            count += 1

    if count > best_count or (count == best_count and x < best_number):
        best_count = count
        best_number = x

print(best_number)
