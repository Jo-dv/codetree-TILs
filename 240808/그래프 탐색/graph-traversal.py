from collections import deque

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dq = deque([])
dq.append(1)
visited[1] = True
answer = 0

while dq:
    cur = dq.popleft()

    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            dq.append(i)
            answer += 1

print(answer)