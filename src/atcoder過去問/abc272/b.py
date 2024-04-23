N, M = map(int, input().split())
X = []
for i in range(M):
    KX = list(map(int, input().split()))
    X.append(KX[1:])

A = [[0] * N for _ in range(N)]
for x in X:
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            A[x[i] - 1][x[j] - 1] = 1
            A[x[j] - 1][x[i] - 1] = 1

if all([sum(a) == N - 1 for a in A]):
    print("Yes")
else:
    print("No")
