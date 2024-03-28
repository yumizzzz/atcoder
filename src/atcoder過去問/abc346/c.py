N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_k = (K * (K + 1)) // 2

A = set(A)
sum_a = sum([a for a in A if a <= K])

print(sum_k - sum_a)
