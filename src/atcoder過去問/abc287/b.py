N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]
T = [str(input()) for _ in range(M)]

ans = 0
for s in S:
    for t in T:
        if s[-3:] == t:
            ans += 1
            break

print(ans)
