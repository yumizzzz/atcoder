A, B, C, D = map(int, input().split())

# 不等式を作成すればOK

if C * D - B <= 0:
    print(-1)
    exit()

n = A / (C * D - B)

if n % 1 == 0:
    print(int(n))
else:
    print(int(n) + 1)
