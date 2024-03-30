from itertools import product

N = int(input())

if N % 2 == 1:
    exit()

# 0 -> "(" , 1 -> ")"
for bit in product([0, 1], repeat=N):
    # 0と1の数が等しいか
    if bit.count(0) != bit.count(1):
        continue

    # i番目までにおいて, 0の数>=1の数か確認
    count_zero = 0
    count_one = 0
    for i in bit:
        if i == 0:
            count_zero += 1
        else:
            count_one += 1
        if count_one > count_zero:
            break
    else:
        ans = "".join(["(" if x == 0 else ")" for x in bit])
        print(ans)
