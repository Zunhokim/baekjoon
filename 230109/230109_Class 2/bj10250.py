#ACM 호텔

import sys

T = int(sys.stdin.readline())

for i in range(T):
    h, w, n = map(int, sys.stdin.readline().split())

    floor = n % h
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1

    print(floor * 100 + room_line)