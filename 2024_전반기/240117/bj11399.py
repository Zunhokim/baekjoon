#ATM

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().strip().split()))

sP = sorted(P)
num = len(sP)
sum = 0

for i in sP:
    sum += i * num
    num -= 1

print(sum)