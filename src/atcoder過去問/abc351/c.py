N = int(input())
A = list(map(int, input().split()))

stack = []
for a in A:
    ball_size = a
    stack.append(ball_size)
    while True:
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + 1)
        else:
            break

print(len(stack))
