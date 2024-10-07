n, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2)]

for _ in range(t):
    up = arr[0][n - 1]
    down = arr[1][n - 1]
    for i in range(n - 1, 0, -1):
        arr[0][i] = arr[0][i - 1]
    arr[0][0] = down
    for i in range(n - 1, 0, -1):
        arr[1][i] = arr[1][i - 1]
    arr[1][0] = up
 
for i in arr:
    print(*i)