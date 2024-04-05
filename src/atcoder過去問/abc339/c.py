N = int(input())
A = list(map(int, input().split()))

s = 0

# 乗客数が負にならないことを利用して計算
for a in A:
    s = max(s + a, 0)

print(s)
