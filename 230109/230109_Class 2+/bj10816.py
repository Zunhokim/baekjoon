# 숫자 카드 2

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

check = {}
for i in A:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

for i in B:
    if i in check:
        print(check[i], end=' ')
    else:
        print('0', end=' ')