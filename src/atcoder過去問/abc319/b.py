N = int(input())

ls = set()
for i in range(1, 10):
    if N % i == 0:
        ls.add(i)

ans = ""
for i in range(N + 1):
    for j in ls:
        if i % (N // j) == 0:
            ans += str(j)
            break
    else:
        ans += "-"

print(ans)
