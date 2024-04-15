S = input()

if len(S) != 8:
    print("No")
    exit()

if not S[0].isupper():
    print("No")
elif not S[-1].isupper():
    print("No")
elif not S[1:-1].isdecimal():
    print("No")
elif 100000 <= int(S[1:-1]) <= 999999:
    print("Yes")
else:
    print("No")
