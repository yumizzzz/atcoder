N = int(input())

# x**3 + x = N and N < 10**6の関係より, x < 100とわかる
# またxは100以下であるため, 二分探索で整数を求めるためには, 100回程度の繰り返しでOK

left = 0
right = 100

for _ in range(100):
    x = (left + right) / 2
    y = x**3 + x

    if y >= N:
        right = x
    else:
        left = x

print(left)
