import sys

input = sys.stdin.readline

# 入力-------------------------------------

# 文字列/整数の入力
S = str(input())
N = int(input())
X = float(input())

# リストとして受け取る
S = input().split()

# 1行に決まった数の整数
A, B = map(int, input().split())

# 1行に複数の整数が入力される場合に, リストとして受け取る
N = int(input())
A = list(map(int, input().split()))

# N個の整数を受け取るとき
N = int(input())
A = [int(input()) for _ in range(N)]

# 行列の入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 便利文法---------------------------------

# リストの要素をスペース区切りで出力
print(*A)

# 空白区切りで出力
print("a", end=" ")

# 高速文字変換
d = {"a": "A", "b": "B"}
S.translate(str.maketrans(d))

# 便利関数---------------------------------

import math
from collections import Counter

# 文字数カウント
S = "aaabbc"
S.count("a")
# 3
s_count = Counter(S)
# Counter({'a': 3, 'b': 2, 'c': 1})

# 組合せの数を計算. 以下5C2の場合
math.comb(5, 2)


from itertools import combinations

# 組合せの列挙
combinations(A, 2)
