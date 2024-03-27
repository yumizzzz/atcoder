H, W = map(int, input().split())

A = []
for i in range(H):
    array = list(map(int, input().split()))
    A.append(array)

# 行の合計
row = []
for i in range(H):
    sum = 0
    for j in range(W):
        sum += A[i][j]
    row.append(sum)

# 列の合計
col = []
for j in range(W):
    sum = 0
    for i in range(H):
        sum += A[i][j]
    col.append(sum)

# 出力
for i in range(H):
    for j in range(W):
        print(row[i] + col[j] - A[i][j], end=" ")
    print()
