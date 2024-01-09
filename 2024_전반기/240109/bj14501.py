#퇴사
#dynamic programming

import sys

N = int(sys.stdin.readline().rstrip())
day = [0 for i in range(N+1)]
cost = [0 for i in range(N+1)]

for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    day[i] = A
    cost[i] = B

dp = [0 for i in range(N+1)]

for i in range(len(day)-2, -1, -1):
    if day[i]+i <= N:
        dp[i] = max(cost[i] + dp[i+day[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])