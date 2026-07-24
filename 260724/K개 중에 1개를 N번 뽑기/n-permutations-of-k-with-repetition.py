K, N = map(int, input().split())

# Please write your code here.
arr = [i for i in range(1, K+1)]

def search(target):
    if len(target) == N:
        print(*target)
        return
    
    for i in range(K):
        target.append(arr[i])
        search(target)
        target.pop()

search([])