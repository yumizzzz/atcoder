H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(H):
    ans = []
    for j in range(W):
        if A[i][j] == 0:
            print(".", end="")
        else:
            print(word[A[i][j] - 1], end="")
    print()
