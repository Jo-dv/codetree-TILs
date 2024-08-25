import heapq

hq = []

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in nums:
    heapq.heappush(hq, (-i, i))

for _ in range(m):
    max_num = heapq.heappop(hq)
    heapq.heappush(hq, (-(max_num[1] - 1), max_num[1] - 1))

print(hq[0][1])