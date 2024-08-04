k, n = map(int, input().split())
answer = []

def dfs(cnt):
    if cnt == n:
        for num in answer:
            print(num, end=" ")
        print()
        return
    
    for i in range(1, k + 1):
        answer.append(i)
        dfs(cnt + 1)
        answer.pop()

dfs(0)