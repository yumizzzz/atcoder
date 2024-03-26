N = int(input())


# とある数字nに対して全探索
def having_eight_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 8


ans = 0

# N以下の奇数に対して全探索
for n in range(1, N + 1, 2):
    if having_eight_divisors(n):
        ans += 1

print(ans)
