x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(lambda i: int(i) + 1000, input().split())
x1[1], y1[1], x2[1], y2[1] = map(lambda i: int(i) + 1000, input().split())
x1[2], y1[2], x2[2], y2[2] = map(lambda i: int(i) + 1000, input().split())

# Please write your code here.
grid = [[0] * 2001 for _ in range(2001)]

for i in range(3):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            grid[y][x] = (1 if i < 2 else 0)

answer = sum(sum(i) for i in grid)
print(answer)