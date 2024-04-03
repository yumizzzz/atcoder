"""
Kの数が大きいため, for文で全探索して合計を求めるとTLEになる
なので数式を使ってまずは全合計を出し, 数が少ないAの数でfor分を回して引いていく
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

all_sum = K * (K + 1) // 2

for a in set(A):
    if a <= K:
        all_sum -= a

print(all_sum)
