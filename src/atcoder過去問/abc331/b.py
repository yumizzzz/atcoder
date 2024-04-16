N, S, M, L = map(int, input().split())

ans = 10 * 8
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            if 6 * i + 9 * j + 20 * k >= N:
                ans = min(ans, S * i + M * j + L * k)

print(ans)
