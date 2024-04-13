from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
ans = N * (N - 1) // 2

for v in counter.values():
    ans -= v * (v - 1) // 2

print(ans)
