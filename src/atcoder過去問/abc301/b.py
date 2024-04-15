N = input()
A = list(map(int, input().split()))

ans = []
for i in range(N - 1):
    if A[i + 1] - A[i] >= 2:
        ans.extend(list(range(A[i], A[i + 1])))
    elif A[i + 1] - A[i] <= -2:
        ans.extend(list(range(A[i], A[i + 1], -1)))
    else:
        ans.append(A[i])

ans.append(A[-1])

print(*ans)
