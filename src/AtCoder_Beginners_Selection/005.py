N, A, B = map(int, input().split())

ans = 0
for n in range(N + 1):
    sum_numebr = sum([int(i) for i in str(n)])
    if A <= sum_numebr <= B:
        ans += n

print(ans)
