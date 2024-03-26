from itertools import combinations

N, M = map(int, input().split())

A = []
for n in range(N):
    a = list(map(int, input().split()))
    A.append(a)

max_score = 0

for m1, m2 in combinations(range(M), 2):
    score = 0
    for a in A:
        score += max(a[m1], a[m2])
    max_score = max(max_score, score)

print(max_score)
