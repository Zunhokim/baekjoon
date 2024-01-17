#가장 가까운 세 사람의 심리적 거리
# 비둘기집 원리

import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().rstrip().split())

    if N > 32:
        print(0)
    else:
        ans = 100000
        p = []

        def dfs(start):
            global ans
            if len(p) == 3:
                temp = 0
                for i in range(4):
                    if(p[0][i] != p[1][i]):
                        temp +=1
                    if(p[1][i] != p[2][i]):
                        temp +=1
                    if(p[2][i] != p[0][i]):
                        temp +=1
                ans = min(ans, temp)
                return

            for i in range(start, N):
                p.append(arr[i])
                dfs(i+1)
                p.pop()

        dfs(0)
        print(ans)