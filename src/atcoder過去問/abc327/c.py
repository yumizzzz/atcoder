A = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    if len(set(A[i])) != 9:
        print("No")
        exit()

for i in range(9):
    if len(set([A[j][i] for j in range(9)])) != 9:
        print("No")
        exit()

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        if len(set([A[i + k][j + l] for k in range(3) for l in range(3)])) != 9:
            print("No")
            exit()

print("Yes")
