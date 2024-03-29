N = int(input())
S = str(input())
Q = int(input())
CD = [list(map(str, input().split())) for _ in range(Q)]

word = "abcdefghijklmnopqrstuvwxyz"
new_word = "abcdefghijklmnopqrstuvwxyz"

for i in range(Q):
    c, d = CD[i]
    new_word = new_word.replace(c, d)

converr_dict = dict(zip(word, new_word))
print(S.translate(str.maketrans(converr_dict)))
