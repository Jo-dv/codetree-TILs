n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
cnt = 0
flag = False

for i in range(n):
    if (i == 0 and t < arr[i]) or (t < arr[i]):
        cnt += 1
        flag = True
    else:
        cnt = 1
    
    answer = max(answer, cnt)

print(answer-1)