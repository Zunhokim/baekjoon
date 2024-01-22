#최대 힙

import sys
import heapq

N = int(sys.stdin.readline())
num = []

for i in range(N):
    line = int(sys.stdin.readline())

    if line == 0:
        if len(num) == 0:
            print(0)
        else:
            print(heapq.heappop(num)[1])
    else:
        heapq.heappush(num, (-line, line))