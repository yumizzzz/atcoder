N, K = map(int, input().split())
S = [str(input()) for _ in range(N)]

S = S[:K]
S.sort()

for s in S:
    print(s)
