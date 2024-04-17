H, W = map(int, input().split())
S = [str(input()) for _ in range(H)]

direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
word = "snuke"

for h in range(H):
    for w in range(W):
        if S[h][w] != "s":
            continue

        move_h = h
        move_w = w

        for d in direction:
            ans = []
            for k in range(5):
                if 0 <= move_h < H and 0 <= move_w < W and S[move_h][move_w] == word[k]:
                    ans.append([move_h, move_w])
                    move_h += direction[d][0]
                    move_w += direction[d][1]
                else:
                    break

            if len(ans) == 5:
                for w in range(5):
                    print(ans[w][0] + 1, ans[w][1] + 1)
