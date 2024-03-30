import math

a, b = map(int, input().split())

lcm = math.lcm(a, b)
if lcm > 10**18:
    print("Large")
else:
    print(lcm)
