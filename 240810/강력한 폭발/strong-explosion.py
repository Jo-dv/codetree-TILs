n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
pos = [(y, x) for x in range(n) for y in range(n) if grid[y][x]]  # 폭탄 위치
temp = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
bombs = {
    1: [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], 
    2: [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)], 
    3: [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
    }
answer = -1


def bomb(y, x, t):
    for dy, dx in bombs[t]:
        my = y + dy
        mx = x + dx

        if 0 <= my < n and 0 <= mx < n and not visited[my][mx]:
            visited[my][mx] = True

def search():
    cnt = 0

    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                cnt += 1
                visited[y][x] = False  # 다음 폭파를 위해서 다시 초기화

    return cnt

def explode():
    for y in range(n):
        for x in range(n):
            if temp[y][x]:  # 설치된 폭탄을 찾으면
                bomb(y, x, temp[y][x])  # 해당 폭탄 폭파

    return search()  # 폭파 범위 탐색


def set_bomb(cnt):
    global answer
    if cnt == len(pos):  # 주어진 위치에 모든 폭탄이 설치됐다면
        answer = max(answer, explode())  # 폭파
        return
    
    for i in range(1, 4):  # 번호 순서대로 폭탄 설치
        y, x = pos[cnt]
        temp[y][x] = i
        set_bomb(cnt + 1)
        temp[y][x] = 0

set_bomb(0)
print(answer)