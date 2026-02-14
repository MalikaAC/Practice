n = input()

is_valid = True

for digit in n:
    if int(digit) % 2 != 0:
        is_valid = False
        break

print("Valid" if is_valid else "Not valid")
