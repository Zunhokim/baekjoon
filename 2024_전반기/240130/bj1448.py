#삼각형 만들기

import sys

N = int(sys.stdin.readline().rstrip())
case = []

for i in range(N):
    length = int(sys.stdin.readline().rstrip())
    case.append(length)

case.sort(reverse=True)

for i in range(len(case)-2):
    if sum(case[i+1:i+3]) > case[i]:
        print(sum(case[i:i+3]))
        break
else:
    print(-1)

