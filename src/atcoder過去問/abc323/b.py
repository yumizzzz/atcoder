from collections import defaultdict

N = int(input())
S = [str(input()) for _ in range(N)]

d = defaultdict(list)
for i in range(N):
    score = S[i].count("o")
    d[score].append(i + 1)

d = sorted(d.items(), reverse=True)
ans = []
for score, indexes in d:
    ans.extend(sorted(indexes))

print(*ans)
