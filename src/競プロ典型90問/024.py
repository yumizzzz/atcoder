N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# AtCoder_Beginners_SelectionのTravelingと同じ

diff = sum([abs(A[n] - B[n]) for n in range(N)])
if diff > K:
    print("No")
elif diff % 2 != K % 2:
    print("No")
else:
    print("Yes")
