n = int(input())

episodes = {}

for _ in range(n):
    name, k = input().split()
    k = int(k)

    if name in episodes:
        episodes[name] += k
    else:
        episodes[name] = k

for name in sorted(episodes):
    print(name, episodes[name])
