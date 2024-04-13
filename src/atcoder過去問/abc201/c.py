S = str(input())

M_set = set()
B_set = set()

# "o"の番号と"x"の番号をそれぞれ集合に格納
for i in range(10):
    if S[i] == "o":
        M_set.add(i)
    elif S[i] == "x":
        B_set.add(i)

count = 0
for i in range(10000):
    s = set(map(int, str(i).zfill(4)))

    # 4桁の数字のうち, "o"の番号が全て含まれている & "x"の番号が含まれていない
    if s & M_set == M_set and s & B_set == set():
        count += 1

print(count)
