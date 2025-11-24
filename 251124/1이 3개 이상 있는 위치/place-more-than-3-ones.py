n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for y in range(n):
    for x in range(n):
        cnt = 0
        for dy, dx in directions:
            my = y + dy
            mx = x + dx
            if 0 <= my < n and 0 <= mx < n and grid[my][mx] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)