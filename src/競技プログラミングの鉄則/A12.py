N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 1
right = 10**9

while left < right:
    mid = (left + right) // 2

    papers = sum([mid // a for a in A])

    if papers >= K:
        right = mid
    else:
        left = mid + 1

print(left)
