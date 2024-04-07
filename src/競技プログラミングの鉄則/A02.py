N, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

for a in A:
    if a == X:
        print("Yes")
        break
else:
    print("No")
