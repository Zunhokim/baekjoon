#리모컨

import sys

target = int(sys.stdin.readline().rstrip())
ans = abs(100 - target)
M = int(sys.stdin.readline().rstrip())

if M:
    broken = set(sys.stdin.readline().rstrip().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)