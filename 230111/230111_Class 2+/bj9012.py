#괄호

import sys

N = int(sys.stdin.readline())
tlist = []

for i in range (N):
    text = sys.stdin.readline().strip()
    tlist.append(text)

for i in tlist:
    if i[0] == '(':
        if i[::-1][0] == ')':
            count1 = i.count('(')
            count2 = i.count(')')

            if count1 == count2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")