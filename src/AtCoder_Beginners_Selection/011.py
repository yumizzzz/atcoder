N = int(input())

T, X, Y = [], [], []
for n in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

pre_t, pre_x, pre_y = 0, 0, 0
for t, x, y in zip(T, X, Y):
    if abs(x - pre_x) + abs(y - pre_y) > t - pre_t:
        print("No")
        exit()
    elif (x + y) % 2 != t % 2:
        print("No")
        exit()
    else:
        pre_t, pre_x, pre_y = t, x, y

print("Yes")
