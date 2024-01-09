#좌표 정렬하기

import sys

N = int(sys.stdin.readline())

array = []

for i in range (N):
    [a,b] = map(int, sys.stdin.readline().split())
    array.append([a,b])

array = sorted(array)

for i in range (N):
    print(array[i][0], array[i][1])