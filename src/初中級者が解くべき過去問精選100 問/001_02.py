from itertools import combinations

n, x = map(int, input().split())

if n == 0 and x == 0:
    exit()

ans = 0

# 全組合せを列挙
for c in list(combinations(range(1, n + 1), 3)):
    if sum(c) == x:
        ans += 1
    # print(c)

print(ans)
