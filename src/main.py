K, G, M = map(int, input().split())

g = 0
m = 0
for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    elif G - g < m:
        m = m - (G - g)
        g = G
    else:
        g = g + m
        m = 0

print(g, m)