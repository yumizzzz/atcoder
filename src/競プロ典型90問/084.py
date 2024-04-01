N = int(input())
S = str(input())


def runLengthEncode(S: str) -> list[tuple[str, int]]:
    """ランレングス圧縮. "aabbbbaac" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1)]"""
    from itertools import groupby

    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


rle = runLengthEncode(S)

# 連続する文字列の取り方
rle_sum = 0
for s, cnt in rle:
    rle_sum += cnt * (cnt - 1) // 2

# 全ての文字列の取り方
all_sum = N * (N - 1) // 2

# 余事象
print(all_sum - rle_sum)
