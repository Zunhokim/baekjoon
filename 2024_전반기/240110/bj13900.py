#순서쌍의 곱의 합

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))

sum = sum(num)
ans = 0

for i in num:
    sum -= i
    ans += sum * i

print(ans)