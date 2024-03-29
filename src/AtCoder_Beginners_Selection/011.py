N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

pre_t, pre_x, pre_y = 0, 0, 0
for t, x, y in A:
    if abs((x - pre_x)) + abs((y - pre_y)) > t - pre_t:
        print("No")
        exit()
    elif ((x - pre_x) + (y - pre_y)) % 2 != (t - pre_t) % 2:
        print("No")
        exit()
    else:
        pre_t, pre_x, pre_y = t, x, y
else:
    print("Yes")
