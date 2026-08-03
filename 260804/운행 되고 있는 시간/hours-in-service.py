n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    temp = [False] * 1001
    for j in range(n):
        if i == j:
            continue
        for k in range(times[j][0], times[j][1]):
            temp[k] = True
    answer = max(answer, sum(temp))

print(answer)        
        