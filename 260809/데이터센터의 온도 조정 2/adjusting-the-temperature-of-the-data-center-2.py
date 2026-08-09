N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0

for i in range(-1, 1002, 1):
    temp = 0
    for a, b in ranges:
        if i < a:
            temp += C
        elif a <= i <= b:
            temp += G
        else:
            temp += H
    answer = max(answer, temp)

print(answer)