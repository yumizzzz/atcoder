from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# forループの中でcountをしない. countはo(n)操作なので
A_counter = Counter(A)
C_counter = Counter(C)

count = 0
for i in range(N):
    a_count = A_counter[B[i]]
    if a_count == 0:
        continue
    count += C_counter[i + 1] * a_count

print(count)
