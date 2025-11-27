N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
directions = {"N": (1, 0), "S": (-1, 0), "W": (0, -1), "E": (0, 1)}
y, x = 0, 0
flag = False
answer = 0

for i in range(N):
    dy, dx = directions[dir[i]]
    for i in range(dist[i]):
        y += dy
        x += dx
        answer += 1
        if (y, x) == (0, 0):
            flag = True
            break
    if flag:
        break

print(answer if flag else -1)