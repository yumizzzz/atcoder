"""
最終的には解けるが, for文の範囲に毎回悩むので...
指定の範囲は1 ≤ i ≤ N−1なので, 0indexスタートで考えると0 ≤ i ≤ N-2となる
range(N)は0 ≤ i < N-1までの範囲なので, 0 ≤ i ≤ N-2を処理したい時はrange(N-1)を使う
"""

N = int(input())
A = list(map(int, input().split()))

ls = []
for i in range(N - 1):
    ls.append(A[i] * A[i + 1])

print(*ls)
