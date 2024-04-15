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
    return str(new_number[::-1])


s = from_10_to_n(N, 2)
s = s[::-1]

count = 0
for i in range(len(s)):
    if s[i] != "0":
        break
    count += 1

print(count)
