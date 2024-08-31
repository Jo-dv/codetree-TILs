n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for standard in range(1, n):
    for previous in range(standard):
        if a[previous] > a[standard]:
            dp[standard] = max(dp[standard], dp[previous] + 1)


print(max(dp))