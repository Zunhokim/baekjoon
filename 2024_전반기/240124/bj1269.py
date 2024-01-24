#대칭 차집합

import sys

n_a, n_b = map(int, sys.stdin.readline().split())
S_a = set(map(int, sys.stdin.readline().split()))
S_b = set(map(int, sys.stdin.readline().split()))

print(len(S_a - S_b) + len(S_b - S_a))