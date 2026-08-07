n, k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
answer = -1

for i in range(n):
    for j in range(i+1, n):
        if bombs[i] == bombs[j] and j - i <= k:
            answer = max(answer, bombs[i])

print(answer)