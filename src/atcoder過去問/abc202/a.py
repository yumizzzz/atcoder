S = str(input())

d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

S = S[::-1]
print(S.translate(str.maketrans(d)))
