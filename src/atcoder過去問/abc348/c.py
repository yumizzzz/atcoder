from collections import defaultdict

N = int(input())
AC = [list(map(int, input().split())) for _ in range(N)]

d = defaultdict(int)
for a, c in AC:
    if c not in d:
        d[c] = a
    else:
        d[c] = min(d[c], a)

print(max(d.values()))
