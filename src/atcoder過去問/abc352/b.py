S = str(input())
T = str(input())

ans = []
for i in range(len(T)):
    if T[i] == S[0]:
        S = S[1:]
        ans.append(i + 1)

print(*ans)
