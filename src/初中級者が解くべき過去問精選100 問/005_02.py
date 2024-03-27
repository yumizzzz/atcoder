A, B, C, X, Y = map(int, input().split())

ans = float("inf")
for i in range(max(X, Y) + 1):
    price = 2 * C * i + A * max(0, X - i) + B * max(0, Y - i)
    ans = min(ans, price)

print(ans)
