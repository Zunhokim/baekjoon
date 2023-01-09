#이항 계수 1

import math
import sys

N, K = map(int, sys.stdin.readline().split())

ans = math.factorial(N)/(math.factorial(K)*math.factorial(N-K))

print(int(ans))