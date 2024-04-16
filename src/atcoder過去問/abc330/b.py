N, L, R = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    a = A[i]
    if L > a:
        print(L, end=" ")
    elif L <= a <= R:
        print(a, end=" ")
    else:
        print(R, end=" ")
