import heapq

n = int(input())
arr = list(map(int, input().split()))
answer = 0

heapq.heapify(arr)
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    answer += (a + b)
    heapq.heappush(arr, a + b)

print(answer)