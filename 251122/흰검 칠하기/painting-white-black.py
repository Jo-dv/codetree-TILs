n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
size = 200001
w = [0] * size
b = [0] * size
result = [0] * size
pos = 100000
answer = [0, 0, 0]  # 1, 2, 3 = 흰, 검, 회

for step, d in zip(x, dir):
    if d == "R":
        for i in range(pos, pos+step):
            b[i] += 1
            result[i] = 3 if w[i] >= 2 and b[i] >= 2 else 2
        pos = i
    else:
        for i in range(pos, pos-step, -1):
            w[i] += 1
            result[i] = 3 if w[i] >= 2 and b[i] >= 2 else 1
        pos = i
    # print(result[100000-5:100000+6])

for i in range(size):
    if result[i] == 1:
        answer[0] += 1
    elif result[i] == 2:
        answer[1] += 1
    elif result[i] == 3:
        answer[2] += 1

print(*answer)