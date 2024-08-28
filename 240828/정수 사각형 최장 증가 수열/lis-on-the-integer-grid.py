n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
blocks = [(i, j) for j in range(n) for i in range(n)]  # 값, 좌표
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

for y, x in blocks:
    for d in directions:
        my = y + d[0]
        mx = x + d[1]
        if 0 <= my < n and 0 <= mx < n and arr[y][x] < arr[my][mx]:
            dp[my][mx] = max(dp[my][mx], dp[y][x] + 1)

for i in dp:
    answer = max(answer, max(i))

print(answer)