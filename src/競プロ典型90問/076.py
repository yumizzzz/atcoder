import itertools
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
# 入力は整数のみなので, 10で割り切れない場合は1/10を取ることはできない
if sum(A) % 10 != 0:
    exit(print("No"))

target = sum(A) // 10

# 2周分作成
A2 = A + A[:-2]

# 累積和作成
cumsum = list(itertools.accumulate(A2))

for i in range(len(A2)):
    # 10で割り切れる場合(0番目からの累積和がtargetと等しい場合)
    if cumsum[i] == target:
        print("Yes")
        exit()

    # 累積和がtargetを超える場合 -> target = cumsum[i] - cumsum[j] となるようなjを探したい
    # cumsum[j]に最も近い値を2分探索で探し、実際にそれが求めるcumsum[j]かどうかを確認する
    elif cumsum[i] > target:
        cumsum_j = cumsum[i] - target
        j = bisect_left(cumsum, cumsum_j)
        if cumsum[j] == cumsum_j:
            print("Yes")
            exit()
else:
    print("No")
