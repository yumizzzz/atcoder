N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(M):
            if S[i][k] == "o" or S[j][k] == "o":
                continue
            else:
                break
        else:
            count += 1

print(count)
