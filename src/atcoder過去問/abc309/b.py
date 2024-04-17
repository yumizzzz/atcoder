import copy

N = int(input())
A = []
for i in range(N):
    a = list(str(input()))
    A.append(a)

B = copy.deepcopy(A)

B[0][0] = A[1][0]
B[0][1:] = A[0][:-1]

B[-1][-1] = A[-2][-1]
B[-1][:-1] = A[-1][1:]

for i in range(1, N - 1):
    B[i][0] = A[i + 1][0]
    B[i][-1] = A[i - 1][-1]

for b in B:
    print(*b, sep="")
