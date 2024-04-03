W, B = map(int, input().split())

S = "wbwbwwbwbwbw"
S_LONG = S * 100

# Sの文字列の中からスタートする位置を探索. range(len(S_LONG))ではない!
for i in range(len(S)):
    s = S_LONG[i : i + W + B]
    if s.count("w") == W and s.count("b") == B:
        print("Yes")
        break
else:
    print("No")
