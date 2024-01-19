# 구간 합 구하기 4

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num_li = [0]

temp = 0

for i in num:
    temp += i
    num_li.append(temp)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(num_li[b] - num_li[a - 1])