n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + 100)
    y1.append(b + 100)
    x2.append(c + 100)
    y2.append(d + 100)

# Write your code here!
grid = [[0] * 201 for _ in range(201)]
answer = 0
for i in range(n):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            if grid[y][x] == 0:
                grid[y][x] = 1
                answer += 1


print(answer)