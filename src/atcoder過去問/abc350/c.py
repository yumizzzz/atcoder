N = int(input())
A = list(map(int, input().split()))

d = {v: i for i, v in enumerate(A)}

ans = []
for i in range(N):
    while A[i] != i + 1:
        j = A[i] - 1
        A[i], A[j] = A[j], A[i]
        ans.append((i + 1, j + 1))

print(len(ans))
for a in ans:
    print(*a)
