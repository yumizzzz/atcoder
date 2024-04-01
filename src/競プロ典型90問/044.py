N, Q = map(int, input().split())
A = list(map(int, input().split()))
TXY = [list(map(int, input().split())) for _ in range(Q)]

shift = 0
for t, x, y in TXY:
    # indexを修正
    X, Y = x - 1, y - 1

    # 今のX,Yの値が最初の状態でどの位置だったか
    X = (X - shift) % N
    Y = (Y - shift) % N

    if t == 1:
        A[X], A[Y] = A[Y], A[X]
    elif t == 2:
        shift += 1
        shift %= N
    else:
        print(A[X])
