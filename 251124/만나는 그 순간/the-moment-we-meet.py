n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
pos_a = [0]
pos_b = [0]

for i in range(n):
    for j in range(t[i]):
        pos_a.append(pos_a[-1]+(1 if d[i] == "R" else -1))

for i in range(m):
    for j in range(t2[i]):
        pos_b.append(pos_b[-1]+(1 if d2[i] == "R" else -1))

for i, pos in enumerate(zip(pos_a[1:], pos_b[1:]), 1):
    a, b = pos
    if a == b:
        print(i)
        break
else:
    print(-1)
