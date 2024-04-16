N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
A.sort()

for a in A[::-1]:
    if a != max_a:
        print(a)
        break
