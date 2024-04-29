N = int(input())
A = list(map(int, input().split()))

a0 = A[0]

for i in range(1, N):
    if A[i] != a0:
        print("No")
        break
else:
    print("Yes")
