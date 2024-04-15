from collections import defaultdict

N, Q = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(Q)]


d = defaultdict(int)
for i in range(1, N + 1):
    d[i] = 2


for e in E:
    c, x = e
    if c == 1:
        d[x] -= 1
    elif c == 2:
        d[x] -= 2
    else:
        if d[x] <= 0:
            print("Yes")
        else:
            print("No")
