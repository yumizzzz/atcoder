N, Y = map(int, input().split())

for n1 in range(N + 1):
    for n2 in range(N + 1 - n1):
        n3 = N - n1 - n2
        if 10000 * n1 + 5000 * n2 + 1000 * n3 == Y:
            print(n1, n2, n3)
            exit()

print(-1, -1, -1)
