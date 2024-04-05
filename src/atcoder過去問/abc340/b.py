Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

A = []
for q in query:
    if q[0] == 1:
        A.append(q[1])
    else:
        print(A[-q[1]])
