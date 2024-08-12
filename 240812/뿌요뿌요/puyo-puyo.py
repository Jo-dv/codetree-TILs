n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
block = 0
max_block_size = 0

def search(y, x, target):
    global current_block_size
    
    if 0 <= y < n and 0 <= x < n and not visited[y][x] and grid[y][x] == target:
        visited[y][x] = True
        block_list.append((y, x))
        current_block_size += 1
        
        search(y - 1, x, target)
        search(y + 1, x, target)
        search(y, x - 1, target)
        search(y, x + 1, target)
        return True
    return False

def explode():
    global block

    block += 1
    for y, x in block_list:
        grid[y][x] = 0

def down_block():
    for x in range(n):
        for i in range(n - 2, -1, -1):  # 반복됨에 따라 천장의 높이를 높여나감
            for y in range(n - 1, i, -1):
                if grid[i][x] != 0 and grid[y][x] == 0:  # 현재 천장(i)에 내릴 블록이 있고, 현재 y는 빈 곳이라면
                    grid[y][x] = grid[i][x]
                    grid[i][x] = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            block_list = []
            visited = [[False] * n for _ in range(n)]
            current_block_size = 0
            if search(i, j, grid[i][j]):
                max_block_size = max(max_block_size, current_block_size)
            if current_block_size >= 4:
                explode()
                down_block()

print(block, max_block_size)