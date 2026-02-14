n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    cmd = input().split()
    
    if cmd[0] == "add":
        x = int(cmd[1])
        arr = list(map(lambda a: a + x, arr))
        
    elif cmd[0] == "multiply":
        x = int(cmd[1])
        arr = list(map(lambda a: a * x, arr))
        
    elif cmd[0] == "power":
        x = int(cmd[1])
        arr = list(map(lambda a: a ** x, arr))
        
    elif cmd[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))

print(*arr)