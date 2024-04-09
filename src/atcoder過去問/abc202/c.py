from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# forループの中でcountをしない. countはo(n)操作なので
A_counter = Counter(A)
C_counter = Counter(C)

# bを軸にしてaとcの数を数える
ans = 0
for i in range(N):
    a_count = A_counter[B[i]]
    c_count = C_counter[i + 1]
    ans += a_count * c_count

print(ans)
