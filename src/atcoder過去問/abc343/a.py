A, B = map(int, input().split())

if A + B == 0:
    print(1)
else:
    print(0)

# 以下でもOK
# print((A + B + 1) % 10)
