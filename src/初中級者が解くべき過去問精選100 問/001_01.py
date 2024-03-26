n, x = map(int, input().split())

if n == 0 and x == 0:
    exit()

ans = 0

# i < j < k となるようにループを回す
for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n + 1):
            if i + j + k == x:
                ans += 1
print(ans)
