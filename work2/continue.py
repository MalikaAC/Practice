i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


n = [2, -9, 5, -4, 8]
i = 0
while i < len(n):
    if n[i] < 0:
        i += 1
        continue
    print(n[i])
    i += 1


text = "banana"
i = 0
while i < len(text):
    if text[i] == "a":
        i += 1
        continue
    print(text[i])
    i += 1


i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)


i = 0
while i < 7:
    i += 1
    if  i != 5:
        continue
    i += 1