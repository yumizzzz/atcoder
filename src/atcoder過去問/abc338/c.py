N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for a in range(max(Q) + 1):
    y = []
    for i in range(N):
        if Q[i] < A[i] * a:
            break
        elif B[i] == 0:
            continue
        else:
            y.append((Q[i] - A[i] * a) // B[i])
    else:
        min_y = min(y) if y else 0
        ans = max(ans, a + min_y)

print(ans)
