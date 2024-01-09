#조합
#import math 쓰면 간단하긴 한데..

import math
import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

print(math.comb(int(n), int(m)))