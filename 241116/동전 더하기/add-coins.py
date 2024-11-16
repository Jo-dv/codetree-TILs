n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = {coin: 0 for coin in coins}
answer = 0

for i in range(n - 1, -1, -1):
    coin = coins[i]
    answer += (k // coin)
    k %= coin

print(answer)