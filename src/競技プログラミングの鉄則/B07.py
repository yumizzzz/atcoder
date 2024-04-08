import itertools

T = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

A = [0] * (T + 1)

# 各日の人数の増減を記録
for L, R in LR:
    A[L] += 1
    A[R] -= 1

# 累積和を取る
S = list(itertools.accumulate(A))

for i in range(T):
    print(S[i])
