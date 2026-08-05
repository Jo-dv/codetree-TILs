n, b = map(int, input().split())
prices = [int(input()) for _ in range(n)]
prices.sort()
answer = 0

for selected in range(n):  # 쿠폰을 쓸 선물
    cost = prices[selected] // 2
    cnt = 1
    for i in range(n):
        if selected == i:
            continue
        if cost + prices[i] <= b:
            cost += prices[i]
            cnt += 1
    answer = max(answer, cnt)

print(answer)