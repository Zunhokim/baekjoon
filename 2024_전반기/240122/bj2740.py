#행렬 곱셈

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

M, K = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

AxB = [[0]*K for _ in range(N)]
for row in range(N):
    for col in range(K):
        e = 0
        for i in range(M):
            e += A[row][i] * B[i][col]
        AxB[row][col] = e

for r in AxB:
    print(*r)