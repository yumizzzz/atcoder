from collections import Counter, defaultdict

S = str(input())

s_counter = Counter(S)
d = defaultdict(int)

for count in s_counter.values():
    d[count] += 1

for k, v in d.items():
    if v != 2 and v != 0:
        print("No")
        exit()
else:
    print("Yes")
