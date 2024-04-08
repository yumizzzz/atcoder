import itertools

D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

A = [0] * (D + 1)

# 各日の人数の増減を記録
for L, R in LR:
    A[L - 1] += 1
    A[R] -= 1

# 累積和を取る
S = list(itertools.accumulate(A))

for i in range(D):
    print(S[i])
