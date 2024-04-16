H, M = list(map(int, input().split()))

while True:
    a, b, c, d = H // 10, H % 10, M // 10, M % 10
    new_hour = a * 10 + c
    new_min = b * 10 + d

    if 0 <= new_hour < 24 and 0 <= new_min < 60:
        print(a * 10 + b, c * 10 + d)
        exit()

    if M == 59:
        if H == 23:
            H = 0
        else:
            H += 1
        M = 0
    else:
        M += 1
