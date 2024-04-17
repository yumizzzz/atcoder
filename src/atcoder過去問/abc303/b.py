import math

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

all_pair = math.comb(N, 2)

s = set()
for i in range(M):
    for j in range(N - 1):
        pair1, pair2 = A[i][j], A[i][j + 1]
        if pair1 < pair2:
            pair1, pair2 = pair2, pair1
        s.add((pair1, pair2))

print(all_pair - len(s))
