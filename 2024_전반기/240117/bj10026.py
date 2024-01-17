#적록색약 / 전재준?

import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

graph = []
visited = [[0] * (N) for _ in range(N)]
sum = 0
sum2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    graph.append(list(sys.stdin.readline()))

def dfs(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0:
            if graph[nx][ny] == color:
                dfs(nx, ny, color)

for color in ['R', 'G', 'B']:
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                sum += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * (N) for _ in range(N)]

for color in ['R', 'B']:
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j, color)
                sum2 += 1

print(sum, sum2)