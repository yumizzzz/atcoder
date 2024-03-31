N, K = map(int, input().split())

AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

ab_dict = {a: 0 for a, b in AB}
for a, b in AB:
    ab_dict[a] += b
AB = [[a, ab_dict[a]] for a in ab_dict]
AB.sort()

pre_i = 0
for i in range(len(AB)):
    diff = K - (AB[i][0] - pre_i)
    if diff >= 0:
        K -= AB[i][0] - pre_i
        K += AB[i][1]
        pre_i = AB[i][0]
    else:
        print(pre_i + K)
        exit()
else:
    print(AB[-1][0] + K)
