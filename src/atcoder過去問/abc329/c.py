from collections import defaultdict

N = input()
S = input()


def runLengthEncode(S: str) -> list[tuple[str, int]]:
    """ランレングス圧縮. "aabbbbaac" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1)]"""
    from itertools import groupby

    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


s_counter = runLengthEncode(S)

d = defaultdict(int)
for v in s_counter:
    s, count = v
    d[s] = max(d[s], count)

print(sum(d.values()))
