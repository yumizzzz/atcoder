N = int(input())

# 1組, 2組で分けて得点を格納する
c1 = [] * N
c2 = [] * N
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        c1[i] = p
    else:
        c2[i] = p

# 累積和を取る
s1 = [0] * (N + 1)
s2 = [0] * (N + 1)

for i in range(N):
    s1[i + 1] = s1[i] + c1[i]
    s2[i + 1] = s2[i] + c2[i]

Q = int(input())

for _ in range(Q):
    ll, r = map(int, input().split())
    sum_01 = s1[r] - s1[ll - 1]
    sum_02 = s2[r] - s2[ll - 1]
    print(sum_01, sum_02)
