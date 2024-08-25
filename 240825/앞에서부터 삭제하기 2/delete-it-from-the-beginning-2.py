import heapq

hq = []

n = int(input())
nums = list(map(int, input().split()))
answer = 0.
heapq.heapify(nums)

for k in range(1, n - 1):
    heapq.heappop(nums)
    answer = max(answer, sum(nums) / len(nums))

print('{:.2f}'.format(answer))