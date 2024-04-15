N = int(input())
S = [str(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        word = S[i] + S[j]
        if word == word[::-1]:
            print("Yes")
            exit()
else:
    print("No")
