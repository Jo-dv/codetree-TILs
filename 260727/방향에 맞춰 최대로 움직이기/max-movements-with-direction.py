n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arrow = [list(map(int, input().split())) for _ in range(n)]
directions = {1: (-1, 0), 2: (-1, 1), 3: (0, 1), 4: (1, 1), 5: (1, 0), 6: (1, -1), 7: (0, -1), 8: (-1, -1)}
sy, sx = map(lambda x: int(x) - 1, input().split())

visited = [[False] * n for _ in range(n)]
visited[sy][sx] = True
answer = 0

def search(y, x, visited, cnt):
    global answer
    if cnt > 0:
        answer = max(answer, cnt)

    d = arrow[y][x]
    dy, dx = directions[d]
    my = y + dy
    mx = x + dx

    while 0 <= my < n and 0 <= mx < n:
        if grid[y][x] < grid[my][mx]:
            visited[my][mx] = True
            search(my, mx, visited, cnt+1)
            visited[my][mx] = False
        my += dy
        mx += dx

search(sy, sx, visited, 0)
print(answer)