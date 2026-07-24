k, n = map(int, input().split())

def check(target):
    for i in range(len(target)-2):
        if target[i] == target[i+1] == target[i+2]:
            return False

    return True

def search(target):
    if len(target) == n:
        if check(target):
            print(*target)
        return

    for i in range(1, k+1):
        target.append(i)
        search(target)
        target.pop()

search([])