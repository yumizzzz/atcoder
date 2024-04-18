H, W = map(int, input().split())
A = [list(str(input())) for _ in range(H)]
B = [list(str(input())) for _ in range(H)]

for dh in range(H):
    for dw in range(W):
        flag = True
        for h in range(H):
            for w in range(W):
                if A[(h + dh) % H][(w + dw) % W] != B[h][w]:
                    flag = False

        if flag:
            print("Yes")
            exit()
else:
    print("No")
