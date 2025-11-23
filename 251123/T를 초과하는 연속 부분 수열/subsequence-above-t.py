n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
cnt = 0

for i in range(n):
    if t < arr[i]:
        cnt += 1
    else:
        cnt = 0

    answer = max(answer, cnt)

print(answer)