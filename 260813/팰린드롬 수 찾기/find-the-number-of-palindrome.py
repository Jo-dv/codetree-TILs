X, Y = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(X, Y+1):
    data = str(i)
    if data == data[::-1]:
        answer += 1

print(answer)