i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1


i = 1
while i < 10:
    if i % 2 == 0:
        print("First even:", i)
        break
    i += 1


i = 8
while True:
    if i % 7 == 0:
         print("First multiple of 7:", i)
         break
    i += 1


while True:
    age = int(input("Age: "))
    if age >= 18:
        print("Allowed")
        break
    print("Too young")


while True:
    login = input("Login: ")
    if login == "admin":
        break
    print("Wrong login")

    