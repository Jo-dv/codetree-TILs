n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
table_a = [0] * 1001
table_b = [0] * 1001

time = 1
for i in range(n):
    for j in range(t[i]):
        table_a[time] = table_a[time-1] + v[i]
        time += 1

time = 1
for i in range(m):
    for j in range(t2[i]):
        table_b[time] = table_b[time-1] + v2[i]
        time += 1

answer = 0
prev_state = None
current_state = None

for i in range(1, time):
    if i == 1:
        prev_state = False if table_a[i] - table_b[i] < 0 else True
        continue
    if table_a[i] - table_b[i] == 0:
        continue
    current_state = False if table_a[i] - table_b[i] < 0 else True
    if prev_state != current_state:
        answer += 1
        prev_state = current_state

print(answer)