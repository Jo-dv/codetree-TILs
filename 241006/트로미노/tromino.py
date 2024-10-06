n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def set_block(y, x, size, value):
    global answer
    if size == 3:
        answer = max(answer, value)
        return
    for dy, dx in directions:
        my = y + dy
        mx = x + dx 
        if 0 <= my < n and 0 <= mx < m and not visited[my][mx]:
            visited[my][mx] = True
            set_block(my, mx, size + 1, value + grid[my][mx])
            visited[my][mx] = False

for y in range(n):
    for x in range(n):
        visited[y][x] = True
        set_block(y, x, 1, grid[y][x])
        visited[y][x] = False

print(answer)