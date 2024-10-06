n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for y in range(n - 3 + 1):
    for x in range(n - 3 + 1):
        check = 0
        for i in range(3):
            check += sum(grid[y + i][x:x + 3])
        answer = max(answer, check)

print(answer)