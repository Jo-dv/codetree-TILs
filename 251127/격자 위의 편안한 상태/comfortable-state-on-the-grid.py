n, m = map(int, input().split())
points = [tuple(map(lambda i: int(i)-1, input().split())) for _ in range(m)]

# Please write your code here.
directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
grid = [[0] * n for _ in range(n)]
answer = []

for point in points:
    y, x = point
    grid[y][x] = 1
    cnt = 0
    for dy, dx in directions:
        my, mx = y + dy, x + dx
        if 0 <= my < n and 0 <= mx < n and grid[my][mx] == 1:
            cnt += 1
    
    answer.append(1 if cnt == 3 else 0)

for i in answer:
    print(i)