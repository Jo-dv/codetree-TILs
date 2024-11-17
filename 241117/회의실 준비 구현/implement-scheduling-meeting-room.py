n = int(input())
table = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

table.sort(key=lambda x: x[1])
recent_time = -1

for start, end in table:
    if recent_time <= start:
        recent_time = end
        answer += 1

print(answer)