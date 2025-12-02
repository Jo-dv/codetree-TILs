n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda i: int(i)-1, input().split())

# Please write your code here.
# 터지기
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
power = grid[r][c]-1
grid[r][c] = 0

for dy, dx in directions:
    my, mx = r + dy, c + dx
    for _ in range(power):
        if 0 <= my < n and 0 <= mx < n:
            grid[my][mx] = 0
            my += dy
            mx += dx

# 내리기
for x in range(n):
    temp = []
    for y in range(n-1, -1, -1):
        if grid[y][x] != 0:
            temp.append(grid[y][x])
    for y in range(n-1, -1, -1):
        grid[y][x] = temp.pop(0) if temp else 0

for i in grid:
    print(*i)