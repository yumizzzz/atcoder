N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]

for h in range(N - 8):
    s = S[h : h + 9]
    for w in range(M - 8):
        if s[0][w : w + 4] != "###.":
            continue
        elif s[1][w : w + 4] != "###.":
            continue
        elif s[2][w : w + 4] != "###.":
            continue
        elif s[3][w : w + 4] != "....":
            continue
        elif s[5][w + 5 : w + 9] != "....":
            continue
        elif s[6][w + 5 : w + 9] != ".###":
            continue
        elif s[7][w + 5 : w + 9] != ".###":
            continue
        elif s[8][w + 5 : w + 9] != ".###":
            continue
        else:
            print(h + 1, w + 1)
