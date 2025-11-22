n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
answer = 0

arr = [0] * (n + 1)
for s, e in commands:
    for i in range(s, e+1):
        arr[i] += 1 
        answer = max(answer, arr[i])

print(answer)