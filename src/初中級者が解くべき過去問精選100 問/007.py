from itertools import combinations

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
A = set(A)

ans = 0
for (x1, y1), (x2, y2) in combinations(A, 2):
    # 選んだ2点のベクトルを求める
    dx = x1 - x2
    dy = y1 - y2

    # 2点のベクトルと直行するベクトルを求める
    if (x2 - dy, y2 + dx) in A and (x1 - dy, y1 + dx) in A:
        d = dx**2 + dy**2
        ans = max(ans, d)

print(ans)
