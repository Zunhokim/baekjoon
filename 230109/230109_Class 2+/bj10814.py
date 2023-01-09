#나이순 정렬

import sys

N = int(sys.stdin.readline())

att = []

for i in range (N):
    [age, name] = map(str, sys.stdin.readline().split())
    att.append([int(age), i, name])

att.sort()

for i in range (N):
    print(att[i][0], att[i][2])