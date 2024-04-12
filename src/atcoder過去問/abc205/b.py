N = int(input())
A = list(map(int, input().split()))

if min(A) == 1 and max(A) == N and len(A) == N:
    print("Yes")
else:
    print("No")
