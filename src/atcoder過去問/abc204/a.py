a, b = map(str, input().split())

ls = ["0", "1", "2"]

if a == b:
    print(a)
else:
    ls.remove(a)
    ls.remove(b)
    print(ls[0])
