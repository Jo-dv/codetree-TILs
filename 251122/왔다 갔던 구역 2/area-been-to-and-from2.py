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
        dest = pos - step
        while pos > dest:
            pos -= 1
            arr[pos] += 1
    else:
        dest = pos + step
        while pos < dest:
            pos += 1
            arr[pos] += 1

answer = 0
for i in arr:
    if i >= 2:
        answer += 1

print(answer)