N = int(input())
S = [str(input()) for _ in range(N)]

for s in S:
    if s[0] not in ["H", "D", "C", "S"]:
        print("No")
        exit()
    elif s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        print("No")
        exit()

if len(set(S)) != N:
    print("No")
else:
    print("Yes")
