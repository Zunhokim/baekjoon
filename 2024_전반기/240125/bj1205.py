#등수 구하기

import sys

N, new, P = map(int, sys.stdin.readline().split())

if N == 0:
    print(1)
else:
    score = list(map(int, sys.stdin.readline().split()))

    if score[-1] >= new and N == P:
        print(-1)
    else:
        case = N + 1

        for i in range(N):
            if score[i] <= new:
                case = i + 1
                break

        print(case)