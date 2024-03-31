H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

count = 0
for h in range(H - 1):
    for w in range(W - 1):
        diff = A[h][w] - B[h][w]
        count += abs(A[h][w] - B[h][w])
        A[h][w + 1] -= diff
        A[h + 1][w] -= diff
        A[h + 1][w + 1] -= diff

    if A[h][-1] != B[h][-1]:
        print("No")
        exit()

print("Yes")
print(count)
