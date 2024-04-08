H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

S = [[0] * (W + 1) for _ in range(H + 1)]

# 横方向に累積和
for h in range(1, H + 1):
    for w in range(1, W + 1):
        S[h][w] = S[h][w - 1] + X[h - 1][w - 1]

# 縦方向に累積和
for w in range(1, W + 1):
    for h in range(1, H + 1):
        S[h][w] = S[h - 1][w] + S[h][w]

for a, b, c, d in ABCD:
    ans = S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1]
    print(ans)
