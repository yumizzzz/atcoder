N = int(input())
A = []
for i in range(N):
    array = list(map(int, input().split()))
    A.append(array)


for a in A:
    for i in range(len(a)):
        if a[i] == 1:
            print(i + 1, end=" ")
    print()
