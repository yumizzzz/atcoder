N = int(input())


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


print(str(from_10_to_n(N, 2)).zfill(10))
