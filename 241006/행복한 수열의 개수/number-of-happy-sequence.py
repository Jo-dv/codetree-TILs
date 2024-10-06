n, m = map(int , input().split())
grid = list(list(map(int, input().split())) for _ in range(n))
answer = 0

for i in range(n):
    cnt, max_cnt = 1, 1
    for x in range(1, n):
        if grid[i][x - 1] == grid[i][x]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        answer += 1       

for i in range(n):
    cnt, max_cnt = 1, 1
    for y in range(1, n):
        if grid[y - 1][i] == grid[y][i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        answer += 1    

print(answer)