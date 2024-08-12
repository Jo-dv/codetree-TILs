n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(y, x):
    if y == n - 1 and x == m - 1:
        return True
    if 0 <= y < n and 0 <= x < m and not visited[y][x] and grid[y][x] == 1:
        visited[y][x] = True
        dfs(y + 1, x)
        dfs(y, x + 1)

    return False

print(1 if dfs(0, 0) else 0)