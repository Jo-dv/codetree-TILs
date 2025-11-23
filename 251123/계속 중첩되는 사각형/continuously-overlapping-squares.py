n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(lambda i: int(i) + 100, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here. 빨 -> 파 -> 빨 -> 파
grid = [[0] * 201 for _ in range(201)]
color = 1  # 1 = red, -1 = blue

for i in range(n):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            grid[y][x] = color
    color *= -1

answer = sum(i.count(-1) for i in grid)
print(answer)