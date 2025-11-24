N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
table_a = [0] * 1000001
table_b = [0] * 1000001

time = 1
for i in range(N):
    for _ in range(t[i]):
        table_a[time] = table_a[time-1] + v[i]
        time += 1

time = 1
for i in range(M):
    for _ in range(t2[i]):
        table_b[time] = table_b[time-1] + v2[i]
        time += 1

winner = [0, 0]
answer = 0
for i in range(1, time):
    if table_a[i] == table_b[i] and winner != [1, 1]:
        winner = [1, 1]
        answer += 1
    elif table_a[i] > table_b[i] and winner != [1, 0]:
        winner = [1, 0]
        answer += 1
    elif table_a[i] < table_b[i] and winner != [0, 1]:
        winner = [0, 1]
        answer += 1

print(answer)