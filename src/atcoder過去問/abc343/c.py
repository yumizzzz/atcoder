N = int(input())

ans = 0
for i in range(1, N + 1):
    a = i**3

    if a > N:
        break

    if str(a) == str(a)[::-1]:
        ans = a

print(ans)
