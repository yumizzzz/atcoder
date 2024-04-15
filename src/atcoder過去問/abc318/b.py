N = int(input())
ABCD = [list(map(int, input().split())) for _ in range(N)]

S = [[0] * 100 for _ in range(100)]

for abcd in ABCD:
    a, b, c, d = abcd
    for x in range(a, b):
        for y in range(c, d):
            S[x][y] = 1

ans = 0
for i in range(100):
    for j in range(100):
        ans += S[i][j]

print(ans)
