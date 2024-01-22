#파도반 수열

import sys

P = [0 for i in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1

for i in range(4, 101):
    P[i] = P[i-3] + P[i-2]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(P[N])