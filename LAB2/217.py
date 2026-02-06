n = int(input())
count = {}

for _ in range(n):
    phone = input()
    if phone in count:
        count[phone] += 1
    else:
        count[phone] = 1

answer = 0
for phone in count:
    if count[phone] == 3:
        answer += 1

print(answer)
