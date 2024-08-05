n, m = map(int, input().split())
arr = list(range(1, n + 1))
answer = []

def dfs(idx, cnt):
    if idx == n - 1:
        if cnt == m:
            print(*answer)
            return
        return
    
    answer.append(arr[idx + 1])
    dfs(idx + 1, cnt + 1)
    answer.pop()
    dfs(idx + 1, cnt)

dfs(-1, 0)