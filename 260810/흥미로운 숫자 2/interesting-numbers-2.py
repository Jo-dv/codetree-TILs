X, Y = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(X, Y+1):
    check = dict()
    while i > 0:
        if (i % 10 not in check):
            check[i % 10] = 1
        else:
            check[i % 10] += 1
        i //= 10
    if len(check) == 2 and (list(check.values())[0] == 1 or list(check.values())[1] == 1):
        answer += 1

print(answer)