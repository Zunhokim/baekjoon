#선물

import sys

N, L, W, H = map(int, sys.stdin.readline().rstrip().split())
S, E = 0, max(L, W, H)

for i in range(100):
    M = (S + E) / 2
    if (L // M) * (W // M) * (H // M) >= N:
        S = M
    else:
        E = M

print("%.10f" %(E))
