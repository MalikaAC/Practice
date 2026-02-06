subjects = ["Calc2", "PP2", "English"]
for x in subjects:
    if x == "PP2":
        continue
    print(x)


colors = ["black", "white", "red"]
cars = ["bmw", "audi", "toyota"]
for c in colors:
    for car in cars:
        if car == "audi":
            continue
        print(c, car)


colors = ["red", "blue", "green"]
for c in colors:
    if c == "blue":
        continue
    print(c)


for i in range(6):
    if i == 3:
        continue
    print(i)


for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
