N = int(input())
S = [str(input()) for _ in range(N)]

U = set()
for i in range(N):
    if S[i] in U:
        continue
    else:
        U.add(S[i])
        print(i + 1)
