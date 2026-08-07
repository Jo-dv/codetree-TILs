k, n = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(k)]
answer = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue

        for data in rank:
            a = data.index(i)
            b = data.index(j)

            if a > b:
                break
        else:
            answer += 1

print(answer)
