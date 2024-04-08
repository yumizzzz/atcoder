H, W, N = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]

S = [[0] * (W + 2) for _ in range(H + 2)]

for a, b, c, d in ABCD:
    S[a][b] += 1
    S[c + 1][d + 1] += 1
    S[a][d + 1] -= 1
    S[c + 1][b] -= 1

# 累積和
T = [[0] * (W + 2) for _ in range(H + 2)]
for h in range(1, H + 1):
    for w in range(1, W + 1):
        T[h][w] = T[h][w - 1] + S[h][w]

for w in range(1, W + 1):
    for h in range(1, H + 1):
        T[h][w] = T[h - 1][w] + T[h][w]

for i in range(1, H + 1):
    print(*T[i][1:-1])
