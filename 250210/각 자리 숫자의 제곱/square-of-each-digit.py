N = int(input())

# Write your code here

def solve(num):
    if num == 0:
        return 0
    return solve(num // 10) + (num % 10)**2

print(solve(N))