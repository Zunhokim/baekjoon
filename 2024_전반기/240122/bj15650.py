#N과 M(2)

import sys

N, M = list(map(int, sys.stdin.readline().split()))
num = []

def dfs(input):
    if len(num) == M:
        print(' '.join(map(str, num)))
        return

    for i in range(input, N+1):
        if i not in num:
            num.append(i)
            dfs(i+1)
            num.pop()

dfs(1)