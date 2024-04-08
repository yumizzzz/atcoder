N = int(input())
A = list(map(int, input().split()))
D = int(input())
LR = [list(map(int, input().split())) for _ in range(D)]

S = [0] * (N)
S[0] = A[0]
for i in range(1, N):
    S[i] = max(S[i - 1], A[i])

T = [0] * (N)
T[N - 1] = A[N - 1]
for i in reversed(range(0, N - 1)):
    T[i] = max(T[i + 1], A[i])

# L-2: L-1番目の1つ前の要素
# R: R-1番目の1つ大きい要素
for L, R in LR:
    print(max(S[L - 2], T[R]))
