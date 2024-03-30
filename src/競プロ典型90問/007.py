from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    x = bisect_left(A, b)
    if x == 0:
        print(A[0] - b)
    elif x == N:
        print(b - A[-1])
    else:
        print(min(A[x] - b, b - A[x - 1]))
