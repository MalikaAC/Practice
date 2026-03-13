n = int(input())
w = input().split()
d = input().split()
p = input()

d = dict(zip(w, d))
print(d.get(p, "Not found"))