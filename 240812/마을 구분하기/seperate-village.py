n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
town = 0
answer = []

def dfs(y, x):
    global people
    if 0 <= y < n and 0 <= x < n and grid[y][x] == 1 and not visited[y][x]:
        visited[y][x] = True
        people += 1
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True
    return False

for i in range(n):
    for j in range(n):
        people = 0
        if dfs(i, j):
            town += 1
            answer.append(people)

answer.sort()
print(town)
for i in answer:
    print(i)