S = str(input())
S = S[::-1]

words = ["dream", "dreamer", "erase", "eraser"]
words = [word[::-1] for word in words]

while len(S) > 0:
    for word in words:
        if S.startswith(word):
            S = S[len(word) :]
            break
    else:
        print("NO")
        exit()

print("YES")
