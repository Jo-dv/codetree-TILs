n = int(input())
answer = 0

def check(num):
    i = 0
    while i < n:
        cnt = 1
        while i + 1 < n and num[i] == num[i + 1]:
            i += 1
            cnt += 1
        if cnt % int(num[i]) != 0:
            return False
        i += 1
    return True

def dfs(num):
    global answer

    if len(num) == n:
        if check(num):
            answer += 1
        return

    for i in range(1, 5):
        dfs(num + str(i))
    
dfs("")
print(answer)