n = int(input())
pointers = [list(map(int, input().split())) for _ in range(n)]
answer = float("inf")

for current in range(n):
    for selected in range(n):
        if current != selected:
            x1, y1 = pointers[current]
            x2, y2 = pointers[selected]
            distance = (x1 - x2)**2 + (y1 - y2)**2
            answer = min(answer, distance)

print(answer)