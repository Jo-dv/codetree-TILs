n = int(input())
arr = list(map(int, input().split()))
dp = [-1] * n
dp[0] = 0

for standard in range(1, n):
    for current in range(standard):
        jump = arr[current]
        if dp[current] != -1 and  standard <= current + jump:
            dp[standard] = max(dp[standard], dp[current] + 1)

print(max(dp))