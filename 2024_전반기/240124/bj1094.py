#막대기

import sys

X = int(sys.stdin.readline())

case = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in case:
    if X >= i:
        count += 1
        X -= i
    elif X == 0:
        break

print(count)
