#듣보잡

import sys

N, M = map(int, sys.stdin.readline().split())
listen = set()
watch = set()

for i in range(N):
    case = sys.stdin.readline()
    listen.add(case)

for i in range(M):
    case = sys.stdin.readline()
    watch.add(case)

ans = sorted(list(listen & watch))

print(len(ans))
for i in ans:
    print(i, end='')
