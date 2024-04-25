N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x_sum = sum(X)
y_sum = sum(Y)

if x_sum > y_sum:
    print("Takahashi")
elif x_sum == y_sum:
    print("Draw")
else:
    print("Aoki")
