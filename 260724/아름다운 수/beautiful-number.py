n = int(input())

# Please write your code here.
arr = [1, 2, 3, 4]
answer = 0

def search(target):
    if len(target) == n:
        check(target)
        return

    for i in arr:
        target.append(i)
        search(target)
        target.pop()

def check(data):
    global answer
    idx = 0
    while idx < n:
        gap = data[idx]
        if data[idx:idx+gap] == [gap] * gap:
            idx += gap
        else:
            break
    else:
        answer += 1
        

search([])
print(answer)