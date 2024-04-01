N, K = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append(a - b)
    AB.append(b)

AB.sort()

ans = 0
for i in range(K):
    ans += AB.pop()

print(ans)
