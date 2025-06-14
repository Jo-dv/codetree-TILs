import sys
import heapq

INF = (2**31) - 1

dRow = [0, 1, 0, -1]
dCol = [1, 0, -1, 0]

MAX_GRID_SIZE = 50
MAX_JUMP_POWER = 5

input = sys.stdin.readline

gridSize = int(input().strip())
lakeGrid = [[''] * (gridSize + 2) for _ in range(gridSize + 2)]
for row in range(1, gridSize + 1):
    rowString = input().strip()
    for col in range(1, gridSize + 1):
        lakeGrid[row][col] = rowString[col - 1]

# 상태 그래프를 3차원 리스트로 정의
stateGraph = [[[[] for _ in range(MAX_JUMP_POWER + 1)] for _ in range(gridSize + 2)] for _ in range(gridSize + 2)]

# 그래프 생성
for row in range(1, gridSize + 1):
    for col in range(1, gridSize + 1):
        if lakeGrid[row][col] != '.':
            continue
        for jumpPower in range(1, MAX_JUMP_POWER + 1):
            # 점프력 증가
            if jumpPower < MAX_JUMP_POWER:
                stateGraph[row][col][jumpPower].append((row, col, jumpPower + 1, (jumpPower + 1) ** 2))
            # 점프력 감소
            for newJump in range(1, jumpPower):
                stateGraph[row][col][jumpPower].append((row, col, newJump, 1))
            # 점프 이동
            for direction in range(4):
                nr, nc = row, col
                valid = True
                for _ in range(jumpPower):
                    nr += dRow[direction]
                    nc += dCol[direction]
                    if nr < 1 or nr > gridSize or nc < 1 or nc > gridSize or lakeGrid[nr][nc] == '#':
                        valid = False
                        break
                if valid and lakeGrid[nr][nc] == '.':
                    stateGraph[row][col][jumpPower].append((nr, nc, jumpPower, 1))

queryCount = int(input().strip())
for _ in range(queryCount):
    startRow, startCol, endRow, endCol = map(int, input().split())
    distance = [[[INF] * (MAX_JUMP_POWER + 1) for _ in range(gridSize + 2)] for _ in range(gridSize + 2)]
    pq = []
    distance[startRow][startCol][1] = 0
    heapq.heappush(pq, (0, startRow, startCol, 1))
    answer = INF

    while pq:
        timeCost, row, col, jumpPower = heapq.heappop(pq)
        if distance[row][col][jumpPower] < timeCost:
            continue
        if row == endRow and col == endCol:
            answer = timeCost
            break
        for nr, nc, nj, cost in stateGraph[row][col][jumpPower]:
            if distance[nr][nc][nj] > timeCost + cost:
                distance[nr][nc][nj] = timeCost + cost
                heapq.heappush(pq, (distance[nr][nc][nj], nr, nc, nj))

    sys.stdout.write((str(answer) if answer < INF else "-1") + "\n")
