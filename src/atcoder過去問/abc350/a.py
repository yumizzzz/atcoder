S = str(input())

if len(S) != 6:
    print("No")
elif S[:3] != "ABC":
    print("No")
elif 1 <= int(S[3:]) <= 349 and int(S[3:]) != 316:
    print("Yes")
else:
    print("No")
