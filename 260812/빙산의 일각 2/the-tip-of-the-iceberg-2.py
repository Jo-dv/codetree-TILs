n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
max_h = max(h)+1
answer = 0
for i in range(max_h):
    temp = []

    for j in h:
        temp.append(0 if j - i <= 0 else j - i)

    prev = False
    cnt = 0
    for j in temp:
        if prev == False:
            if j > 0:
                cnt += 1
                prev = True
        else:
            if j == 0:
                prev = False

    answer = max(answer, cnt)

print(answer)