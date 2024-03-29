from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

new_A = [a % P for a in A]

ans = 0
for a, b, c, d, e in combinations(new_A, 5):
    if (a * b * c * d * e) % P == Q:
        ans += 1

print(ans)
