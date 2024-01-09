#괄호

import sys

N = int(sys.stdin.readline())
tlist = []

for i in range (N):
    text = sys.stdin.readline().strip()
    tlist.append(text)

for i in tlist:
    count = 0

    for j in range (len(i)):

        if i[j] == '(':
            count += 1
        elif i[j] == ')':
            count -= 1

        if count < 0:
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')
