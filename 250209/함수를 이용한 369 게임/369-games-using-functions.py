a, b = map(int, input().split())

# Write your code here!
def solve(a, b):
    answer = 0
    for i in range(a, b + 1):
        if i % 3 == 0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
            answer += 1
    
    print(answer)
    return

solve(a, b)