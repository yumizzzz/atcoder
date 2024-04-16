from collections import defaultdict

N = int(input())
C = []
A = []
for i in range(N):
    c = int(input())
    a = list(map(int, input().split()))
    C.append(c)
    A.append(a)
X = int(input())

d = defaultdict(set)

for i in range(N):
    for a in A[i]:
        d[a].add(i)

x_list = [C[i] for i in d[X]]
min_x = min(x_list)

ans = set()
for i in d[X]:
    if C[i] == min_x:
        ans.add(i + 1)

print(len(ans))
print(*ans)
