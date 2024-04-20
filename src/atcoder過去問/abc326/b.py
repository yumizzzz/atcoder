N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(0, N - 1):
    b = A[i] * A[i + 1]
    ans.append(b)

print(*ans)
