n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
answer = 0
nums.sort()
for i in range(n):
    answer = max(answer, nums[i] + nums[-(i+1)])

print(answer)