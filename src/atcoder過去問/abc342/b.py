N = int(input())
P = list(map(int, input().split()))
Q = int(input())
AB = [list(map(int, input().split())) for _ in range(Q)]

for a, b in AB:
    if P.index(a) < P.index(b):
        print(b)
    else:
        print(a)
