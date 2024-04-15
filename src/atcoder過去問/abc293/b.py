N = int(input())
A = list(map(int, input().split()))

# Listを使うとTLEになる

s = set(range(1, N + 1))

for i in range(1, N + 1):
    if i in s and A[i - 1] in s:
        s.remove(A[i - 1])

print(len(s))
print(*s)
