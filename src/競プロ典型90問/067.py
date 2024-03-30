N, K = map(int, input().split())


def from_n_to_10(number: str | int, n: int) -> int:
    """numberをbase進法から10進法に変換"""
    return int(str(number), n)


def from_10_to_n(number: str | int, n: int) -> int:
    """10進法をn進法に変換"""
    number = int(number)
    if number == 0:
        return 0
    new_number = ""
    while number > 0:
        new_number += str(number % n)
        number //= n
    return int(new_number[::-1])


for _ in range(K):
    num10 = from_n_to_10(N, 8)
    num9 = from_10_to_n(num10, 9)
    N = str(num9).replace("8", "5")

print(N)
