#모든 순열

from itertools import permutations
import sys

N = int(sys.stdin.readline().rstrip())
res = permutations(range(1, N+1), N)

for perm in res:
    for i in perm:
        print(i, end=" ")
    print()