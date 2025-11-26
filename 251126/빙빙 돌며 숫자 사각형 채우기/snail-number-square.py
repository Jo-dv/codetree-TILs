n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
y, x = 0, 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
arr[y][x] = 1

for i in range(2, n * m + 1):
    dy, dx = directions[d]
    my, mx = y + dy, x + dx

    if (my < 0 or my >= n or mx < 0 or mx >= m) or arr[my][mx] != 0:
        d = (d + 1) % 4

    dy, dx = directions[d]
    my, mx = y + dy, x + dx

    arr[my][mx] = i
    y = my
    x = mx

for i in arr:
    print(*i)