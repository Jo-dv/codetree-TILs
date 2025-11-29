n, m = map(int, input().split())

# Please write your code here.
grid = [[0] * m for _ in range(n)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
y, x, d = 0, 0, 0
grid[y][x] = 1

for i in range(2, n * m + 1):
    dy, dx = directions[d]
    my, mx = y + dy, x + dx

    if 0 <= my < n and 0 <= mx < m and grid[my][mx] == 0:
        grid[my][mx] = i
        y = my
        x = mx
    else:
        d = (d + 1) % 4
        dy, dx = directions[d]
        my, mx = y + dy, x + dx
        grid[my][mx] = i
        y = my
        x = mx

for i in grid:
    print(*i)