A, B, C, D = map(int, input().split())


def divide_round_up(a: int, b: int) -> int:
    """切り上げ除算
    https://atcoder.jp/contests/abc345/editorial
    """
    return (a + b - 1) // b


if C * D - B <= 0:
    print(-1)
    exit()

print(divide_round_up(A, C * D - B))
