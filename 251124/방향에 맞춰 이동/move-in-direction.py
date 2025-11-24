n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
directions = {"N": (1, 0), "S": (-1, 0), "W": (0, -1), "E": (0, 1)}
y, x = 0, 0

for d, step in zip(dir, dist):
    dy, dx = directions[d]
    for _ in range(step):
        y += dy
        x += dx

print(x, y)