n = int(input())
arr = list(map(int, input().split()))
answer = -1000 * 100000 -1
temp = 0

for i in arr:
    temp += i
    if temp < 0:
        answer = max(answer, temp)
        temp = 0

print(answer)