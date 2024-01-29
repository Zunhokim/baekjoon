#수열 정렬

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

sort_A = sorted(A, reverse=False)

P = []

for i in range(N):
    P.append(sort_A.index(A[i]))
    sort_A[sort_A.index(A[i])] = -1

for i in range(N):
    print(str(P[i]), end=' ')