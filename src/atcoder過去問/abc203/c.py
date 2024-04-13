from collections import defaultdict

N, K = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

d = defaultdict(int)
for i in range(N):
    d[A[i]] += B[i]


ans = 0
for i, v in sorted(d.items()):
    if K - (i - ans) < 0:
        print(K + ans)
        exit()

    K -= i - ans
    K += v
    ans = i

print(K + ans)
