n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer = 1
cnt = 0

for i in range(n):
    if i == 0 or arr[i] == arr[i-1]:
        cnt += 1
    else:
        answer = max(answer, cnt)
        cnt = 1

print(answer)