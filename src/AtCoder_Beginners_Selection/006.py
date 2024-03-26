N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)
print(sum(sorted_A[::2]) - sum(sorted_A[1::2]))
