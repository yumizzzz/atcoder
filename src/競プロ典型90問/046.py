from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = [a % 46 for a in A]
B = [b % 46 for b in B]
C = [c % 46 for c in C]

A_count = Counter(A)
B_count = Counter(B)
C_count = Counter(C)

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += A_count[i] * B_count[j] * C_count[k]

print(ans)
