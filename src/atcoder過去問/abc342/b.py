N = int(input())
P = list(map(int, input().split()))
Q = int(input())
A = [list(map(int, input().split())) for _ in range(Q)]

p_dict = {p: i + 1 for i, p in enumerate(P)}
for i in range(Q):
    a, b = A[i]
    if p_dict[a] < p_dict[b]:
        print(a)
    else:
        print(b)
