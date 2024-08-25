import heapq

hq = []

n = int(input())
nums = list(map(int, input().split()))
answer = 0.

for k in range(1, n - 1):
    removed_nums = nums[k:]
    temp = removed_nums.copy()
    heapq.heapify(temp)
    heapq.heappop(temp)
    answer = max(answer, sum(temp) / len(temp))

print('{:.2f}'.format(answer))