import heapq

n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))

INF = float("inf")
distance = [INF] * (n + 1)
distance[k] = 0

heap = [(0, k)] 

while heap:
    current_distance, node = heapq.heappop(heap)

    if current_distance > distance[node]:
        continue

    for nxt, weight in graph[node]:
        new_distance = current_distance + weight

        if new_distance < distance[nxt]:
            distance[nxt] = new_distance
            heapq.heappush(heap, (new_distance, nxt))

for i in range(1, n + 1):
    print(-1 if distance[i] == INF else distance[i])