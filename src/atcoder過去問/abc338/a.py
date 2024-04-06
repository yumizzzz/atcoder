S = str(input())

if not S[0].isupper():
    print("No")
elif len(S) >= 2 and not S[1:].islower():
    print("No")
else:
    print("Yes")


# print("Yes" if S.istitle() else "No")
