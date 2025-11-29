n, m = map(int, input().split())

# Please write your code here.
# A ~ Z = 65 ~ 90

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
y, x, d = 0, 0, 0
grid = [[""] * m for _ in range(n)]
data = 0
grid[y][x] = chr(data + 65)

for i in range(1, n * m):
    dy, dx = directions[d]
    my, mx = y + dy, x + dx

    if not (0 <= my < n and 0 <= mx < m and grid[my][mx] == ""):
        d = (d + 1) % 4
        dy, dx = directions[d]
        my, mx = y + dy, x + dx
    
    data = (data + 1) % 26
    grid[my][mx] = chr(data + 65)
    y = my
    x = mx

for i in grid:
    print(*i)
