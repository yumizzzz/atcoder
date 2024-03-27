A, B, C, X, Y = map(int, input().split())

ans1 = A * X + B * Y
ans2 = 2 * C * min(X, Y) + A * max(0, X - Y) + B * max(0, Y - X)
ans3 = 2 * C * max(X, Y)

print(min(ans1, ans2, ans3))
