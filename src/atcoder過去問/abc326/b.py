N = int(input())

for i in range(N, 920):
    number100 = i // 100
    number10 = (i % 100) // 10
    number1 = i % 10

    if number100 * number10 == number1:
        print(i)
        break
