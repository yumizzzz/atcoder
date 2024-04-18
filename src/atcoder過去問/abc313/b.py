N, M = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

s = set(range(1, N + 1))

# 全員を最強候補として, 負けた人を除外していく
for b in B:
    s.discard(b)

if len(s) == 1:
    print(s.pop())
else:
    print(-1)
