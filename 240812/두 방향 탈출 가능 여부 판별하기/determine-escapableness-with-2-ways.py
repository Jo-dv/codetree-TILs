n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
flag = False

def dfs(y, x):
    global flag
    if y == n - 1 and x == m - 1:
        flag = True
        return
    if 0 <= y < n and 0 <= x < m and not visited[y][x] and grid[y][x] == 1:
        visited[y][x] = True
        dfs(y + 1, x)
        dfs(y, x + 1)
        return

    return

dfs(0, 0)
print(1 if flag else 0)