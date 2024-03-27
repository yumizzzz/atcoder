N = int(input())
S = str(input())

ans = 0
for i in range(1000):
    number = str(i).zfill(3)
    if S.find(number[0]) == -1:
        continue
    S1 = S[S.find(number[0]) + 1 :]
    if S1.find(number[1]) == -1:
        continue
    S2 = S1[S1.find(number[1]) + 1 :]
    if S2.find(number[2]) == -1:
        continue
    ans += 1

print(ans)
