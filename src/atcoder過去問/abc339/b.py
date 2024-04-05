H, W, N = map(int, input().split())

A = [["." for _ in range(W)] for _ in range(H)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
h, w = 0, 0
d = 0

for i in range(N):
    if A[h][w] == ".":
        A[h][w] = "#"
        d = (d + 1) % 4
    else:
        A[h][w] = "."
        d = (d - 1) % 4

    h += directions[d][0]
    w += directions[d][1]
    h %= H
    w %= W

for a in A:
    print("".join(a))
