n = int(input())
book = {}

for _ in range(n):
    command = input().split()

    if command[0] == "set":
        book[command[1]] = command[2]

    else:
        key = command[1]
        if key in book:
            print(book[key])
        else:
            print("KE: no key " + key + " found in the document")
