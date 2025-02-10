n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Write your code here!
from collections import defaultdict

hashmap = defaultdict(int)

for i in arr:
    hashmap[i] += 1

for i in nums:
    print(hashmap.get(i, 0), end=' ')