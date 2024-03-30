N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 貪欲法
# https://algo-method.com/descriptions/95

A.sort()
B.sort()

sum = 0
for a, b in zip(A, B):
    sum += abs(a - b)

print(sum)
