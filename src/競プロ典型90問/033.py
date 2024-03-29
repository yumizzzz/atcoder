H, W = map(int, input().split())

if H == 1 or W == 1:
    print(max(H, W))
else:
    h = H // 2 + H % 2
    w = W // 2 + W % 2
    print(h * w)
