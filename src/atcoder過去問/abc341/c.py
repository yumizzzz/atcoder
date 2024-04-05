H, W, N = map(int, input().split())
T = str(input())
S = [str(input()) for _ in range(H)]

d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue

        ii = i
        jj = j
        for t in T:
            dx, dy = d[t]
            ii += dx
            jj += dy
            if ii < 0 or ii >= H or jj < 0 or jj >= W:
                break
            elif S[ii][jj] == "#":
                break
        else:
            count += 1

print(count)
