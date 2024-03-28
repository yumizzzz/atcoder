N = int(input())
A = list(map(int, input().split()))

ls = []
for i in range(N - 1):
  ls.append(A[i] * A[i + 1])

print(*ls)
