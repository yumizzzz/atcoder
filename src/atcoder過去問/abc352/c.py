N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: x[1] - x[0])

print(sum([x[0] for x in AB[:-1]]) + AB[-1][1])
