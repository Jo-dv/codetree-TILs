n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr = [0] * 2001
pos = 1000
# 0 ~ 999, 1000, 1001~2000

for step, d in zip(x, dir):
    if d == "L":
        for i in range(pos, pos-step, -1):
            arr[i] += 1
        pos -= step
    else:
        for i in range(pos, pos+step):
            arr[i] += 1
        pos += step

answer = 0
for i in arr:
    if i >= 2:
        answer += 1

print(answer)