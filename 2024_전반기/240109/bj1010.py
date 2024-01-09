#1010번 다리 놓기
#조합을 만들면 될듯

import math

case = int(input())
combi = []

for i in range(case):
    n,m = map(int, input().split())
    combi.append(math.comb(m, n))

for i in combi:
    print(i)
