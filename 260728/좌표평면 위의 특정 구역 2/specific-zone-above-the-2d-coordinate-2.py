n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

if n <= 2:
    print(0)
else:
    answer = float('inf')

    for removed in range(n):
        min_x = float('inf')
        max_x = float('-inf')
        min_y = float('inf')
        max_y = float('-inf')

        for i, (x, y) in enumerate(points):
            if i == removed:
                continue

            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        area = (max_x - min_x) * (max_y - min_y)
        answer = min(answer, area)

    print(answer)