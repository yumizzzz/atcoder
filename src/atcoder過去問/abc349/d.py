L, R = map(int, input().split())

ans = []

while L != R:
    i = 0

    # l=(2^i)*j, r=L+(2^i)と表現できることを利用
    while L % pow(2, i + 1) == 0 and L + pow(2, i + 1) <= R:
        i += 1
    r = L + pow(2, i)
    ans.append([L, r])
    L = r

print(len(ans))
for lr in ans:
    print(*lr)
