n, m = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
info = [(i[0], i[1], i[1] / i[0]) for i in jewels]  # 무게, 가격
info.sort(key=lambda x: x[2] ,reverse=True)
answer = 0

for i in info:
    w, v, vpw = i
    if m - w > 0:
        answer += v
        m -= w
    else:
        answer += ((m / w) * v)
        break

print("%.3f" %answer)