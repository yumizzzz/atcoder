import itertools
import math
import sys
from bisect import bisect_left, bisect_right
from collections import Counter
from itertools import combinations, product

input = sys.stdin.readline

# 入力-------------------------------------------------------------------

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

# 縦方向に並んだN個の整数を受け取るとき
N = int(input())
A = [int(input()) for _ in range(N)]

# 行列の入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 行列を分けて受け取る
N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# H行W列の行列を受け取る. indexは[行][列]
H, W = map(int, input().split())
A = [["."] * W for _ in range(H)]


# 便利文法----------------------------------------------------------------

# リストの要素をスペース区切りで出力
print(*A)

# 空白区切りで出力
print("a", end=" ")

# 高速文字変換
d = {"a": "A", "b": "B"}
S.translate(str.maketrans(d))

# 文字数カウント
S = "aaabbc"
S.count("a")  # 3
s_count = Counter(S)  # Counter({'a': 3, 'b': 2, 'c': 1})

# 最小公約数
math.gcd(4, 6)
# 最小公倍数
math.lcm(4, 6)
# 備忘: 元の2数の積は最小公倍数と最大公約数の積に等しい
# 感覚的には → https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10199287735

# 累積和
list(itertools.accumulate(A))

# 順列/組合せ ------------------------------------------------------------

# 組合せの数を計算. 以下5C2の場合
math.comb(5, 2)

# 組合せの列挙
combinations(A, 2)

# 直積集合. N**3通り
product(range(N), repeat=3)

# 階乗
math.factorial(N)

# 探索 -------------------------------------------------------------------

# bit全探索. 直積集合
product([0, 1], repeat=3)  # (0, 0, 0), (0, 0, 1), (0, 1, 0), ...

# 二分探索
# https://amateur-engineer-blog.com/python-bisect
A.sort()
bisect_left(A, N)  # Nが挿入できる最初のindex
bisect_right(A, N)  # Nが挿入できる最後のindex


# 進数変換 ---------------------------------------------------------------
def from_n_to_10(number: str | int, n: int) -> int:
    """numberをbase進法から10進法に変換"""
    return int(str(number), n)


def from_10_to_n(number: str | int, n: int) -> int:
    """10進法をn進法に変換"""
    number = int(number)
    if number == 0:
        return 0
    new_number = ""
    while number > 0:
        new_number += str(number % n)
        number //= n
    return int(new_number[::-1])


# ランレングス圧縮 ---------------------------------------------------------
def runLengthEncode(S: str) -> list[tuple[str, int]]:
    """ランレングス圧縮. "aabbbbaac" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1)]"""
    from itertools import groupby

    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


# 切り上げ除算 -----------------------------------------------------------
def divide_round_up(a: int, b: int) -> int:
    """切り上げ除算
    https://atcoder.jp/contests/abc345/editorial
    """
    return (a + b - 1) // b
