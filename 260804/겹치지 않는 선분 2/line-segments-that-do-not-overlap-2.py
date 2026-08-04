n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for i in range(n):
    flag = False
    for j in range(n):
        if i == j:
            continue

        if (lines[i][0] <= lines[j][0] and lines[i][1] >= lines[j][1]) or (lines[j][0] <= lines[i][0] and lines[j][1] >= lines[i][1]):
            flag = True
            break
    
    if not flag:
        answer += 1

print(answer)