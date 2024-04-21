from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]

A.sort()

for x in X:
    ans = bisect_left(A, x)
    print(ans)
