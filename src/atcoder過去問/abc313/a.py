N = int(input())
P = list(map(int, input().split()))

max_p = max(P[1:])
print(max(0, max_p - P[0] + 1))
