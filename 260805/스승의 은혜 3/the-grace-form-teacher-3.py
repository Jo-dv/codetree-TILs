N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
answer = 0
gifts.sort(key=lambda i: i[0] + i[1])

for selected in range(N):
    cost = (gifts[selected][0] // 2) + gifts[selected][1]
    cnt = 1

    for i in range(N):
        if selected == i:
            continue
        
        if cost + (gifts[i][0] + gifts[i][1]) <= B:
            cost += (gifts[i][0] + gifts[i][1])
            cnt += 1

    answer = max(answer, cnt)

print(answer)