digit_map = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

reverse_map = {v: k for k, v in digit_map.items()}

s = input().strip()

for op in "+-*":
    if op in s:
        left, right = s.split(op)
        operator = op
        break

def to_number(st):
    return int("".join(digit_map[st[i:i+3]] for i in range(0, len(st), 3)))

num1 = to_number(left)
num2 = to_number(right)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2

print("".join(reverse_map[d] for d in str(result)))