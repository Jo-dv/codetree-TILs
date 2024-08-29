n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], arr[i][0])

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1], arr[0][i])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), arr[i][j])
        # 지나온 길에서 만난 최댓값 중 가장 작은 값을 찾는 문제
        # dp[i - 1][j], dp[i][j - 1] 해당 값들은 직전의 값으로 최대일 것이므로 이 중 최소를 선택
        # 그 중 최종적으로 최댓값을 선택

print(dp[-1][-1])