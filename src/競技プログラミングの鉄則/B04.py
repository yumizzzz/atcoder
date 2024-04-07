N = int(input())


def from_n_to_10(number: str | int, n: int) -> int:
    """numberをbase進法から10進法に変換"""
    return int(str(number), n)


print(from_n_to_10(N, 2))
