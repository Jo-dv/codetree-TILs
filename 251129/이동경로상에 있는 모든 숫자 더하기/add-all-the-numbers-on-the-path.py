N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
y = x = N // 2
answer = board[y][x]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0

for i in str:
    if i == "L":
        d = (d - 1) % 4
    elif i == "R":
        d = (d + 1) % 4
    else:
        dy, dx = directions[d]
        my, mx = y + dy, x + dx
        if 0 <= my < N and 0 <= mx < N:
            y, x = my, mx
            answer += board[y][x]

print(answer)