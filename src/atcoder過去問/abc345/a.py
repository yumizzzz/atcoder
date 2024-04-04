S = str(input())

if S[0] != "<":
    print("No")
elif S[-1] != ">":
    print("No")
elif S[1:-1].count("=") != len(S[1:-1]):
    print("No")
else:
    print("Yes")
