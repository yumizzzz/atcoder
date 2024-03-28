import math
from collections import Counter

S = str(input())
s_count = Counter(S)

ans = math.comb(len(S), 2)

for _, count in s_count.items():
    if count > 1:
        ans -= math.comb(count, 2)

# 重複を考慮して差し引きした際, S自体を作れる場合も削除されているので補完
if max(s_count.values()) > 1:
    ans += 1

print(ans)
