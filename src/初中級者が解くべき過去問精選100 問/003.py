S = str(input())

ans = 0
cnt = 0

# 1文字ずつ見ていく. 文字がACGTならカウントを増やし, それ以外ならカウントを0に戻す
for c in S:
    if c in "ACGT":
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)
