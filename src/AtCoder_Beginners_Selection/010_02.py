S = str(input())

# 順番大事. dreamerとeraseの関係からeraseを先に消す
S = S.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")

if len(S) == 0:
    print("YES")
else:
    print("NO")
