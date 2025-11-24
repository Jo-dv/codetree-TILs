dirs = input()

# Please write your code here.
y, x = 0, 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = 0

for i in dirs:
    if i == "L":
        d = (d - 1) % 4
    elif i == "R":
        d = (d + 1) % 4
    else:
        dy, dx = directions[d]
        y += dy
        x += dx

print(x, y)