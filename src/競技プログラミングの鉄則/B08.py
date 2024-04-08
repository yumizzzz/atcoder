N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

S = [[0] * 1501 for _ in range(1501)]
for x, y in XY:
    S[x][y] += 1


T = [[0] * 1501 for _ in range(1501)]
# 横方向に累積和を取る
for i in range(1, 1501):
    for j in range(1, 1501):
        T[i][j] = T[i][j - 1] + S[i][j]

# 縦方向に累積和を取る
for i in range(1, 1501):
    for j in range(1, 1501):
        T[i][j] = T[i - 1][j] + T[i][j]


for a, b, c, d in ABCD:
    ans = T[c][d] - T[a - 1][d] - T[c][b - 1] + T[a - 1][b - 1]
    print(ans)
