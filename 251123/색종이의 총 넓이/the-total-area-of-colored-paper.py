n = int(input())
points = [tuple(map(lambda i: int(i) + 100, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
grid = [[0] * 201 for _ in range(201)]
for point in points:
    x, y = point

    for i in range(y, y+8):
        for j in range(x, x+8):
            grid[i][j] = 1

answer = sum(sum(i) for i in grid)
print(answer)