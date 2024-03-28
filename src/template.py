import sys

input = sys.stdin.readline


# 文字列の入力
S = str(input())

# 整数の入力
N = int(input())

# 少数の入力
x = float(input())

# リストとして受け取る
S = input().split()

# 1行に決まった数の整数
a, b = map(int, input().split())

# 1行に複数の整数が入力される場合に, リストとして受け取る
N = int(input())
A = list(map(int, input().split))

# 行列の入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
