X, Y = map(int, input().split())

# Please write your code here.
answer = 0
for i in range(X, Y+1):
    temp = 0
    while i > 0:
        temp += (i % 10)
        i //= 10
    
    answer = max(answer, temp)

print(answer)
