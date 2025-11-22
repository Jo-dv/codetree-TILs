n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
arr = [0] * 201

for s, e in segments:
    for i in range(s+100, e+101):
        arr[i] += 1
        answer = max(answer, arr[i])

print(answer)