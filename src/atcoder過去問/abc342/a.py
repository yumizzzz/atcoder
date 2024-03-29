from collections import Counter

S = str(input())

s_count = Counter(S)

for i in range(len(S)):
    if s_count[S[i]] == 1:
        print(i + 1)
        exit()
