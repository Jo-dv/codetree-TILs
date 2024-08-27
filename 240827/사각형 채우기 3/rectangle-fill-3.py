n = int(input())

dp = [0] * 1001
dp[0] = 1
dp[1] = 2

for i in range(2, 1001):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % 1000000007
    for j in range(i - 3, -1, -1):
        dp[i] += (dp[j] * 2) % 1000000007

print(dp[n])