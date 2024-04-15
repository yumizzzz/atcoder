N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

money_dict = {}
for d, p in zip(D, P[1:]):
    money_dict[d] = p

ans = 0
for c in C:
    if c in money_dict:
        ans += money_dict[c]
    else:
        ans += P[0]

print(ans)
