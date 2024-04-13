S = str(input())
T = str(input())

t = T.lower()
step = 0

for i in range(len(S)):
    if step == 2 and T[2] == "X":
        print("Yes")
        exit()
    if t[step] == S[i]:
        if step == 2:
            print("Yes")
            exit()
        else:
            step += 1

if step == 2 and T[2] == "X":
    print("Yes")
else:
    print("No")
