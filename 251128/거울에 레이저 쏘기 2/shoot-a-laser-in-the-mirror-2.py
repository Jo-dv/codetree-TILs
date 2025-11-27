n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

# 위치 찾기
y, x, pos = 0, 0, 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

while pos != k:
    dy, dx = directions[d]
    my, mx = y + dy, x + dx
    if 0 <= my < n and 0 <= mx < n:
        y = my
        x = mx
    else:
        d = (d + 1) % 4
        dy, dx = directions[d]
    pos += 1

# 레이저 발사
answer = 0
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = pos // 4

while True:
    if y < 0 or y >= n or x < 0 or x >= n:
        print(answer+1)
        break
    dy, dx = directions[d]

    if grid[y][x] == "/":
        dy, dx = -dx, -dy
    else:
        dy, dx = dx, dy
    
    y += dy
    x += dx
    answer += 1