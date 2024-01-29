#회의실 배정

import sys

N = int(sys.stdin.readline())
meet = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meet.append((start, end))

meet.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0

for i in meet:
    if time <= i[0]:
        time = i[1]
        answer += 1

print(answer)