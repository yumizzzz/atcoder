N = int(input())
A, B, C = map(int, input().split())

# 9999以下という条件があるので全探索可能

ans = 10**9
max_coins = 10000

for i in range(max_coins):  # A
    for j in range(max_coins):  # B
        z = N - A * i - B * j
        if z < 0:
            continue
        elif z == 0:
            ans = min(ans, i + j)
        elif z % C == 0:
            k = z // C
            ans = min(ans, i + j + k)

print(ans)
