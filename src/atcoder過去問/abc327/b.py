B = int(input())

for a in range(1, B + 1):
    v = pow(a, a)
    if v > B:
        print(-1)
        exit()
    elif v == B:
        print(a)
        exit()
