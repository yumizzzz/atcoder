import sys
from math import gcd

input = sys.stdin.readline
A, B, C = map(int, input().split())

# 最小公倍数
d = gcd(gcd(A, B), C)

ans = (A // d) - 1 + (B // d) - 1 + (C // d) - 1

print(ans)
