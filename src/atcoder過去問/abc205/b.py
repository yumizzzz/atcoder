N = int(input())
A = list(map(int, input().split()))

a = list(set(A))
a.sort()

if min(a) == 1 and max(a) == N and len(a) == N:
    print("Yes")
else:
    print("No")
