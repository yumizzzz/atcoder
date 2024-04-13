from itertools import combinations

N = int(input())
TLR = [list(map(int, input().split())) for _ in range(N)]


def get_min_max(tlr):
    T, L, Y = tlr
    if T == 1:
        return L, Y
    elif T == 2:
        return L, Y - 0.1
    elif T == 3:
        return L + 0.1, Y
    else:
        return L + 0.1, Y - 0.1


count = 0
for a, b in combinations(range(N), 2):
    tlr01 = TLR[a]
    tlr02 = TLR[b]

    min1, max1 = get_min_max(tlr01)
    min2, max2 = get_min_max(tlr02)

    if max(min1, min2) <= min(max1, max2):
        count += 1

print(count)
