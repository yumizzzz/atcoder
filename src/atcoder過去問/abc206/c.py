from collections import Counter

N = int(input())
A = list(map(int, input().split()))

all = N * (N - 1) // 2
A_count = Counter(A)
for k, v in A_count.items():
    if v >= 2:
        all -= v * (v - 1) // 2

print(all)
