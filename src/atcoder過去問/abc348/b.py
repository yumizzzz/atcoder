N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    max_distance = 0
    max_idx = 0

    for j in range(N):
        if i == j:
            continue

        distance = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5
        if distance > max_distance:
            max_distance = distance
            max_idx = j + 1

    print(max_idx)
