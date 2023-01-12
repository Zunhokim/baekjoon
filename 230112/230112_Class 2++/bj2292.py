#벌집

import sys

N = int(sys.stdin.readline())

count = 1
plusnum = 0
sumnum = 1

while True:

    if N == 1:
        print(count)
        break
    else:
        if sumnum < N:
            count += 1
            plusnum += 6
            sumnum += plusnum
            continue
        elif sumnum == N:
            print(count)
            break
        else:
            print(count)
            break