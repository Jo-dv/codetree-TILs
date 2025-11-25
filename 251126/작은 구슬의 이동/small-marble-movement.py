n, t = map(int, input().split())
y, x, d = input().split()
y, x = int(y)-1, int(x)-1

# Please write your code here.
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for _ in range(t):
    dy, dx = directions[d]
    my, mx = y + dy, x + dx
    if 0 <= my < n and 0 <= mx < n:
        y, x = my, mx
    else:
        if d == "U":
            d = "D"
        elif d == "D":
            d = "U"
        elif d == "L":
            d = "R"
        else:
            d = "L"

print(y+1, x+1)
