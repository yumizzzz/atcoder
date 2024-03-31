N = int(input())

data = []
for _ in range(N):
    s, t = map(str, input().split())
    data.append([int(t), s])

data.sort()
print(data[-2][1])
