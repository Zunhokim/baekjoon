#좌표 정렬하기 2

import sys

N = int(sys.stdin.readline())
array = []

for i in range (N):
    x, y = list(map(int, sys.stdin.readline().split()))
    array.append([y, x])

array = sorted(array)

for i in range (N):
    print(array[i][1], array[i][0])