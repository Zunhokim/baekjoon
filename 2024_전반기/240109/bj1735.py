#분수 합

import math

A, B = list(map(int, input().rstrip().split()))
C, D = list(map(int, input().rstrip().split()))

son = (B*C) + (A*D)
mom = B*D
gcd = math.gcd(son, mom)

son = int(son / gcd)
mom = int(mom / gcd)

print(f"{son} {mom}")