x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(lambda i: int(i) + 1000, input().split())
x1[1], y1[1], x2[1], y2[1] = map(lambda i: int(i) + 1000, input().split())

# Please write your code here.
grid = [[0] * 2001 for i in range(2001)]
for i in range(2):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            grid[y][x] = (1 if i == 0 else 0)

min_x, max_x = 2001, 0
min_y, max_y = 2001, 0
for y in range(2001):
    for x in range(2001):
        if grid[y][x] == 1:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

y = max_y - min_y + 1
x = max_x - min_x + 1
print(y * x)