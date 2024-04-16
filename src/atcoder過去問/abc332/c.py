N, M = map(int, input().split())
S = str(input())

L = 0
m_stock = M
l_stock = 0

for s in S:
    if s == "0":
        m_stock = M
        l_stock = L
    elif s == "1":
        if m_stock > 0:
            m_stock -= 1
        elif l_stock > 0:
            l_stock -= 1
        else:
            L += 1
    else:
        if l_stock > 0:
            l_stock -= 1
        else:
            L += 1

print(L)
