from collections import Counter

S = str(input())

S_count = Counter(S)
max_count = max(S_count.values())

for s in "abcdefghijklmnopqrstuvwxyz":
    if S_count[s] == max_count:
        ans = s
        break

print(ans)

