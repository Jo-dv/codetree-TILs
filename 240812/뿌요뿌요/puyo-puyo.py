n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
block = 0
max_block_size = 0

def search(y, x, target):
    global current_block_size
    
    if 0 <= y < n and 0 <= x < n and not visited[y][x] and grid[y][x] == target:
        visited[y][x] = True
        current_block_size += 1
        
        search(y - 1, x, target)
        search(y + 1, x, target)
        search(y, x - 1, target)
        search(y, x + 1, target)
        return True
    return False

for i in range(n):
    for j in range(n):
        current_block_size = 0
        if search(i, j, grid[i][j]):
            max_block_size = max(max_block_size, current_block_size)
            if current_block_size >= 4:
                block += 1

print(block, max_block_size)