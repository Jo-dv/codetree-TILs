import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_k = max(max(i) for i in grid)
answer = [1, 0]

def dfs(y, x, k):
    if 0 <= y < n and 0 <= x < m and not visited[y][x] and grid[y][x] <= k:
        visited[y][x] = True
        dfs(y - 1, x, k)
        dfs(y + 1, x, k)
        dfs(y, x - 1, k)
        dfs(y, x + 1, k)
        return True
    return False

def dfs2(y, x):
    if 0 <= y < n and 0 <= x < m and not visited[y][x]:
        visited[y][x] = True
        dfs2(y - 1, x)
        dfs2(y + 1, x)
        dfs2(y, x - 1)
        dfs2(y, x + 1)
        return True
    return False

for k in range(1, max_k):
    area = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j, k)
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs2(i, j):
                    area += 1
    
    if answer[1] < area:
        answer[0] = k
        answer[1] = area

print(*answer)