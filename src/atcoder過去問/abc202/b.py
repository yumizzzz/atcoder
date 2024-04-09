S = str(input())

S = S[::-1]

# 以下の方法だと一気に変換できる
d = {"6": "9", "9": "6"}
S = S.translate(str.maketrans(d))

print(S)
