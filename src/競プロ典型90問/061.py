from collections import deque

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

A = deque()

for t, x in TX:
    if t == 1:
        A.appendleft(x)
    elif t == 2:
        A.append(x)
    elif t == 3:
        print(A[x - 1])
