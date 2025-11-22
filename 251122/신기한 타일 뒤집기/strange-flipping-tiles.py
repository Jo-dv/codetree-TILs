n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
size = 200001
pos = 100000
arr = [0] * size
answer = [0, 0]

for step, d in zip(x, dir):
    if d == 'L':
        for i in range(pos, pos-step, -1):
            arr[i] = -1
        pos = i
    else:
        for i in range(pos, pos+step):
            arr[i] = 1
        pos = i

for i in arr:
    if i == -1:
        answer[0] += 1
    elif i == 1:
        answer[1] += 1

print(*answer)