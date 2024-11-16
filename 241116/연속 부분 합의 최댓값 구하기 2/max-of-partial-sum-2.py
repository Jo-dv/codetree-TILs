n = int(input())
arr = list(map(int, input().split()))
answer = -1000 * 100000 + 1
temp = 0

for i in arr:
    temp += i
    if temp < 0:
        temp = 0
    else:
        answer = max(answer, temp)

print(answer)