n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
table_a = [0]
table_b = [0]

for i in range(n):
    for j in range(t[i]):
        table_a.append(table_a[-1] + (1 if d[i] == "R" else -1))

for i in range(m):
    for j in range(t_b[i]):
        table_b.append(table_b[-1] + (1 if d_b[i] == "R" else -1))

if len(table_a) < len(table_b):
    for i in range(len(table_b) - len(table_a)):
        table_a.append(table_a[-1])
elif len(table_a) > len(table_b):
    for i in range(len(table_a) - len(table_b)):
        table_b.append(table_b[-1])

answer = 0
for i in range(1, max(len(table_a), len(table_b))):
    if table_a[i] == table_b[i] and table_a[i-1] != table_b[i-1]:
        answer += 1

print(answer)
