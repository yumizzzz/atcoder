N = int(input())
W, X = [], []
for i in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans = 0
for i in range(0, 24):
    count = 0
    for w, x in zip(W, X):
        if 9 <= (i + x) % 24 <= 17:
            count += w

    ans = max(ans, count)

print(ans)
