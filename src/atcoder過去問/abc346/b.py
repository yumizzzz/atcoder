W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * 100
N = W + B

for i in range(len(S)):
    s = S[i : i + N]
    if s.count("w") == W and s.count("b") == B:
        print("Yes")
        break
else:
    print("No")
