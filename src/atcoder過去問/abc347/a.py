N, K = map(int, input().split())
A = list(map(int, input().split()))

ls = []
for a in A:
    if a % K == 0:
        ls.append(a // K)

ls.sort()
print(*ls)
