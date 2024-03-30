N, A, B = map(int, input().split())
D = list(map(int, input().split()))

week = A + B
new_D = []
for d in D:
    day_in_week = d % week
    new_D.append(day_in_week)
new_D.sort()
new_D.append(new_D[0] + week)

for i in range(N):
    if new_D[i + 1] - new_D[i] > B:
        print("Yes")
        exit()
else:
    print("No")
