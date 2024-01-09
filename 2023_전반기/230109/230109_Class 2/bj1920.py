# 수 찾기

import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split())) # list로 받는것 보다는 set으로 받는게 시간 절약에 도움됨

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print("1")
    else:
        print("0")