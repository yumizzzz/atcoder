import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

all = list(itertools.accumulate(A))
all = [0] + all

for i in range(Q):
    L, R = LR[i]
    print(all[R] - all[L - 1])
