N = int(input())
ABCD = [list(map(int, input().split())) for _ in range(N)]

H = 1500
W = 1500
S = [[0] * (W + 1) for _ in range(H + 1)]

for a, b, c, d in ABCD:
    S[a][b] += 1
    S[c][d] += 1
    S[a][d] -= 1
    S[c][b] -= 1

# 累積和
for h in range(H + 1):
    for w in range(1, W + 1):
        S[h][w] = S[h][w - 1] + S[h][w]

for w in range(W + 1):
    for h in range(1, H + 1):
        S[h][w] = S[h - 1][w] + S[h][w]

ans = 0
for i in range(H + 1):
    for j in range(W + 1):
        if S[i][j] > 0:
            ans += 1

print(ans)
