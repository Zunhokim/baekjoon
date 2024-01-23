#N과 M(1)

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num = []

def dfs():
    if len(num) == M:
        print(' '.join(map(str, num)))
        return
    for i in range(1, N+1):
        if i not in num:
            num.append(i)
            dfs()
            num.pop()

dfs()