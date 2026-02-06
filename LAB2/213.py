x = int(input())

if x < 2:
    print("No")
else:
    prm = True

    for i in range(2, x):
        if x % i == 0:
            prm = False
            break

    if prm:
        print("Yes")
    else:
        print("No")