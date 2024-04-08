N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

# 累積和
atari = [0] * (N + 1)
hazure = [0] * (N + 1)

for i in range(1, N + 1):
    if A[i - 1] == 1:
        atari[i] = atari[i - 1] + 1
        hazure[i] = hazure[i - 1]
    else:
        atari[i] = atari[i - 1]
        hazure[i] = hazure[i - 1] + 1


for i in range(Q):
    L, R = LR[i]

    atari_count = atari[R] - atari[L - 1]
    hazure_count = hazure[R] - hazure[L - 1]

    if atari_count > hazure_count:
        print("win")
    elif atari_count == hazure_count:
        print("draw")
    else:
        print("lose")
