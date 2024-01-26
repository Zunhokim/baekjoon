#패션왕 신혜빈

import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    weardict = {}
    for j in range(n):
        wear = list(sys.stdin.readline().rstrip().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)