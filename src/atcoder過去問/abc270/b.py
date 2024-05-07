X, Y, Z = map(int, input().split())

if Y < 0:
    X, Y, Z = -X, -Y, -Z

if X < Y:
    print(abs(X))
elif Y < X and Y < Z:
    print(-1)
else:
    print(abs(Z) + abs(X - Z))
