from math import atan2, cos, pi, sin, sqrt

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

for e in E:
    upper = (L / 2) * (1 - cos(2 * pi * e / T))
    lower_part = Y + L / 2 * sin(2 * pi * e / T)
    lower = sqrt(X**2 + lower_part**2)

    angle = atan2(upper, lower)
    print(angle * 180 / pi)
