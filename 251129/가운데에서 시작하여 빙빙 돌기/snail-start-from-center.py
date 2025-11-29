n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
y = x = n // 2
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
d = 0
cnt = 0
step = 1
num = 1
grid[y][x] = 1

while True:
    if cnt == 2:
        step += 1
        cnt = 0
    
    dy, dx = directions[d]
    for _ in range(step):
        y += dy
        x += dx
        if x == n:
            for i in grid:
                print(*i)
            exit()
        num += 1
        grid[y][x] = num

    d = (d + 1) % 4
    cnt += 1