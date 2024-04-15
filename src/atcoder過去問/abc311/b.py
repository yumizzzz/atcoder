N, D = map(int, input().split())
S = [str(input()) for _ in range(N)]

ans = 0
count = 0
for d in range(D):
    for i in range(N):
        if S[i][d] != "o":
            count = 0
            break
    else:
        count += 1
        ans = max(ans, count)

print(ans)
