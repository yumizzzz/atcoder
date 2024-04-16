N = int(input())
S = str(input())

ls = S.split('"')
for i in range(len(ls)):
    if i % 2 == 0:
        ls[i] = ls[i].replace(",", ".")

print('"'.join(ls))
