n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(lambda x: int(x) - 1, input().split())

target = grid[r][c] - 1

for y in range(r - target, r + target + 1):
    if y < 0 or y >= n:
        continue
    grid[y][c] = 0

for x in range(c - target, c + target + 1):
    if x < 0 or x >= n:
        continue
    grid[r][x] = 0

temp = [[0] * n for _ in range(n)]
for x in range(n):
    i = n - 1
    for y in range(n - 1, -1, -1):
        if grid[y][x] != 0:
            temp[i][x] = grid[y][x]
            i -= 1

for i in temp:
    print(*i)