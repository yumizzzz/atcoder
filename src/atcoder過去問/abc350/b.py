N, Q = map(int, input().split())
T = list(map(int, input().split()))

ls = [True] * N

for t in T:
    ls[t - 1] = not ls[t - 1]

print(sum(ls))
