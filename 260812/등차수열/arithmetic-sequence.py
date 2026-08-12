n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
answer = 0
for k in range(102):
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[j] - k == k - a[i]:
                cnt += 1
    answer = max(answer, cnt)

print(answer)