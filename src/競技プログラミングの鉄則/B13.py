import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [None] * N
sum_A = [0] + list(itertools.accumulate(A))

for i in range(N):
    if i == 0:
        R[i] = -1
    else:
        R[i] = R[i - 1]

    while R[i] < N - 1 and sum_A[R[i] + 2] - sum_A[i] <= K:
        R[i] += 1

ans = 0
for i in range(N):
    ans += R[i] - i + 1
print(ans)
