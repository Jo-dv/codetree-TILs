commands = input()

# Please write your code here.
answer = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
y, x = 0, 0

for c in commands:
    if c == "L":
        d = (d - 1) % 4
        answer += 1
    elif c == "R":
        d = (d + 1) % 4
        answer += 1
    else:
        dy, dx = directions[d]
        y += dy
        x += dx
        answer += 1
    
    if (y, x) == (0, 0):
        print(answer)
        break
else:
    print(-1)