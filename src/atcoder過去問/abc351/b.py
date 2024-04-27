N = int(input())
A = [str(input()) for _ in range(N)]
B = [str(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
            exit()
