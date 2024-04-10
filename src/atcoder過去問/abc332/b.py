K, G, M = map(int, input().split())

g, m = 0, 0

for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    elif G - g < m:
        m -= G - g
        g = G
    else:
        g += m
        m = 0

print(g, m)
